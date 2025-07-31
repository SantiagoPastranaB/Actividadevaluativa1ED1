
boo= True
arr=[0,1]
arr2=[]
acu=0

while(boo):
    
    print("Presione 1 para imprimir n terminos de la sucesiòn")
    print("Presione 2 para imprimir el n-èsimo termino de la sucesiòn")
    print("Presione 3 para sumar el array")
    print("Presione 4 para salir")

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
    elif z==3:
        p=int(input("Ingrese el tamaño del array: "))

        while p>0:
            g=int(input("Ingrese un valor: "))
            arr2.append(g)
            p=p-1
        for i in arr2:
            acu=acu+i
        print(acu)
    elif z==4:
        print("Saliendo...")
        boo=False
    else:
        print("Error de digitaciòn")           

            
        