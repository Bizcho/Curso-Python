#funcionvaloresdefecto.py

def myfunc(a = 4, b = 6):
    sum = a + b
    return sum
print myfunc()
print myfunc(b = 1) #a es 4, sobreescribir b a 8 