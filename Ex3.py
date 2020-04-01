def pow(nombre,puissance):
    if puissance==0:
        return 1
    if puissance ==1:
        return nombre
    else:
        return nombre*pow(nombre,puissance-1)




print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49
