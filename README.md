# AAPS_Tandem_Testing :  t:mobi
Testing for AAPS Tandem t:mobi Integration

# AAPS - t:mobi integration status
You can see status in project view: [on https://github.com/andyrozman](https://github.com/users/andyrozman/projects/1/views/1)
We started on Phase 1 on 17th February.


## Download all neded parts (needs to be done 1st time only)
1. Download Tandem branch from Andy's Android APS repository: https://github.com/andyrozman/AndroidAPS, branch andy_tandem, and build it

## Update all needed parts (needs to be done afterwards when versions change)
1. Update local AndroidAPS repo to specific tag (or to branch, depending on what is being tested

## Prepare Android APS (needs to be done once)
1. Go into Maintainance option (click on button in left upper corner, this should give you some options) and select Log Settings and then inside select first 3 pump options: Pump, PumpBtComm and PumpComm
2. To get advanced options working, you will need to go through objectives... If you ahev running AAPS somewhere, export settings from there and import them here, but be careful to update (or remove Nightscout URL), or else test data will go to NS from AAPS instance you exported.
3. If you find error please post it in discord chat first, so that we don't get duplicates or reports of functionalities not yet developed

## Testing Mode
You can test either from tag (when provided) or from branch.

### Testing from tag
After certaing phase or functionality in phase is done, tag will be created which can be then be tested. When tag is created, functionalities are *supposed* to be ready. When testing in tag, if you find any problem report it first in chat (discord), if we decide that it is an error, then open issue here.

### Testing from branch
If you feel adventerous you can try to test from andy_tandem branch directly. Problem with testing from branch is that things are changed a lot, so it can happen that you get code, that has not been fully implemented, which could break your AAPS... If you find problem here you can mention it in chat, but don't open issue for it...

## Overview of Phases

I decided to divide development process into 5 phases. After each of phases we have product that can be used (not fully, but its still usable).

**Phase 1**: This will be probably the longest one, because driver framework needs to be established, pairing solved and communication running, as well as some basic commands implemented, such as: getting certain configurations, reading certain statuses (battery, remaining insulin), setting pump in non-ControlIQ mode, geting profile, setting profile, getting and setting TBR. Bigest work however will probably be work on Cartridge Change/Filling Canula and stuff needed before we can get pump running. Phase 1 will have only oref0 support (TBRs only)

**Phase 2**: In this phase we will take a look at pairing UI and implementation of methods for Bolus, taking look at history

**Phase 3**: Advanced stuff: reading and parsing history (1), Alerts and Alarms investigation and handling, Quick bolus UI and handling

**Phase 4**: More Advanced stuff: integrate security from reading the history. Getting product stable...

**Phase 5**: Release phase. When we reach this phase we will start preparing for release (merge into /dev) and preparing relevant documentation... 


## Overview
If you want to see detailed view of what functionalities are being done, you can go to [Project View](https://github.com/users/andyrozman/projects/1/views/1), and there you can visually see what is being worked on and what is comming down the lane. 

## Release Notes for tags:

No tags so far.


## Special note for Phase_1

Pairing in Phase 1 is done without UI, so for this to work you need to get your PIN (if you remove reservoir, its lower number, 6 characters). Then you have to go to classes and find TandemPumpConfig and put your PIN there (this will be removed in Phase_2, when we have UI for pairing).

## History
0.1.x - 0.3.x - Framework for new driver - refactor what was being prepared for t:slim and split into 2 implementations
0.4.x - This is current version on the branch
