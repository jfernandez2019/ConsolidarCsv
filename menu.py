from consolidar import consolidar;
from consumir_archivo import consumir_archivo;
def mostrar_menu():
    print("=============MENU=============")
    print("1 - CONSOLIDAR ARCHIVO")
    print("2 - CONSUMIR ARCHIVO")
    print("90 - SALIR")
    print("==============================")
    
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            consolidar()
        elif opcion == "2":
            consumir_archivo()
        elif opcion == "90":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
        print()  # Para dar un espacio entre iteraciones del menú

if __name__ == "__main__":
    main()