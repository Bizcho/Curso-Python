#variableslocalesglobales.py

a, b = 2, 3
def algo():
    global a
    a, b = 4, 4
    print a, b
print a, b
algo()
print a, b