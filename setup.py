import os
from setuptools import setup,Extension
from Cython.Build import cythonize

os.environ['CC'] = '/localdisk/psxe_16/compilers_and_libraries_2016.2.181/linux/bin/intel64/icc'
#os.environ['CC'] = '/localdisk/psxe_16/compilers_and_libraries_2016.3.210/linux/bin/intel64/icc'
os.environ['CXX'] = os.environ['CC']
extensions = [Extension(name='ibenchn.benchmarks.inv',
                        extra_compile_args=['-mkl'],
                        extra_link_args=['-mkl'],
                        sources=['ibenchn/benchmarks/inv.pyx','ibenchn/benchmarks/c/inv.cpp']
                    )]

setup(name='ibenchn',
      version='0.1',
      description='Benchmarking for scientific python',
      url='http://github.com/rscohn2/ibenchn',
      author='Robert Cohn',
      author_email='Robert.S.Cohn@intel.com',
      license='MIT',
      packages=['ibenchn','ibenchn/benchmarks'],
      ext_modules=cythonize(extensions),
      zip_safe=False)
