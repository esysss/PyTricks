#lists
y = ['esysss','ali','mori','ross','chandler']
x = [2,4,6,2,1,8,96,694,65,65,6,464,6,468,6]

print(x[-1])#the last one in the list
print(x[1:]) # print all the elements except the first one
y.pop() #it remover the last item
idx = y.index('esysss') # it gives the index of esysss
count = x.count(2) # it count the number of 2s
c = x.copy()
c.reverse() # it reverse it
x.append(85)
x.append('esysss')#it adds this to last of list

strr = 'my name is no one \nhello'
print(strr)
newStrr = strr.replace('no one','esysss')
print(newStrr)

x.insert(2,86) # it puts 86 to second position
x.remove(8)  # removes the first 8 number
x.remove('esysss')
x.remove(x[5])  # removes the 6th number
print(x[2:-1])   # till the end
indexOfANumber = x.index(96)
NumberOfX = x.count
HowManySix = x.count(6)
x.sort() # it changes the x and sorts it
y.clear() # it removes all
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

#dictunarys
Exdic = {'esysss': 25, 'erfun': 14, 'ross': 30} # it's a dictunary
print("Exdic['esysss']", Exdic['esysss'])
Exdic['asghar']= 60
Exdic['erfun']=15
del Exdic['ross']
dic = {'esysss': [25,'good behavior'], 'erfun': [14,'cute'], 'ross': [30,'lame with woman']}
print(dic['esysss'])

#tuples : you can't change anything
a = (1,2,3,4,5,6,7,8,9,10)
print(a)