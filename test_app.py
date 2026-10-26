import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_kernel_symmetry(self):
        x=np.array([[0.,0.],[1.,1.]]);np.testing.assert_allclose(kernel(x,x),kernel(x,x).T)
    def test_observed_uncertainty_smaller(self):
        _,var=posterior(np.array([[0.,0.]]),np.array([1.]),np.array([[0.,0.],[2.,2.]]));self.assertLess(var[0],var[1])
    def test_posterior_finite_duplicates(self):self.assertTrue(np.isfinite(posterior(np.ones((2,2)),np.ones(2),np.zeros((1,2)))[0]).all())
