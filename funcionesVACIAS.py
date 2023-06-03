from principal import *
from configuracion import *
import random
import math

#lee el archivo y carga en la lista diccionario todas las palabras

def lectura(diccionario): #Fede
    lista = []
    with open(diccionario, 'r') as dic: #leo las palabras del dic -con with para no tener que cerrarlo
        for palabra in dic: #Para cada palabra en el dic agrego la palabra en la lista vacia
            lista.append(palabra)
        return lista #Retorno la lista

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():#TODOS
    letras_juego = []
    vocales = ['a','e','i','o','u']
    consonantes_normal = ['b','c','d','f','g','h','j','l','m','n','p','q','r','s','t','v','w']
    consonantes_dificiles = ['k','x','y','z']
    
    random.shuffle(vocales) #Mezclo las listas
    random.shuffle(consonantes_normal)
    random.shuffle(consonantes_dificiles)
    
    def letras(lista, lista_vacia,cant_letras):
        contador = 0
        for letra in lista:
            if letra not in lista_vacia and contador < cant_letras: #Comparo si la letra al azar no esta en el juego + contador < cant_letras
                lista_vacia.append(letra)
                contador +=1
    letras(vocales, letras_juego,2)
    letras(consonantes_normal, letras_juego, 4)
    letras(consonantes_dificiles,letras_juego,1)
    
    random.shuffle(letras_juego)
    
    return letras_juego

def dameLetra(letrasEnPantalla):#elige una letra de las letras en pantalla // TOM
    vocales = ['a','e','i','o','u']
    consonantes_normal = ['b','c','d','f','g','h','j','l','m','n','p','q','r','s','t','v','w']
    
    for letra in letrasEnPantalla:
        if letra in vocales or letra in consonantes_normal: #La primer letra que encuentre - sea vocal o cons - devolvela
            return letra

#si es valida la palabra devuelve puntos sino resta. // Gonza
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    return Puntos(candidata)

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario // FEDe
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    return True

#devuelve los puntos // TOM
def Puntos(candidata):
    return(5)

#busca en el diccionario paralabras correctas y devuelve una lista de estas // Gonza
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    return ['adanida', 'adrian', 'aduana', 'aduanar', 'adunar', 'adunia', 'adan', 'ahina', 'ana', 'anadina', 'anana', 'anda', 'andada', 'andadura', 'andana', 'andanada', 'andar', 'andarina', 'andarin', 'andriana', 'andrina', 'anidar', 'anidiar', 'anudadura', 'anudar', 'anuria', 'arana', 'arduran', 'arna', 'arnadi', 'arruinar', 'aran', 'aun', 'aunar', 'aina', 'aun', 'dan', 'dandi', 'diana', 'din', 'dina', 'dinar', 'dinarada', 'duna', 'durina', 'harina', 'hin', 'hindi', 'hindu', 'hirundinaria', 'hundir', 'inanidad', 'india', 'indiada', 'indiana', 'indinar', 'inri', 'inundar', 'irani', 'nada', 'nadadura', 'nadar', 'nadi', 'nadir', 'nahua', 'nana', 'narina', 'narra', 'narrar', 'narria', 'niara', 'nidada', 'nin', 'nudrir', 'nadir', 'nia', 'radian', 'rain', 'rana', 'randa', 'ranina', 'ranura', 'rin', 'rinran', 'ruana', 'ruin', 'ruina', 'ruinar', 'ruindad', 'runa', 'runrun', 'ruan', 'unidad', 'unir', 'urna']
