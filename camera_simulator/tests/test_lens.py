from camera_simulator.classes import Lens
import numpy as np

def test_lens():
    lens = Lens(width=2,height=2)
    assert lens.process( np.array([1,3]) ) == np.array([2]), "image should be 2x2"