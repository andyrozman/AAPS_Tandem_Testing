# AAPS_Tandem_Testing
Testing for AAPS Tandem Integration

_Important note:_ Tandem X2 supports only Remote Bolus, which means you can't Loop with it in Closed Loop mode. If Tandem decides to extend functionalities (with Set TBR command) 

## Download all neded parts (needs to be done 1st only)
1. Download pumpX2 from jwoglom's repo: https://github.com/jwoglom/pumpX2, branch dev, and build it
2. Download Tandem branch from Andy's Android APS repository: https://github.com/andyrozman/AndroidAPS, branch andy_tandem, and build it

## Update all needed parts (needs to be done afterwards when versions change)
1. Update local pumpX2 repo and (git pull) build it, (when pumpX2 will start doing tags, you will need to build specific tag (the one specified in AAPS Project (tandem/build.gradle look at variable tandem/build.gradle)
2. Update local AndroidAPS repo to specific tag

## Prepare Android APS (needs to be done once)
1. Go into Maintainance option (click on button in left upper corner, this should give you some options) and select Log Settings and then inside select first 3 pump options: Pump, PumpBtComm and PumpComm
2. To get advanced options working, you will need to go through objectives... If you ahev running AAPS somewhere, export settings from there and import them here, but be careful to update (or remove Nightscout URL), or else test data will go to NS from AAPS instance you exported.
3. If you find error please post it in discord chat first, so that we don't get duplicates or reports of functionalities not yet developed

## Overview
If you want to see what functionalities are being done, you can switch to Projects tab, and there you can visually see what is being worked on and what is comming down the lane. 

## Release Notes for tags:

No relase so far. Relase 0.2 planned by end of september
CURRENT: 
- basic driver framework (fake communication enabled)
- pairing with pump
