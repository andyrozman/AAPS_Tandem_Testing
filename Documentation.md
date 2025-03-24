# t:mobi documentation

NOTE: This is preliminary documentation which will grow as driver is being developed. For now it is intended for testers so that they can setup the driver correctly. Installation instruction for AAPS and controlX2 are in README

## Connection setup

### A.) Using shared connection with controlX2 (in Phase 1 this is the only way)

While we can share "connection" with controlX2, this doesn't mean that both apps can run at same time. If you wish to use controlX2, then you need to "Force close" AAPS and then you can start controlX2 (and vice-versa). If you want to use shared connection, you need to get latest controlX2 version (at least version 1.0.0-20250304). Then you need to install it and pair your t:mobi pump with it. After you paired your pump with controlX2, you need to go into Settings -> Debug -> View Pump State. There will be json with all connection data, use option "Save to Clipboard". Force close the app and then start AAPS.
In AAPS select t:mobi driver and go to configuration. Enable "Use Shared Connection", click on "Shared Connection Data" copy the value you got from controlX2 and exit configuration. AAPS should now be able to connect to your pump. If for some reason doesn't work, "Force Close" AAPS and restart. Driver should be able to connect to pump now.


### B.) Using only AAPS
This will be added in Phase 2, when all needed methods are implemented and UI options are available.


## Configuration options

![Screenshot_20250321_132047_AAPS](https://github.com/user-attachments/assets/87019777-0101-4c81-b584-7712522a768b)


Configuration options description...


## Starting / Stopping pump / Cartridge - Cannula Actions (solution with controlX2 - only possible option at the moment)

If you need to change cartridge (empty or almost empty), you need to "Force Close" AAPS and start controlX2. There you go into "Actions" and Stop the pump (if its not already stopped), then you do "Cartridge Change" (follow instructions), after you are done, you need to do "Fill Cannula" action and when its done, you need to restart the pump. When you are finished "Force Stop" controlX2 and restart AAPS.


## Overview in T:MOBI tab

Once you have Mobi configured, tab T:MOBI becomes available, displaying all important information. Information is 6 different areas. Fist one is shwong information about your pump: Firmware, Serial Number and BT address. If you have configured display of driver version, then version of driver will also be displayed (while doing testing please have this turned on at all times, so that when you report something you can tell me in which version of driver it happened, this will help find problems faster and also see if the problem was fixed in meantime). 2nd are shows state of pump connection, this shows Connected if pump is connected, or if command is running it will show name of command running and also the Queue of commands (queue hides when empty). 3rd area is showing battery statys, reservoir and when last commands were processed. 4th section, shows last bolus, base basal rate and if temp basal is currently running. 5th section shows if there are any driver errors (mostly this would be filled if there is problem with configuration or if for some reason we lost connection with the pump). Last sections shows Pump Events (when something major happens on pump, pump sends so called Qualyfing Events, here the list of events will be shown (on next event old list will be cleaned). This functionality will be extended in Phase 3, to show only indicator that events were received, and events will be visible in another view.

![Screenshot_20250320_230155_AAPS](https://github.com/user-attachments/assets/08925d55-3094-414f-b352-47b06f7c33a3)

