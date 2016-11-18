import subprocess

from ibench_mkl.benchmarks.inv import Inv_mkl
from ibench.benchmarks import benchmarks

def test_inv():
    n = Inv_mkl(1)
    n._make_args(2)
    n._compute()

def test_add():
    assert('inv_mkl' in benchmarks)

def test_ibench():
    subprocess.check_call('python -m ibench run -p ibench_mkl -b inv_mkl --quick --file foo',shell=True)
