import numpy as np
from setuptools import Extension
from Cython.Build import build_ext, cythonize
from setuptools.errors import CCompilerError, PackageDiscoveryError

ext_modules = [
    Extension(
        "othello.cothello",
        sources=[
            "modules/othello/cothello.pyx",
        ],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        language="c++",
        include_dirs=[np.get_include()],
    ),
]


class MyBuildExt(build_ext):
    def run(self):
        try:
            build_ext.run(self)
        except FileNotFoundError:
            raise Exception("File not found. Could not compile C extension.")

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, PackageDiscoveryError, ValueError):
            raise Exception("Could not compile C extension.")


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": cythonize(ext_modules, language_level="3"),
            "cmdclass": {"build_ext": MyBuildExt},
        }
    )
