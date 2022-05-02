from operator import itemgetter
A = [[10,8],[90,2],[45,6]]
print("Sorted List A based on index 0: % s" % (sorted(A,
key=itemgetter(0))))

B = [[50,'Yes'],[20,'No'],[100,'Maybe']]
print("Sorted List B based on index1: % s" % (sorted(B,
key=itemgetter(1))))