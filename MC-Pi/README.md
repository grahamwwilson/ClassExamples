# ClassExamples/MC-Pi

## Monte Carlo calculation of pi
Several implementations with improving functionality.

## Circle.py
Original basic implementation.  With one "experiment".

## NewCircle.py
Uses Pie.py and its PieEstimate function with 
a tuple return argument to conduct multiple experiments 
using ROOT to histogram the results.
The PiEstimate function is essentially the code of Circle.py refactored 
into its own function.

## ntCircle.py
Uses PieNamedTuple.py and its PieEstimate function based on the 
NamedTuple module of the typing package to conduct multiple experiments.
This returns an Estimator class and ROOT is used 
to histogram the results. This is provided in case you have version 
compatibility issues with DataClasses (see below) which I recommend.

## dcCircle.py
Uses PieDataClass.py and its PieEstimate function based on the 
dataclass module of the dataclasses package to conduct multiple experiments.
This returns an Estimator class and ROOT is used 
to histogram the results. The dataclass language feature needs python 3.7+.

## NOTES
The class based approach avoids hard-coding in the histogramming part, and is 
better practice. What is rather neat is that the dataclass syntax avoids 
the usual verbosity and details usually associated with using classes. 
Here it has been used mostly just for Plain Old Data (POD) but one can 
add also methods/member functions.
