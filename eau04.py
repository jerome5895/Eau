import sys

nbr = int(sys.argv[1])

for i in range(nbr+1):
    if nbr % 2 != 0:
        print("This number is already odd, the next is .")
        sys.exit()
    else: