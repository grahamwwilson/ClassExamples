# fitconfig.py
#
# Specific fit configurations such as FitBW and FitPoly
# Note that this contains also the initial values for the parameters and 
# optionally whether some parameters are fixed.
#
import mymodels
from iminuit import Minuit
import MyLeastSquares
from fitting import FixParameters, GenericFit

def FitModel1(x, y, dy):

    print(" ")
    print(" ")
    print("-------------------------------")
    print("Running fitconfig.FitModel1 fit")
    print("-------------------------------")
    print(" ")
# Model is a single parameter model y(x) = a0
    lsq = MyLeastSquares.LsqDriver(mymodels.quadmodel, x, y, dy)
    m = Minuit(lsq, a0 = 1.0, a1 = 0.0, a2 = 0.0)
    FixParameters(m, ["a1", "a2"])    
    GenericFit(m, lsq, len(x))
    
    y_model = mymodels.quadmodel(x, *m.values)
    
    return y_model
    
def FitModel2(x, y, dy):

    print(" ")
    print(" ")
    print("-------------------------------")
    print("Running fitconfig.FitModel2 fit")
    print("-------------------------------")
    print(" ")
# Model is a single paramerer model with y(x) = 0.95 + a1*x
    lsq = MyLeastSquares.LsqDriver(mymodels.quadmodel, x, y, dy)
    m = Minuit(lsq, a0 = 0.95, a1 = 0.0, a2 = 0.0)
    FixParameters(m, ["a0", "a2"])    
    GenericFit(m, lsq, len(x))
    
    y_model = mymodels.quadmodel(x, *m.values)
    
    return y_model
    
def FitModel3(x, y, dy):

    print(" ")
    print(" ")
    print("-------------------------------")
    print("Running fitconfig.FitModel3 fit")
    print("-------------------------------")
    print(" ")
# Model is a single parameter model with y(x) = 0.95 + a2*x**2  
    lsq = MyLeastSquares.LsqDriver(mymodels.quadmodel, x, y, dy)
    m = Minuit(lsq, a0 = 0.95, a1 = 0.0, a2 = 0.0)
    FixParameters(m, ["a0", "a1"])    
    GenericFit(m, lsq, len(x))
    
    y_model = mymodels.quadmodel(x, *m.values)
    
    return y_model
    
def FitModel4(x, y, dy):

    print(" ")
    print(" ")
    print("-------------------------------")
    print("Running fitconfig.FitModel4 fit")
    print("-------------------------------")
    print(" ")
 # Model is y(x) = a0 + a1*x   (2-parameters)
    lsq = MyLeastSquares.LsqDriver(mymodels.quadmodel, x, y, dy)
    m = Minuit(lsq, a0 = 0.95, a1 = 0.0, a2 = 0.0)
    FixParameters(m, ["a2"])    
    GenericFit(m, lsq, len(x))
    
    y_model = mymodels.quadmodel(x, *m.values)
    
    return y_model    
    
def FitModel5(x, y, dy):

    print(" ")
    print(" ")
    print("-------------------------------")
    print("Running fitconfig.FitModel5 fit")
    print("-------------------------------")
    print(" ")
# Model is y(x) = a0 + a1*x + a2*x**2 (3 parameters)   
    lsq = MyLeastSquares.LsqDriver(mymodels.quadmodel, x, y, dy)
    m = Minuit(lsq, a0 = 1.0, a1 = 0.0, a2 = 0.0)
    GenericFit(m, lsq, len(x))
    
    y_model = mymodels.quadmodel(x, *m.values)
    
    return y_model
    
def FitModel6(x, y, dy):

    print(" ")
    print(" ")
    print("-------------------------------")
    print("Running fitconfig.FitModel6 fit")
    print("-------------------------------")
    print(" ")
# Model is y(x) = a0 + a2*x**2 (2 parameters)   
    lsq = MyLeastSquares.LsqDriver(mymodels.quadmodel, x, y, dy)
    m = Minuit(lsq, a0 = 1.0, a1 = 0.0, a2 = 0.0)
    FixParameters(m, ["a1"]) 
    GenericFit(m, lsq, len(x))
    
    y_model = mymodels.quadmodel(x, *m.values)
    
    return y_model    
