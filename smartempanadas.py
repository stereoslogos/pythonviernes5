sentinel=100

#while
print("")
print("MENU")
print("1 - Create 1 Empanada")
print("2 - Show Empanada")
print("3 - Exit")
print("")

empanadas={}
ingredients=[]

while sentinel!=3:
    sentinel=int(input("Type 1, 2 or 3: "))
    if sentinel == 1:
        empanadas["name"]=input('Add a name to it: ')
        ingredients[ingredients]
        empanadas["ingredients",0]=input('Add an ingredient: ')
        empanadas["ingredients",1]=input('Add an ingredient: ')
        empanadas["ingredients",2]=input('Add an ingredient: ')
        empanadas["priceFac"]=input('Add a Factory price: ')
        empanadas["priceSal"]=input('Add a Sales price: ')
    elif sentinel == 2:
        print(empanadas)
    elif sentinel == 0:
        break
    else:
        print("Try 1, 2 or 0!")
else:
    print("Done!")