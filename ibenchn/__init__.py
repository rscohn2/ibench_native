# python loads libraries with RTLD_LOCAL, but MKL requires RTLD_GLOBAL
# pre-load MKL with RTLD_GLOBAL before loading the native extension
import ctypes
ctypes.CDLL('libmkl_rt.so', ctypes.RTLD_GLOBAL)

import ibenchn.benchmarks
