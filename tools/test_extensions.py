"""Finite oracles independent of the algorithms used by the extension functions."""
import itertools
import random
import unittest
import research_core as c
import research_extensions as e


class ExtensionTests(unittest.TestCase):
    def test_bct_against_pair_definition(self):
        rng=random.Random(20261030)
        tables=[list(p) for p in itertools.permutations(range(4))]
        tables += [rng.sample(range(8),8) for _ in range(12)]
        for f in tables:
            n=(len(f)-1).bit_length()
            got=e.boomerang(f,n)
            direct=[[sum(f[x]^f[y]==b and f[x^a]^f[y^a]==b
                         for x in range(len(f)) for y in range(len(f)))
                     for b in range(len(f))] for a in range(len(f))]
            self.assertEqual(got['bct'],direct)
        with self.assertRaises(ValueError):
            e.boomerang([0,0,1,1],2)

    def test_trace_duality_and_reconstruction(self):
        for n,mod in [(1,3),(2,7),(3,11),(4,19)]:
            a=e.trace_and_dual(n,mod)
            tr=a['trace_table']
            self.assertEqual(a['duality_matrix'],[[int(i==j) for j in range(n)] for i in range(n)])
            for x in range(1<<n):
                bits=[tr[c.mul(x,b,mod,n)] for b in a['dual_basis']]
                self.assertEqual(sum(v<<i for i,v in enumerate(bits)),x)
                for y in range(1<<n):
                    self.assertEqual(tr[x^y],tr[x]^tr[y])
        with self.assertRaises(ValueError):
            e.trace_and_dual(3,9)
        with self.assertRaises(ValueError):
            e.trace_and_dual(3,-11)
        with self.assertRaises(ValueError):
            c.field_power(3,-11,1)

    def test_ea_and_ccz_certificates(self):
        f=c.field_power(3,11,3)
        # Independent coordinate formula: input permutation x -> rotate bits then XOR 1.
        g=[]
        for x in range(8):
            u=((x>>1)&1) | (((x>>2)&1)<<1) | ((x&1)<<2)
            g.append(f[u^1] ^ (x&1) ^ 2)
        r=e.ea_certificate(f,g,3,3,[2,4,1],[1,2,4],[1,0,0],input_offset=1,add_offset=2)
        self.assertTrue(r['equivalent_under_certificate'])
        wrong=list(g)
        wrong[3]^=1
        fail=e.ea_certificate(f,wrong,3,3,[2,4,1],[1,2,4],[1,0,0],input_offset=1,add_offset=2)
        self.assertFalse(fail['equivalent_under_certificate'])
        self.assertEqual(fail['failure']['x'],3)
        inverse=[f.index(x) for x in range(8)]
        self.assertTrue(e.ccz_certificate(f,inverse,3,3,[8,16,32,1,2,4])['equivalent_under_certificate'])
        self.assertFalse(e.ccz_certificate([0]*4,[0]*4,2,1,[4,2,1])['equivalent_under_certificate'])
        for call in [lambda:e.ea_certificate(f,g,3,3,[1,1,4],[1,2,4]),
                     lambda:e.ccz_certificate(f,f,3,3,[1]*6)]:
            with self.assertRaises(ValueError):
                call()

    def test_higher_order_all_three_variable_functions(self):
        # Independently evaluate every quadratic polynomial as a candidate, no Gray code.
        mon=[0,1,2,4,3,5,6]
        candidates=[]
        for coefficients in range(128):
            candidates.append([sum((coefficients>>j&1)*int(x&u==u) for j,u in enumerate(mon))%2 for x in range(8)])
        for mask in range(256):
            f=[mask>>x&1 for x in range(8)]
            answer=e.higher_order(f,3,2)
            self.assertEqual(answer['distance'],min(sum(a!=b for a,b in zip(f,g)) for g in candidates))
            witness=[sum(int(x&u==u) for u in answer['closest_anf_masks'])%2 for x in range(8)]
            self.assertEqual(sum(a!=b for a,b in zip(f,witness)),answer['distance'])
        with self.assertRaises(ValueError):
            e.higher_order([int(x==63) for x in range(64)],6,2)

    def test_function_code_distinct_words(self):
        rng=random.Random(13)
        for n,m in [(2,2),(3,2),(3,3)]:
            for _ in range(6):
                f=[rng.randrange(1<<m) for _ in range(1<<n)]
                for include in (False,True):
                    words={tuple(c.parity(a&x)^c.parity(b&f[x])^constant for x in range(1<<n))
                           for a in range(1<<n) for b in range(1<<m) for constant in ((0,1) if include else (0,))}
                    hist={str(w):sum(sum(word)==w for word in words) for w in {sum(word) for word in words}}
                    got=e.function_code(f,n,m,include)
                    self.assertEqual(got['weight_distribution'],hist)
                    self.assertEqual(1<<got['dimension'],len(words))
        identity=e.function_code(list(range(4)),2,2)
        self.assertEqual(identity['dimension'],3)
        self.assertTrue(identity['rank_deficient'])
        self.assertEqual(identity['weight_distribution'],{'0':1,'2':6,'4':1})

    def test_operations_and_batch_boundaries(self):
        jobs=[{'n':2,'table':[0,0,0,1]},
              {'operation':'field-trace','n':3,'modulus':11},
              {'operation':'boomerang','n':2,'table':[0,0,1,1]}]
        result=c.analyze({'operation':'batch','jobs':jobs})
        self.assertEqual((result['completed'],result['failed']),(2,1))
        self.assertEqual(result['records'][2]['status'],'error')
        for spec in [{'operation':'batch','jobs':[{'operation':'batch','jobs':jobs}]},
                     {'operation':'batch','jobs':jobs*11}, {'operation':'nonexistent'}, []]:
            with self.assertRaises(ValueError):
                c.analyze(spec)


    def test_full_eight_bit_inverse_and_function_code(self):
        inverse=c.field_power(8,0x11b,254)
        metrics=c.vector(inverse,8,8)
        self.assertTrue(metrics['permutation'])
        self.assertEqual(metrics['differential_uniformity'],4)
        self.assertEqual(metrics['nonlinearity'],112)
        code=e.function_code(inverse,8,8)
        self.assertEqual(code['dimension'],17)
        self.assertEqual(code['enumerated_codewords'],131072)
        self.assertEqual(code['minimum_distance'],112)
        # Independent Walsh-to-weight identity; full rank prevents repeated parameter words.
        weights={'0':1,'128':510,'256':1}
        for component in metrics['components'].values():
            for w in component['walsh']:
                for sign in (-1,1):
                    weight=str((256+sign*w)//2)
                    weights[weight]=weights.get(weight,0)+1
        self.assertEqual(code['weight_distribution'],weights)


if __name__=='__main__':
    unittest.main(verbosity=2)
