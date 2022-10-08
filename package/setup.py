from setuptools import setup

setup(
    name='camera_simulator',
    version='0.0.1',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.9"',
        'numpy',
        'pytest',
    ],
)