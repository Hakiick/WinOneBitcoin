"""import random

coucou = random.randint(2500, 7200)
print(coucou)"""

"""import random 

x=[1,3,6,7] 
print(random.choices(x)) 
# Output is (1 or 3 or 6 or 7). 
print (random.__file__)
"""

import random 
from random import choices
from numpy.random import choice
  
sampleList = [100, 200, 300, 400, 500]
randomNumberList = choices(
  sampleList, 5, p=[0.05, 0.1, 0.15, 0.20, 0.5])
  
print(randomNumberList)