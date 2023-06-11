#
# Coup Launcher (part of CoupPrepSim
# by EuroNutella
# Last update: 09/06/2023
#
import sys
import pyfiglet

# Pyfiglet
figlet = pyfiglet.Figlet(font="standard")
winfig = pyfiglet.Figlet(font="rectangles")
GovWin = winfig.renderText("Government Wins")
CoupWin = winfig.renderText("Coupers Win")

# Colors

RED = "\033[1;31m"
BLUE = "\033[1;34m"
ORANGE = "\033[1;38;2;255;140;0m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Fetching variables

CoupPop = float(sys.argv[1])
MilPop = float(sys.argv[2])
PolPop = float(sys.argv[3])
KeySup = float(sys.argv[4])
WeapStr = float(sys.argv[5])
Intel = float(sys.argv[6])
GovPop = float(sys.argv[7])
gMilPop = float(sys.argv[8])
gPolPop = float(sys.argv[9])
gKeySup = float(sys.argv[10])
gWeapStr = float(sys.argv[11])
gIntel = float(sys.argv[12])

# Fetching and reconverting lists

pInv_str = sys.argv[13]
pInvPops_str = sys.argv[14]
gInv_str = sys.argv[15]
gInvPops_str = sys.argv[16]
pInv = list(pInv_str.split(";"))
pInvPops = list(map(float,pInvPops_str.split(";")))
gInv = list(gInv_str.split(";"))
gInvPops = list(map(float,gInvPops_str.split(";")))

print("Coupers:",CoupPop,MilPop,PolPop,KeySup,WeapStr,Intel)
print("Government:",GovPop,gMilPop,gPolPop,gKeySup,gWeapStr,gIntel)
print(pInv)
print(pInvPops)
print(gInv)
print(gInvPops)

### PROGRAM ###

## More variables

Parliament = "Gov"
Ministries = "Gov"
SupremeCourt = "Gov"
ArmyBase = "Gov"
NavyBase = "Gov"
AirBase = "Gov"
Airport = "Gov"
Port = "Gov"
TrainStation = "Gov"
RadioTower = "Gov"
NewsOutlet = "Gov"
Internet = "Gov"
GovPers = "Active"
Military = "Active"
CoupLeads = "Active"
CoupMil = "Active"
Population = "Neutral"

## Title

coup = figlet.renderText("        COUP")
launched = figlet.renderText("STARTED")
print(PURPLE,coup,sep='')
print(launched,RESET,sep='')

## Phase 1: Seizing infrastructure

# Seize government buildings

# Seize military bases

# Seize communication networks

# Seize critical infrastructure

## Aftermath of phase 1

# Street clashes

# Military skirmishes

# Government remnants

## Phase 2: response

# Government actions

# Coup actions

## Victory screens

# Coupers win

# Government wins

# Civil war

## Beta disclaimer

print("NOTICE: This part is still WIP. For now the simulator ends here. Thanks for trying this beta.")
print("Please if you have any problem or feedback make sure to let me know on Discord.")
print("If you get an error please explain to me what you did and copy the error.")
print("Alternaively you can copy the whole terminal in a text file and send it to me.")
