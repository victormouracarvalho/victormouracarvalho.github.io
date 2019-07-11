import math
import random as rnd
from hashlib import sha256
import inicio as boba 

alpha = list((a/10)*2*math.pi for a in range (11))
print(alpha)
print(list(map(math.cos, alpha)))




def dado():
    """
    simula dados de 6 faces
    """
    return rnd.randint(1, 6) 

for i in range(10):
    print(dado())

print(sha256(b'Igor Peretta').hexdigest())

print(boba.divisainteira(15,6))

