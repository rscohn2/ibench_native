import subprocess

from ibench_native.benchmarks.inv import Inv_native
from ibench.benchmarks import benchmarks

def test_add():
    assert('inv_native' in benchmarks)

def test_det():
    subprocess.check_call('IBENCH_PLUGINS="ibench_native" python -m ibench run -b det_native --size test --file foo',shell=True)

def test_dot():
    subprocess.check_call('IBENCH_PLUGINS="ibench_native" python -m ibench run -b dot_native --size test --file foo',shell=True)

def test_inv():
    subprocess.check_call('IBENCH_PLUGINS="ibench_native" python -m ibench run -b inv_native --size test --file foo',shell=True)

def test_lu():
    subprocess.check_call('IBENCH_PLUGINS="ibench_native" python -m ibench run -b lu_native --size test --file foo',shell=True)



