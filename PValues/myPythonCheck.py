# myPythonCheck.py
import sys

# Require python3. In some code I've relied recently on python3 features like 12/5 = 2.4.
def Check():
    if sys.version_info[0] < 3: # I don't know that this is strictly necessary - but seems like good practice for my setup.
        raise Exception("I'm requiring the use of Python 3 or a more recent version")
