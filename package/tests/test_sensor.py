from camera_simulator.classes import Sensor
import numpy as np

def test_width():
    a = Sensor(gain=1.0)
    assert a.gain == 1.0, "Sensor: gain should be 1.0"

def test_process():
    a = Sensor(gain=2.0)
    assert (a.process( np.array([1,3]) ) == np.array([2.0,6.0])).all, "Sensor: result should be [2.0,6.0]"