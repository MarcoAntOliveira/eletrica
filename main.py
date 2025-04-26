import numpy as np

if __name__ == "__main__":
  A = np.array([ [0.75, -0.2],[-1, 1.6],])
  A_inv = np.linalg.inv(A)

  B = np.array([[10], [0]])
  C = A_inv@B

