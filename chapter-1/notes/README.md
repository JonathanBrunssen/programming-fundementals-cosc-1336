# Chapter 1

## Table of Contents
  - [History of the Computer](https://github.com/JonathanBrunssen/programming-fundementals-cosc-1336/tree/master/chapter-1/notes#history-of-the-computer)
  - [History of PC](https://github.com/JonathanBrunssen/programming-fundementals-cosc-1336/tree/master/chapter-1/notes#history-of-pc)
  - [History of Software/Languages](https://github.com/JonathanBrunssen/programming-fundementals-cosc-1336/tree/master/chapter-1/notes#history-of-softwarelanguages)
  - [Binary](https://github.com/JonathanBrunssen/programming-fundementals-cosc-1336/tree/master/chapter-1/notes#binary)
    - [Base 10](https://github.com/JonathanBrunssen/programming-fundementals-cosc-1336/tree/master/chapter-1/notes#base-10)
    - [Hexadecimal](https://github.com/JonathanBrunssen/programming-fundementals-cosc-1336/tree/master/chapter-1/notes#hexadecimal)

## History of the Computer

 - The first computer was made in 1945. It was made by Herman Hollerith it used punch cards for coding.
 - All original computers where 8-bit. Which 8 bits is equal to 1 byte
 - E.B.C.D.I.C. - Extended binary coded decimal info
 - Herman Hollerith founder of Tabulating Machine Company which with three other companies created which is now known as I.B.M.
 - In 1981 the first PC was made.
 - The first PC's used ASCII (American standard code for info interchange)
 - In 1987 clones of I.B.M. came about. For example: Dell and HP.

---
## History of PC
| Year | Name | Brain | RAM | OS/DOS | Number of bits | Hard disk | Cache | Cost |
|------|------|-------|-----|--------|----------------|-----------|-------|------|
| 1981 |  PC  |808/8088|640KB|DOS 1.0|        8       |   None    |  None | 5,000$|
| 1983 | PC/XT|808/8088|1MB | DOS 2.0|        8       |   10MB    | None  |Unknown|
| 1985 | AT   | 80286 | 4MB | DOS 3.0|       16       |   40MB    | None  |Unknown|
| 1987 | A7   | 80386 | 8MB | DOS 4.0|       16       |    4GB    | None  |Unknown|
| 1987 | PS/2 | 80386 | 8MB | DOS 4.0|       16       |    4GB    | None  |Unknown|
| 1990 | PS/2 |  4886 | 1GB | DOS 5.0|       16       |    8GB    | 640K 1MB|Unknown|
| 1995 | PS/2 |Intel Pentium|  4GB   |95/98/XP/Vista|16|500GB|2MB|Unknown|
| 2018 |Brand Name|I5,I7|8GB|Windows 7,8,10|64|1TB|2MB|500$|

RISC =  Reduced Instruction Set Computers.

RISC move most frequently used instructions (cache)

ttl = time to leave

---
## History of Software/Languages
  - 1st generation
    - Machine language or Binary.
    - Uses 1's & 0's.
    - Difficult to find errors.
    - Optimized memory.
  - 2nd generation
    - Assembly language.
    - Writing in mnemonics (short form of a word).
    - Machine dependent not portable.
  - 3rd generation
    - High level language.
    - Too many rules (syntax errors).
    - Easy to understand & find errors.
    - Examples
      - Basic, Pascal, ADA (NASA), Java, C, C++, Python.
  - 4th generation
    - Very high level.
    - Examples
      - Excel, Access, BB, Nomad, AI, Lisp, Prolog, Java Script, Python, C, C++.
    - AI is used in robots, or expert systems.
  - 5th generation
    - Big data, Machine Language.
    - Almost human.

---
## Binary
Number System - 1's & 0's

Compiler - A software that changes H.L.L. to Machine language

0 means off 1 means on.

### Base 10

To change a number to binary base 10 you can use the Subtraction method or the division method. The subtraction method is best so we will use this.

|2^8|2^7|2^6|2^5|2^4|2^3|2^2|2^1|2^0|
|---|---|---|---|---|---|---|---|---|
|256|128| 64| 32| 16| 8 | 4 | 2 | 1 |

So to get 197 into base 10 we use the subtraction method

128 goes into 197 so we know that the slot in 2^7 is on and we are then left with 26. Now the next number that fits is 16 so 2^4 is now turned on and we are left with 10. So you subtract 8 so 2^3 is used. Then you are left with 2 so you subtract 2 which turns on 2^1.

So 197 in binary base 10 is 10011010

We can use the same method to find 154 and turn it into base 10 and get 10011010

To add two or more binary numbers line them up so they match starting at the 2^0 mark then just add them like you are doing normal math where if there are three 1's you leave one of the 1's behind and carry a 1 over if there are only two 1's in the slot it turned off and you carry the 1 over.

Multiplication is very similar to addition you just multiply like in normal math then add.

Division is just like normal division method.

you can also shift a binary number to the left or to the right. A shift to the right multiplies by 2. While if you shift it to the left you divide by 2.

### Hexadecimal
Base 16(0-15)

break up the base 10 number into strands of 4 and use the 8,4,2,1 on them and figure out the number that is given for example if we break apart.

11001110011100111100111 into Hexadecimal.

110|0111|0011|1001|1110|0111 you then get.

 6 | 7  | 3  | 9  | 14 | 7 as your numbers now you just apply the numbers to the graph below.

|Dec|Hex|
|---|---|
| 0 | 0 |
| 1 | 1 |
|2|2|
|3|3|
|...|...|
|9|9|
|10|A|
|11|B|
|12|C|
|13|D|
|14|E|
|15|F|

So 11001110011100111100111 changed to hexadecimal is really 6739E7.

You can also find out the Mac/Physical Address of your computer now.

So the method to conversion is 2 steps
  - Step 1: take the number to binary.
  - Step 2: take it to destination base.

All math functions in base 10 and hexadecimal are the exact. Just that if you borrow a number during subtraction add 16 to the number you are giving it to.

---
