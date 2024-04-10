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
  if testInputNum == "1":
    return 1
  elif testInputNum == "2":
    return 2
  elif testInputNum == "3":
    return 3
  elif testInputNum == "4":
    return 4
  else:
    return 99

# F(x) to check authorization of vehicle #
def checkVehicleFX(testInputVehicle):
  with open("DataFiles/AllowVehicleList", "r") as db:
    vehicleRow = db.read()
    if testInputVehicle in vehicleRow:
     print(f"\n{testInputVehicle} {TextControlFile.authorizedVehicle}")
    else:
      print(f"{testInputVehicle} {TextControlFile.unauthorizedVehicle}")


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
      db.write(appendVehicle)
      db.write("\n")
      print (f"\n You have added {appendVehicle} as an authorized vehicle. \n")

  ## Input = 4 ##
  if processedInput == 4:
    print(TextControlFile.thankYouMessage)
    activeProgram = False

  ## Input = 99, error ##
  if processedInput == 99:
    print(TextControlFile.errorMessage)
