# Phase 1 documentation (archived)

:::{warning}
This page is kept for reference only. It describes driver version 0.4.x (Phase 1, April 2025) and
is **out of date**. Use the rest of this documentation for the current driver.
:::

In Phase 1:

- The only way to connect was a [shared connection with ControlX2](#tandem-mobi-pair-controlx2).
  Pairing from AAPS arrived in Phase 2.
- Cartridge changes, cannula fills, and starting or stopping the pump had to be done in ControlX2:
  force-stop AAPS, start ControlX2, stop the pump, change the cartridge, fill the cannula, restart
  the pump, then force-stop ControlX2 and restart AAPS.
- If the pump was stopped but a temp basal was still running, the temp basal had to be stopped
  separately.
- An "Unknown Mobi 20 error" popup could appear during these operations and could be ignored.
- Pump events, alerts and alarms were shown in a "Last Pump Event" section on the tab instead of
  the Data views.

:::{container} screens
```{figure} ../images/tandem/mobi_driver_overview_v1.jpg
Phase 1 T:MOBI tab.
```
```{figure} ../images/tandem/mobi_driver_prefs_v1.jpg
Phase 1 preferences.
```
:::
