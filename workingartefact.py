import random
import csv
import numpy as np
import matplotlib.pyplot as plt

print("PENALTY SHOOTOUT")
print("You have to try score as many penalties in a row")
playerName = input("Enter your name: ")
print("Welcome", playerName, "to the penalty shootout game")
print("The coordinates on the goal are: T1, T2, T3, T4, B1, B2, B3, B4")
print("Note that: ")
print("SINGLE stands for SINGLE-PLAYER")
print("MULTI stands for MULTI-PLAYER")
print("SIM stands for SIMULATION")

#visual representation of the goal
print("Looks like this to make it easier to understand...")
print("----------------------")
print("┃ T1   T2   T3   T4 ┃")
print("┃-------------------┃")
print("┃ B1   B2   B3   B4 ┃")
print("┃                   ┃")

print("Note that: ")
print("SINGLE stands for SINGLE-PLAYER")
print("MULTI stands for MULTI-PLAYER")
print("SIM stands for SIMULATION")


goal = ["T1", "T2", "T3", "T4", "B1", "B2", "B3", "B4"] #creates list for goal coordinate choices

endScore = 0

def singlePlayer():
  
  endScore = 0 #end score is 0 at the beginning, outside of loop
  difficulty = ["EASY" , "NORMAL", "HARD"] #list of difficulties
  diffChoice = input("Which difficulty? Easy/Normal/Hard :")
  diffChoice = diffChoice.upper() #capitalisation
  print(diffChoice)  # to test if capitalisation works
  checkDiff = difficulty.count(diffChoice)  # to check if coordinate is a valid input
  while checkDiff == difficulty.count(diffChoice):
    if checkDiff > 0:
      print("OK!")
      break
    else:
      print("This is not a valid difficulty.")
      diffChoicetwo = input("Which difficulty? EASY/NORMAL/HARD :")
      diffChoice = diffChoicetwo.upper() # make sure it capitalizes so it matches inputs in last
      print(diffChoice) #check capitalisation
      checkDiff = difficulty.count(diffChoice) #checks again
      continue
    
  while gameChoice == "SINGLE":
    playerChoice = input("Choose a coordinate to shoot at: ")
    playerChoice = playerChoice.capitalize() #just to make sure player uses capital letters for function to work
    checkGoal = goal.count(playerChoice) # to check if coordinate is a valid input
    while checkGoal == goal.count(playerChoice):
      if checkGoal > 0:
        print(playerName, "shoots the ball at", playerChoice,"!")
        break
      else:
        print("This is not a valid goal coordinate.")
        playerChoice = input("Choose a coordinate to shoot at: ")
        playerChoice = playerChoice.capitalize() #capitalisation of the t or b in coordinate
        checkGoal = goal.count(playerChoice) #checks again
        continue
    
        
    #easy is randomised    
    if diffChoice == "EASY":
      compGoal = random.choice(goal)
      print("The goalkeeper dived at", compGoal, "!")



    #hard is a 50-50 chance of scoring
    if diffChoice == "HARD":
      goalchance = (0.5, 0.5) # percentages all add up to 1
      def roll(i):
          randRoll = random.random() 
          sum = 0
          result = 1
          for a in i:
            sum += a
            if randRoll < sum:
                return result
            result+=1
  
  
      x = roll(goalchance) # rolls between all the chances
    
      
      if x == 1:
        compGoal = playerChoice #compgoal matches player's input
        ("The goalkeeper dived in the ball's direction!!!")
      elif x == 2:
        compGoal = ("x") #compGoal does not match player's input
        print("The goalkeeper dived in the wrong direction!!")
      
    
    
    
    
    if diffChoice == "NORMAL":
      goalcoordinates = (0.0575, 0.15, 0.135, 0.05, 0.1725, 0.15, 0.135, 0.15) # percentages all add up to 1
      def roll(i):
          randRoll = random.random() 
          sum = 0
          result = 1
          for a in i:
            sum += a
            if randRoll < sum:
                return result
            result+=1
  

      x = roll(goalcoordinates) # rolls between all the chances
   
      #depending on the rolled calculation it will output the rolled coordinate
      if x == 1:
        compGoal = "T1"
      elif x == 2:
        compGoal = "T2"
      elif x == 3:
        compGoal = "T3"
      elif x == 4:
        compGoal = "T4"
      elif x == 5:
        compGoal = "B1"
      elif x == 6:
        compGoal = "B2"
      elif x == 7:
        compGoal = "B3"
      elif x == 8:
        compGoal = "B4"

      print("The goalkeeper dived at", compGoal, "!")


  
    # MATCHING INPUTS
    if compGoal == playerChoice:
      print("GAME OVER.")
      print("You scored", endScore ,"goals.")
      break # breaks loop
    
    # NOT MATCHING INPUTS
    if compGoal != playerChoice:
      print("GOALLLL! Keep going!")
      endScore = endScore + 1
      print("You have", endScore, "goal(s).")
      continue # continues loop




def multiplayer():
  endScore = 0
  while gameChoice == "MULTI":
    firstplayerChoice = input("First player, choose a coordinate to shoot at: ")
    firstplayerChoice = firstplayerChoice.capitalize() #just to make sure player uses capital letters for function to work
    print(firstplayerChoice) # to test if capitalisation works
    checkGoal = goal.count(firstplayerChoice) # to check if coordinate is a valid input
    while checkGoal == goal.count(firstplayerChoice):
      if checkGoal > 0:
        print("PLAYER 1 shoots the ball at", firstplayerChoice,"!")
        break
      else:
        print("This is not a valid goal coordinate.")
        firstplayerChoice = input("Choose a coordinate to shoot at: ")
        firstplayerChoice = firstplayerChoice.capitalize() #capitalisation of the t or b in coordinate
        checkGoal = goal.count(firstplayerChoice) # checks again
        continue
        
    secondplayerChoice = input("PLAYER 2, choose a coordinate to dive at: ")
    secondplayerChoice = secondplayerChoice.capitalize() #capitalisation of the t or b in coordinate
    checkGoalTwo = goal.count(secondplayerChoice) #checks if goal is valid
    while checkGoalTwo == goal.count(secondplayerChoice):
      if checkGoalTwo > 0:
        print(playerName, "dived at", secondplayerChoice,"!")
        break
      else:
        print("This is not a valid goal coordinate.")
        secondplayerChoice = input("PLAYER 2, choose a coordinate to dive at: ")
        secondplayerChoice = secondplayerChoice.capitalize() #capitalisation of the t or b in coordinate
        checkGoalTwo = goal.count(secondplayerChoice) # checks again
        continue
     
    print("PLAYER 2 dived at", secondplayerChoice + "!")
    
    
    # MATCHING GOALS
    if secondplayerChoice == firstplayerChoice: 
      print("PLAYER 2 saved it!!")
      print("PLAYER 1 scored", endScore ,"goals.")
      print("GAME OVER.")
      break
    
    # NOT MATCHING GOALS
    if secondplayerChoice != firstplayerChoice:
      print("GOALLLLL!!! Keep going!")
      endScore = endScore + 1
      print("PLAYER 1 has", endScore, "goal(s).")
      continue
  

def simulation():
  endScore = 0 
  difficulty = ["EASY" , "NORMAL", "HARD"] # list of difficulties
  print("Choose the difficulty: EASY/NORMAL/HARD")
  diffChoice = input("Enter: ")
  diffChoice = diffChoice.upper() #capitalisation
  #print(diffChoice)  # to test if capitalisation works
  checkDiff = difficulty.count(diffChoice)  # to check if coordinate is a valid input
  while checkDiff == difficulty.count(diffChoice): #repeatedly prompts the user to enter a valid input if they input an invalid one
    if checkDiff > 0:
      print("OK!")
      break
    else:
      print("This is not a valid difficulty.")
      print("Choose the difficulty: EASY/NORMAL/HARD")
      diffChoicetwo = input("Enter: ")
      diffChoice = diffChoicetwo.upper() #capitalisation
      checkDiff = difficulty.count(diffChoice) #checks again
      continue
    
    
  shooterTypes = ['SHARP', 'NORMAL']  #list of shooter choices
  print("Which kind of player? SHARP/NORMAL")
  shooter_type = input("Enter: ")
  shooter_type = shooter_type.upper() #capitalisation
  #print(shooter_type)  # to test if capitalisation works
  checkType = shooterTypes.count(shooter_type)  # to check if coordinate is a valid input
  while checkType == shooterTypes.count(shooter_type): #repeatedly prompts the user to enter a valid input if they input an invalid one
    if checkType > 0:
      print("OK!")
      break
    else:
      print("This is not a valid player type.")
      print("Choose the difficulty: SHARP/NORMAL")
      shooter_typetwo = input("Enter: ")
      shooter_type = shooter_typetwo.upper() #capitalisation
      checkType = shooterTypes.count(shooter_type) #checks again
      continue  
  
  overallScores = [] #creates list for score of each run to go into
  for i in range(30): #runs 30 times
    endScore = 0
    
    while gameChoice == "SIM":
    
      if shooter_type == "NORMAL":
          shooters_shot = (0.0825, 0.13, 0.1075, 0.06, 0.1475, 0.195, 0.1625, 0.115) # percentages all add up to 1
          def roll(i):
              randRoll = random.random() 
              sum = 0
              result = 1
              for a in i:
                  sum += a
                  if randRoll < sum:
                      return result
                  result+=1
        
        
        
            
          x = roll(shooters_shot) # rolls between all the chances
        
          #depending on the rolled calculation it will output the rolled coordinate
          if x == 1:
              shooter = "T1"
          elif x == 2:
              shooter = "T2"
          elif x == 3:
              shooter = "T3"
          elif x == 4:
              shooter = "T4"
          elif x == 5:
              shooter = "B1"
          elif x == 6:
              shooter = "B2"
          elif x == 7:
              shooter = "B3"
          elif x == 8:
              shooter = "B4"
      
          
      if shooter_type == "SHARP":
          shooters_shot = (0.125, 0.0375, 0.0375, 0.375, 0.0625, 0.0375, 0.0375, 0.1875) # percentages all add up to 1
          def roll(i):
              randRoll = random.random() 
              sum = 0
              result = 1
              for a in i:
                  sum += a
                  if randRoll < sum:
                      return result
                  result+=1
        
        
        
            
          x = roll(shooters_shot) # rolls between all the chances
              
              
             
          #depending on the rolled calculation it will output the rolled coordinate
          if x == 1:
              shooter = "T1"
          elif x == 2:
              shooter = "T2"
          elif x == 3:
              shooter = "T3"
          elif x == 4:
              shooter = "T4"
          elif x == 5:
              shooter = "B1"
          elif x == 6:
              shooter = "B2"
          elif x == 7:
              shooter = "B3"
          elif x == 8:
              shooter = "B4"
      
      # easy is just randomised
      if diffChoice == "EASY":
        compGoal = random.choice(goal)
 
      # hard is a 50-50 chance of matching shooter
      if diffChoice == "HARD":
          goalchance = (0.5, 0.5) # percentages all add up to 1
          def roll(i):
              randRoll = random.random() 
              sum = 0
              result = 1
              for a in i:
                sum += a
                if randRoll < sum:
                    return result
                result+=1
      
          x = roll(goalchance) # rolls between all the chances
        
          
          if x == 1:
            compGoal = shooter
          elif x == 2:
            compGoal = ("x")  #compGoal does not match player's input
    
  
      if diffChoice == "NORMAL":
        goalcoordinates = (0.0575, 0.15, 0.135, 0.05, 0.1725, 0.15, 0.135, 0.15) # percentages all add up to 1
        def roll(i):
            randRoll = random.random()
            sum = 0
            result = 1
            for a in i:
              sum += a
              if randRoll < sum:
                  return result
              result+=1
    

        x = roll(goalcoordinates) # rolls between all the chances
          
          
        #depending on the rolled calculation it will output the rolled coordinate
        if x == 1:
          compGoal = "T1"
        elif x == 2:
          compGoal = "T2"
        elif x == 3:
          compGoal = "T3"
        elif x == 4:
          compGoal = "T4"
        elif x == 5:
          compGoal = "B1"
        elif x == 6:
          compGoal = "B2"
        elif x == 7:
          compGoal = "B3"
        elif x == 8:
          compGoal = "B4"
  
    
      if shooter == compGoal:
        print("GAME OVER.")
        print("Comp 1 scored", endScore ,"goals.")
        overallScores.append(endScore) # the score from each run is stored in this list
        break
  
      if shooter != compGoal:
        
        endScore = endScore + 1 # keeps adding 1 goal until goal matches
        
        continue
  
  print("OVERALL RESULTS", overallScores)

  average = (sum(overallScores)/len(overallScores)) #calculates mean of all 30 runs
  mean = round(average,2)

  print("Average of 30 runs: ", mean)
  print(mean, "is added to the database!") # tells the user that the mean has been sent to the database


  f = open('database.csv', 'a') # opens the file
  
  writer = csv.writer(f)
  
  header = ['EASY', 'NORMAL-N','NORMAL-S', 'HARD'] # all the headers
  #puts 0 in difficulties not chosen
  if diffChoice and shooter_type == "NORMAL":
      data = [[0 , mean, 0, 0]]
  if diffChoice == "NORMAL" and shooter_type == "SHARP":
      data = [[0 , 0, mean, 0]]
  if diffChoice == "EASY":
      data = [[mean, 0, 0, 0]]
  if diffChoice == "HARD":
      data = [[0, 0, 0, mean]]
  
  #write the header
  #writer.writerow(header)
  writer.writerows(data) # writes new row with data collected
  f.close()
  
  #extracts columns from csv file, puts them into lists for calculations
  with open('database.csv', encoding='utf-8-sig') as csvfile:
      reader = csv.DictReader(csvfile)
      count = 0
      fsa_easy = [] #list for easy
      fsa_normaln = [] #list for normal with normal shooter
      fsa_normals = [] #list for normal shooter with sharp shooter
      fsa_hard = [] #list for hard
      for row in reader:
          count = count + 1
          fsa_easy.append(row['EASY'])
          fsa_normaln.append(row['NORMAL-N'])
          fsa_normals.append(row['NORMAL-S'])
          fsa_hard.append(row['HARD'])



  #CALCULATIONS FOR EASY        
  y = ([float(x) for x in fsa_easy]) #turns list into float for calculations
  def check_score_y(y): # filters out all the 0s in the list
      if y >=0.01:
          return True
      return False
  filtered_score_y = filter(check_score_y, y)
  scores_y = list(filtered_score_y)
 
      
  def average(scores_y):
      return ((sum(scores_y)) / (len(scores_y))) #calculations for mean
  final_mean_y = average(scores_y)
      
  final_mean_easy = round(final_mean_y,2)
 

  
  #CALCULATIONS FOR NORMAL WITH NORMAL SHOOTING
  z = ([float(x) for x in fsa_normaln]) #turns list into float for calculations
  def check_score_z(z): # filters out all the 0s in the list
      if z >=0.01:
          return True
      return False
  filtered_score_z = filter(check_score_z, z)
  scores_z = list(filtered_score_z)
  
      
  def average(scores_z):
      return ((sum(scores_z)) / (len(scores_z))) #calculations for mean
  final_mean_z = average(scores_z)
      
  final_mean_normaln = round(final_mean_z,2)
  
  
  
  #CALCULATIONS FOR NORMAL WITH SHARP SHOOTING
  za = ([float(x) for x in fsa_normals]) #turns list into float for calculations
  def check_score_za(za): # filters out all the 0s in the list
      if za >=0.01:
          return True
      return False
  filtered_score_za = filter(check_score_za, za) 
  scores_za = list(filtered_score_za)
  
      
  def average(scores_za):
      return ((sum(scores_za)) / (len(scores_za))) #calculations for mean
  final_mean_za = average(scores_za)
      
  final_mean_normals = round(final_mean_za,2)
  

  
  #CALCULATIONS FOR HARD
  w = ([float(x) for x in fsa_hard]) #turns list into float for calculations
  def check_score_w(w): # filters out all the 0s in the list
      if w >=0.01:
          return True
      return False
  filtered_score_w = filter(check_score_w, w)
  scores_w = list(filtered_score_w)
 
      
  def average(scores_w):
      return ((sum(scores_w)) / (len(scores_w))) #calculations for mean
  final_mean_w = average(scores_w)
      
  final_mean_hard = round(final_mean_w,2)

  
                
  if diffChoice == "EASY":
      print("EASY AVERAGES FROM DATABASE:", scores_y)
      
      print("Mean of the list =", final_mean_easy)
      
      def medianAllAverages(scores_y):
          scores_y.sort() # sorts code by order highest to lowest
          lengthList = len(scores_y)
          middle = (lengthList) //2
          if (middle % 2) == 0: #if length of list is an even number
              median = (scores_y[middle] + scores_y[middle + 1]) /2.0  # calculates median of list with an even number
          else: # if length of list is an odd number
              median = scores_y[middle]
          print("Median of the list =", round(median,2))
      medianAllAverages(scores_y)



  if diffChoice and shooter_type == "NORMAL":

      print("NORMAL AVERAGES FROM DATABASE:", scores_z)

      print("Mean of the list =", final_mean_normaln)
  
      def medianAllAverages(scores_z):
          scores_z.sort() # sorts code by order highest to lowest
          lengthList = len(scores_z)
          middle = (lengthList) //2
          if (middle % 2) == 0: #if length of list is an even number
              median = (scores_z[middle] + scores_z[middle + 1]) /2.0  # calculates median of list with an even number
          else: # if length of list is an odd number
              median = scores_z[middle]
          print("Median of the list =", round(median,2))
      medianAllAverages(scores_z)
      
      

  if diffChoice == "NORMAL" and shooter_type == "SHARP":

      print("NORMAL AVERAGES FROM DATABASE:", scores_za)

      print("Mean of the list =", final_mean_normals)
  
      def medianAllAverages(scores_za):
          scores_za.sort() # sorts code by order highest to lowest
          lengthList = len(scores_za)
          middle = (lengthList) //2
          if (middle % 2) == 0: #if length of list is an even number
              median = (scores_za[middle] + scores_za[middle + 1]) /2.0  # calculates median of list with an even number
          else: # if length of list is an odd number
              median = scores_za[middle]
          print("Median of the list =", round(median,2))
      medianAllAverages(scores_za)  
  

  
  if diffChoice == "HARD":

      print("HARD AVERAGES FROM DATABASE:", scores_w)

      print("Mean of the list =", final_mean_hard)
      
      def medianAllAverages(scores_w):
          scores_w.sort() # sorts code by order highest to lowest
          lengthList = len(scores_w)
          middle = (lengthList) //2
          if (middle % 2) == 0: #if length of list is an even number
              median = (scores_w[middle] + scores_w[middle + 1]) /2.0 # calculates median of list with an even number
          else: # if length of list is an odd number
              median = scores_w[middle]
          print("Median of the list =", round(median,2))
      medianAllAverages(scores_w)
  
  
  # for the graph
  def bleh(): 
    data = {'Easy':final_mean_easy,'Normal-N':final_mean_normaln, 'Normal-S':final_mean_normals, 'Hard':final_mean_hard} #puts all calculations into list 
    diffTypes = list(data.keys()) # on x axis
    values = list(data.values()) # on y axis

    fig = plt.figure(figsize = (10, 7)) # sizes of the axes

    plt.bar(diffTypes, values, color ='dodgerblue', width = 0.4) # design of the bars

    plt.xlabel("DIFFICULTIES")
    plt.ylabel("AVERAGE COMPUTER PERFORMANCE")
    plt.title("Average computer performance in each difficulty")
    plt.show()
  bleh()



gameChoice = input("Which gamemode would you like to play? SINGLE/MULTI/SIM :")
gameChoice = gameChoice.upper() # makes sure input is capitalized to match choice in the list
games = ["SINGLE", "MULTI", "SIM"] 
checkGame = games.count(gameChoice)  # to check if coordinate is a valid input in the list
while checkGame == games.count(gameChoice): # loops until user inputs a valid input for game mode choice
  if checkGame > 0:
    print("Let's do this!")
    break 
  else:
    print("This is not a valid gamemode.")
    gameChoice = input("Which gamemode would you like to play? SINGLE/MULTI/SIM :")
    gameChoice = gameChoice.upper()
    checkGame = games.count(gameChoice)
    continue


# depending on the game choice it will call the function of the game mode
if gameChoice == "SINGLE":
  singlePlayer()

if gameChoice == "MULTI":
  multiplayer()

if gameChoice == "SIM":
  simulation()