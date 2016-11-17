# distutils: language = c++
# xxdistutils: sources = ibenchn/benchmarks/inv.cpp

from ibench.benchmarks.inv import Inv

# Expose the C++ class
cdef extern from 'inv.h':
     cdef cppclass C_inv:
        C_inv(int) except +
        c_compute() except +

# Wrap the c++ class in an extension class
cdef class Foo:
    cdef C_inv* c_inv
    def __cinit__(self, int n):
        self.c_inv = new C_inv(n)
    def __dealloc__(self):
        del self.c_inv

# The extension class cannot inherit from python class, so we need 1 more layer
class Native_inv(Inv):
    def _make_args(self, n):
        pass

    def _compute(self):
        self.c_compute()
