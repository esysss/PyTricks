a = list(range(10))
b = list(range(2,12))

for i , j in zip(a,b):
    print(i+j)

c = type(a) # says the type of a variable
d = a.copy() # it's so important to copy

for i,j in enumerate(b):
    print(i,j)

print(a[0:5])

def esysss():
    print('esysss is awesome')

x = esysss #you can assign a function to a variable and then run it ......
x() # bananas............

l = []
for idx in reversed(range(10)):# it reverse it
    l.append(idx)
print(l)

number = 10
name = 'esysss'
print(f"i can put number and name in {number} and {name} \n it's awesome")

import itertools #make a cycle in a list
lis = [3,2,1]
lis = itertools.cycle(lis)
for i in range(10):
    print(lis.__next__())
    #or
    print(next(lis))#it works both ways but i like this more

strr = "   ".join(str(i) for i in range(5))#it repeat the numbers and place spaces between them
print(strr)

forPrint = [[0 for i in range(3)] for i in range(5)] # in makes a 5*3 zeros matrix
[print(row) for row in forPrint]
[print(row) for row in [[1 for i in range(5)]for i in range(7)]] #it prints the 7*5 ones matrix

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.BRIGHT + 'and in dim text')
print(Style.RESET_ALL + 'back to normal now')