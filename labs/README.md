# Labs

## Table of Contents
  - [Templet]()
  - [Lab one]()

### Templet

```python
#description of Lab
#Name
#Fundamentals of Programming COSC 1336 python
#ACC Fall 2018
#Lab#.py
#Prof Onabajo
def main():

main()

```
### Lab One

```python
#report the total income of a movie based on child and adult tickets sold
#Name
#Fundamentals of Programming COSC 1336 python
#ACC Fall 2018
#Lab1.py
#Prof Onabajo
atc = 6 #adult ticket cost
ctc = 3 #child ticket cost
def main():
  mn = input("What is the name of the movie that was watched? ")#asks the user for the name of the movie
  ats = float(input("How many adult tickets were sold? "))#asks the user for how many adult tickets were sold
  cts = float(input("How many children tickets were sold? "))#asks the user for the number of child tickets sold
  ati = ats * atc #income of adult tickets
  cti = cts * ctc #income of child tickets
  gbop = ati + cti #gross box office profit
  nbop = gbop * .2 # net box office profit
  apmc = gbop - nbop #amount paid to movie company
  #print outcome
  print('Movie Name:                      "'+mn+'"')
  print("Adult tickets sold:                ",int(ats))
  print("Child tickets sold:                ",int(cts))
  print("Gross Box Office Profit:            $"+str(gbop))
  print("Net Box Office Profit:              $"+str(nbop))
  print("Amount Paid to Movie Co:            $"+str(apmc))

main()
```

### Lab Two

```python
#Determine the total cost of a house after a five year period
#Name
#Fundamentals of Programming COSC 1336 python
#ACC Fall 2018
#Lab2.py
#Prof Onabajo
def main():
  for x in range(3): #starts a loop
      globals()["ich"+str(x+1)] = float(input("What was the initial cost of house "+str(x+1)+": "))#asks the user to input the initial cost of what the house is
      globals()["fch"+str(x+1)] = float(input("What was the annual fule cost of house "+str(x+1)+": "))#asks the user for the anual fule cost of the house
      globals()["trh"+str(x+1)] = float(input("What was the tax rate of house "+str(x+1)+":(please use 0.000 to format correctly) "))#asks the user what the tax rate is for thw house
      globals()["tfch"+str(x+1)] = globals()["fch"+str(x+1)] *5 #calculates the anual fule cost over five years
      globals()["th"+str(x+1)] = (globals()["ich"+str(x+1)]*globals()["trh"+str(x+1)])*5 #calculates the taxes paid on the house over five years
      globals()["thc"+str(x+1)] = globals()["ich"+str(x+1)] + globals()["th"+str(x+1)] + globals()["tfch"+str(x+1)]#calculates the total cost of the house over five years
      #print the outputs of the house cost
      print("The total fule cost over five years for house "+str(x+1)+" is: $"+str(globals()["tfch"+str(x+1)]))
      print("The total taxes paid on house "+str(x+1)+" over five years is: $"+str(globals()["th"+str(x+1)]))
      print("The total house cost of house "+str(x+1)+" over five years is: $"+str(globals()["thc"+str(x+1)]))
  #find out which house is the better house to buy
  if(thc1 < thc2 and thc1 < thc3):
      print("House one is the best house to buy.")
  elif(thc2 < thc1 and thc2 < thc3):
      print("House two is the best house to buy.")
  else:
      print("House three is the best house to buy.")

main()

```
