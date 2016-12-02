from Cython.Build import cythonize
from jinja2 import FileSystemLoader
from jinja2 import Environment
import os
from setuptools import setup,Extension
import subprocess
import sys

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

try:
    os.mkdir('pyx')
except OSError:
    pass

def make_bench(name):
    tpl_env = Environment(loader=FileSystemLoader('ibench_native/benchmarks'))
    with open('pyx/%s.pyx' % name,'w') as pyxf:
        pyxf.write(tpl_env.get_template('tpl.bench.pyx').render({'bench': name}))
    return Extension(name='ibench_native.benchmarks.%s' % name,
                     extra_compile_args=extra_args,
                     extra_link_args=extra_args,
                     sources=['pyx/%s.pyx' % name])

extensions = [make_bench('Inv')
#              make_bench('Det'),
#              make_bench('dot'),
#              make_bench('lu'),
#              make_bench('fft')
]

setup(name='ibench_native',
      version='0.1',
      description='Benchmarking for scientific python',
      url='http://github.com/rscohn2/ibench_native',
      author='Robert Cohn',
      author_email='Robert.S.Cohn@intel.com',
      license='MIT',
      packages=['ibench_native','ibench_native/benchmarks'],
      ext_modules=cythonize(extensions),
      package_data={'ibench_native': ['benchmarks/tpl.bench.pyx']},
      zip_safe=False)

