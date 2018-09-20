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

main().loop

```
### Lab one

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
  print('Movie Name:                "'+mn+'"')
  print("Adult tickets sold           ",int(ats))
  print("Adult tickets sold           ",int(cts))
  print("Adult tickets sold            $"+str(gbop))
  print("Adult tickets sold            $"+str(nbop))
  print("Adult tickets sold            $"+str(apmc))

main().loop
```
