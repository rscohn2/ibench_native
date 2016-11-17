import subprocess

from ibenchn.benchmarks.inv import Native_inv

def test_inv():
    n = Native_inv(1)
    n._make_args(2)
    n._compute()

def test_ibench():
    subprocess.check_call('python -m ibench run -p ibenchn -b inv_native --quick --file foo',shell=True)
