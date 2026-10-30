"""Small exact Boolean-function laboratory. Python 3.10+, standard library only.

Independent implementation, not code transcribed from Carlet's book.
Input x uses bit i as x_i; output masks use the same little-endian convention.
"""
import argparse
import hashlib
import json
from math import comb
from pathlib import Path


def parity(x):
    return x.bit_count() & 1


def validate(table, n, m=1):
    if type(n) is not int or not 1 <= n <= 10:
        raise ValueError('n must be in 1..10 (exact computation budget)')
    if type(m) is not int or not 1 <= m <= 8:
        raise ValueError('m must be in 1..8')
    if len(table) != 1 << n or any(type(y) is not int or not 0 <= y < 1 << m for y in table):
        raise ValueError('table length/range/type mismatch')


def fwht(values):
    a = list(values)
    if not a or len(a) & (len(a)-1):
        raise ValueError('power-of-two length required')
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return a


def anf(table):
    a = list(table)
    for i in range((len(a)-1).bit_length()):
        for x in range(len(a)):
            if x & (1 << i):
                a[x] ^= a[x ^ (1 << i)]
    return a


def scalar(table, n):
    validate(table, n)
    w = fwht([1-2*y for y in table])
    a = anf(table)
    ac = [sum(1-2*(table[x] ^ table[x ^ d]) for x in range(1 << n)) for d in range(1 << n)]
    ci = 0
    for t in range(1, n+1):
        if any(w[u] for u in range(1, 1 << n) if u.bit_count() <= t):
            break
        ci = t
    pc = 0
    for t in range(1, n+1):
        if any(ac[d] for d in range(1, 1 << n) if d.bit_count() <= t):
            break
        pc = t
    maximum = max(map(abs, w))
    return dict(n=n, weight=sum(table), balanced=sum(table)*2 == 1 << n,
                anf_masks=[i for i,c in enumerate(a) if c],
                degree=max((i.bit_count() for i,c in enumerate(a) if c), default=-1),
                walsh=w, nonlinearity=(1 << (n-1))-maximum//2,
                autocorrelation=ac, correlation_immunity=ci,
                resiliency=ci if w[0] == 0 else None, pc_order=pc,
                bent=n % 2 == 0 and all(v*v == 1 << n for v in w),
                plateaued=len({abs(v) for v in w if v}) == 1,
                parseval=sum(v*v for v in w) == 1 << (2*n))


def vector(table, n, m):
    validate(table, n, m)
    if n > 8 or n+m > 14:
        raise ValueError('vector budget: n<=8 and n+m<=14')
    rows = []
    for d in range(1 << n):
        row = [0] * (1 << m)
        for x in range(1 << n):
            row[table[x] ^ table[x ^ d]] += 1
        rows.append(row)
    components = {}
    # bitwise AND, not integer multiplication, defines a component mask.
    for b in range(1, 1 << m):
        f = [parity(b & y) for y in table]
        w = fwht([1-2*y for y in f])
        components[str(b)] = {'walsh': w, 'nonlinearity': (1 << (n-1))-max(map(abs,w))//2,
                              'balanced': sum(f)*2 == 1 << n}
    delta = max(max(row) for row in rows[1:])
    return dict(n=n, m=m, permutation=n == m and len(set(table)) == 1 << n,
                balanced=all(c['balanced'] for c in components.values()),
                nonlinearity=min(c['nonlinearity'] for c in components.values()),
                differential_uniformity=delta, apn=n == m and delta == 2, ddt=rows, components=components)


def rank(rows):
    basis = {}
    for row in rows:
        while row:
            p = row.bit_length()-1
            if p in basis:
                row ^= basis[p]
            else:
                basis[p] = row
                break
    return len(basis)


def quadratic(table, n):
    s = scalar(table,n)
    if s['degree'] > 2:
        raise ValueError('quadratic polar rank requires degree<=2')
    matrix = [sum((table[(1<<i)^(1<<j)] ^ table[1<<i] ^ table[1<<j] ^ table[0]) << j
                  for j in range(n)) for i in range(n)]
    r = rank(matrix)
    return dict(polar_rows=matrix, rank=r, predicted_nonzero_amplitude=1 << (n-r//2),
                predicted_support_size=1 << r, actual_support_size=sum(v != 0 for v in s['walsh']))


def mm(k, pi, g):
    if not 1 <= k <= 5 or sorted(pi) != list(range(1 << k)) or len(g) != 1 << k or any(v not in (0,1) for v in g):
        raise ValueError('MM requires k<=5, pi permutation and binary g of length 2^k')
    return [parity((z & ((1<<k)-1)) & pi[z >> k]) ^ g[z >> k] for z in range(1 << (2*k))]


def rm(r, n):
    if not 0 <= r <= n <= 20:
        raise ValueError('RM requires 0<=r<=n<=20')
    return dict(length=1 << n, dimension=sum(comb(n,i) for i in range(r+1)),
                minimum_distance=1 << (n-r), dual_order=n-r-1 if r<n else None)


def nullvector(rows, columns):
    a = list(rows)
    pivots = []
    k = 0
    for j in range(columns):
        p = next((i for i in range(k,len(a)) if a[i] >> j & 1),None)
        if p is None:
            continue
        a[k],a[p] = a[p],a[k]
        for i in range(len(a)):
            if i != k and a[i] >> j & 1:
                a[i] ^= a[k]
        pivots.append(j)
        k += 1
    free = next((j for j in range(columns) if j not in pivots),None)
    if free is None:
        return None
    v = 1 << free
    for i,j in reversed(list(enumerate(pivots))):
        if parity(a[i] & v):
            v |= 1 << j
    return v


def immunity(table,n):
    validate(table,n)
    if n>6:
        raise ValueError('exact AI budget n<=6')
    for d in range((n+1)//2+1):
        mon = [u for u in range(1 << n) if u.bit_count() <= d]
        for target in (1,0):
            rows = [sum(int(x & u == u) << j for j,u in enumerate(mon))
                    for x in range(1 << n) if table[x] == target]
            v = nullvector(rows,len(mon))
            if v is not None:
                masks = [u for j,u in enumerate(mon) if v >> j & 1]
                assert masks and all(not (table[x] if target else table[x]^1) or
                       not (sum(int(x & u == u) for u in masks)&1) for x in range(1 << n))
                return dict(algebraic_immunity=d, annihilates='f' if target else 'f+1', anf_masks=masks)
    raise AssertionError('AI bound violated')


def mul(a,b,mod,n):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & (1 << n):
            a ^= mod
    return z


def power(a,d,mod,n):
    z = 1
    while d:
        if d & 1:
            z = mul(z,a,mod,n)
        a = mul(a,a,mod,n)
        d >>= 1
    return z


def field_power(n,mod,d):
    if not 1<=n<=8 or type(d) is not int or d<1 or type(mod) is not int or mod.bit_length()!=n+1:
        raise ValueError('field power: n<=8, degree-n binary modulus, positive exponent required')
    # In a field every nonzero residue is a unit; this exhaustive check also rejects reducible moduli.
    if any(power(x,(1<<n)-1,mod,n) != 1 for x in range(1,1<<n)):
        raise ValueError('modulus is not irreducible')
    return [power(x,d,mod,n) for x in range(1 << n)]


def symmetry(table,n):
    validate(table,n)
    layers = [[table[x] for x in range(1 << n) if x.bit_count()==k] for k in range(n+1)]
    mask=(1<<n)-1
    return dict(symmetric=all(len(set(layer)) == 1 for layer in layers),
                rotation_symmetric=all(table[x] == table[((x<<1)&mask)|(x>>(n-1))] for x in range(1<<n)),
                layer_weights=[sum(layer) for layer in layers], layer_sizes=[len(layer) for layer in layers])


def analyze(spec):
    n,m,table = spec['n'],spec.get('m',1),spec['table']
    validate(table,n,m)
    result = scalar(table,n) if m==1 else vector(table,n,m)
    if m==1:
        result['symmetry']=symmetry(table,n)
        if result['degree']<=2:
            result['quadratic']=quadratic(table,n)
        if n<=6:
            result['immunity']=immunity(table,n)
    result['specification']={'n':n,'m':m,'bit_order':'x_i=(x>>i)&1','table':table}
    result['input_sha256']=hashlib.sha256(json.dumps(result['specification'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
    result['evidence']='exhaustive for the supplied finite table; not an infinite-family proof'
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('spec',type=Path)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    try:
        result=analyze(json.loads(args.spec.read_text(encoding='utf-8')))
    except (ValueError,KeyError,TypeError) as e:
        p.exit(2,str(e)+'\n')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(str(args.out))
