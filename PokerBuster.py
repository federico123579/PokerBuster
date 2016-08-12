import os
import sys
os.system('clear')
mano = []
for x in range(1, 6):
 seme = input("Qual e' il seme della carta?\n\n1 - Cuori\n2 - Quadri\n3 - Fiori\n4 - Picche\n")
 numero = input("Qual e' il numero della carta?\n\n1 - Asso\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11 - J\n12 - Q\n13 - K\n")
 mano.append([seme, numero])
 os.system('clear')
print mano
