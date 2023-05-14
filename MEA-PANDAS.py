#Universidad del Valle
#Algoritmos y Programacion Basica
#Vianka Castro 23201
#Nadissa Vela 23764
#Ejercicio 05 - MEA y PANDAS


import pandas as pd
import matplotlib.pyplot as plt
import os
#from matplotlib import rcParams
#import seaborn as sns

movies = pd.read_csv('movies2023-1.csv', sep=',', low_memory=False, index_col=False)


#1
def mostrarInfo():
    print("*" * 30)
    print("Informacion de Peliculas por Año!")
    print("*" * 30)
    year = input("Ingrese el año de peliculas que desea: \n >")
    df1 = pd.DataFrame(movies, columns=['primaryTitle', 'principalGenre','directorName','startYear'])
    ok1 = pd.DataFrame(df1.query("startYear=="+ year)).sort_values(by=['primaryTitle'], ascending=False, ignore_index=True)
    print("*" * 30)
    print("LAS PELICULAS DEL AÑO ", year, "SON:")
    print("*" * 30)
    print (ok1)
    menu()

#2
def tops():
    print("*" * 30)
    print("Top de Votos!")
    print("*" * 30)
    n = int(input("Ingrese la cantidad de peliculas que desea en el top: \n >"))
    gen = input("Ingrese el genero que desea en el top: \n >")
    df2 = pd.DataFrame(movies, columns=['primaryTitle', 'principalGenre','averageRating'])
    print("*" * 30)
    print("El TOP", n, "DE PELICULAS DE ", gen.upper(), "ES:")
    print("*" * 30)
    print(df2[df2.principalGenre.str.contains(gen, na=False)].sort_values(by=['averageRating'], ascending=False, ignore_index =True).head(n))
    menu()

#3
def peliYear():
    print("*" * 30)
    print("Top de Generos por Año!")
    print("*" * 30)
    year1 = input("Ingrese el año de peliculas que desea: \n >")
    df3 = pd.DataFrame(movies, columns=['primaryTitle', 'principalGenre','startYear'])
    ok3 = pd.DataFrame(df3.query("startYear==" + year1 + "and principalGenre in ('Adventure','Action','Mystery','Horror','Thriller') ")).sort_values(by=['primaryTitle'], ascending=False, ignore_index=True)
    print("*" * 30)
    print("El TOP DE PELICULAS EN EL AÑO", year1, "SON:")
    print("*" * 30)
    print(ok3)
    menu()

#4
#el promedio de duración en minutos de las películas de un género principal determinado que ingrese el usuario
def minMean():
    print("*" * 30)
    print("Duracion de minutos en un genero!")
    print("*" * 30)
    gen = input("Ingrese el genero que desea en el promedio: \n >")
    df4 = pd.DataFrame(movies, columns=['principalGenre','runtimeMinutes'])
    ok4 = df4[df4.principalGenre.str.contains(gen, na=False)].groupby('principalGenre').mean()
    print("*" * 30)
    print("El PROMEDIO DEL GENERO ", gen.upper(), "ES DE:")
    print("*" * 30)
    print(ok4)
    menu()
#5
# Cantidad peliculas por año de lanzamiento
def peliYearCount():
    df5 = pd.DataFrame(movies, columns=['startYear'])
    ok5 = df5.groupby('startYear').size().reset_index(name='Total')#.tail(50)
    print(ok5)

#6 mostrar grafico de barras con la info anterior.
def graphVoto():
    ax = ok5.plot.barh(x='startYear', y='Total', rot=0)
    ax.plot(kind = 'bar')
    plt.show()


#7 top con mas votos
def votosMean():
    df7 = pd.DataFrame(movies, columns=['primaryTitle','numVotes'])
    ok7 = df7.sort_values(by=['numVotes'], ascending=False, ignore_index=True).head(5)
    print(ok7)

#8 Mostrar pelis de un director especifico
def peliEscritor():
    print("*" * 30)
    print("Peliculas de un Escritor!")
    print("*" * 30)
    nombre = input("Ingrese el nombre del Escritor: \n >")
    df8 = pd.DataFrame(movies, columns=['directorName', 'primaryTitle'])
    print("*" * 30)
    print("PELICULAS POR ",nombre.upper(), "SON:")
    print("*" * 30)
    print(df8[df8.directorName.str.contains(nombre, na=False)].sort_values(by=['directorName'], ascending=False, ignore_index=True))
    menu()


#9 Directores que tienen una mayor cantidad de pelis
def topEscritores():
    df9 = pd.DataFrame(movies, columns=['directorName'])
    ok9 = pd.DataFrame(df9.groupby('directorName').size().reset_index(name='Total')).sort_values(by=['Total'],ascending=False,ignore_index=True).head(50)
    print(ok9)

#10 Directores que no son directores
def topNoEscritores():
    df10 = pd.DataFrame(movies, columns=['directorName', 'director1stProfession'])
    dff10 = df10[['directorName','director1stProfession']].groupby(['directorName','director1stProfession'],dropna=True)['directorName'].size().reset_index(name='Count')
    print(dff10[~dff1-director1stProfession.str.contains('director', na=False)].sort_values(by=['directorName','director1stProfession'], ascending=False,ignore_index=True).head(50))


def signIn():
    
    if os.path.isfile('usuarios.csv'):
        #leo el archivo y agrego un nuevo usuario
        print("\n")
        print("*" * 30)
        print('Crear cuenta')
        print("*" * 30)
        dfUsuario = pd.read_csv('usuarios.csv')
        ultimaFila = dfUsuario.tail(1)
        ultimoId = int(ultimaFila['idUsuario'].values[0])
        nombre = input ('Ingrese su nombre: ')
        apellido = input ('Ingrese su apellido: ')
        correo = input ('Ingrese su correo: ')
        password = input('Ingrese su contraseña: ')
        datos = {
            'idUsuario': (ultimoId + 1),
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'password': password,
        }
        dfUsuario = pd.concat([dfUsuario, pd.DataFrame(datos, index=[0])], ignore_index=True)
        dfUsuario.to_csv('usuarios.csv', index=False)
        print("\nUsuario creado correctamente!")
        menu1()
        
    else:
        #primer usuario
        print("\n")
        print("*" * 30)
        print('Crear cuenta')
        print("*" * 30)
        nombre = input ('Ingrese su nombre: ')
        apellido = input ('Ingrese su apellido: ')
        correo = input ('Ingrese su correo: ')
        password = input('Ingrese su contraseña: ')
        datos = {
            'idUsuario': 1,
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'password': password,
        }
        dfUsuario = pd.DataFrame(datos, index =[0])
        dfUsuario.to_csv('usuarios.csv', index=False)
        print("\nUsuario creado correctamente!")
        menu1()

def logIn():
    print("\n")
    print("*" * 30)
    print("Iniciar Sesión")
    print("*" * 30)
    email = input("Ingrese su correo: ")
    password = input("Ingrese su contraseña: ")
    dfUsuario = pd.read_csv('usuarios.csv')
    usuario = dfUsuario.loc[(dfUsuario['correo'] == email) & (dfUsuario['password'] == password)]
    if ((dfUsuario['correo'] == email) & (dfUsuario['password'] == password)).any():
        print("\nBienvenid@ " + usuario['nombre'].values[0] + " " + usuario['apellido'].values[0] +"!")
        menu()
    else:
        print("\nCredenciales incorrectas")
        menu1()
    
def menu1():
    print("*" * 30)
    print("BIENVENIDO A CINEPOLIS+!!")
    print("*" * 30)
    print(" 1. Crear Cuenta \n 2. Iniciar Sesion \n 3. Salir")
    opcion1 = input("Elige una opcion: \n > ")
    if opcion1 == "1":
        signIn()
    elif opcion1 == "2":
        logIn()
    elif opcion1 == "3":
        print("-" * 50)
        print("Gracias por usar Cinepolis+ !")
        exit()
    else:
        print("-" * 50)
        print("Ingrese un numero correcto ")
        print("-" * 50)
        menu1()


def menu():
    print("*" * 30)
    print("Bienvenido a las opciones!")
    print("*" * 30)
    print(" 1. Mostrar Informacion \n 2. Tops de peliculas \n 3. Peliculas del año \n 4. Promedio de Minutos \n 5. Promedio de Votos \n 6. Grafica de Promedio de Votos \n 7. Top Rating \n 8. Peliculas segun Escritor \n 9. Top Escritores \n 10. Top de escritores que no son escritores \n 11.  Favoritos \n 12. Recomendaciones \n 13. Salir")
    print("*" * 30)
    opcion = input("Elige una opcion: \n > ")

    if opcion == "1":
        #mostrar informacion
        mostrarInfo()
    elif opcion == "2":
        #Top de peliculas segun votos
        tops()
    elif opcion == "3":
        #Peliculas del año
        peliYear()
    elif opcion == "4":
        #promedio de duracion de peliculas segun genero
        minMean()
    elif opcion == "5":
        #Promedio de Votos segun un genero especifico
        votosMean()
    elif opcion == "6":
        #Grafia de la opcion 4
        graphVoto()
    elif opcion == "7":
        #Top Rating averageRating
        rating()
    elif opcion == "8":
        #Peliculas segun un Escritor
        peliEscritor()
    elif opcion == "9":
        #Top de Escritores segun mas peliculas
        topEscritores()
    elif opcion == "10":
        #Top de escritores que no son escritores xd
        topNoEscritores()
    elif opcion == "11":
        # Agregar pelicula a Favoritos
        fav()
    elif opcion == "12":
        # Recomendar pelicuals segun el genero
        recomendar()
    elif opcion == "13":
        #Regresar a menu1
        menu1()
    else:
        print("-" * 50)
        print("Ingrese un numero correcto ")
        print("-" * 50)
        menu()

menu1()
