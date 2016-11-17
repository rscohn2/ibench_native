from ibench.benchmarks import benchmarks
from ibenchn.benchmarks.inv import Inv

local_benchmarks = {
    'inv_native': Inv
}

benchmarks.extend(local_benchmarks)
