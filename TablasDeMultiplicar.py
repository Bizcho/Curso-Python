def imprimeTabla(num):
    print "Tabla del numero", num
    for i in range(1, 11):
        print i, "x", num, "=", i * num
    print "\n"
print "Tablas de multiplicar usando funciones"
for tabla in range(1, 11):
    imprimeTabla(tabla)
print "\n"
        