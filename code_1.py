import math
from rich.console import Console
from scipy.stats import chi2
from scipy.stats import norm
import numpy as np
from colorama import Fore, Style
from rich.table import Table

console = Console()
def uniformidad():
  table=Table(show_header=True, header_style="bold magenta")
  table.add_column("Intervalo", style="green", width=12)
  table.add_column("O", style="green", width=12)
  table.add_column("E=n/m", style="green", width=12)
  table.add_column("Intervalo", style="green", width=12)
  table.add_column("((E-O)^2)/E", style="green", width=12)

  console.print(table)

def varianza(confianza,numerosAleatorios):
  
  significancia=(1-confianza)/2
  alpha=significancia+confianza
  data=numerosAleatorios
  gradosLibertad=len(data)-1
  
  l1=chi2.ppf(1-alpha, gradosLibertad)
  l2=chi2.ppf(alpha, gradosLibertad)
  varianza = np.var(data, ddof=1)
  console.print(l1/(12*(gradosLibertad)))
  console.print("varianza ", varianza)
  console.print(l2/(12*(gradosLibertad)))

def media(datos,confianza):
  
  table=Table(show_header=True, header_style="bold blue")
  table.add_column("Limite Inferior", style="green", width=12)
  table.add_column("Media", style="green", width=12)
  table.add_column("Limite Superior", style="green", width=12)
  

  significancia=(1-confianza)/2
  alpha=significancia+confianza
  n = len(datos)  # Número de elementos en la lista (equivalente a CONTAR)
  error_estandar = 1 / math.sqrt(12 * n)
  valor_critico = norm.ppf(alpha)  # Función inversa de la distribución normal estándar
  resultado1 = 0.5 - valor_critico * error_estandar
  resultado2 = 0.5 + valor_critico * error_estandar
  media=1/n*sum(datos)
  table.add_row(str(resultado1),str(media),str(resultado2))
  console.print(table)
  #console.print(resultado1)
  #console.print(media)
  #console.print(resultado2)

def cuadrados_medios(semilla, iteraciones):
  """
  Genera una secuencia de números pseudoaleatorios utilizando el método de los cuadrados medios.

  Args:
    semilla: Un número entero de tamaño par como semilla inicial.
    iteraciones: La cantidad de números aleatorios a generar.

  Returns:
    Una lista de números pseudoaleatorios.
  """

  numeros_aleatorios = []
  for _ in range(iteraciones):
    # Elevar al cuadrado y convertir a cadena
    cuadrado = str(semilla**2)

    # Añadir ceros a la izquierda si es necesario para mantener el tamaño
    while (len(cuadrado)-len(str(semilla))) % 2 != 0 :
      cuadrado = "0" + cuadrado

    # Extraer los dígitos centrales
    indice_inicio = int(((len(cuadrado) - len(str(semilla)))/2))
    indice_fin = indice_inicio + len(str(semilla))
    nuevo_numero = int(cuadrado[indice_inicio:indice_fin])

    # Añadir el nuevo número a la lista y actualizar la semilla
    nuevo_numero
    x=nuevo_numero/1000
    numeros_aleatorios.append(x)
    semilla = nuevo_numero

  return numeros_aleatorios

def productos_medios(semilla1, semilla2, iteraciones):
  """
  Genera una secuencia de números pseudoaleatorios utilizando el método de los productos medios.

  Args:
    semilla1: Primer número de la semilla inicial.
    semilla2: Segundo número de la semilla inicial.
    iteraciones: La cantidad de números aleatorios a generar.

  Returns:
    Una lista de números pseudoaleatorios.
  """

  numeros_aleatorios = []
  for _ in range(iteraciones):
    # Multiplicar las semillas
    producto = semilla1 * semilla2

    # Convertir a cadena y añadir ceros si es necesario
    producto_str = str(producto)
    while ((len(producto_str)-len(str(semilla1)))%2)!=0:
      producto_str = "0" + producto_str

    # Extraer los dígitos centrales
    indice_inicio = int(((len(producto_str) - len(str(semilla1)))/2))
    indice_fin = indice_inicio + len(str(semilla1))
    nuevo_numero = int(producto_str[indice_inicio:indice_fin])

    # Añadir el nuevo número a la lista y actualizar las semillas
    numeros_aleatorios.append(nuevo_numero/10000)
    semilla1 = semilla2
    semilla2 = nuevo_numero

  return numeros_aleatorios

def multiplicador_constante(semilla, constante, iteraciones):
  """
  Genera una secuencia de números pseudoaleatorios utilizando el método del multiplicador constante.

  Args:
    semilla: Número inicial para comenzar la generación.
    constante: Constante a multiplicar por la semilla.
    iteraciones: La cantidad de números aleatorios a generar.

  Returns:
    Una lista de números pseudoaleatorios.
  """

  numeros_aleatorios = []
  for _ in range(iteraciones):
    # Multiplicar la semilla por la constante
    producto = semilla * constante
    #print(producto)
    # Convertir a cadena y añadir ceros si es necesario
    producto_str = str(producto)
    while (len(producto_str) - len(str(semilla)))%2!=0:
      producto_str = "0" + producto_str

    # Extraer los dígitos centrales
    indice_inicio = int(((len(producto_str) - len(str(semilla)))/2))
    indice_fin = indice_inicio + len(str(semilla))
    nuevo_numero = int(producto_str[indice_inicio:indice_fin])

    # Añadir el nuevo número a la lista y actualizar la semilla
    numeros_aleatorios.append(nuevo_numero)
    semilla = nuevo_numero

  return numeros_aleatorios


def main():
  
  
  uniformidad() # prueba de como se ve una tabla

  while True:

    console.print("Cuadrados medios --- 1\nProductos medios --- 2\nMultiplicador constante --- 3\n")
    operacion = int(input("Elija una opcion de generacion de numeros pseudoaleatorios: "))
    
    if(operacion==1):
      console.print("----- CUADRADOS MEDIOS ----- \n")
      semilla = int(input("Inserte la semilla: "))
      iteraciones = int(input("Inserte el numero de iteraciones: "))

      numerosAleatorios=cuadrados_medios(semilla,iteraciones)

      console.print(numerosAleatorios)
      confianza = int(input("Nivel de confianza: "))/100
      confianza = int(input("Nivel de confianza: "))/100
      console.print("----   PRUEBAS DE MEDIAS-----")
      media(numerosAleatorios,confianza)
      console.print("----   PRUEBAS DE VARIANZA-----")
      varianza(confianza,numerosAleatorios)

      


    elif (operacion==2):
      console.print("----- PRODUCTOS MEDIOS ----- \n")
      semilla = int(input("Inserte la semilla 1: "))
      semilla2 = int(input("Inserte la semilla 2: "))
      iteraciones = int(input("Inserte el numero de iteraciones: "))

      numerosAleatorios=productos_medios(semilla,semilla2,iteraciones)

      console.print(numerosAleatorios)

      confianza = int(input("Nivel de confianza: "))/100
      console.print("----   PRUEBAS DE MEDIAS-----")
      media(numerosAleatorios,confianza)
      console.print("----   PRUEBAS DE VARIANZA-----")
      varianza(confianza,numerosAleatorios)

    else: 
      console.print("----- MULTIPLICADOR CONSTANTE ----- \n")
      semilla = int(input("Inserte la semilla: "))
      constante = int(input("Inserte la constante: "))
      iteraciones = int(input("Inserte el numero de iteraciones: "))

      numerosAleatorios=multiplicador_constante(semilla,constante,iteraciones)

      console.print(numerosAleatorios)
      confianza = int(input("Nivel de confianza: "))/100
      confianza = int(input("Nivel de confianza: "))/100
      console.print("----   PRUEBAS DE MEDIAS-----")
      media(numerosAleatorios,confianza)
      console.print("----   PRUEBAS DE VARIANZA-----")
      varianza(confianza,numerosAleatorios)

  


main()




