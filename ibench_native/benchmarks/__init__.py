from ibench.benchmarks import benchmarks
from . import inv

local_benchmarks = {
    'inv_native': inv.Inv
}

# add to the list of benchmark options
benchmarks.update(local_benchmarks)
