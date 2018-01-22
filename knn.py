from numpy import *
from figure import *
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))

    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector
returnMat = zeros((3,3))
print(type(returnMat))

fr = open('123.txt')
try:
    arrayOLines = fr.readlines()
finally:
    fr.close()
#print(arrayOLines)
line = arrayOLines[0]
line = line.strip()
listFormLine = line.split('\t')
print(line)
print(listFormLine)

