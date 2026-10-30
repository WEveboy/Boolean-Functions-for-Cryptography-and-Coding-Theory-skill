"""Exact bounded research operations, independently implemented from mathematical definitions."""
import hashlib
import json
from math import comb
import research_core as c


def integer(value,low,high,name):
    if type(value) is not int or not low<=value<=high:
        raise ValueError(f'{name} must be an integer in {low}..{high}')
    return value


def boomerang(table,n):
    """BCT[a,b]=#{x: inv(F(x)+b)+inv(F(x+a)+b)=a}."""
    c.validate(table,n,n)
    if n>8 or len(set(table)) != 1 << n:
        raise ValueError('BCT requires a permutation with n<=8')
    size=1 << n
    inv=[0]*size
    for x,y in enumerate(table):
        inv[y]=x
    bct=[[sum((inv[table[x]^b]^inv[table[x^a]^b])==a for x in range(size))
          for b in range(size)] for a in range(size)]
    maximum=max(bct[a][b] for a in range(1,size) for b in range(1,size))
    a,b=next((a,b) for a in range(1,size) for b in range(1,size) if bct[a][b]==maximum)
    return {'bct':bct,'boomerang_uniformity':maximum,'witness':{'a':a,'b':b,
            'solutions':[x for x in range(size) if inv[table[x]^b]^inv[table[x^a]^b]==a]},
            'definition':'inverse-based BCT; maximum excludes a=0 and b=0'}


def trace_and_dual(n,mod):
    c.field_power(n,mod,1)  # validates the finite field, including irreducibility
    size=1 << n
    def trace(x):
        z=0
        for _ in range(n):
            z^=x
            x=c.mul(x,x,mod,n)
        if z not in (0,1):
            raise AssertionError('trace must lie in F2')
        return z
    traces=[trace(x) for x in range(size)]
    # basis alpha_i=X^i; dual beta_j satisfies Tr(alpha_i*beta_j)=delta_ij.
    pairing=[sum(trace(c.mul(1<<i,1<<j,mod,n))<<j for j in range(n)) for i in range(n)]
    dual=[]
    for j in range(n):
        beta=next(x for x in range(size) if all(c.parity(pairing[i]&x)==int(i==j) for i in range(n)))
        dual.append(beta)
    return dict(n=n,modulus=mod,trace_table=traces,polynomial_basis=[1<<i for i in range(n)],
                dual_basis=dual,pairing_rows=pairing,
                duality_matrix=[[trace(c.mul(1<<i,beta,mod,n)) for beta in dual] for i in range(n)],
                linearity='F2-linear, not generally GF(2^n)-linear')


def matrix(rows,inputs,outputs,name,invertible=False):
    if not isinstance(rows,list) or len(rows)!=outputs:
        raise ValueError(f'{name} requires {outputs} row masks')
    for row in rows:
        integer(row,0,(1<<inputs)-1,name)
    if invertible and (inputs!=outputs or c.rank(rows)!=inputs):
        raise ValueError(name+' must be invertible')
    return rows


def affine(rows,x,offset):
    return sum(c.parity(row&x)<<i for i,row in enumerate(rows)) ^ offset


def ea_certificate(f,g,n,m,inp,out,add=None,input_offset=0,output_offset=0,add_offset=0):
    """Check G(x)=A_out(F(A_in(x))) XOR L(x); all matrices use row masks."""
    c.validate(f,n,m)
    c.validate(g,n,m)
    if n>8 or n+m>16:
        raise ValueError('EA budget n<=8,n+m<=16')
    matrix(inp,n,n,'input_rows',True)
    matrix(out,m,m,'output_rows',True)
    add=[0]*m if add is None else add
    matrix(add,n,m,'add_rows')
    integer(input_offset,0,(1<<n)-1,'input_offset')
    integer(output_offset,0,(1<<m)-1,'output_offset')
    integer(add_offset,0,(1<<m)-1,'add_offset')
    for x in range(1<<n):
        predicted=affine(out,f[affine(inp,x,input_offset)],output_offset)^affine(add,x,add_offset)
        if predicted!=g[x]:
            return {'equivalent_under_certificate':False,'failure':{'x':x,'predicted':predicted,'actual':g[x]}}
    return {'equivalent_under_certificate':True,'checked_points':1<<n,'relation':'EA','search_performed':False}


def ccz_certificate(f,g,n,m,rows,offset=0):
    c.validate(f,n,m)
    c.validate(g,n,m)
    if n>8 or n+m>16:
        raise ValueError('CCZ budget n<=8,n+m<=16')
    matrix(rows,n+m,n+m,'graph_rows',True)
    integer(offset,0,(1<<(n+m))-1,'offset')
    seen=set()
    for x in range(1<<n):
        z=affine(rows,x | (f[x]<<n),offset)
        u,y=z&((1<<n)-1),z>>n
        if u in seen:
            return {'equivalent_under_certificate':False,'failure':{'x':x,'reason':'input projection collision','u':u}}
        seen.add(u)
        if y!=g[u]:
            return {'equivalent_under_certificate':False,'failure':{'x':x,'u':u,'predicted':y,'actual':g[u]}}
    return {'equivalent_under_certificate':True,'checked_points':1<<n,'relation':'CCZ','search_performed':False}


def higher_order(table,n,r):
    c.validate(table,n)
    integer(r,0,n,'r')
    if n>8:
        raise ValueError('higher-order NL requires n<=8')
    coeff=c.anf(table)
    degree=max((u.bit_count() for u,v in enumerate(coeff) if v),default=-1)
    if degree<=r:
        return {'order':r,'distance':0,'closest_anf_masks':[u for u,v in enumerate(coeff) if v],
                'enumerated_codewords':0,'proof':'input ANF already belongs to RM(r,n)'}
    mon=[u for u in range(1<<n) if u.bit_count()<=r]
    if len(mon)>16:
        raise ValueError('RM enumeration budget exceeded: dimension must be <=16')
    words=[sum(int(x&u==u)<<x for x in range(1<<n)) for u in mon]
    target=sum(v<<x for x,v in enumerate(table))
    best=(1<<n)+1
    current=0
    best_mask=0
    for i in range(1<<len(mon)):
        if i:
            changed=(i&-i).bit_length()-1
            current^=words[changed]
        distance=(target^current).bit_count()
        if distance<best:
            best=distance
            best_mask=i^(i>>1)
    masks=[u for i,u in enumerate(mon) if best_mask>>i&1]
    return {'order':r,'distance':best,'closest_anf_masks':masks,
            'enumerated_codewords':1<<len(mon),'rm_dimension':len(mon)}


def function_code(table,n,m,include_constant=True):
    c.validate(table,n,m)
    if n>8 or n+m>16 or type(include_constant) is not bool:
        raise ValueError('function code: n<=8,n+m<=16; include_constant must be boolean')
    size=1<<n
    rows=[sum(((x>>i)&1)<<x for x in range(size)) for i in range(n)]
    rows += [sum(((y>>i)&1)<<x for x,y in enumerate(table)) for i in range(m)]
    if include_constant:
        rows.append((1<<size)-1)
    # Preserve an independent set of actual generator rows, not coefficient tuples.
    independent=[]
    for row in rows:
        if c.rank(independent+[row])>len(independent):
            independent.append(row)
    dimension=len(independent)
    if dimension>17:
        raise ValueError('code enumeration budget dimension<=17')
    histogram={}
    word=0
    for i in range(1<<dimension):
        if i:
            word^=independent[(i&-i).bit_length()-1]
        wt=word.bit_count()
        histogram[str(wt)]=histogram.get(str(wt),0)+1
    return {'length':size,'dimension':dimension,'parameter_count':n+m+int(include_constant),
            'rank_deficient':dimension<n+m+int(include_constant),'generator_rows':rows,
            'independent_generator_rows':independent,'weight_distribution':histogram,
            'minimum_distance':min((int(w) for w in histogram if int(w)>0),default=None),
            'enumerated_codewords':1<<dimension,
            'definition':'C={ (a dot x) XOR (b dot F(x)) XOR c : all x in F2^n }; c=0 if include_constant=false',
            'weight_formula':'wt(a,b,c)=(2^n-(-1)^c*W_F(a,b))/2; full parameter tuples may repeat codewords'}


def run(spec):
    op=spec['operation']
    if op=='boomerang':
        result=boomerang(spec['table'],spec['n'])
    elif op=='field-trace':
        result=trace_and_dual(spec['n'],spec['modulus'])
    elif op=='higher-order':
        result=higher_order(spec['table'],spec['n'],spec['r'])
    elif op=='function-code':
        result=function_code(spec['table'],spec['n'],spec['m'],spec.get('include_constant',True))
    elif op=='ea-certificate':
        result=ea_certificate(spec['table'],spec['target'],spec['n'],spec['m'],spec['input_rows'],spec['output_rows'],
                              spec.get('add_rows'),spec.get('input_offset',0),spec.get('output_offset',0),spec.get('add_offset',0))
    elif op=='ccz-certificate':
        result=ccz_certificate(spec['table'],spec['target'],spec['n'],spec['m'],spec['graph_rows'],spec.get('offset',0))
    elif op=='batch':
        jobs=spec['jobs']
        if not isinstance(jobs,list) or not 1<=len(jobs)<=32:
            raise ValueError('batch requires 1..32 jobs')
        if any(not isinstance(job,dict) or job.get('operation')=='batch' for job in jobs):
            raise ValueError('nested batch or non-object job is not supported')
        records=[]
        for i,job in enumerate(jobs):
            try:
                records.append({'index':i,'status':'ok','result':c.analyze(job)})
            except (ValueError,TypeError,KeyError) as exc:
                records.append({'index':i,'status':'error','error':str(exc)})
        result={'records':records,'completed':sum(x['status']=='ok' for x in records),
                'failed':sum(x['status']=='error' for x in records)}
    else:
        raise ValueError('unknown operation: '+str(op))
    result['operation']=op
    result['tool_version']='0.2.0'
    result['input_sha256']=hashlib.sha256(json.dumps(spec,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    result['specification']=spec
    result['evidence']='exact for supplied finite objects / certificate; no equivalence search or infinite-family proof'
    return result
