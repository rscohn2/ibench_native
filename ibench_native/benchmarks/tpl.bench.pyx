# distutils: language = c++

from ibench.benchmarks.{{bench}} import {{bench}}

# Expose the C++ class
cdef extern from '../ibench_native/benchmarks/c/{{bench}}.h':
     cdef cppclass {{bench}}_C:
        {{bench}}_C() except +
        void make_args(int) except +
        void compute() except +

# Wrap the c++ class in an extension class
# extension class cannot inherit from python classes
cdef class Wrapper:
    cdef {{bench}}_C c_class
    def make_args(self,n):
        self.c_class.make_args(n)
    def compute(self):
        self.c_class.compute()

# Inherit from python bench with methods specific to native
class {{bench}}_native({{bench}}):
    def _make_args(self, n):
        self._wrapper = Wrapper()
        self._wrapper.make_args(n)

    def _compute(self):
        self._wrapper.compute()
