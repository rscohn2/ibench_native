import os
import subprocess
from setuptools import setup,Extension
from Cython.Build import cythonize

try:
    # use icc if it is available
    icc = subprocess.check_output('which icc',shell=True).decode('utf-8')
except:
    icc = None

if icc:
    print('Using icc: %s' % icc)
    os.environ['CC'] = icc
    os.environ['CXX'] = os.environ['CC']
    extra_args = ['-mkl']
else:
    extra_args = []

extensions = [Extension(name='ibench_mkl.benchmarks.inv',
                        extra_compile_args=extra_args,
                        extra_link_args=extra_args,
                        sources=['ibench_mkl/benchmarks/inv.pyx']
                    )]

setup(name='ibench_mkl',
      version='0.1',
      description='Benchmarking for scientific python',
      url='http://github.com/rscohn2/ibench_mkl',
      author='Robert Cohn',
      author_email='Robert.S.Cohn@intel.com',
      license='MIT',
      packages=['ibench_mkl','ibench_mkl/benchmarks'],
      ext_modules=cythonize(extensions),
      zip_safe=False)
