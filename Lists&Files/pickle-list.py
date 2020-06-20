##Pickle allows objects to be saved to a file and maintain format

thislist = ["apple", "banana", "cherry"]

import pickle

##write
with open('outfile', 'wb') as fp:
    pickle.dump(thislist, fp)

##read
with open ('outfile', 'rb') as fp:
    itemlist = pickle.load(fp)

print(itemlist)
