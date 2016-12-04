from ibench.benchmarks import benchmarks
from ibench_native.benchmarks.inv import Inv

local_benchmarks = {
    'inv_native': Inv
}

# add to the list of benchmark options
benchmarks.update(local_benchmarks)
