'''
This script shows an example of how to optimize the profit of stocks
based on their price and the given investment amount, taking into account
buying a portion of a stock, not necessarily a full whole stock.
'''
import itertools
import csv
import time

filename='KnapSack-portion.csv'

ITEMS=[]
W=[]
V=[]
with open(filename,'r') as csvfile:
	for line in csvfile.readlines():
		array=line.split(',')
		ITEMS.append(array[0])
		W.append(float(array[1].strip()))
		V.append(float(array[2].strip()))  


#####NAME, weight, VALUE (for this weight)
items = [(i,w,v) for i,w,v in itertools.izip(ITEMS,W,V)]


MAXWT = 1600
 
sorted_items = sorted(((value/weight, weight, name) for name, weight, value in items), reverse = True)	  
wt = val = 0
bagged = []
for unit_value, weight, name in sorted_items:
    portion = min(MAXWT - wt, weight)
    wt     += portion
    addval  = portion * unit_value
    val    += addval
    bagged += [(name, portion, addval)]
    if wt >= MAXWT:
        break

print("\n      ITEM\tweight\tVALUE")
print("\n".join("%10s\t%6.2f\t%6.2f" % item for item in bagged))
print("\nTOTAL weight: %5.2f\nTOTAL VALUE: %5.2f" % (wt, val))
print("bagged stocks: "+str(bagged))