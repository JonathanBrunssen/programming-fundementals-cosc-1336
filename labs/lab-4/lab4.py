#compute the sum, mean, devieation, deviation squared, Sum of deviation from the mean squared, Standard deviation, Standard scores, Sum of the standard scores of a test
#Jonathan Brunssen
#Fundamentals of Programming COSC 1336 python
#ACC Fall 2018
#Lab4.py
#Prof Onabajo
def main():
    infile = open("lab4.dat","r")#open our data file
    outfile = open("lab4.out","w")#open the file we write to
    outfile.write("SCORES		DEV		DEV1		SD1 \n")#write out the header of our out file
    test_data = infile.readline().strip("\n").split(",")##get the data of the tests
    test_scores = []#create an empty list to dump our scores into
    deviations = []
    deviations_squared = []
    standard_scores = []
    
    #convert the data into integers
    for foo in range(len(test_data)): #repeat for how big test_data is
        test_score = int(test_data[foo])#convert the xth obj of the list into a int
        test_scores.append(test_score)#add the test score to the list

    #get the sum & avg of the test
    sumx_of_tests = sum(test_scores)#get the sum of the tests
    avg_of_test = sumx_of_tests/len(test_scores)#get the average of the tests

    #get the deviation, deviation squared, & standard deviation
    for bar in range(len(test_scores)):
        test_score = test_scores[bar]
        deviation = avg_of_test - test_score
        deviations.append(deviation)
        deviation_squared = deviation ** 2
        deviations_squared.append(deviation_squared)
    
    standard_deviation = (sum(deviations_squared)/len(deviations_squared))**.5

    for r in range(len(test_scores)):
        standard_score = (avg_of_test - test_scores[r])/standard_deviation
        standard_scores.append(standard_score)
        outfile.write(str(test_scores[r])+"              "+str(format(deviations[r],'.2f'))+
                      "           "+str(format(deviations_squared[r],'.5f'))+
                      "           "+str(format(standard_score,'.5f'))+"\n")
    
    for x in range(3):
        outfile.write("\n")
    outfile.write("Sum="+str(sumx_of_tests)+"		Average ="+str(avg_of_test)+
                  "			Standard Deviation   = "+
                  str(format(standard_deviation,'.4f'))+"\n")
    outfile.write("sum of standard score = "+str(format(sum(standard_scores),'.0f')))
        

    #close out files
    infile.close()
    outfile.close()
main()
