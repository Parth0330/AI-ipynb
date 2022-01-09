import numpy as np

# sigmoid FUNCTION: sigmoid
def sigmoid(z):
# z -- A scalar or numpy array of any size.
  s=1/(1+np.exp(-z))
  return s