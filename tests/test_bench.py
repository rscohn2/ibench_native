import subprocess

from ibench_native.benchmarks.inv import Inv_native
from ibench.benchmarks import benchmarks

def test_inv():
    n = Inv_native(1)
    n._make_args(2)
    n._compute()

def test_add():
    assert('inv_native' in benchmarks)

def test_ibench():
    subprocess.check_call('python -m ibench run -p ibench_native -b inv_native --size test --file foo',shell=True)
