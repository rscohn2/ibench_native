# distutils: language = c++
# distutils: sources = ibench_mkl/benchmarks/c/inv.cpp

from ibench.benchmarks.inv import Inv

# Expose the C++ class
cdef extern from 'c/inv.h':
     cdef cppclass C_inv:
        C_inv() except +
        void make_args(int) except +
        void compute() except +

# Wrap the c++ class in an extension class
# extension class cannot inherit from python classes
cdef class Wrapper:
    cdef C_inv c_class
    def make_args(self,n):
        self.c_class.make_args(n)
    def compute(self):
        self.c_class.compute()

# Inherit from python inv with methods specific to native
class Inv_mkl(Inv):
    def _make_args(self, n):
        self._wrapper = Wrapper()
        self._wrapper.make_args(n)

    def _compute(self):
        self._wrapper.compute()
