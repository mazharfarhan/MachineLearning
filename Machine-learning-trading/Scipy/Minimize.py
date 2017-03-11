import pandas as pd
import numpy as np
import scipy.optimize as spo

def f(X):
  
    // give a scalar return a real value
    Y= (X-1.5) ** 2 +0.5
    print "X = {}, Y= {}".format(X,Y)
    return Y
    
  
