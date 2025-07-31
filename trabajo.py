
boo= True
arr=[0,1]

while(boo):
    
    print("Presione 1 para imprimir n terminos de la sucesiòn")
    print("Presione 2 para imprimir el n-èsimo termino de la sucesiòn")
    z=int(input("ELija una opciòn: "))

    if z==1:
        n=int(input("Ingrese el nùmero de tèrminos: "))
        a=0
        b=1
        for i in range(n):
            c=a+b
            a=b
            b=c
            arr.append(c)
        print(arr)
    elif z==2:
        n=int(input("Ingrese el n-èsimo termno: " ))
        a=0
        b=1
        for i in range(n):
            c=a+b
            a=b
            b=c
            arr.append(c)
        print(arr[i-1])


        
