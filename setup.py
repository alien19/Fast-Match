"""
Setup for compiling cache

Jonas Toft Arnfred, 2013-04-22
"""
from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize(["cache.pyx", "fastmatch.pyx"], language_level = "3"), # , "turntable_ground_truth.pyx"
    include_dirs=[numpy.get_include()]
)
