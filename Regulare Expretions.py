import re
sentence = '''
Ehsan is 25 yeas old and his friend Hooman is 26 years old
and Erfan his good cousin is 12 and he love him a lot
there is no girl in ehsan'n life and it's becouse of his flosify for life.
'''
ages = re.findall(r'\d{1,2}',sentence)
names = re.findall(r'[A-Z][a-z]*',sentence)
print('the ages are', ages, '\nand the names are', names)
dick={}
counter = 0
for eachName in names :
    dick[eachName] = ages[counter]
    counter += 1
print(dick)
