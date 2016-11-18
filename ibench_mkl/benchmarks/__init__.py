from ibench.benchmarks import benchmarks
from ibench_mkl.benchmarks.inv import Inv

local_benchmarks = {
    'inv_mkl': Inv
}

# add to the list of benchmark options
benchmarks.update(local_benchmarks)
