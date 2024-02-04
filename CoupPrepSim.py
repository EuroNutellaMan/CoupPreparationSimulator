#
# Coup preparation sim
# by EuroNutella
# Last update: 09/06/2023
#
import random
import time
import pyfiglet
import subprocess

RED = "\033[1;31m"
BLUE = "\033[1;34m"
ORANGE = "\033[1;38;2;255;140;0m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

figlet = pyfiglet.Figlet(font="bulbhead")
winfig = pyfiglet.Figlet(font="rectangles")

coup = figlet.renderText("          COUP")
preparation = figlet.renderText("PREPARATION")
simulator = figlet.renderText("  SIMULATOR")

print()
print(PURPLE, coup, RESET, sep='')
print(CYAN, preparation, RESET, sep='')
print(GREEN, simulator, RESET, sep='')
print()

viewcount = 0

# Coupers
pInvolved = []
pUninvolved = []
pInvPops = []
pUninvPops = []
pTotSeats = int(input("Number of seats in your parliament: "))
AllowedActions = []

# Coup starter
pStart = input('Which party is starting the coup? ')
pInvolved.append(pStart)
pStartPop = input('Seats: ')
pStartPop = int(pStartPop)
pInvPops.append(pStartPop)

# Potential coupers
PotParties = input('How many parties can join the coup? ')
PotParties = int(PotParties)
for i in range(PotParties):
    pUninv = input('Potential couper: ')
    pUninvolved.append(pUninv)
    pUninvPop = int(input('Seats: '))
    pUninvPops.append(pUninvPop)

# Initial coup support values
CoupPop = int(round(sum(pInvPops) / pTotSeats * 100, 0))
iMilPop = random.randint(0,CoupPop*2)
iPolPop = random.randint(0,CoupPop)
iKeySup = random.randint(0,CoupPop*2)
iWeapStr = random.randint(0,100)
iFunds = random.randint(0,100)
iIntel = random.randint(0,100)

# New coup support values
nMilPop = 0
nPolPop = 0
nKeySup = 0
nWeapStr = 0
nFunds = 0
nIntel = 0

# Coup support values names
SVNames = ['Parliamentary support','Military support', 'Popular support', 'Key figures support', 'Weapon strength', 'Funds', 'Intelligence']

# Government
gInvolved = []
gUninvolved = []
gInvPops = []
gUninvPops = []

# Gov starter
NumGov = int(input("How many parties are in the government? "))
for i in range(NumGov):
    gInvName = input("Name of party: ")
    gInvolved.append(gInvName)
    gInvSeats = int(input("Seats: "))
    gInvPops.append(gInvSeats)

# Potential gov supporters
gPotParties = int(input("How many parties can support the government? "))
for i in range(gPotParties):
    gUninvName = input("Potential supporter: ")
    gUninvolved.append(gUninvName)
    gUninvSeats = int(input("Seats: "))
    gUninvPops.append(gUninvSeats)

# Initial gov values
GovPop = int(round(sum(gInvPops) / pTotSeats * 100, 0))
igMilPop = random.randint(0, min(int(round(GovPop/2,0)), 100 - iMilPop))
igPolPop = random.randint(0, GovPop)
igKeySup = random.randint(0, min(int(round(GovPop/2,0)), 100 - iKeySup))
igWeapStr = random.randint(50,100)
igIntel = 1

# New gov values
ngMilPop = 0
ngPolPop = 0
ngKeySup = 0
ngWeapStr = 0
ngIntel = 0

# Gov support values names
gSVNames = ["Parliamentary support", "Military support", "Popular support", "Key figures support", "Weapon strength"]

# Main interface function
def viewer():
    print('Starting next turn.',end='')
    for i in range(3):
        time.sleep(1)
        print(".",end='',flush=True)
    print()
    global CoupPop
    global MilPop
    global PolPop
    global KeySup
    global WeapStr
    global Funds
    global Intel
    global SupVals
    global GovPop
    global gMilPop
    global gPolPop
    global gKeySup
    global gWeapStr
    global gIntel
    global gSupVals
    global viewcount
    global ntrMil
    global ntrPop
    global ntrKeySup
    CoupPop = int(round(sum(pInvPops) / pTotSeats * 100, 0))
    MilPop = iMilPop + nMilPop
    PolPop = iPolPop + nPolPop
    KeySup = iKeySup + nKeySup
    WeapStr = iWeapStr + nWeapStr
    Funds = iFunds + nFunds
    Intel = iIntel + nIntel
    SupVals = [CoupPop, MilPop, PolPop, KeySup, WeapStr, Funds, Intel]
    GovPop = int(round(sum(gInvPops) / pTotSeats * 100, 0))
    gMilPop = igMilPop + ngMilPop
    gPolPop = igPolPop + ngPolPop
    gKeySup = igKeySup + ngKeySup
    gWeapStr = igWeapStr + ngWeapStr
    gIntel = igIntel + ngIntel
    gSupVals = [GovPop, gMilPop, gPolPop, gKeySup, gWeapStr, gIntel]
    ntrMil = 100 - (MilPop + gMilPop)
    ntrPop = 100 - (PolPop + gPolPop)
    ntrKeySup = 100 - (KeySup + gKeySup)
    print(PURPLE,"============ Coup strength: ============",RESET,sep='')
    for i in range(len(SupVals)):
        if SupVals[i] > 80:
            print(BLUE,SVNames[i]+': Very strong ['+str(SupVals[i])+'/100]',RESET,sep='')
        elif SupVals[i] > 60:
            print(GREEN,SVNames[i]+': Strong ['+str(SupVals[i])+'/100]',RESET,sep='')
        elif SupVals[i] > 40:
            print(YELLOW,SVNames[i]+': Moderate ['+str(SupVals[i])+'/100]',RESET,sep='')
        elif SupVals[i] > 20:
            print(ORANGE,SVNames[i]+': Weak '+'['+str(SupVals[i])+'/100]',RESET,sep='')
        else:
            print(RED,SVNames[i]+': Very weak ['+str(SupVals[i])+'/100]',RESET,sep='')
    avg = int(round(sum(SupVals)/len(SupVals)))
    if avg > 80:
        print(BLUE,'Average strength: Very strong ['+str(avg)+'/100]',RESET,sep='')
    elif avg > 60:
        print(GREEN,'Average strength: Strong ['+str(avg)+'/100]',RESET,sep='')
    elif avg > 40:
        print(YELLOW,'Average strength: Moderate ['+str(avg)+'/100]',RESET,sep='')
    elif avg > 20:
        print(ORANGE,'Average strength: Weak ['+str(avg)+'/100]',RESET,sep='')
    else:
        print(RED,'Average strength: Very weak ['+str(avg)+'/100]',RESET,sep='')
    print('')
    print(CYAN, "========= Government strength: =========",RESET,sep='')
    for i in range(len(gSVNames)):
        if gSupVals[i] > 80:
            print(BLUE,gSVNames[i]+': Very strong ['+str(gSupVals[i])+'/100]',RESET,sep='')
        elif gSupVals[i] > 60:
            print(GREEN,gSVNames[i]+': Strong ['+str(gSupVals[i])+'/100]',RESET,sep='')
        elif gSupVals[i] > 40:
            print(YELLOW,gSVNames[i]+': Moderate ['+str(gSupVals[i])+'/100]',RESET,sep='')
        elif gSupVals[i] > 20:
            print(ORANGE,gSVNames[i]+': Weak '+'['+str(gSupVals[i])+'/100]',RESET,sep='')
        else:
            print(RED,gSVNames[i]+': Very weak ['+str(gSupVals[i])+'/100]',RESET,sep='')
    if gIntel == 100:
        print(BLUE,"Intelligence: Complete network knoweledge ["+str(gIntel)+"/100]",RESET,sep='')
    elif gIntel >= 75:
        print(GREEN,"Intelligence: Partial network knoweledge ["+str(gIntel)+"/100]",RESET,sep='')
    elif gIntel >= 50:
        print(YELLOW,"Intelligence: Aware ["+str(gIntel)+"/100]",RESET,sep='')
    elif gIntel >= 25:
        print(ORANGE,"Intelligence: Rumors ["+str(gIntel)+"/100]",RESET,sep='')
    else:
        print(RED,"Intelligence: Unaware ["+str(gIntel)+"/100]",RESET,sep='')
    avg = int(round(sum(gSupVals)/len(gSupVals)))
    if avg > 80:
        print(BLUE,'Average strength: Very strong ['+str(avg)+'/100]',RESET,sep='')
    elif avg > 60:
        print(GREEN,'Average strength: Strong ['+str(avg)+'/100]',RESET,sep='')
    elif avg > 40:
        print(YELLOW,'Average strength: Moderate ['+str(avg)+'/100]',RESET,sep='')
    elif avg > 20:
        print(ORANGE,'Average strength: Weak ['+str(avg)+'/100]',RESET,sep='')
    else:
        print(RED,'Average strength: Very weak ['+str(avg)+'/100]',RESET,sep='')
    print('')
    viewcount = viewcount + 1
    if viewcount % 2 == 0:
        GovActions()
    else:
        CoupActions()

# Coup action selector
def CoupActions():
    global AllowedActions
    AllowedActions = []
    print(PURPLE,'---------------------',sep='')
    print('|!! CHOOSE ACTION !!|')
    print('---------------------')
    if Funds >= 5:
        if len(pUninvolved) > 0:
            print('pi = invite a party to the coup (5 funds)')
            AllowedActions.append('pi')
        print('df = start a disinformation campaign (5 funds)')
        AllowedActions.append('df')
        print('gi = gather intelligence (5 funds)')
        AllowedActions.append('gi')
    if Funds > 0:
        print('bk = bribe key figures')
        AllowedActions.append('bk')
        print('bm = bribe military personnel')
        AllowedActions.append('bm')
        print('pw = purchase weapons')
        AllowedActions.append('pw')
    print('fr = start a fundraiser')
    AllowedActions.append('fr')
    print('sf = siphon funds')
    AllowedActions.append('sf')
    print('sw = steal weapons')
    AllowedActions.append('sw')
    print('lc = launch coup (No going back!)')
    AllowedActions.append('lc')
    crep = 'y'
    while crep == 'y':
        choice = input('Choice: ')
        if choice not in AllowedActions:
            print('Invalid choice! Try again!')
            crep = 'y'
        else:
            crep = 'n'
            print(RESET)
    if choice == 'pi':
        pInvite()
    elif choice == 'fr':
        pFundraise()
    elif choice == 'df':
        pDisinfo()
    elif choice == 'gi':
        pGathIntel()
    elif choice == 'bk':
        pCorruptKeyFig()
    elif choice == 'bm':
        pCorruptMilPop()
    elif choice == 'pw':
        pPurWeaps()
    elif choice == 'sf':
        pSphFunds()
    elif choice == 'sw':
        pStealWeaps()
    elif choice == 'lc':
        CoupLaunch()

# Function to invite another party to the plot
def pInvite():
    print('Choose a party to invite!')
    for i in range(len(pUninvolved)):
        print(i,':',pUninvolved[i],sep='')
    np = input('Choose number: ')
    np = int(np)
    nps = []
    nps.append(np)
    for i in nps:
        print('You have selected',pUninvolved[i],'with',pUninvPops[i],'seats')
        global nFunds
        global nMilPop
        global nPolPop
        global nKeySup
        global ngIntel
        nFunds = nFunds - 5
        decider = random.randint(1,100)
        if decider > 75:
            print(BLUE,'GREAT SUCCESS! They are fully on board!',RESET,sep='')
            pInvolved.append(pUninvolved[i])
            pInvPops.append(pUninvPops[i])
            pUninvolved.pop(i)
            nMilPop = nMilPop + random.randint(0,min(int(round(pUninvPops[i]/pTotSeats*100,0)), ntrMil))
            nPolPop = nPolPop + random.randint(0,min(int(round(pUninvPops[i]/pTotSeats*100,0)), ntrPop))
            nKeySup = nKeySup + random.randint(0,min(int(round(pUninvPops[i]/pTotSeats*100,0)), ntrKeySup))
            pUninvPops.pop(i)
        elif decider > 50:
            print(GREEN,'SUCCESS! They are partially on board!',RESET,sep='')
            sj = random.randint(1,pUninvPops[i]-1)
            pInvolved.append(pUninvolved[i])
            pInvPops.append(sj)
            nMilPop = nMilPop + random.randint(0,min(int(round(sj/pTotSeats*100,0)), ntrMil))
            nPolPop = nPolPop + random.randint(0,min(int(round(sj/pTotSeats*100,0)), ntrPop))
            nKeySup = nKeySup + random.randint(0,min(int(round(sj/pTotSeats*100,0)), ntrKeySup))
            pUninvPops[i] = pUninvPops[i] - sj
        elif decider > 25:
            print(ORANGE,'FAILURE! They were not convinced!',RESET,sep='')
            ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
        else:
            print(RED,'CRITICAL FAILURE! They ratted us out!',RESET,sep='')
            nMilPop = nMilPop - random.randint(0,min(int(round(pUninvPops[i]/pTotSeats*100,0)),MilPop))
            nPolPop = nPolPop - random.randint(0,min(int(round(pUninvPops[i]/pTotSeats*100,0)),PolPop))
            nKeySup = nKeySup - random.randint(0,min(int(round(pUninvPops[i]/pTotSeats*100,0)),KeySup))
            if gIntel >= 50:
                ngIntel = ngIntel + random.randint(min(100-gIntel,6),min(10,100-gIntel))
            else:
                ngIntel = 50 - igIntel
        if pUninvolved == []:
            print('All parties available were invited!')
    viewer()

# Fundraiser
def pFundraise():
    global nFunds
    global ngIntel
    fr = random.randint(0,min(PolPop,100-Funds))
    nFunds = nFunds + fr
    if gIntel >= 25:
        ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
    print(YELLOW,'You have raised ',fr,' in funds!',RESET,sep='')
    viewer()

# Disinformation campaign
def pDisinfo():
    global nFunds
    global nPolPop
    global ngIntel
    nFunds = nFunds - 5
    succRate = random.randint(0,100)
    if gIntel >= 25:
        ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
    if succRate > 50:
        ns = random.randint(min(1,ntrPop),min(10,ntrPop))
        nPolPop = nPolPop + ns
        print(GREEN,'SUCCESS! Your popular support has risen by ',ns,RESET,sep='')
    else:
        ns = random.randint(min(1,PolPop),min(10,PolPop))
        nPolPop = nPolPop - ns
        print(ORANGE,'FAILURE! Your popular support has decreased by ',ns,RESET,sep='')
    viewer()


# Gather intel
def pGathIntel():
    global nFunds
    global nKeySup
    global nIntel
    global ngIntel
    nFunds = nFunds - 5
    succRate = random.randint(0,100)
    if succRate > 75:
        nib = random.randint(min(6,100-Intel),min(10,100-Intel))
        nks = random.randint(0,min(5,ntrKeySup))
        nIntel = nIntel + nib
        nKeySup = nKeySup + nks
        print(BLUE,'GREAT SUCCESS! You have gathered ',nib,' intel and ',nks,' key supporters!',RESET,sep='')
    elif succRate > 50:
        ni = random.randint(min(1,100-Intel),min(5,100-Intel))
        nIntel = nIntel + ni
        print(GREEN,'SUCCESS! You have gathered ',ni,' intel!',RESET,sep='')
    elif succRate > 25:
        ni = random.randint(min(1,Intel),min(5,Intel))
        nIntel = nIntel - ni
        ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
        print(ORANGE,'FAILURE! The government stopped our agent, you lost ',ni,' intel!',RESET,sep='')
    else:
        nib = random.randint(min(6,Intel),min(10,Intel))
        nks = random.randint(0,min(5,KeySup))
        nIntel = nIntel - nib
        nKeySup = nKeySup - nks
        if gIntel >= 50:
            ngIntel = ngIntel + random.randint(min(100-gIntel,6),min(10,100-gIntel))
        else:
            ngIntel = 50 - igIntel
        print(RED,'CRITICAL FAILURE! The government discovered us, you lost ',nib,' intel and ',nks,' key supporters!',RESET,sep='')
    viewer()

# Corrupt key figures
def pCorruptKeyFig():
    global nFunds
    global nKeySup
    global ngIntel
    KSValue = random.randint(1,3)
    if KSValue == 3:
        print('You have interested a high level figure!')
        ConvKF = random.randint(11,15)
        KFV = min(15,ntrKeySup)
    elif KSValue == 2:
        print('You have interested a medium level figure!')
        ConvKF = random.randint(6,10)
        KFV = min(10,ntrKeySup)
    elif KSValue == 1:
        print('You have interested a low level figure!')
        ConvKF = random.randint(1,5)
        KFV = min(5,ntrKeySup)
    xrep = 'y'
    while xrep == 'y':
        Bribe = int(input('Insert amount of funds you want to use as a bribe: '))
        if Bribe > Funds or Bribe < 0:
            print("You can't do that!")
            xrep = 'y'
        else:
            xrep = 'n'
    nFunds = nFunds - Bribe
    if Bribe >= ConvKF:
        print(GREEN,'SUCCESS! You spent ',Bribe,' funds to gain ',KFV,' support from key figures!',RESET,sep='')
        nKeySup = nKeySup + KFV
    else:
        print(ORANGE,'FAILURE! You spent ',Bribe,' funds but got no support!',RESET)
        ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
    viewer()

# Corrupt military personnel
def pCorruptMilPop():
    global nFunds
    global nMilPop
    global nWeapStr
    global ngIntel
    MPValue = random.randint(1,3)
    if MPValue == 3:
        print('You have interested a high level figure!')
        ConvMP = random.randint(11,15)
        MPV = min(15,100-MilPop)
        WSV = random.randint(min(11,100-WeapStr),min(15,WeapStr))
    elif MPValue == 2:
        print('You have interested a medium level figure!')
        ConvMP = random.randint(6,10)
        MPV = min(10,100-KeySup)
        WSV = random.randint(min(6,100-WeapStr),min(10,WeapStr))
    elif MPValue == 1:
        print('You have interested a low level figure!')
        ConvMP = random.randint(1,5)
        MPV = min(5,100-KeySup)
        WSV = random.randint(min(1,100-WeapStr),min(5,WeapStr))
    xrep = 'y'
    while xrep == 'y':
        Bribe = int(input('Insert amount of funds you want to use as a bribe: '))
        if Bribe > Funds or Bribe < 0:
            print("You can't do that!")
            xrep = 'y'
        else:
            xrep = 'n'
    nFunds = nFunds - Bribe
    if Bribe >= ConvMP:
        print(GREEN,'SUCCESS! You spent ',Bribe,' funds to gain ' ,MPV,' support from the military and ',WSV,' new weapons!',RESET,sep='')
        nMilPop = nMilPop + MPV
        nWeapStr = nWeapStr + WSV
    else:
        print(ORANGE,'FAILURE! You spent ',Bribe,' funds but got no support and no weapons!',RESET)
        ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
    viewer()

# Purchase weapons
def pPurWeaps():
    global nFunds
    global nWeapStr
    global ngIntel
    xrep = 'y'
    while xrep == 'y':
        spend = int(input('Insert funds to use to buy weapons (1W = 1F): '))
        if spend > Funds or spend < 0:
            print("You can't do that!")
            xrep = 'y'
        else:
            xrep = 'n'
    NW = min(spend,100-WeapStr)
    nFunds = nFunds - spend
    nWeapStr = nWeapStr + NW
    ngIntel = ngIntel + min(int(round(spend/2,0)),100-gIntel)
    print(YELLOW,'You bought ',NW,' weapons using ',spend,' funds!',RESET,sep='')
    viewer()

# Siphon funds
def pSphFunds():
    global nFunds
    global nKeySup
    global ngIntel
    chance = CoupPop + KeySup
    randNum = random.randint(0,100)
    succRate = min((chance - randNum),100)
    if succRate > 75:
        nf = random.randint(min(6,100-Funds),min(10,100-Funds))
        nFunds = nFunds + nf
        print(BLUE,'GREAT SUCCESS! You have siphoned ',nf,' funds!',RESET,sep='')
    elif succRate > 50:
        nf = random.randint(min(1,100-Funds),min(5,100-Funds))
        nFunds = nFunds + nf
        print(GREEN,'SUCCESS! You have gathered ',nf,' funds!',RESET,sep='')
    elif succRate > 25:
        nf = random.randint(min(1,Funds),min(5,Funds))
        nFunds = nFunds - nf
        ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
        print(ORANGE,'FAILURE! The government fined us, you lost ',nf,' funds!',RESET,sep='')
    else:
        nf = random.randint(min(6,Funds),min(10,Funds))
        nks = random.randint(0,min(5,KeySup))
        nFunds = nFunds - nf
        nKeySup = nKeySup - nks
        if gIntel >= 50:
            ngIntel = ngIntel + random.randint(min(100-gIntel,6),min(10,100-gIntel))
        else:
            ngIntel = 50 - igIntel
        print(RED,'CRITICAL FAILURE! The government discovered us, you lost ',nf,' funds and ',nks,' key supporters!',RESET,sep='')
    viewer()

# Steal weapons
def pStealWeaps():
    global nMilPop
    global nWeapStr
    global nIntel
    global ngIntel
    chance = MilPop + Intel
    randNum = random.randint(0,100)
    succRate = min((chance - randNum),100)
    if succRate > 75:
        nws = random.randint(min(6,100-WeapStr),min(10,100-WeapStr))
        nmp = random.randint(0,min(5,ntrMil))
        nWeapStr = nWeapStr + nws
        nMilPop = nMilPop + nmp
        print(BLUE,'GREAT SUCCESS! You have gathered ',nws,' weapons and ',nmp,' military supporters!',RESET,sep='')
    elif succRate > 50:
        nws = random.randint(min(1,100-WeapStr),min(5,100-WeapStr))
        nWeapStr = nWeapStr + nws
        print(GREEN,'SUCCESS! You have gathered ',nws,' intel!',RESET,sep='')
    elif succRate > 25:
        ni = min(5,Intel)
        nIntel = nIntel - ni
        ngIntel = ngIntel + random.randint(min(1,100-gIntel),min(5,100-gIntel))
        print(ORANGE,'FAILURE! The government stopped our agent, you lost ',ni,' intel and gained no weapons!',RESET,sep='')
    else:
        nmp = random.randint(0,min(5,MilPop))
        ni = min(5,Intel)
        nIntel = nIntel - ni
        nMilPop = nMilPop - nmp
        if gIntel >= 50:
            ngIntel = ngIntel + random.randint(min(100-gIntel,6),min(10,100-gIntel))
        else:
            ngIntel = 50 - igIntel
        print(RED,'CRITICAL FAILURE! The government discovered us, you lost ',ni,' intel and ',nmp,' military supporters!',RESET,sep='')
    viewer()

# Gov actions
def GovActions():
    global gAllowedActions
    gAllowedActions = []
    print(CYAN,'---------------------',sep='')
    print('|!! CHOOSE ACTION !!|')
    print('---------------------')
    if gIntel == 100:
        gAllowedActions.append("al")
        print("al = arrest leadership")
    if gIntel >= 75:
        gAllowedActions.append("ag")
        print("ag = arrest generals (5 intel)")
        gAllowedActions.append("ak")
        print("ak = arrest key figures (5 intel)")
    if gIntel >= 50:
        gAllowedActions.append("db")
        print("db = debunk coupers' claims (3 intel)")
        gAllowedActions.append("rf")
        print("rf = recover funds (3 intel)")
        gAllowedActions.append("rw")
        print("rw = raid weapon storage (3 intel)")
        gAllowedActions.append("ge")
        print("ge = gather equipment")
        if len(gUninvolved) > 0:
            gAllowedActions.append("ip")
            print("ip = invite party to support the government")
        gAllowedActions.append("ek")
        print("ek = ensure key support")
        gAllowedActions.append("em")
        print("em = ensure military support")
    if gIntel >= 25:
        gAllowedActions.append("pc")
        print("pc = propaganda campaign")
        gAllowedActions.append("is")
        print("is = investigate suspicious rumors")
    choice = ''
    if gIntel < 25:
        print("No actions available!",RESET,sep='')
        viewer()
    else:
        crep = 'y'
        choice = input('Choice: ')
        while crep == 'y':
            if choice not in gAllowedActions:
                print('Invalid choice! Try again!')
                crep = 'y'
            else:
                crep = 'n'
    print(RESET)
    if choice == "al":
        gArrLeads()
    elif choice == "ag":
        gArrGens()
    elif choice == "ak":
        gArrKeys()
    elif choice == "db":
        gDebunk()
    elif choice == "rf":
        gRecFunds()
    elif choice == "rw":
        gRaidWeaps()
    elif choice == "ge":
        gEquipGath()
    elif choice == "ip":
        gPartyInv()
    elif choice == "ek":
        gEnKeySup()
    elif choice == "em":
        gEnMilPop()
    elif choice == "pc":
        gPropCamp()
    elif choice == "is":
        gInvCoup()

# Gov propaganda campaign
def gPropCamp():
    global ngPolPop
    succRate = random.randint(1,100)
    if succRate > 80:
        newPolPop = random.randint(min(6,ntrPop),min(10,ntrPop))
        ngPolPop = ngPolPop + newPolPop
        print(BLUE,"GREAT SUCCESS! We gathered ",newPolPop," popular support!",RESET,sep='')
    elif succRate > 60:
        newPolPop = random.randint(min(1,ntrPop),min(5,ntrPop))
        ngPolPop = ngPolPop + newPolPop
        print(GREEN,"SUCCESS! We gathered ",newPolPop," popular support!",RESET,sep='')
    elif succRate > 40:
        print(YELLOW,"INCONCLUSIVE! We have neither gathered nor lost popular support!",RESET,sep='')
    elif succRate > 20:
        newPolPop = random.randint(min(1,gPolPop),min(5,gPolPop))
        ngPolPop = ngPolPop - newPolPop
        print(ORANGE,"FAILURE! We lost ",newPolPop," popular support!",RESET,sep='')
    else:
        newPolPop = random.randint(min(6,gPolPop),min(10,gPolPop))
        ngPolPop = ngPolPop - newPolPop
        print(RED,"CRITICAL FAILURE! We lost ",newPolPop," popular support!",RESET,sep='')
    viewer()

# Investigate coupers
def gInvCoup():
    global ngIntel
    succRate = random.randint(1,3)
    newInt = random.randint(min(1,100-gIntel),min(5,100-gIntel))
    if succRate == 3:
        ngIntel = ngIntel + newInt
        print(GREEN,"SUCCESS! You have successfully gathered ",newInt," intelligence on a potential coup!",RESET,sep='')
    elif succRate == 2:
        print(YELLOW,"Your investigation found nothing!",RESET,sep='')
    else:
        ngIntel = ngIntel - newInt
        print(RED,"FAILURE! Your lead turned out to be false, you lost ",newInt," intelligence on a potential coup!",RESET,sep='')
    viewer()

# Ensure military loyalty
def gEnMilPop():
    global ngMilPop
    succRate = random.randint(1,100)
    if succRate > 75:
        newMilSup = random.randint(min(6,ntrMil),min(10,ntrMil))
        ngMilPop = ngMilPop + newMilSup
        print(BLUE,"GREAT SUCCESS! We ensured the loyalty of our military by ",newMilSup,"!",RESET,sep='')
    elif succRate > 50:
        newMilSup = random.randint(min(1,ntrMil),min(5,ntrMil))
        ngMilPop = ngMilPop + newMilSup
        print(GREEN,"SUCCESS! We ensured the loyalty of our military by ",newMilSup,"!",RESET,sep='')
    elif succRate > 25:
        newMilSup = random.randint(min(1,gMilPop),min(5,gMilPop))
        ngMilPop = ngMilPop - newMilSup
        print(ORANGE,"FAILURE! We lost the loyalty of our military by ",newMilSup,"!",RESET,sep='')
    else:
        newMilSup = random.randint(min(6,gMilPop),min(10,gMilPop))
        ngMilPop = ngMilPop - newMilSup
        print(RED,"CRITICAL FAILURE! We lost the loyalty of our military by ",newMilSup,"!",RESET,sep='')
    viewer()

# Ensure key figures loyalty
def gEnKeySup():
    global ngKeySup
    succRate = random.randint(1,100)
    if succRate > 75:
        newKeySup = random.randint(min(6,ntrKeySup),min(10,ntrKeySup))
        ngKeySup = ngKeySup + newKeySup
        print(BLUE,"GREAT SUCCESS! We ensured the loyalty of key figures by ",newKeySup,"!",RESET,sep='')
    elif succRate > 50:
        newKeySup = random.randint(min(1,ntrKeySup),min(5,ntrKeySup))
        ngKeySup = ngKeySup + newKeySup
        print(GREEN,"SUCCESS! We ensured the loyalty of key figures by ",newKeySup,"!",RESET,sep='')
    elif succRate > 25:
        newKeySup = random.randint(min(1,gKeySup),min(5,gKeySup))
        ngKeySup = ngKeySup - newKeySup
        print(ORANGE,"FAILURE! We lost the loyalty of key figures by ",newKeySup,"!",RESET,sep='')
    else:
        newKeySup = random.randint(min(6,gKeySup),min(10,gKeySup))
        ngKeySup = ngKeySup - newKeySup
        print(RED,"CRITICAL FAILURE! We lost the loyalty of our military by ",newKeySup,"!",RESET,sep='')
    viewer()

# Search support from another party
def gPartyInv():
    global ngMilPop
    global ngPolPop
    global ngKeySup
    print("Available parties:")
    for i in range(len(gUninvolved)):
        print(i,':',gUninvolved[i],sep='')
    nps = int(input("Choose a party to invite (integer): "))
    print("You have chosen",gUninvolved[nps])
    succRate = random.randint(1,2)
    if succRate == 2:
        gInvolved.append(gUninvolved[nps])
        gInvPops.append(gUninvPops[nps])
        gUninvolved.pop(nps)
        ngMilPop = nMilPop + random.randint(0,min(int(round(gUninvPops[nps]/pTotSeats*100,0)), ntrMil))
        ngPolPop = ngPolPop + random.randint(0,min(int(round(gUninvPops[nps]/pTotSeats*100,0)), ntrPop))
        ngKeySup = ngKeySup + random.randint(0,min(int(round(gUninvPops[nps]/pTotSeats*100,0)), ntrKeySup))
        gUninvPops.pop(nps)
        print(GREEN,"SUCCESS! We convinced them to support us!",RESET,sep='')
    else:
        print(RED,"FAILURE! We couldn't convince them to support us!",RESET,sep='')
    if gUninvolved == []:
        print("All parties available have been invited!")
    viewer()

# Gather equipment
def gEquipGath():
    global ngWeapStr
    newEquip = random.randint(0,min(10,100-gWeapStr))
    ngWeapStr = ngWeapStr + newEquip
    print(YELLOW,"We have gathered ",newEquip," pieces of equipment.",RESET,sep='')
    viewer()

# Debunk coup propaganda
def gDebunk():
    global nPolPop
    global ngIntel
    if gIntel >= 53:
        ngIntel = ngIntel - 3
    succRate = random.randint(1,100)
    if succRate > 80:
        np = random.randint(min(6,PolPop),min(10,PolPop))
        nPolPop = nPolPop - np
        print(BLUE,"GREAT SUCCESS! We lowered the coupers popularity by ",np,"!",RESET,sep='')
    elif succRate > 60:
        np = random.randint(min(1,PolPop),min(5,PolPop))
        nPolPop = nPolPop - np
        print(GREEN,"SUCCESS! We lowered the coupers popularity by ",np,"!",RESET,sep='')
    elif succRate > 40:
        print(YELLOW,"INCONCLUSIVE! No significant change in popularity was observed.",RESET,sep='')
    elif succRate > 20:
        np = random.randint(min(1,ntrPop),min(5,ntrPop))
        nPolPop = nPolPop + np
        print(ORANGE,"FAILURE! Our campaign backfired and the coupers gained ",np," in popularity!",RESET,sep='')
    else:
        np = random.randint(min(6,ntrPop),min(10,ntrPop))
        nPolPop = nPolPop + np
        print(RED,"GREAT FAILURE! Our campaign backfired and the coupers gained ",np," in popularity!",RESET,sep='')
    viewer()

# Raid suspected weapons depot
def gRaidWeaps():
    global ngIntel
    global nWeapStr
    global ngWeapStr
    if gIntel >= 53:
        ngIntel = ngIntel - 3
    chance = (gMilPop + gWeapStr) - (MilPop + WeapStr)
    if chance > 0:
        wl = min(10,WeapStr)
        nWeapStr = nWeapStr - wl
        ngWeapStr = ngWeapStr + min(wl,100-gWeapStr)
        print(GREEN,"SUCCESS! We have recovered ",wl," weapons!",RESET,sep='')
    elif chance == 0:
        print(YELLOW,"INCONCLUSIVE! We couldn't recover any weapons!",RESET,sep='')
    else:
        wl = min(10,gWeapStr)
        nWeapStr = nWeapStr + wl
        ngWeapStr = ngWeapStr - min(wl,gWeapStr)
        print(RED,"FAILURE! We lost ",wl," weapons!",RESET,sep='')
    viewer()

# Recover funds
def gRecFunds():
    global ngIntel
    global nFunds
    if gIntel >= 53:
        ngIntel = ngIntel - 3
    chance = gKeySup - KeySup
    if chance > 0:
        fl = min(10,Funds)
        nFunds = nFunds - fl
        print(GREEN,"SUCCESS! We recovered ",fl," funds!",RESET,sep='')
    else:
        print(RED,"FAILURE! We didn't recover any funds!",RESET,sep='')
    viewer()

# Arrest generals
def gArrGens():
    global ngIntel
    global nMilPop
    global ngMilPop
    global nWeapStr
    global ngWeapStr
    ngIntel = ngIntel - 5
    succRate = random.randint(1,100)
    if succRate > 75:
        msl = random.randint(min(6,MilPop),min(10,MilPop))
        wsl = random.randint(min(1,WeapStr),min(5,WeapStr))
        nMilPop = nMilPop - msl
        nWeapStr = nWeapStr - wsl
        ngWeapStr = ngWeapStr + min(wsl, 100-gWeapStr)
        print(BLUE,"GREAT SUCCESS! We arrested the generals and seized some weapons! They lost ",msl," military support and ",wsl," weapon strength.",RESET,sep='')
    elif succRate > 50:
        msl = random.randint(min(1,MilPop),min(5,MilPop))
        nMilPop = nMilPop - msl
        print(GREEN,"SUCCESS! We arrested the generals! They lost ",msl," military support.",RESET,sep='')
    elif succRate > 25:
        print(ORANGE,"FAILURE! The generals escaped capture!",RESET,sep='')
    else:
        msl = random.randint(min(1,gMilPop),min(5,gMilPop))
        ngMilPop = ngMilPop - msl
        print(RED,"CRITICAL FAILURE! Our intel was wrong, we arrested one of our own generals! We lost ",msl," military support.",RESET,sep='')
    viewer()

# Arrest key figures
def gArrKeys():
    global ngIntel
    global nKeySup
    global ngKeySup
    global nFunds
    ngIntel = ngIntel - 5
    succRate = random.randint(1,100)
    if succRate > 75:
        msl = random.randint(min(6,KeySup),min(10,KeySup))
        nf = random.randint(min(1,Funds),min(5,Funds))
        nKeySup = nKeySup - msl
        print(BLUE,"GREAT SUCCESS! We arrested the key figures and seized some funds! They lost ",msl," key support and ",nf," funds.",RESET,sep='')
    elif succRate > 50:
        msl = random.randint(min(1,KeySup),min(5,KeySup))
        nKeySup = nKeySup - msl
        print(GREEN,"SUCCESS! We arrested the key figures! They lost ",msl," key support.",RESET,sep='')
    elif succRate > 25:
        print(ORANGE,"FAILURE! The key figures escaped capture!",RESET,sep='')
    else:
        msl = random.randint(min(1,gKeySup),min(5,gKeySup))
        ngKeySup = ngKeySup - msl
        print(RED,"CRITICAL FAILURE! Our intel was wrong, we arrested one of our own key supporters! We lost ",msl," key support.",RESET,sep='')
    viewer()

# Arrest ring leaders
def gArrLeads():
    global iMilPop
    global nMilPop
    global iKeySup
    global nKeySup
    global iFunds
    global nFunds
    global iWeapStr
    global nWeapStr
    global iIntel
    global nIntel
    global ngIntel
    ngIntel = ngIntel - 10
    chance = (gMilPop + gKeySup + gWeapStr) - (MilPop + KeySup + WeapStr)
    if chance > 0:
        iMilPop = 0
        iKeySup = 0
        iWeapStr = 0
        iFunds = 0
        iIntel = 0
        nMilPop = 0
        nKeySup = 0
        nWeapStr = 0
        nFunds = 0
        nIntel = 0
        GovPrevCoup()
    elif chance == 0:
        iMilPop = int(round(iMilPop/2,0))
        iKeySup = int(round(iKeySup/2,0))
        iWeapStr = int(round(iWeapStr/2,0))
        iFunds = int(round(iFunds/2,0))
        iIntel = int(round(iIntel/2,0))
        nMilPop = int(round(nMilPop/2,0))
        nKeySup = int(round(nKeySup/2,0))
        nWeapStr = int(round(nWeapStr/2,0))
        nFunds = int(round(nFunds/2,0))
        nIntel = int(round(nIntel/2,0))
        print(GREEN,"We managed to arrest half the leadership!",RESET,sep='')
        viewer()
    else:
        iMilPop = int(round(iMilPop*0.75,0))
        iKeySup = int(round(iKeySup*0.75,0))
        iWeapStr = int(round(iWeapStr*0.75,0))
        iFunds = int(round(iFunds*0.75,0))
        iIntel = int(round(iIntel*0.75,0))
        nMilPop = int(round(nMilPop*0.75,0))
        nKeySup = int(round(nKeySup*0.75,0))
        nWeapStr = int(round(nWeapStr*0.75,0))
        nFunds = int(round(nFunds*0.75,0))
        nIntel = int(round(nIntel*0.75,0))
        ngIntel = ngIntel - 10
        print(YELLOW,"We managed to arrest a quarter of the leadership!",RESET,sep='')
        viewer()

# Coup launch

# Launch the coup
def CoupLaunch():
    CoupPop = str(round(sum(pInvPops) / pTotSeats * 100, 0))
    MilPop = str(iMilPop + nMilPop)
    PolPop = str(iPolPop + nPolPop)
    KeySup = str(iKeySup + nKeySup)
    WeapStr = str(iWeapStr + nWeapStr)
    Intel = str(iIntel + nIntel)
    GovPop = str(round(sum(gInvPops) / pTotSeats * 100, 0))
    gMilPop = str(igMilPop + ngMilPop)
    gPolPop = str(igPolPop + ngPolPop)
    gKeySup = str(igKeySup + ngKeySup)
    gWeapStr = str(igWeapStr + ngWeapStr)
    gIntel = str(igIntel + ngIntel)
    pInv_str = ";".join(str(element) for element in pInvolved)
    pInvPops_str = ";".join(str(element) for element in pInvPops)
    gInv_str = ";".join(str(element) for element in gInvolved)
    gInvPops_str = ";".join(str(element) for element in gInvPops)
    command = ["python3","CoupLaunch.py",CoupPop,MilPop,PolPop,KeySup,WeapStr,Intel,GovPop,gMilPop,gPolPop,gKeySup,gWeapStr,gIntel,pInv_str,pInvPops_str,gInv_str,gInvPops_str]
    subprocess.run(command)

# Victory screens

# Coup prevented
def GovPrevCoup():
    GovWin = winfig.renderText("Government Wins")
    print(CYAN,GovWin,sep='')
    print()
    print("We have successfully prevented a coup on our government!")
    for i in range(len(pInvolved)):
        if pInvolved[i] in pUninvolved:
            print(pInvPops[i]," parliamentarians from ",pInvolved[i]," were arrested.",sep='')
        else:
            print(pInvolved[i]," was banned and its parliamentarians arrested.",sep='')
    print("The leaders of the coup have been arrested.")
    print("Loyalty in the military has been secured.")
    print("Loyalty among key figures has been secured.")
    print("All stolen weapons and funds were recovered.",RESET,sep='')
    if PolPop >= 75:
        print(RED,"The arrests sparked nationwide protests and riots among the population.",RESET,sep='')
    elif PolPop >= 50:
        print(ORANGE,"The arrests sparked major protests among the population.",RESET,sep='')
    elif PolPop >= 25:
        print(YELLOW,"The arrests sparked minor protests among the population.",RESET,sep='')
    else:
        if gPolPop >= 50:
            print(CYAN,"Citizens accross the nation celebrate this victory.",RESET,sep='')
        else:
            print(CYAN,"Citizens move on with their day to day life.",RESET,sep='')

# Starting text
print(PURPLE)
print("As the head of ",pInvolved[0]," you have decided that enough is enough. Your country needs a new leader, and that is you!",sep='')
print("Unfortunately the elections weren't enough to secure the victory you rightfully deserve and now a weak government stands in your way.")
print("Our party currently has ",pInvPops[0]," seats out of ",pTotSeats,".",sep='')
if len(pUninvolved) > 0:
    print("There are ",len(pUninvolved)," potential partners that may join our cause too.",sep='')
print(RESET)

time.sleep(5)

viewer()