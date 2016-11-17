from ibench.benchmarks import benchmarks
from ibenchn.benchmarks.inv import Inv

local_benchmarks = {
    'inv_native': Inv
}

benchmarks.update(local_benchmarks)
