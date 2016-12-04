from ibench.benchmarks import benchmarks
from . import inv
from . import dot

local_benchmarks = {
    'dot_native': dot.Dot,
    'inv_native': inv.Inv
}

# add to the list of benchmark options
benchmarks.update(local_benchmarks)
