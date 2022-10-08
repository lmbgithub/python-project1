# Python Project #1: Camera Simulator

This is a simple example of creating and consuming a distributable Python package. 

# Contents

- `camera_simulator` contains a project directory for a Python package. Note that its only content is the `camera_simulator/camera_simulator` directory for now. If you wanted to add tests or something you could put those in `camera_simulator/tests` or something.
- `camera_simulator/camera_simulator` is the actual "package". In accordance with Python's [documented behavior](https://docs.python.org/3.9/tutorial/modules.html#tut-packages), the directory is a package because it contains an `__init__.py` file.

## Docker
install and run all tests
`./docker/run.sh`

Turn off docker container 
`./docker/run.sh down`


## FAQ

### How do I install and use a package in Development Mode?

[Development Mode](https://setuptools.pypa.io/en/latest/userguide/quickstart.html) installs the package in "editable" mode so that you can change the source for your package in the actual source directory and consuming Python scripts/applications will see your edits the next time they run. 

### How do I Package/Bundle/Zip/Prepare my source code into a distributable package that I can distribute to others to use in their own Python apps?

Run `python -m build` to prepare your package source code for distribution. This will deploy a distributable Python package into `camera_simulator/src/dist/camera_simulator-0.0.1.tar.gz`.

### How do other users install the package once it's built?

Other users can run `pip install camera_simulator-0.0.1.tar.gz` to install your package.

Alternatively, you can [upload your built package to PyPI](https://packaging.python.org/distributing/#uploading-your-project-to-pypi) and then they can install it by running `pip install camera_simulator`.

### What are the differences between "Python Packages" and eggs?

I've been trying to figure that out myself. I can tell you that eggs appear to [essentially be deprecated](https://packaging.python.org/discussions/wheel-vs-egg/) and as noted on the previously linked python.org site _Wheel is currently considered the standard for built and binary packaging for Python._ Therefore I no longer maintain an example of building eggs, but some docs you might find interesting are as follows: "Python Packages" are documented at https://packaging.python.org/distributing/ and Eggs are documented at http://peak.telecommunity.com/DevCenter/PythonEggs

## Troubleshooting

### After installing the package I still see the error 'ImportError: No module named Camera Simulator' when trying to use it in a script/app.

It is important that the `setup.py` is in the **parent** of the actual root package folder. If you don't do this you won't get any errors, and pip will show you're package as installed (e.g. with `pip show Camera Simulator`) but consuming scripts of the package won't ever find the package and will always get the `ImportError`.

So this also implies that the "package" isn't what you specify as the name of your package in `setup.py`. Although `pip` uses the name in `setup.py` to determine whether it is installed, Python itself only cares about the directory that contains the `__init__.py` file.