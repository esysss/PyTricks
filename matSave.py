import pickle

#write the variable to a file for saving
exampleDict = {'ehsan':'best of the programming','naem':'best of being with','erfan':'best of the bests'}
theFile = open("dick.pickle","wb")#it says to write in bite
pickle.dump(exampleDict,theFile)
theFile.close()

#load the pickle
pickleIN = open("dick.pickle","rb") #says read it to bite
theSameFile = pickle.load(pickleIN)
pickleIN.close()
print(theSameFile)