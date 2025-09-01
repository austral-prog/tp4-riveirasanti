def leap_year():
   anio=int(input("Ingrese un año: "))
   if (anio % 4 == 0) and ((anio % 100 != 0) or (anio % 400 == 0)):
       print(f"El año {anio} es bisiesto") 
   else:
       print(f"El año {anio} no es bisiesto")    

if __name__ == "__main__":

    leap_year()       
