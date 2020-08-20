import time
import os
import datetime

Settings.MoveMouseDelay = 1

#variables
version = 'v1.05.6'
logfilename = os.getcwd()+"\\logs\\"+(datetime.datetime.now()).strftime("%Y-%m-%d-%H-%M-%S")+".txt"
    
#create log file
with open(logfilename, "w") as file:
    file.write("----- V4 Ruinous Volcano Grind Bot - "+version+" Event Log -----\n\n")

### START FUNCTIONS ###
#logging function
def log(string):
    ts = time.ctime(time.time())
    with open(logfilename, "a") as file:
        file.write(ts+": "+string+"\n")

#kill loop function
running = True
def runHotkey(event):
    global running
    running = False
Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

#region exists() function
def myExists(reg, similar, *images):
    for img in images:
        if reg.exists(Pattern(img).similar(similar), 0):
            return True;
    return False;

#run back to zone function
def gotoZone():
    click(Location(171, 228))
    click(Location(536, 121))
    dragDrop(Location(1655, 980), Location(1655, 245))
    if zoneresult == 'Ruinous Branch Road':
        log("Running to Ruinous Branch Road")
        click(Location(1585, 862))
    elif zoneresult == 'Ruinous Crater':
        log("Running to Ruinous Crater")
        click(Location(1561, 926))
    elif zoneresult == 'Ruinous Ancient Rubble':
        log("Running to Ruinous Ancient Rubble")
        click(Location(1599, 990))
    dragDrop(Location(1655, 980), Location(1655, 245))
    click(Location(1779, 735))
    click(Location(1699, 38))
    
### END FUNCTIONS ###

#get zone
log("Initiating zone selection")
popup("Must be in Dimensional Bounty!!! Go there now if you are not\nBot will auto pot, rez, redeploy companion and unlock potential when bags full\nMake sure your bundle setting for potential is only set to whites and greens\nOnly works with 1920x1080 and UI Ratio set to 3\nHappy farmin :)", 'V4 Ruinous Volcano Grind Bot - '+version)
zones = ('Ruinous Branch Road','Ruinous Crater','Ruinous Ancient Rubble')
zoneresult = select('Pick a 112k zone to farm', 'V4 Ruinous Volcano Grind Bot - '+version, options = zones)
pots = ('Purple - 500 HP','Blue - 300 HP','Green - 200 HP')
potlvl = select('Pick which HP pot to buy', 'V4 Ruinous Volcano Grind Bot - '+version, options = pots)
#focus V4
switchApp("V4GL")

if zoneresult == 'Ruinous Branch Road':
    log("Ruinous Branch Road selected")
elif zoneresult == 'Ruinous Crater':
    log("Ruinous Crater selected")
elif zoneresult == 'Ruinous Ancient Rubble':
    log("Ruinous Ancient Rubble selected")

#get into Ruinous Volcano
log("Going to Evelyn1 - Ruinous Volcano")
click(Location(1702, 118))
click(Location(1456, 229))
click(Location(1867, 230))
wait("1596983049141.png",45)
click(Location(374, 664))
click(Location(1659, 1028))
click(Location(959, 715))
sleep(5)
#inside ruinous, teleport to closest base
log("Inside Ruinous Volcano")
click(Location(173, 227))
click(Location(535, 122))
dragDrop(Location(1655, 245), Location(1655, 980))
if zoneresult == 'Ruinous Branch Road':
    log("Porting to closest camp: Byway Hideout")
    click(Location(1557, 724))
elif zoneresult == 'Ruinous Crater':
    log("Porting to closest camp: Crater Border Post")
    click(Location(1572, 790))
elif zoneresult == 'Ruinous Ancient Rubble':
    log("Porting to closest camp: Ruins Recon Spot")
    click(Location(1569, 980))
click(Location(1812, 111))
click(Location(1110, 716))
sleep(5)
    
#go to zone    
gotoZone()

### MAIN GRIND LOOP ###
while running:
    if myExists(Region(1305,996,78,75), 0.9, "mp2.png"):
        click(Location(1789, 118))
        click(Location(1109, 714))  
        sleep(5)
        log("No MP pots detected, ported to camp to buy x500")
        
        #fixed way of go to option merchant
        click(Location(1703, 119))
        click(Location(1616, 230))
        click(Location(1865, 229))

        wait("1596933099517.png",15)
        #pick pot
        click(Location(426, 783))
        sleep(2)
        if exists("1597189055288.png"):
            click(Location(959, 717))
            click(Location(1701, 40))
            #bag
            click(Location(1700, 40))
            click(Location(1658, 1027))
            #register in bulk
            click(Location(1739, 1029))
            click(Location(711, 1028))
            sleep(3)
            click(Location(1739, 1029))
            click(Location(711, 1028))
            sleep(3)
            #close potential
            click(Location(1700, 38))

            #fixed way of go to option merchant
            click(Location(1703, 119))
            click(Location(1616, 230))
            click(Location(1865, 229))
            wait("1596933099517.png",15)
            #pick pot
            click(Location(426, 783))
            sleep(2)
            #click +100 x5
            for _ in range(5):
                click(Location(1090, 557))
                sleep(0.5)            
            click(Location(1079, 813))
            click(Location(1701, 40))
            sleep(3)
        else:
            #click +100 x5
            for _ in range(5):
                click(Location(1090, 557))
                sleep(0.5) 
            click(Location(1079, 813))
            click(Location(1701, 40))
            sleep(3)

        #go back to farm
        gotoZone()
    if myExists(Region(1226,996,78,77), 0.9, "hp2.png"):        
        click(Location(1789, 118))
        click(Location(1109, 714))  
        sleep(5)
        log("No HP pots detected, ported to camp to buy x500")
        #fixed way of go to potion merchant
        click(Location(1703, 119))
        click(Location(1616, 230))
        click(Location(1865, 229))
        wait("1596933099517.png",15)
        #pick pot
        if potlvl == 'Purple - 500 HP':
            click(Location(426, 556))
        elif potlvl == 'Blue - 300 HP':
            click(Location(426, 445))
        elif potlvl == 'Green - 200 HP':
            click(Location(427, 332))
        sleep(2)
        #check if inventory full
        if exists("1597189055288.png"):
            click(Location(959, 717))
            click(Location(1701, 40))
            #bag
            click(Location(1700, 40))
            click(Location(1658, 1027))
            #register in bulk
            click(Location(1739, 1029))
            click(Location(711, 1028))
            sleep(3)
            click(Location(1739, 1029))
            click(Location(711, 1028))
            sleep(3)
            #close potential
            click(Location(1700, 38))

            #fixed way of go to potion merchant
            click(Location(1703, 119))
            click(Location(1616, 230))
            click(Location(1865, 229))
            wait("1596933099517.png",15)
            #pick pot
            if potlvl == 'Purple - 500 HP':
                click(Location(426, 556))
            elif potlvl == 'Blue - 300 HP':
                click(Location(426, 445))
            elif potlvl == 'Green - 200 HP':
                click(Location(427, 332))
            sleep(2)
            #click +100 x5
            for _ in range(5):
                click(Location(1090, 557))
                sleep(0.5)            
            click(Location(1079, 813))
            click(Location(1701, 40))
            sleep(3)
        else:
            #click +100 x5
            for _ in range(5):
                click(Location(1090, 557))
                sleep(0.5) 
            click(Location(1079, 813))
            click(Location(1701, 40))
            sleep(3)

        #go back to farm
        gotoZone()
    if myExists(Region(315,37,1359,179), 0.75, "1596987144883.png"):
        click(Location(961, 1022))
        sleep(10)
        log("DEATH DETECTED!!! Revived at camp")
        sleep(5)
        if exists(Pattern("1596985391335.png").similar(0.60)):
            log("Death fatigue detected! Removing")
            click(Pattern("1596985391335.png").similar(0.60))
            wait("1596975644832.png",30)
            #get rid of fatigue depending on free or not
            if exists("1596975668498.png"):
                click(Location(362, 299))
                log("Used Free Recovery")
            else:
                click(Location(363, 301))
                #confirm
                click(Location(957, 714))
                log("Used Gold Recovery")

            #check for any lost gear
            if exists("1596975823489.png"):
                log("No gear lost detected")
            else: 
                log("GEAR LOST DETECTED!!! Make sure to check and recover item!")
        else:
            log("No death fatigue detected")
        #close healer
        click(Location(1699, 40))
        #resume the grind
        log("Resuming grind after death")
        gotoZone()

    if myExists(Region(333,247,100,86), 0.92, "companion2.png"):
        log("Companion detected")
        click(Location(385, 291))
        sleep(3)
        if exists("1597075959739.png"):
            click("1597076063845.png")
            log("Gathering Companion dispatched again")
        elif exists("1597076037321.png"):
            click("1597076063845.png")
            sleep(1)
            log("Hunting Companion dispatched again")
            log("Bundle Unlocking Potential to prevent full inventory")
            click(Location(1700, 41))
            click(Location(1659, 1029))
            sleep(1)
            click(Location(1740, 1025))
            click(Location(716, 1032))
            sleep(3)
            click(Location(1700, 38))
       
        elif exists("1597076158114.png"):
            click("1597076176593.png")
            log("Region Conquest companion collected")
            
                    
        
        
