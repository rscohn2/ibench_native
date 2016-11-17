#include "bench.h"

class C_inv : public Bench {
 public:
  C_inv();
  ~C_inv();
  void make_args(int n);
  void compute();
 private:
  double *x_mat, *r_mat;
  int *ipiv;
  int N,M,LDA;
};
