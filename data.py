# from numpy import *
# a=[1,2,2,2,4,5,5]
# mylist=[item*4 for item in a if item > 2]
# for item in mylist:
#     print(item)
#
# b={1:23,'name':'shenjie'}
# for item in b:
#     print(b[item])
#
from numpy import mat
from imp import reload
import os
reload(os)
# jj = mat([[1,5,2],[3,7,4]])
# print(jj)
# jj.sort()
# print(jj)
a = mat([[1,0,5],[4,1,7],[3,2,9]])
b = mat([[1,0,0],[0,1,0],[0,0,1]])
# a = mat([[1],[4],[3]])
# b = mat([[0],[1],[2]])
print(a)
print(a*b)




