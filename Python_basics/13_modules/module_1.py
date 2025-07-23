# a module is a file containing a block of code.
# the purpose of it is to reuse it across different projects.
# for instance, math or time are built in Python modules.
# you can create your own module by defining functions in it
# then, you import it and use these functions.
#
# it is used for both modularity and also information hiding,
# although the concept is better explained in C via the use of headers and implementation
#
# there are several ways to import a module:
#   1.  import math
#   2.  import math as m (to change locally the name of the module)
#   3.  from math import pi (to import a specific thing from the module)
from math import pi # note that it can create naming issues if not carefully used

print(pi)