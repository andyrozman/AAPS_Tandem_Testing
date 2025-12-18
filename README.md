# AAPS_Tandem_Testing: Tandem Mobi
Testing for AAPS Tandem t:mobi Integration

# AAPS - Tandem Mobi integration status
You can see status in project view: [on https://github.com/users/andyrozman/projects/1/views/1](https://github.com/users/andyrozman/projects/1/views/1)

We started on Phase 1 on 17th February and it was completed on 4th April 2025.

As of December 2025, we are in Phase 2/Phase 3.


> [!CAUTION]
> **IMPORTANT SAFETY NOTE**:
> At the moment, the current integration is NOT safe for non-testing use. TESTING ON LIVING PERSONS OR ANIMALS IS STRICTLY FORBIDDEN.
> 
> You can test with your pump, with it not being connected to anything.
> Until we have reached the end of Phase 3, important security measures will not yet be fully implemented
> (comparing treatment data with pump history records, reporting to AAPS/Loop that treatment has stopped and at what time, etc). 


# AAPS - Tandem Mobi Driver Documentation

Full documentation is maintained on this page: https://andyrozman.github.io/AAPS_Tandem_Testing/


## Prerequisites (one time actions)

1. [ControlX2](https://github.com/jwoglom/controlX2)
    - Download the latest ControlX2 release on the [GitHub Releases page](https://github.com/jwoglom/controlX2/releases)
    - Install the app and go through the setup wizard to pair it with your pump. (to pair your pump you need to put it on the charging pad, wait, then remove it and press the button on the pump quickly 2 times). 

2. Download the `andy_tandem` branch from [Andy's AndroidAPS repository](https://github.com/andyrozman/AndroidAPS) and build it in Android Studio.

```
git clone https://github.com/andyrozman/AndroidAPS.git
cd AndroidAPS
git checkout andy_tandem

```



## Prepare AndroidAPS (needs to be done once)
1. Go into Maintainance option (click on button in left upper corner, this should give you some options) and select Log Settings and then inside select first 3 pump options: Pump, PumpBtComm and PumpComm (you can deselect most of other ones, especially if you see a lot of logs from them). 
2. To get advanced options working, you will need to go through objectives... If you have an existing running instance of AAPS somewhere, export settings from there and import them here, but be careful to update (or remove Nightscout URL), or else test data will go to NS from AAPS instance you exported.
3. If you run into any errors, please post it in the discord chat first, so that we don't get duplicates or reports of functionalities not yet developed


## Testing Mode
You can test either from tag (when provided) or from the branch directly.

### Testing from branch
If you feel adventerous you can try to test from the `andy_tandem` branch directly.
However, keep in mind that are changed a lot, so the latest code on the branch may not be fully implemented and/or tested, which could break your AAPS install.
If you find any problems here you can mention it in chat, but don't open issue for it.


### Testing from tag
After enough implementation work has been done, tags will be created which can be then be tested.
When a tag is created, we will denote specific functionalities which are *supposed* to be ready.

When testing a released tag, if you find any problems report it first in chat (discord), and if we decide that it is an error, then open an issue here.

#### How to get a tag
Once you are in previously checked out repository (see prerequisite 2)

```
# Create branch from a tag
git checkout tags/<tag_name> -b <branch_name>

# So our command would be something like this
git checkout tags/tandem_0.4.26 -b tag_tandem_0.4.26

```

You can use any name for branch, just the tag name must be same as the one specified (see Release notes for tags with list of all available tags)



## How to test
You just need to install AAPS and start testing.

If you see that something is crashing, you can connect your phone to computer and go into Android Studio and look at Logcat window, there you would see all the active logs (there will be a lot of them, you can filter it with using "package:mine level:info" (if you need more info you can leave level out of search string).

Some specific log strings which may be helpful to use when filtering:

* `X2` - all logs emitted by the [PumpX2](https://github.com/jwoglom/pumpX2) library (which powers all of the bluetooth connections with the Mobi pump) will have "X2" in the log line
* `SENT-MESSAGE` / `PARSED-MESSAGE` - request messages sent to the pump and response messages received from the pump

## Overview of Phases

I decided to divide development process into 5 phases. After each of phases we have product that can be used (not fully, but its still usable).

**Phase 1**: Driver framework needs to be established, pairing solved and communication running, as well as some basic commands implemented, such as: getting certain configurations, reading certain statuses (battery, remaining insulin), setting pump in non-ControlIQ mode, geting profile, setting profile, getting and setting TBR, and some other settings. In this version there is requirement to use controlX2 application for setting up the pump (see documentation for more details). Phase 1 will have only oref0 support (TBRs only)

**Phase 2**: In this phase we will take a look at pairing UI, but the biggest work will probably be work on Cartridge Change/Filling Cannula and stuff needed before we can get pump fully running from AAPS (working with Compose UI, since AAPS will be fully refactored to use it in near future). We are the first driver to use Compose and I will have to get trained on it, which will make this phase much longer than it was planned in beginning. Methods for Bolus will also be done here (and support for oref1), also taking first look at history, Qualifying Events (Pump events).

**Phase 3**: Advanced stuff: reading and parsing history (1) and putting it into the AAPS database, Alerts and Alarms investigation and handling (and db), Qualifying Events better display and db, Quick bolus configuration, Pump Info UI

**Phase 4**: More Advanced stuff: integrate security from reading the history. Getting product stable...

**Phase 5**: Release phase. When we reach this phase we will start preparing for release (merge into /dev) and preparing relevant documentation... 


## Overview
If you want to see detailed view of what functionalities are being done, you can go to [Project View](https://github.com/users/andyrozman/projects/1/views/1), and there you can visually see what is being worked on and what is comming down the lane. 

## Release Notes for tags:

tandem_0.4.26.1 - release for Phase 1 (completed)



## History
0.1.x - 0.3.x - Framework for new driver - refactor what was being prepared for t:slim and split into 2 implementations
0.4.x - This is current version on the branch (Phase 1 implementation)
