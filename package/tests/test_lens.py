from camera_simulator.classes import Lens
import numpy as np

def test_width():
    """test_width."""
    lens = Lens(width=2,height=2)
    assert lens.width == 2, "Lens: width should be 2"

def test_height():
    """test_height."""
    lens = Lens(width=2,height=3)
    assert lens.height == 3, "Lens: width should be 3"

def test_process():
    """test_process."""
    lens = Lens(width=2,height=2)
    assert (lens.process( np.array([[1,3],[1,3]]) ) ==  np.array([[1,3],[1,3]]) ).all, "Lens: image should be 2x2"