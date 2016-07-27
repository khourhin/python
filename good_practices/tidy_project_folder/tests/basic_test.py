import os
import sys
# Add the path to the module to be tested
sys.path.insert(1, os.path.abspath('..'))
from a_module.basic import say_hi

say_hi()
