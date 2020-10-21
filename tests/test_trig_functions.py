import numpy as np
import pytest
from simple_functions import sin



class TestTrigFunctions(object):
    '''Class to test my trigonometric functions implementation'''

    @pytest.mark.parametrize('x', [
        (0),
        (np.pi),
        (3*np.pi),
        (-3.5*np.pi)
    ])
    def test_sin(self, x):
        '''Test computation of sin'''
        my_sin = sin(x)
        assert np.isclose(my_sin, np.sin(x), atol=1e-12)
