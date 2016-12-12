from ibench.benchmarks import benchmarks
from . import det
from . import dot
from . import inv
from . import lu

local_benchmarks = {
    'dot_native': dot.Dot,
    'det_native': det.Det,
    'inv_native': inv.Inv,
    'lu_native': lu.Lu
}

# add to the list of benchmark options
benchmarks.update(local_benchmarks)
