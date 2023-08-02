#importamos la libreria random para que nos de numeros aleatorios
import random
#Definimos la funcion lanzar_dado para que haga la simulacion y utilizamo la funcion return random.randint (1,6)
#para que nos de valores que van de los numeros del 1 al 6 aleatoriamente simulando así un dado de 6 caras
def lanzar_dado():
    return random.randint(1, 6)
#Definimos la funcion main que se encarga de interactuar con el ususario y así mostrar los resultados, tambien mostramos
#un mensaje de bienvenida y le pedimos al usuario que ingrese la cantidad de lanzamientos y guardamos ese valor 
#en la variable num_lanzamientos
def main():
    print("Simulador de Dados")
    num_lanzamientos = int(input("Ingrese la cantidad de lanzamientos: "))
    
#Utilizamos una comprensión de listas para generar los resultados de los lanzamientos. La expresión 
#[lanzar_dado() for _ in range(num_lanzamientos)] genera una lista con num_lanzamientos elementos, 
# donde cada elemento es el resultado de llamar a la función lanzar_dado()
    resultados = [lanzar_dado() for _ in range(num_lanzamientos)]
    
#Imprimimos un mensaje indicando que mostraremos los resultados de los lanzamientos
    print("\nResultados de los lanzamientos:")
#Usamos un bucle for junto con enumerate(resultados, 1) para recorrer la lista de resultados y 
#mostrar cada lanzamiento junto con su número. La función enumerate() agrega un contador a la lista resultados
#y comenzamos en 1 con el argumento 1, de esta forma mostramos "Lanzamiento 1:", "Lanzamiento 2:", y así sucesivamente
    for i, resultado in enumerate(resultados, 1):
        print(f"Lanzamiento {i}: {resultado}")

if __name__ == "__main__":
    main()
