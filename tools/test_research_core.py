"""Independent finite oracles and boundary checks; run with unittest."""
import itertools
import unittest
import research_core as c


class ExactTests(unittest.TestCase):
    def test_all_three_variable_functions(self):
        for bits in range(256):
            f=[bits>>x&1 for x in range(8)]
            s=c.scalar(f,3)
            direct=[sum((-1)**(f[x]^c.parity(x&u)) for x in range(8)) for u in range(8)]
            self.assertEqual(s['walsh'],direct)
            self.assertEqual(s['nonlinearity'],min(sum(f[x]!=(c.parity(x&a)^b) for x in range(8)) for a in range(8) for b in (0,1)))
            self.assertEqual(c.anf(c.anf(f)),f)
            # Independent enumeration of every possible nonzero annihilator.
            best=4
            for gbits in range(1,256):
                g=[gbits>>x&1 for x in range(8)]
                if all(not(f[x]&g[x]) for x in range(8)) or all(not((f[x]^1)&g[x]) for x in range(8)):
                    degree=max(i.bit_count() for i,a in enumerate(c.anf(g)) if a)
                    best=min(best,degree)
            self.assertEqual(c.immunity(f,3)['algebraic_immunity'],best)

    def test_mm_quadratic_and_rm(self):
        f=c.mm(2,[0,1,2,3],[0,0,0,0])
        s=c.scalar(f,4)
        self.assertTrue(s['bent'])
        self.assertEqual(s['nonlinearity'],6)
        self.assertFalse(s['balanced'])
        self.assertEqual(c.quadratic(f,4)['rank'],4)
        self.assertEqual(c.rm(1,3),dict(length=8,dimension=4,minimum_distance=4,dual_order=1))
        for pi in itertools.permutations(range(4)):
            for g in itertools.product((0,1),repeat=4):
                self.assertTrue(c.scalar(c.mm(2,list(pi),list(g)),4)['bent'])

    def test_vector_all_components_and_field(self):
        f=c.field_power(3,0b1011,3)
        r=c.vector(f,3,3)
        self.assertEqual(r['differential_uniformity'],2)
        self.assertTrue(r['permutation'])
        self.assertEqual(r['nonlinearity'],2)
        self.assertEqual(len(r['components']),7)
        self.assertTrue(all(sum(row)==8 for row in r['ddt']))
        # Every pair of balanced coordinates can hide a constant nonzero component.
        trap=c.vector([0,3,0,3],2,2)
        self.assertFalse(trap['components']['3']['balanced'])
        self.assertFalse(trap['balanced'])
        self.assertEqual(trap['nonlinearity'],0)
        rectangular=c.vector([0,0,0,1],2,3)
        self.assertEqual(rectangular['differential_uniformity'],2)
        self.assertFalse(rectangular['apn'])

    def test_resilience_propagation_symmetry(self):
        f=[c.parity(x) for x in range(8)]
        s=c.scalar(f,3)
        self.assertEqual(s['resiliency'],2)
        self.assertEqual(s['pc_order'],0)
        self.assertTrue(c.symmetry(f,3)['symmetric'])
        self.assertTrue(c.scalar([c.parity(x&3) ^ ((x>>2)&1) for x in range(8)],3)['parseval'])

    def test_invalid_inputs(self):
        for f,n,m in [([0,1],2,1),([0,2],1,1),([True,False],1,1),([0]*4,2,0)]:
            with self.assertRaises(ValueError):
                c.validate(f,n,m)
        with self.assertRaises(ValueError):
            c.field_power(3,0b1001,3)
        with self.assertRaises(ValueError):
            c.field_power(3,0b1011,-1)
        with self.assertRaises(ValueError):
            c.mm(2,[0,0,1,2],[0]*4)
        with self.assertRaises(ValueError):
            c.immunity([0]*128,7)
        with self.assertRaises(ValueError):
            c.quadratic([int(x==7) for x in range(8)],3)


if __name__=='__main__':
    unittest.main(verbosity=2)
