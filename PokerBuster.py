import os
import sys
from decimal import Decimal
os.system('clear')
mano = []
carte_tot = input("Quante carte ha il mazzo?\n")
os.system('clear')
#checker = [0, 0]
for x in range(1, 6):
 try:
  seme = input("Qual e' il seme della carta?\n\n1 - Cuori\n2 - Quadri\n3 - Fiori\n4 - Picche\n")
 except:
  print "Seme \t\t.\t.\t.\t.\tFAIL"
  os.system(quit())
 os.system('clear')
 try:
  numero = input("Qual e' il numero della carta?\n\n1 - Asso\t8\n2\t\t9\n3\t\t10\n4\t\t11 - J\n5\t\t12 - Q\n6\t\t13 - K\n7\n")
 except:
  print "Numero \t\t.\t.\t.\t.\tFAIL"
  os.system(quit())
 os.system('clear')
 try:
  mano.append([seme, numero])
 except:
  print "Appending \t.\t.\t.\t.\tFAIL"
  os.system(quit())
print mano
def calcProb():
 carte_rimanenti = carte_tot - len(mano)
 return "%0.2f\%" % (Decimal(1)/Decimal(carte_rimanenti)*100)
print calcProb()
