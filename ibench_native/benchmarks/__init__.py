from ibench.benchmarks import benchmarks
from ibench_native.benchmarks.inv import Inv
from ibench_native.benchmarks.det import Det
from ibench_native.benchmarks.dot import Dot
from ibench_native.benchmarks.fft import FFT
from ibench_native.benchmarks.lu import LU

local_benchmarks = {
    'inv_native': Inv,
    'det_native': Det,
    'dot_native': Dot,
    'fft_native': FFT,
    'lu_native': LU
}

# add to the list of benchmark options
benchmarks.update(local_benchmarks)
