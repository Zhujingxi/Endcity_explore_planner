from setuptools import setup, Extension
import pybind11
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "generate_path_module",
        ["generate_path.cpp"],
        include_dirs=[pybind11.get_include()],
        language='c++',
    ),
]

setup(
    name="generate_path_module",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
