# python_package_template
Template for creating python packages that can be published to PyPi


## Folder structure
Each folder that should be considered a module must contain an `__init__.py` file. The file may be blank, but at can also contain imports to decrease the number of imports needed in files using the package

## Handle python versions
Use the [pyenv](https://github.com/pyenv/pyenv) library to control which python version is installed in your local virtual environment. With pyenv you can install different versions of python to use for virtual environments and the relevant version is simply activated by running `pyenv global 3.9.5`

## Handle dependencies
For easy collaboration use poetry to handle dependencies. Regardless, dependencies should be added to the `pyproject.toml` file.


## Handle files
When using file types other than .py, it is necessary to add a MANIFEST.in file  


## Test installation
Navigate to this folder and run `pip install .`

## Wheel
To build wheel based on toml file, simply run `python -m pip wheel .`
