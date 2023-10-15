#Librerías usadas
from tkinter import*    #GUI
from tkinter import messagebox  #Ventanas emergentes
import os   #Manejo de archivos
#Constantes a usar
CARPETA = "contactos/"
EXTENSION = ".txt"
ICONO = "pelota.ico"

#Clase contacto: ¿Que datos y operaciones hacemos en torno al objeto contacto
class Contacto:
    def __init__(self, nombre, telefono, categoria):    #Contrsuctor para llenar datos del contacto
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

#------Funciones correspondientes a la logica de la aplicacion------
#Creando directorio
def crear_directorio():
        if not os.path.exists(CARPETA):    #Si la carpeta 'contactos' no existe entonces...
            #Crear la carpeta
            os.makedirs(CARPETA)
            #Esto sirve para que el usuario no esté creando manualmente la carpeta

#Comprobando si un contacto existe o no (en base a carpetas)
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

#Funcion para agregar contactos
def agregar_contacto(nombre_contacto, telefono_contacto, categoria_contacto):
    #print("Escribe los datos para agregar el nuevo contacto: ")
    #nombre_contacto = input('Nombre del contacto:\r\n')
    #Verificando si un contacto ya existe o no
    existe = existe_contacto(nombre_contacto)
    if not existe:
    #Generando el archivo txt con el nombre del contacto, dentro de la carpeta "contactos"
    #Tener en cuenta la ubicacion del archivo, la cual es:
    #contactos/nombre_contacto.txt
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            #Resto de los campos
            #telefono_contacto = input('Agrega el teléfono:\r\n')
            #categoria_contacto = input('Categoria del contacto:\r\n')
            #Instanciar la clase
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
            #Escribiendo el contenido del archivo txt
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')
            #Mostrar un mensaje de éxito
            messagebox.showinfo("Información", "Contacto creado correctamente")
            print('\r\nContacto creado correctamente\r\n')
    else:
        print('Ese contacto ya existe') #No se reescribirá, messagebox
        messagebox.showwarning("Error", "El dato que quieres agregar ya existe")

#Funcion para editar contactos
def editar_contacto(nombre_anterior, nombre_contacto, telefono_contacto, categoria_contacto):
    #print('Escribe el nomnbre del contacto a editar:\r\n')
    #nombre_anterior = input('Nombre del contacto que desea editar:\r\n')
    #Verificando si un contacto ya existe o no (Se hizo una funcion de existencia)
    existe = existe_contacto(nombre_anterior)
    if existe:  #Si existe el contacto, se puede editar...
        #Se puede usar funcion de creacion de archivos
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #nombre_contacto = input('Agregue el nuevo nombre\r\n')
            #telefono_contacto = input('Agrega el nuevo teléfono:\r\n')
            #categoria_contacto = input('Agrega la nueva categoría:\r\n')
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')
            #Juan habia puesto el metodo os.rename aqui...
        #Renombrar el archivo (Usé os.renames)
        os.renames(CARPETA + nombre_anterior + EXTENSION,CARPETA + nombre_contacto + EXTENSION)
        print('\r\nEl contacto se editó correctamente\r\n')
        messagebox.showinfo("Información", "El contacto se editó correctamente")
    else:   #Si no existe, pues...
        print('No puedes editar, el contacto no existe')
        messagebox.showwarning("Error", "El contacto que desea editar no existe")

#Funcion para mostrar contactos
#Opcion 1: Mostrar en un Label o Entry los datos del contacto
#Opcion 2: Abrir el archivo txt
def mostrar_contactos():
    #Ver el video de nuevo con más detalle
    #Listando los archivos de un directorio
    archivos = os.listdir(CARPETA)
    #Validando únicamente archivos txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    #Mensaje
    messagebox.showinfo("Información", "Mostrando los contactos y sus datos en la consola...")
    print("---Lista de contactos---")

    #Recorriendo los archivos txt
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            #Recorriendo en cada línea
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rstrip())   #Eliminando espacios en blanco
            #Imprime un separador entre contactos
            print('\r\n')

#Funcion para buscar contactos
def buscar_contacto(nombre):
    #nombre = input('Seleccione el contacto que desea buscar:\r\n')
    #Mensajes de error (El archivo buscado no existe)
    #Normalmente se usa try-catch
    #Gasta un poco mas de memoria que un if-else
    #Hacerlo en lugares donde pueda haber un error
    try:    #Se ejecuta normalmente
        with open(CARPETA + nombre + EXTENSION) as contacto:
            messagebox.showinfo("Información", "Mostrando los datos del contacto en la consola...")
            print('Informacion del contacto:\r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError: #Se ejecuta en caso de error del programa
        print('El archivo no existe')
        print(IOError)
        messagebox.showwarning("Error", "El contacto buscado no existe")

#Funcion para eliminar contactos
def eliminar_contacto(nombre):
    #nombre = input('Escribe el contacto que desea eliminar:\r\n')
    try:
        #Eliminar archivo
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEl contacto ha sido eliminado con éxito\r\n')
        messagebox.showinfo("Información", "El contacto ha sido eliminado con éxito")
    except IOError:
        print('No existe ese contacto')
        print(IOError)
        messagebox.showwarning("Error", "El contacto que desea eliminar no existe")
    #Reiniciar la app

#--------------------------------------------------------------------

#Se agregan nuevas ventanas en realidad
#------Ventanas que se usaran en el programa------
def ventanaAgregar():
    print("Agregando contacto...")
    #raiz.withdraw() #Cerrando el menú, para dar paso a otra ventana

    agregar = Tk()
    agregar.title("Agregando")
    agregar.iconbitmap(ICONO)

    miFrame = Frame(agregar)
    miFrame.pack()

    cuadroNombre = Entry(miFrame)   #ENTRADA: Nombre del contacto que desea agregar
    cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
    nombreLabel = Label(miFrame, text = "Nombre:")
    nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    cuadroTelefono = Entry(miFrame) #ENTRADA: Telefono del contacto
    cuadroTelefono.grid(row=1, column=1, padx=10, pady=10)
    telefonoLabel = Label(miFrame, text = "Teléfono:")
    telefonoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    cuadroCategoria = Entry(miFrame)    #ENTRADA: Categoria del contacto
    cuadroCategoria.grid(row=2, column=1, padx=10, pady=10)
    categoriaLabel = Label(miFrame, text = "Categoria:")
    categoriaLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    Button(agregar, text="Agregar", command=lambda: agregar_contacto(cuadroNombre.get(), cuadroTelefono.get(), cuadroCategoria.get())).pack()  #ENTRADA: Confirmación
    agregar.mainloop()

def ventanaEditar():
    print("Editando contacto...")
    agregar = Tk()
    agregar.title("Editar")
    agregar.iconbitmap(ICONO)

    miFrame = Frame(agregar)
    miFrame.pack()

    cuadroNombreAnterior = Entry(miFrame)   #ENTRADA: Nombre del contacto que desea agregar
    cuadroNombreAnterior.grid(row=0, column=1, padx=10, pady=10)
    nombreAnteriorLabel = Label(miFrame, text = "Nombre anterior:")
    nombreAnteriorLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    cuadroNombre = Entry(miFrame)   #ENTRADA: Nombre del contacto que desea editar
    cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
    nombreLabel = Label(miFrame, text = "Nombre nuevo:")
    nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    cuadroTelefono = Entry(miFrame) #ENTRADA: Telefono del contacto
    cuadroTelefono.grid(row=2, column=1, padx=10, pady=10)
    telefonoLabel = Label(miFrame, text = "Teléfono:")
    telefonoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    cuadroCategoria = Entry(miFrame)    #ENTRADA: Categoría del contacto
    cuadroCategoria.grid(row=3, column=1, padx=10, pady=10)
    categoriaLabel = Label(miFrame, text = "Categoria:")
    categoriaLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

    Button(agregar, text="Editar", command=lambda: editar_contacto(cuadroNombreAnterior.get(), cuadroNombre.get(), cuadroTelefono.get(), cuadroCategoria.get())).pack()   #ENTRADA: Confirmación
    agregar.mainloop()    

def ventanaVer():
    print("Mostrando contactos...")
    #SALIDA: MOSTRAR LOS CONTACTOS EN UNA VENTANA

def ventanaBuscar():
    print("Buscando contacto...")
    agregar = Tk()
    agregar.title("Búsqueda")
    agregar.iconbitmap(ICONO)

    miFrame = Frame(agregar)
    miFrame.pack()

    cuadroNombre = Entry(miFrame)   #ENTRADA: Nombre del contacto que se desea buscar
    cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
    nombreLabel = Label(miFrame, text = "Nombre del contacto que busca:")
    nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    #nombreBusqueda = Label(miFrame, text="Datos del contacto")
    #nombreBusqueda.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    #nombre = Label(miFrame, text="Nombre: ")
    #nombre.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    #telefono = Label(miFrame, text="Telefono: ")
    #telefono.grid(row=3, column=0, sticky="e", padx=10, pady=10)

    #categoria = Label(miFrame, text="Categoria: ")
    #categoria.grid(row=4, column=0, sticky="e", padx=10, pady=10)
    
    Button(agregar, text="Buscar", command=lambda:buscar_contacto(cuadroNombre.get())).pack()   #ENTRADA: Confirmación
    #SALIDA: MOSTRAR LOS DATOS DEL CONTACTO CONSULTADO
    agregar.mainloop()

def ventanaEliminar():
    print("Eliminando contacto...")
    agregar = Tk()
    agregar.title("Eliminar")
    agregar.iconbitmap(ICONO)
    
    miFrame = Frame(agregar)
    miFrame.pack()

    cuadroNombre = Entry(miFrame)   #ENTRADA: Nombre del contacto que se desea eliminar
    cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
    nombreLabel = Label(miFrame, text = "Nombre del contacto que desea eliminar:")
    nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

    Button(agregar, text="Eliminar", command=lambda: eliminar_contacto(cuadroNombre.get())).pack() #ENTRADA: Confirmación
    agregar.mainloop()

#(Funcion de prueba para mostrar que los datos ingresados en los Entry se guardan)
def mostrar(a,b,c):
    print(f"Número: {a}")
    print(f"Teléfono: {b}")
    print(f"Categoría: {c}")
    messagebox.showinfo("Información", "Datos agregados correctamente")

#def salirAplicacion():  #Salir de la aplicación
    #raiz.destroy()

def ventanaMenu():
    
    raiz=Tk()
    raiz.title("Contactos")
    raiz.iconbitmap(ICONO)
    raiz.config(bg="yellow")


    miFrame = Frame(raiz)
    #miFrame.config(width="650", height="650")
    miFrame.pack(fill="none", expand="True")
    miFrame.config(bg="blue")
    
    

    botonAgregarNuevoContacto = Button(miFrame, text="Agregar nuevo contacto", command=lambda: ventanaAgregar())  #ENTRADA: Confirmación
    botonAgregarNuevoContacto.grid(row=0, column=0, padx=10, pady=10)
    botonAgregarNuevoContacto.config(background="red", fg="white")
    
    botonEditarContacto = Button(miFrame, text="Editar contacto", command=ventanaEditar)    #ENTRADA: Confirmación
    botonEditarContacto.grid(row=1, column=0, padx=10, pady=10)
    botonEditarContacto.config(background="red", fg="white")
    
    botonVerContactos = Button(miFrame, text="Ver contactos", command=lambda: mostrar_contactos())   #ENTRADA: Confirmación
    botonVerContactos.grid(row=2, column=0, padx=10, pady=10)
    botonVerContactos.config(background="red", fg="white")
    
    botonBuscarContactos = Button(miFrame, text="Buscar contacto", command=ventanaBuscar)   #ENTRADA: Confirmación
    botonBuscarContactos.grid(row=3, column=0, padx=10, pady=10)
    botonBuscarContactos.config(background="red", fg="white")
    
    botonEliminarContacto = Button(miFrame, text="Eliminar contacto", command=ventanaEliminar)  #ENTRADA: Confirmación  
    botonEliminarContacto.grid(row=4, column=0, padx=10, pady=10)
    botonEliminarContacto.config(background="red", fg="white")
    
    botonSalir = Button(miFrame, text="Salir de la aplicación", command=raiz.destroy)   #ENTRADA: Confirmación
    botonSalir.grid(row=5, column=0, padx=10, pady=10)
    botonSalir.config(background="red", fg="white")
    
    raiz.mainloop()
#---------------------------------------------------

#------Aplicacion del programa------
#Creando directorio
crear_directorio()
#Mostrando la ventana de Menú
ventanaMenu()
#------------------------------------

