# -*- coding: utf-8 -*-
"""functions

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U0qBaENXwRt1hE_xVP2-_NhQAEwxhh32
"""

def calcula_media(n1, n2, n3):
  media= (n1 + n2 + n3)/3
  return media

n1= float(input("digite a 1 nota: "))
n2= float(input("digite a 2 nota: "))
n3= float(input("digite a 3 nota: "))

resultado_media = calcula_media(n1, n2, n3)
print("a média das notas é de",resultado_media)

def verifica_par(numero):
  resto= numero % 2
  if resto == 0:
    return True
  else:
    return False

numero= int(input("digite um número: "))
par= verifica_par(numero)
if par:
  print("o número digitado é par")
else:
  print("o número digitado é impar")

def calcula_media(lista):
  return lista

lista = [10, 5, 3.5, 7, 8, 8.5, 9]
soma= sum(lista)
print(f"A média dos números é {soma/7:.2f}")

def encontra_palavra(palavra, lista):
  return palavra in lista

palavra = "java"
lista = ["ravi", "camundongo", "amora", "estetoscópio", "barata"]
if encontra_palavra(palavra, lista):
  print(f"A palavra {palavra} foi encontrada")
else:
  print(f"A palavra {palavra} não foi encontrada")

def fibonacci(numero, sequencia):
  return sequencia

numero = 10
sequencia = [0, 1]

while len(sequencia) < numero:
  prox_numero = sequencia[-1] + sequencia[-2]
  sequencia.append(prox_numero)

print (sequencia)

def conta_vogais(palavra, dicionario):
  for letra in palavra:
    letra = letra.lower() # deixa tudo minúsculo
    if letra in 'aeiou':
      dicionario[letra] = dicionario.get(letra, 0) + 1


dicionario_cont = {}
palavra = "claustrofobia"
conta_vogais(palavra, dicionario_cont)
print(dicionario_cont)

def verifica_palindromo(palavra):
  palavra = palavra.replace(" ","").lower()
  return palavra == palavra[::-1]

palavra = "ovo"
resultado = verifica_palindromo(palavra)
print (resultado)

import random
import string

def gera_senha(n):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(n))
    return senha

senha_gerada = gera_senha(8)
print(senha_gerada)