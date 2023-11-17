import numpy as np
from setuptools import Extension, setup
from Cython.Build import build_ext, cythonize


class MyBuildExt(build_ext):
    def build_extensions(self):
        if self.compiler.compiler_type == "unix":
            for e in self.extensions:
                e.extra_compile_args = [
                    "-O3",
                    "-std=c++11",
                    "-fopenmp",
                ]
        elif self.compiler.compiler_type == "msvc":
            for e in self.extensions:
                e.extra_compile_args = [
                    "/O2",
                    "/std:c11",
                    "/openmp",
                ]

        super(MyBuildExt, self).build_extensions()

    def finalize_options(self):
        super(MyBuildExt, self).finalize_options()
        self.include_dirs.append(np.get_include())


extensions = [
    Extension(
        "cutils",
        sources=["cutils.pyx"],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        language="c++",
    )
]

setup(
    name="cutils",
    ext_modules=cythonize(
        extensions,
        language_level="3",
    ),
    cmdclass={"build_ext": MyBuildExt},
    install_requires=["numpy"],
)
