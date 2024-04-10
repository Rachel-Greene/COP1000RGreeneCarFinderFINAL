## This is the program to run the AutoCountry Vehicle Finder app, version 0.2 ##
## Import text- based message variables python file ##
import sys

sys.path.append('DataFiles/')
import TextControlFile


## ------------------------------ Functions ------------------------------ ##
# F(x) to run and start the program
def startProgram():
  print(TextControlFile.welcomeMessage)
  customerChoiceInput = input()
  validChoiceInput = checkValidInputFX(customerChoiceInput)
  return validChoiceInput

# F(x) to check which choice inputted, validate choice #
def checkValidInputFX(testInputNum):
  if testInputNum == "1": #Print
    return 1
  elif testInputNum == "2": #Search
    return 2
  elif testInputNum == "3": #Add
    return 3
  elif testInputNum == "4": #Delete
    return 4
  elif testInputNum == "5": #Exit
    return 5
  else: #Error
    return 99 

# F(x) to check authorization of vehicle #
def checkVehicleFX(testInputVehicle):
  with open("DataFiles/AllowVehicleList", "r") as db:
    vehicleRow = db.read()
    if testInputVehicle in vehicleRow:
     print(f"\n{testInputVehicle} is an authorized vehicle")
    else:
      print(f"{testInputVehicle} is not an authorized vehicle, if you recieved this in error please check the spelling and try again.")

def processRemovalFX(testRemovalInput):
  ## open the text file as a python file ##
  with open("DataFiles/AllowVehicleList", "r") as db:
    contentsList = db.readlines()
    ## Get rid of new line artifacts ## 
    formattedContentsList = []
    for x in contentsList: 
      formattedContentsList.append(x.strip())
    ## Removal taking place, or not ##
    if testRemovalInput in formattedContentsList:
      formattedContentsList.remove(testRemovalInput)
      print(f"{testRemovalInput} has been removed.")
    else:
      print(f"{testRemovalInput} is not found. Please check spelling and please try again.")
  ## Overwrite with the created list ##
  with open("DataFiles/AllowVehicleListNew", "w") as db:
    print(formattedContentsList)
    for c in formattedContentsList:
      db.write(c+ "\n")
    

## ------------------------------------------------------------ ##
## --------- Run Program, take inputs and process  ------------ ##
# ActiveProgram = true/false defines the ending condition #
activeProgram = True
while activeProgram:
  processedInput = startProgram()

  ## Input = 1 ##
  if processedInput == 1:
    print(TextControlFile.choice1Message)
    with open("DataFiles/AllowVehicleList", "r") as vehicleList:
     for a in vehicleList:
       print(f"{a}")
       activeProgram = False

  ## Input = 2 ##
  if processedInput == 2:
    print(TextControlFile.choice2Message)
    customerVehicleInput = input()
    validVehicleInput = checkVehicleFX(customerVehicleInput)
    activeProgram = False

  ## Input = 3 ##
  if processedInput == 3:
    with open("DataFiles/AllowVehicleList", "a") as db:
      print(TextControlFile.choice3Message)
      appendVehicle = input("")
      db.write("\n")
      db.write(appendVehicle)
    print (f"\n You have added {appendVehicle} as an authorized vehicle. \n")
    activeprogram = False
  ## Input = 4 ##
  if processedInput == 4:
    print(TextControlFile.choice4Message)
    removalInput = input()
    print(f"Are you sure you want to remove \"{removalInput}\" from the authorized vehicle list?")
    decisionInput = input()
    if decisionInput == "yes" or decisionInput == "Yes":
      processRemovalFX(removalInput)
      print("works")
    else:
      print(f"\"{removalInput}\" has not been removed")
       
  ## Input = 5 ##
  if processedInput == 5:
    print(TextControlFile.thankYouMessage)
    activeProgram = False

  ## Input = 99, error ##
  if processedInput == 99:
    print(TextControlFile.errorMessage)
