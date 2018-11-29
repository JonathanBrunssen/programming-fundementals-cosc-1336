#Given X as an array/List of [5,3] and y as [3,7] perform the following: Load array X column-wise and array Y row-wise Multiply X by Y to compute array Z Compute the sum of all elements on column 2 of array X and add it to the sum of all the elements in row 2 of Y Compute the smallest element in row 1 of Y Print out matrices X,Y,Z Print out the sum and the smallest element Use appropriate Headings
#Jonathan Brunssen
#Fundamentals of Programming COSC 1336 python
#ACC Fall 2018
#Lab5.py
#Prof Onabajo
def LOAD_X(file):
    r=5 #how many rows?
    c=3 #how many columns
    xs = [[0,0,0],#create the x list that we need to return 5x3
          [0,0,0],
          [0,0,0],
          [0,0,0],
          [0,0,0]]
    tempx = file.readline().strip("\n").split(" ")#strip the x's from the data file
    for foo in range(r):#loop for the rows
        for bar in range(c):#loop for the columns
            xs[foo][bar] = int(tempx[0])#set the row and the column by the first value in the list
            del tempx[0]#delete the first value in the tempx list
    return xs#return the matrix

def LOAD_Y(file):
    r=3 #how many rows
    c=7 #how many columns
    ys = [[0,0,0,0,0,0,0],#create the y list 3x7
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]
    tempy = file.readline().strip("\n").split(" ")#strip the y's from the data file
    for foo in range(c):#loop through the columns
        for bar in range(r):#loop through the rows
            ys[bar][foo] = int(tempy[0])#set the row by the column by the first thing in tempy list
            del tempy[0]#delete the first value in tempy
    return ys#return the matrix

def COMPUTE_Z(xList,yList): 
    zList = [[0,0,0,0,0,0,0], #create the z list 5x7
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    
    for foo in range(5):
        for bar in range(7):
            for i in range(3):
                zList[foo][bar] = zList[foo][bar] + xList[foo][i]*yList[i][bar]
    return zList

def SMALLEST(ys):
    smallestNum = 0
    for foo in range(7):#loop through row 2
        temp = ys[1][foo]
        if(temp < smallestNum): #check if the temp value is smaller than the smallest num in the 2nd row
            smallestNum = temp #if it is make it the smallest num
    return smallestNum#return the smallest num

def SUMMATION_OF_XLIST(xs):
    sumX = 0
    temp = 0
    for foo in range(5):
        temp = xs[foo][2]
        sumX = sumX + temp#add the sum of column 2 
    return sumX#return the sum of column 2

def SUMMATION_OF_YLIST(ys):
    sumY = 0
    temp = 0
    for foo in range(7):
        temp = ys[2][foo]
        sumY = sumY + temp
    return sumY

def OUT_DATA(file,sumOfX,sumOfY,smallest,xList,yList,zList,sumXandY):
    file.write("  X               Y             Z \n")
    for foo in range(5):
        for i in range(7):
            for bar in range(3):
                if(i < 1):
                    file.write(str(xList[foo][bar])+" ")
                    #file.write(" "+str(yList[bar][i])+" ")
            
        file.write("\n")
    

def main():
    #def variables
    xList = []
    yList = []
    zList = []
    smallestOfYRowOne = 0
    sumColumnTwoXList = 0
    sumRowTwoYList = 0
    sumOfXandY = 0
    
    #open data files
    infile = open("lab5.dat","r")
    outfile = open("lab5.out","w")

    #load xs
    xList = LOAD_X(infile)
    print(xList)

    #load ys
    yList = LOAD_Y(infile)
    print(yList)

    #compute z list
    zList = COMPUTE_Z(xList,yList)
    print(zList)

    #compute the sum of all of row 2 of both xList and Ylist
    sumColumnTwoXList = SUMMATION_OF_XLIST(xList)
    sumRowTwoYList = SUMMATION_OF_YLIST(yList)
    print("Sum x:",sumColumnTwoXList)
    print("Sum y:",sumRowTwoYList)

    #Compute the sum of column 2 of x list by row 2 of y list
    sumOfXandY = sumColumnTwoXList + sumRowTwoYList
    print("Sum:",sumOfXandY)
    
    #get the smallest element in row one of y list
    smallestOfYRowOne = SMALLEST(yList)
    print("smallest:",smallestOfYRowOne)

    OUT_DATA(outfile,sumColumnTwoXList,sumRowTwoYList,smallestOfYRowOne,xList,yList,zList,sumOfXandY)

    #close data files
    infile.close()
    outfile.close()

main()
