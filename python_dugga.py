#python dugga
#mathilda järkestig 16-10-26

#I am sorry for any spelling mistakes in my annotation
#my speling is bad normaly and now I'm writing fast and focusion on the code so it is probobly way worse


###question 1

#a)

name = "Mathilda Järkestig"


#b)

#print length of varible name 
print(len(name))


#c)

#print the count of occurences of ä in varible name 
print(name.count("ä"))


###question 2

my_list = [1, 5, "4", "six", 3.14]


#a) & #b)

def clean_list(list): #define function clean list thet takes a list as an input
    new_list = [] #make a new list
    for nr in list: #loop over the numbers in the inputed list
        try: #since error is expected try is used
            nrint = int(nr) #try to convert the numbers to int
            new_list.append(nrint) #append converted numbers to the new list
        except ValueError: #when an error occurs, print a message and skip that entry in the list
            print(f"skipping invalid value: {nr}")
    return new_list #the output returend by the function is the new list

#call function with as input my list and print output 
new_list = clean_list(my_list)
print(new_list)


#c

#for n in new_list:
#sumlist = []
#nandajacent = slice list [nposition:nposition + 1]
#sum = nandajacent.sum()
#sumlist.append(sum)



###question 3

#imports:

import sys
import pandas as pd
import plotly.express as px

#c)

####### run the code with: python filename.py imputfilename.csv outputfilename #######

file = sys.argv[1] #the first argument after python python_dugga.py will be saved as file and used as input
output = sys.argv[2] #the second argument after python python_dugga.py will be saved as output and used to name the outputed plott


#a)

data = pd.read_csv(file) #load in the inputed csv with pandas and save it as a datafram (I like pandas :D)
print(data) #quick look at the data

#make scatterplot and save it as plot
plot = px.scatter(data, #use the saved dataframe
                  x="position_mb", #define the x axis
                  y="log2_ratio", #define the y axis
                  title="Postion mb vs log2 ratio") #add a title


#b)

#save the plot using the user inputed name
plot.write_html(f"{output}.html")


###question4

#a) & #b)

import random

def dicegame(player1, player2, games): #define a function thet takes 2 players and the total number of games as input 
    gamescore = {player1 : 0, player2 : 0, "draw": 0} #make a dictionary to keep track of score, at the start no gemes have been playd as all scores are 0
    game = 1 #make a varible to count games 
    while game < games + 1: #make a loop that runs while the number of games is below the defined nuber or games (to run the last loop add 1 to games)
        player1score = random.randint(1,6) #generate ranom nuber for player 1
        player2score = random.randint(1,6) #generate ranom nuber for player 2
        if player1score > player2score: #add a point to player1 in gamescore if player1 has a higher number
            gamescore[player1] +=1
        elif player1score < player2score: #add a point to player2 in gamescore if player2 has a higher number
            gamescore[player2] +=1
        elif player1score == player2score: #add a point to draw if the numbers are equal
            gamescore["draw"] += 1
        game += 1 #add 1 to game to keep track of the amout of games 
    return gamescore #the output of the function is the gamescore list

#call the function with original parameters:
game = dicegame("Alice", "Bob", 20)
print(game)










