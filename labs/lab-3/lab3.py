#compute the batting average and the slugging average of players
#Jonathan Brunssen
#Fundamentals of Programming COSC 1336 python
#ACC Fall 2018
#Lab3.py
#Prof Onabajo
def Compute_Batting_Average(s,d,t,hr,ab): #creates a function wit 5 arguments
    total_hits = s+d+t+hr#calculates the number of hits
    batting_average = total_hits/ab#calculates the batting average
    return(batting_average)#returns the batting average

def Compute_Slugging_Average(s,d,t,hr,ab):#creates a function with 5 arguments
    total_bases = (s*1)+(d*2)+(t*3)+(hr*4)#calculates the total number of bases
    slugging_average = total_bases/ab#computes the slugging average
    return(slugging_average)#returns the slugging average
    
def main():
    infile = open("lab3a.dat","r")#open our data file
    outfile = open("lab3a.out","w")#open the file we write to
    outfile.write("Player       Batting Average      Slugging Average \n")#writes the header of our out file
    for x in range(9):
        globals()["stats_of_player"+str(x+1)] = infile.readline().strip("\n").split(",")#get the stats from a line
        globals()["player_number"+str(x+1)] = globals()["stats_of_player"+str(x+1)][0]#get the player number
        globals()["singles_for_player"+str(x+1)] = int(globals()["stats_of_player"+str(x+1)][1])#get the number of singles
        globals()["doubles_for_player"+str(x+1)] = int(globals()["stats_of_player"+str(x+1)][2])#get the number of doubles
        globals()["triples_for_player"+str(x+1)] = int(globals()["stats_of_player"+str(x+1)][3])#get the number of triples
        globals()["homeruns_for_player"+str(x+1)] = int(globals()["stats_of_player"+str(x+1)][4])#get the number of home runs
        globals()["atbats_for_player"+str(x+1)] = int(globals()["stats_of_player"+str(x+1)][5])#gets the number of at bats
        globals()["batting_average_for_player"+str(x+1)] = Compute_Batting_Average(globals()["singles_for_player"+str(x+1)],
                        globals()["doubles_for_player"+str(x+1)],
                        globals()["triples_for_player"+str(x+1)],globals()["homeruns_for_player"+str(x+1)],
                        globals()["atbats_for_player"+str(x+1)])#compue the batting average
        globals()["slugging_average_for_player"+str(x+1)] = Compute_Slugging_Average(globals()["singles_for_player"+str(x+1)],
                        globals()["doubles_for_player"+str(x+1)],
                        globals()["triples_for_player"+str(x+1)],globals()["homeruns_for_player"+str(x+1)],
                        globals()["atbats_for_player"+str(x+1)])#compute the slugging average
        outfile.write(str(globals()["player_number"+str(x+1)])+"            "+
                      str(format(float(globals()["batting_average_for_player"+str(x+1)]),'.3f'))+
                      "                "+str(format(float(globals()["slugging_average_for_player"+str(x+1)]),'.3f'))+
                      " \n")#writes only the first three decimal places and writes the data we need
    #close the files
    infile.close()
    outfile.close()

main()
