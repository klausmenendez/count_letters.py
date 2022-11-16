




def count_letters(word1):
    '''
    The program prints out the number of times a particulkar letter shows up in a string
    '''

    words=word1.upper()
    letters={} #creates a dictionary
    count1 = 0  #variables to increment
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0
    count15 = 0
    count16 = 0
    count17 = 0
    count18 = 0
    count19 = 0
    count20 = 0
    count21 = 0
    count22 = 0
    count23 = 0
    count24 = 0
    count25 = 0
    count26 = 0
    for i in range(0,len(words)): #creates a for loop that iterates over a string
        if words[i]=='A':
           count1+=1 #For each time A appears, add 1
           letters['A']=count1
        elif words[i]=='B':
            count2+=1
            letters["B"]=count2
        elif words[i]=="C":
            count3+=1
            letters["C"]=count3
        elif words[i]=="D":
            count4+=1
            letters["D"]=count4
        elif words[i]=="E":
            count5+=1
            letters["E"]=count5
        elif words[i]=="F":
            count6+=1
            letters["F"]=count6
        elif words[i]=="G":
            count7+=1
            letters["G"]=count7
        elif words[i]=="H":
            count8+=1
            letters["H"]=count8
        elif words[i]=="I" :
            count9+=1
            letters["I"]=count9
        elif words[i]=="J":
            count10+=1
            letters["J"]=count10
        elif words[i]=="K":
             count11+=1
             letters["K"]=count11
        elif words[i]=="L":
            count12+=1
            letters["L"]=count12
        elif words[i]=="M":
            count13+=1
            letters["M"]=count13
        elif words[i]=="N":
            count14+=1
            letters["N"]=count14
        elif words[i]=="O":
            count15+=1
            letters["O"]=count15
        elif words[i]=="P":
            count16+=1
            letters["P"]=count16
        elif words[i]=="Q":
            count17+=1
            letters["Q"]=count17
        elif words[i]=="R":
            count18+=1
            letters["R"]=count18
        elif words[i]=="S":
            count19+=1
            letters["S"]=count19
        elif words[i]=="T":
            count20+=1
            letters["T"]=count20
        elif words[i]=="U":
            count21+=1
            letters["U"]=count21
        elif words[i]=="V":
            count22+=1
            letters["V"]=count22
        elif words[i]=="W":
            count23+=1
            letters["W"]=count23
        elif words[i]=="X":
            count24+=1
            letters["X"]=count24
        elif words[i]=="Y":
            count25+=1
            letters["Y"]=count25
        elif words[i]=="Z":
            count26+=1
            letters["Z"]=count26
    return letters

#print(count_letters("xexex"))








