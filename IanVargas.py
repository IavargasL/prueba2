CarillasPo=250000
ImplantesD=475000
OrtodonciaB=800000
Subtotal=0
DescuentoA=15
DescuentoAd=10
DescuentoDo=5
Cuotasmen=12
Total=0
cant1=0
cant2=0
cant3=0
print("*"*30)
print("BIENVENIDO AL DIENTE DE ORO ")
print("*"*30)
while True:
    print(""""
    1.- Cotización
    2.- Renunciar 
    3.- Salir""")
    opc=int(input("Ingrese opción : "))
    if opc==1:
        print("""
        Estos son los tratamientos que tenemos: 
1.- Carillas Porcelana
2.- Implantes Dentales
3.- Ortodoncia Dentales""")
        opc1=int(input("Ingrese tratamiento : "))
        if opc1==1:
            cant1=int(input("Ingrese la cantidad de tratamientos : "))
            cant1*CarillasPo
            Subtotal+CarillasPo
        if opc1==2:
            cant2=int(input("Ingrese la cantidad de tratamientos : "))
            cant2*ImplantesD
            Subtotal+ImplantesD
        if opc1==3:
            cant3=int(input("Ingrese la cantidad de tratamientos : "))
            cant3*OrtodonciaB
            Subtotal+OrtodonciaB
        Descuento=int(input("Usted tiene descuento? : 1.-[SI] 2.-[NO] : "))
        if Descuento==1:
            print("*"*30)
            print("Tipos de Descuentos")
            print("""
1.-Trabajador Auxiliar
2.-Trabajador Administrativo
3.-Trabajador Docente""")
            opcD=int(input("Ingrese tipo de descuento : "))
            if opcD==1:
                Total=DescuentoA/Subtotal
                print("Su total es ",Total)
            if opcD==2:
                Total=Subtotal/DescuentoAd
            if opcD==3:
                Total=Subtotal/DescuentoDo
            print("El total de la cotizacion es" ,Total)
        if Descuento==2:
            print("Precio sin descuento",Subtotal)
        print(f"""
        -----------------------------------------------------------
                                Cotización
        -----------------------------------------------------------
        -->{cant1} Carillas   Porcelana      ${CarillasPo}
        -->{cant2} Implantes  Dentales       ${ImplantesD}
        -->{cant3} Ortodoncia Dentales       ${OrtodonciaB}
        -----------------------------------------------------------
        SubTotal            ${Subtotal}
        Descuento           ${Total}
        -----------------------------------------------------------
        Total               ${Total}
        -----------------------------------------------------------
        Son 12 cuotas de    ${Total/Cuotasmen}
        
        Sonría Bonito!!!""")
    if opc==2:
        print("""
        1.- Eliminar la cotización""")
    Reopc=int(input("Eliga la opción : "))
    if Reopc==1:
        print("Cotización ha sido eliminada con éxito!!")
    
   