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
    subprocess.check_call('IBENCH_PLUGINS="ibench_native" python -m ibench run -b inv_native dot_native --size test --file foo',shell=True)
