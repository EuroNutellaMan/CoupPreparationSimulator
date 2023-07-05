#
# Coup Launcher (part of CoupPrepSim
# by EuroNutella
# Last update: 09/06/2023
#
import sys
import pyfiglet
import time

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
WeapStr = float(sys.argv[5])/100
Intel = float(sys.argv[6])/100
GovPop = float(sys.argv[7])
gMilPop = float(sys.argv[8])
gPolPop = float(sys.argv[9])
gKeySup = float(sys.argv[10])
gWeapStr = float(sys.argv[11])/100
gIntel = float(sys.argv[12])/100
ntrPop = 100 - (PolPop + gPolPop)

# Fetching and reconverting lists

pInv_str = sys.argv[13]
pInvPops_str = sys.argv[14]
gInv_str = sys.argv[15]
gInvPops_str = sys.argv[16]
pInv = list(pInv_str.split(";"))
pInvPops = list(map(float,pInvPops_str.split(";")))
gInv = list(gInv_str.split(";"))
gInvPops = list(map(float,gInvPops_str.split(";")))

#### PROGRAM ####

### More variables

Parliament = "Gov"
Ministries = "Gov"
PresHouse = "Gov"
ArmyBase = "Gov"
NavyBase = "Gov"
AirBase = "Gov"
Airport = "Gov"
Port = "Gov"
TrainStation = "Gov"
RadioTower = "Gov"
NewsOutlets = "Gov"
Internet = "Gov"
GovPers = "Active"
Military = "Active"
CoupLeads = "Active"
CoupMil = "Active"
Population = "Neutral"
PopCare = "Unaware"

### Title

coup = figlet.renderText("        COUP")
launched = figlet.renderText("STARTED")
print(PURPLE,coup,sep='')
print(launched,RESET,sep='')

### Functions

## Phase 1: Seizing infrastructure

# Seize government buildings
def sezParl():
    global Parliament
    CoupStr = MilPop*WeapStr*0.5 + CoupPop*0.5
    CoupStr = CoupStr*Intel
    GovStr = gMilPop*gWeapStr*0.5 + GovPop*0.5
    GovStr = GovStr*gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        Parliament = "Coup"
        print(PURPLE,"The parliament has been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        Parliament = "Contested"
        print(YELLOW,"The parliament is contested!",RESET,sep="")
    elif Outcome < -2.5:
        Parliament = "Gov"
        print(CYAN,"The government has maintained control of the parliament!",RESET,sep="")

def sezMins():
    global Ministries
    CoupStr = MilPop*WeapStr*0.6 + KeySup*0.4
    CoupStr = CoupStr*Intel
    GovStr = gMilPop*gWeapStr*0.6 + gKeySup*0.4
    GovStr = GovStr*gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        Ministries = "Coup"
        print(PURPLE,"The ministries have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        Ministries = "Contested"
        print(YELLOW,"The ministries are contested!",RESET,sep="")
    elif Outcome < -2.5:
        Ministries = "Gov"
        print(CYAN,"The government has maintained control of the ministries!",RESET,sep="")

def sezPres():
    global PresHouse
    CoupStr = MilPop*WeapStr*0.4 + KeySup*0.6
    CoupStr = CoupStr*Intel
    GovStr = gMilPop*gWeapStr*0.4 + gKeySup*0.6
    GovStr = GovStr*gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        PresHouse = "Coup"
        print(PURPLE,"The presidential palace has been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        PresHouse = "Contested"
        print(YELLOW,"The presidential palace is contested!",RESET,sep="")
    elif Outcome < -2.5:
        PresHouse = "Gov"
        print(CYAN,"The government has maintained control of the presidential palace!",RESET,sep="")

# Seize military bases
def sezArmy():
    global ArmyBase
    CoupStr = (MilPop*WeapStr*0.9 + KeySup*0.1) * Intel
    GovStr = (gMilPop*gWeapStr*0.9 + gKeySup*0.1) * gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        ArmyBase = "Coup"
        print(PURPLE,"Army bases have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        ArmyBase = "Contested"
        print(YELLOW,"Army bases are contested!",RESET,sep="")
    elif Outcome < -2.5:
        ArmyBase = "Gov"
        print(CYAN,"The government has maintained control of the army bases!",RESET,sep="")

def sezNavy():
    global NavyBase
    CoupStr = (MilPop*WeapStr*0.8 + KeySup*0.2) * Intel
    GovStr = (gMilPop*gWeapStr*0.8 + gKeySup*0.2) * gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        NavyBase = "Coup"
        print(PURPLE,"Navy bases have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        NavyBase = "Contested"
        print(YELLOW,"Navy bases are contested!",RESET,sep="")
    elif Outcome < -2.5:
        NavyBase = "Gov"
        print(CYAN,"The government has maintained control of the navy bases!",RESET,sep="")

def sezAirf():
    global AirBase
    CoupStr = (MilPop*WeapStr*0.7 + KeySup*0.3) * Intel
    GovStr = (gMilPop*gWeapStr*0.7 + gKeySup*0.3) * gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        AirBase = "Coup"
        print(PURPLE,"Airforce bases have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        AirBase = "Contested"
        print(YELLOW,"Airforce bases are contested!",RESET,sep="")
    elif Outcome < -2.5:
        AirBase = "Gov"
        print(CYAN,"The government has maintained control of the airforce bases!",RESET,sep="")

# Seize communication networks
def sezRadt():
    global RadioTower
    CoupStr = MilPop*WeapStr
    GovStr = gMilPop*gWeapStr*gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        RadioTower = "Coup"
        print(PURPLE,"Radio towers have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        RadioTower = "Contested"
        print(YELLOW,"Radio towers are contested!",RESET,sep="")
    elif Outcome < -2.5:
        RadioTower = "Gov"
        print(CYAN,"The government has maintained control of the radio towers!",RESET,sep="")

def sezNews():
    global NewsOutlets
    CoupStr = MilPop*WeapStr
    GovStr = gMilPop*gWeapStr*gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        NewsOutlets = "Coup"
        print(PURPLE,"News outlets have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        NewsOutlets = "Contested"
        print(YELLOW,"News outlets are contested!",RESET,sep="")
    elif Outcome < -2.5:
        NewsOutlets = "Gov"
        print(CYAN,"The government has maintained control of the news outlets!",RESET,sep="")

def sezIntr():
    global Internet
    CoupStr = MilPop*WeapStr
    GovStr = gMilPop*gWeapStr*gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        Internet = "Coup"
        print(PURPLE,"Internet providers have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        Internet = "Contested"
        print(YELLOW,"Internet providers are contested!",RESET,sep="")
    elif Outcome < -2.5:
        Internet = "Gov"
        print(CYAN,"The government has maintained control of the internet providers!",RESET,sep="")

# Seize critical infrastructure
def sezArpt():
    global Airport
    CoupStr = (MilPop*WeapStr*0.6 + KeySup*0.4) * Intel
    GovStr = (gMilPop*(gWeapStr/2)*0.6 + gKeySup*0.4) * gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        Airport = "Coup"
        print(PURPLE,"Airports have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        Airport = "Contested"
        print(YELLOW,"Airports are contested!",RESET,sep="")
    elif Outcome < -2.5:
        Airport = "Gov"
        print(CYAN,"The government has maintained control of the airports!",RESET,sep="")

def sezPort():
    global Port
    CoupStr = (MilPop*WeapStr*0.7 + KeySup*0.3) * Intel
    GovStr = (gMilPop*(gWeapStr/2)*0.7 + gKeySup*0.3) * gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        Port = "Coup"
        print(PURPLE,"Harbors have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        Port = "Contested"
        print(YELLOW,"Harbors are contested!",RESET,sep="")
    elif Outcome < -2.5:
        Port = "Gov"
        print(CYAN,"The government has maintained control of the harbors!",RESET,sep="")

def sezTrns():
    global TrainStation
    CoupStr = (MilPop*WeapStr*0.8 + KeySup*0.2) * Intel
    GovStr = (gMilPop*(gWeapStr/2)*0.8 + gKeySup*0.2) * gIntel
    Outcome = CoupStr - GovStr
    if Outcome > 2.5:
        TrainStation = "Coup"
        print(PURPLE,"Train stations have been seized by the coupers!",RESET,sep="")
    elif -2.5 <= Outcome <= 2.5:
        TrainStation = "Contested"
        print(YELLOW,"Train stations are contested!",RESET,sep="")
    elif Outcome < -2.5:
        TrainStation = "Gov"
        print(CYAN,"The government has maintained control of the train stations!",RESET,sep="")

## Aftermath of phase 1

# Result calculations
def StsUpd():
    varbs = [GovPers, Military, CoupLeads, CoupMil, PopCare, Population]
    lGovPers, lMilitary, lCoupLeads, lCoupMil, lPopCare, lPopulation = varbs
    varbs2 = [lGovPers, lMilitary, lCoupLeads, lCoupMil, lPopCare, lPopulation]
    for i in range(len(varbs)):
        if varbs[i] == "Neutralized" or varbs[i] == "Apathetic" or varbs[i] == "Nobody":
            varbs2[i] = RED + varbs[i] + RESET
        elif varbs[i] == "Government":
            varbs2[i] = CYAN + varbs[i] + RESET
        elif varbs[i] == "Alert":
            varbs2[i] = ORANGE + varbs[i] + RESET
        elif varbs[i] == "Divided" or varbs[i] == "Agitated":
            varbs2[i] = YELLOW + varbs[i] + RESET
        elif varbs[i] == "Coup":
            varbs2[i] = PURPLE + varbs[i] + RESET
        else:
            varbs2[i] = GREEN + varbs[i] + RESET
    lGovPers, lMilitary, lCoupLeads, lCoupMil, lPopCare, lPopulation = varbs2
    print("Status update:")
    print(CYAN + "Government personnel: " + RESET, lGovPers, sep="")
    print(CYAN + "Government military:  " + RESET, lMilitary, sep="")
    print(PURPLE + "Coup leadership:      " + RESET, lCoupLeads, sep="")
    print(PURPLE + "Coup military:        " + RESET, lCoupMil, sep="")
    print(YELLOW + "Population:           " + RESET, lPopCare, sep="")
    print(YELLOW + "Popular support:      " + RESET, lPopulation, sep="")

def statuses():
    global GovPers
    global Military
    global CoupLeads
    global CoupMil
    global PopCare
    global Population
    x = 0
    if Parliament == "Coup" and Ministries == "Coup" and PresHouse == "Coup":
        GovPers = "Neutralized"
    if ArmyBase == "Coup" and NavyBase == "Coup" and AirBase == "Coup":
        Military = "Neutralized"
    if KeySup == 0:
        CoupLeads = "Neutralized"
    if MilPop == 0:
        CoupMil = "Neutralized"
    if ntrPop >= 75:
        PopCare = "Apathetic"
        x = 0
    elif ntrPop >= 50:
        PopCare = "Alert"
        x = 0.25
    elif ntrPop >= 25:
        PopCare = "Agitated"
        x = 0.5
    elif ntrPop >= 0:
        PopCare = "Rioting"
        x = 0.75
    PopReact = (PolPop - gPolPop)*x
    if PopReact > 2.5:
        Population = "Coup"
    elif PopReact < -2.5:
        Population = "Government"
    elif PopReact == 0 and x == 0:
        Population = "Nobody"
    elif -2.5 <= PopReact <= 2.5:
        Population = "Divided"
    StsUpd()

def recalc():
    global KeySup
    global gKeySup
    global MilPop
    global gMilPop
    gH = 0.0
    cH = 0.0
    if Parliament == "Coup":
        gH = gH + 1
    elif Parliament == "Contested":
        gH = gH + 0.5
        cH = cH + 0.5
    elif Parliament == "Gov":
        cH = cH + 1
    if Ministries == "Coup":
        gH = gH + 1
    elif Ministries == "Contested":
        gH = gH + 0.5
        cH = cH + 0.5
    elif Ministries == "Gov":
        cH = cH + 1
    if PresHouse == "Coup":
        gH = gH + 1
    elif PresHouse == "Contested":
        gH = gH + 0.5
        cH = cH + 0.5
    elif PresHouse == "Gov":
        cH = cH + 1
    KeySup = KeySup - (KeySup/3)*cH
    gKeySup = gKeySup - (gKeySup/3)*gH
    gH = 0.0
    cH = 0.0
    if ArmyBase == "Coup":
        gH = gH + 1
    elif ArmyBase == "Contested":
        gH = gH + 0.5
        cH = cH + 0.5
    elif ArmyBase == "Gov":
        cH = cH + 1
    if NavyBase == "Coup":
        gH = gH + 1
    elif NavyBase == "Contested":
        gH = gH + 0.5
        cH = cH + 0.5
    elif NavyBase == "Gov":
        cH = cH + 1
    if AirBase == "Coup":
        gH = gH + 1
    elif AirBase == "Contested":
        gH = gH + 0.5
        cH = cH + 0.5
    elif AirBase == "Gov":
        cH = cH + 1
    MilPop = MilPop - (MilPop/3)*cH
    gMilPop = gMilPop - (gMilPop/3)*gH
    statuses()

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

### Execution

time.sleep(2)
print("Seizing government buildings...")
time.sleep(1)
sezParl()
time.sleep(1)
sezMins()
time.sleep(1)
sezPres()

time.sleep(2)
print("Seizing military bases...")
time.sleep(1)
sezArmy()
time.sleep(1)
sezNavy()
time.sleep(1)
sezAirf()

time.sleep(2)
print("Seizing key infrastructure...")
time.sleep(1)
sezArpt()
time.sleep(1)
sezPort()
time.sleep(1)
sezTrns()

time.sleep(2)
print("Seizing communication networks...")
time.sleep(1)
sezRadt()
time.sleep(1)
sezNews()
time.sleep(1)
sezIntr()

time.sleep(2)
recalc()
### Beta disclaimer

time.sleep(2)
print("NOTICE: This part is still WIP. For now the simulator ends here. Thanks for trying this beta.")
print("Please if you have any problem or feedback make sure to let me know on Discord.")
print("If you get an error please explain to me what you did and copy the error.")
print("Alternaively you can copy the whole terminal in a text file and send it to me.")
