# -*- coding: utf-8 -*-
"""ex indice lista

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cTdmVWWf7JYfmWoTi0fBQ9gCxrWbbqUD
"""

lista = ["o", "ravi", "é", "muito", "muito", "legal"]
for indice, valor in enumerate(lista):
  print(f"a palavra {valor} está na posição {indice}")

lista = [3, 6, 9, 12, 15]
soma= 0
for valor in lista:
  soma += valor

print (f"a soma dos números da lista é {soma}")

lista = ["duda", "é", "a", "ultra", "boboca", "apocalíptica", "ateia", "avarenta"]
print("palavras que começam com a: ")

for palavra in lista:
  if palavra[0] == "a":
    print(palavra)

lista = [6, 27, 32, 252, 344, 546, 123]
print("os números pares da lista são: ")

for numero in lista:
  resto= numero % 2
  if resto == 0:
    print(numero)

lista = ["duda", "é", "a", "ultra", "boboca", "apocalíptica", "ateia", "avarenta"]
print("palavras que possuem mais de 5 caracteres: ")

for palavra in lista:
  caracter= 0
  for letra in palavra:
    caracter += 1
  if caracter > 5:
   print(palavra,)

lista = [8, 2, 16, 24, 32, 17, 57, 68, 29, 169, 353]
print("o menor número desses é: ")
menor= 0

for numero in lista:
  if menor == 0:
    menor= numero
  if menor > numero:
    menor= numero
print (menor)

lista = [3, 6, 9, 12, 15]
soma= 0
for valor in lista:
  soma += valor

print (f"a média dos números da lista é {soma/5}")

nomes = ["Lucas Rossi", "Duda", "Ravi", "Caio", "Matue" , "Carlão"]
nomes_ordenados = sorted(nomes)
print("Nomes em ordem alfabética:")
for nome in nomes_ordenados:
    print(nome)



lista = [4, 50, 5, 89, 12, 169]
print("a posição do número igual a 5 é: ")

for indice, numero in enumerate(lista):
  if numero == 5:
    print (indice)