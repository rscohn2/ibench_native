from __future__ import print_function

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
        pyxf.write(tpl_env.get_template('tpl.bench.pyx').render({'bench': name, 'Bench': name.capitalize()}))
    return Extension(name='ibench_native.benchmarks.%s' % name,
                     extra_compile_args=extra_args,
                     extra_link_args=extra_args,
                     sources=['pyx/%s.pyx' % name])

extensions = [
    make_bench('det'),
    make_bench('dot'),
    make_bench('inv'),
    make_bench('lu')
]

setup(name='ibench_native',
      version='0.1',
      description='Plugin for ibench http://github.com/IntelPython/ibench that provides native implementations of benchmarks',
      url='http://github.com/IntelPython/ibench_native',
      author='Robert Cohn',
      author_email='Robert.S.Cohn@intel.com',
      license='MIT',
      platforms='Linux',
      packages=['ibench_native','ibench_native/benchmarks'],
      ext_modules=cythonize(extensions),
      package_data={'ibench_native': ['benchmarks/tpl.bench.pyx']},
      zip_safe=False,
      long_description=
      '''This is a plugin that provides native (e.g. C) implementations for benchmarks that can be called form ibench. See http://github.com/IntelPython/ibench for more information.'''
)

