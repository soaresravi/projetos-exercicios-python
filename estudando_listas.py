# -*- coding: utf-8 -*-
"""estudando listas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eLzqB_aJEUnN1mrrTNo62D0dEdil-0qx
"""

list = []

def displayList():
  for x, item in enumerate(list, start=1):
    print(f"{x}. {item}")
  print()

print ("SHOPPING LIST\n")

while True:
  print("MENU")
  print("1. Display list")
  print("2. Add item to list")
  print("3. Remove item from list")
  print("4. Show number of items on list")
  print("5. Export list to a .txt file")
  print("6. Exit")

  opcao = int(input("Type the option: "))

  if opcao == 1:
    print("\n")
    displayList()
    print("\n")
  elif opcao == 2:
    item= input("Write the item to be added: ")
    list.append(item)
    print(f"The item '{item}' was added with successfully!\n")
  elif opcao == 3:
    item= input("Write the item for be removed: ")
    if item in list:
      list.remove(item)
      print(f"The item '{item}' was removed successfully!\n")
    else:
      print(f"The item '{item}' isn't in list\n")
  elif opcao == 4:
    total= len(list)
    print(f"There are {total} items on the list\n")
  elif opcao == 5:
    with open('list.txt', 'w') as archive:
      for item in list:
        archive.write(item + "\n")
    print("List exported to 'list.txt' successfully!\n")
  elif opcao == 6:
    print("Closing program...\n")
    break
  else:
    print("Type a valid option\n")



list = []
listNumbers = []

def displayList():
  print("\nSHOPPING LIST")
  for x, item in enumerate(list, start=1):
    print(f"{x}.{item}")
  print()

def displayListN():
  print("\nLIST OF NUMBERS")
  for x, number in enumerate(listNumbers, start=1):
    print(f"{x}. {number}")
  print()

def add():
  list.append(item)
  print(f"The item '{item}' was added sucessfully!\n")

def addNumbers():
  listNumbers.append(number)
  print(f"The number {number} was added sucessfully!\n")

def remove():
  list.remove(item)
  print(f"The item '{item}' was removed sucessfully!\n")

def removeNumbers():
  listNumbers.remove(number)
  print(f"The number {number} was removed sucessfully!\n")

while True:

  print("1. Add in the list")
  print("2. Remove in the list")
  print("3. Add up all numbers in the list")
  print("4. Average all numbers in the list")
  print("5. Show number of items on list")
  print("6. Display list")
  print("7. Export list to a .txt file")
  print("8. Exit")

  answer= int(input("\nWhat you need?: "))

  if answer == 1:
    answer2= str(input("You want to add a number or an item?: "))
    if answer2 == "Number" or answer2 == "number":
      number= int(input("Type the number you want to add: "))
      addNumbers()
    elif answer2 == "Item" or answer2 == "item":
      item= input("Type the item to be added: ")
      add()
    else:
      print("Invalid item\n")
  elif answer == 2:
    answer2= input("You want to remove a number or an item?: ")
    if answer2 == "Number" or answer2 == "number":
      number= int(input("Type the number you want to remove: "))
      if number in listNumbers:
        removeNumbers()
      else:
        answer3= input(f"The number {number} isn't on the list, you want to add?: ")
        if answer3 == "Yes" or answer3 == "yes":
          addNumbers()
        elif answer3 == "No" or answer3 == "no":
          print("Ok!\n")
        else:
          print("Invalid answer\n")
    elif answer2 == "Item" or answer2 == "item":
      item= input("Type the item you want to remove: ")
      if item in list:
        remove()
      else:
        answer3= input(f"The item '{item}' isn't on the list, you want to add?: ")
        if answer3 == "Yes" or answer3 == "yes":
          add()
        elif answer3 == "No" or answer3 == "no":
          print("Ok!\n")
        else:
          print("Invalid answer\n")
  elif answer == 3:
    addUp= sum(listNumbers)
    print(f"The sum of all the numbers in this list's {addUp} \n")
  elif answer == 4:
    addUp= sum(listNumbers)
    total= len(listNumbers)
    print(f"The average of numbers in the list's {addUp/total:2} \n")
  elif answer == 5:
    answer2= input("Do you want to know about numbers or itens?: ")
    if answer2 == "Numbers" or answer2 == "numbers":
      print(f"There are {total} numbers in the list\n")
    elif answer2 == "Itens" or answer2 == "itens":
      total2= len(list)
      print(f"There are {total2} itens in the list\n")
    else:
      print("Invalid answer\n")
  elif answer == 6:
    answer2= input("Do you want the list of numbers or itens?: ")
    if answer2 == "Numbers" or answer2 == "numbers":
      displayListN()
      print("\n")
    elif answer2 == "Itens" or answer2 == "itens":
      displayList()
      print("\n")
    else:
      print("Invalid answer\n")
  elif answer == 7:
    answer2= input("Do you want export the list of numbers or itens?: ")
    if answer2 == "Numbers" or answer2 == "numbers":
      with open('listNumbers.txt', 'w') as archive:
        for number in listNumbers:
          archive.write(number + "\n")
          print("The list of numbers was exported sucessfully!\n")
    elif answer2 == "Itens" or answer2 == "itens":
      with open('list.txt', 'w') as archive:
        for item in list:
          archive.write(item + "\n")
          print("The shopping list was exported sucessfully!\n")
  elif answer == 8:
    print("Closing program...")
    break
  else:
    print("Invalid option\n")