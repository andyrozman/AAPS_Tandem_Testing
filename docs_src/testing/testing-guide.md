# Testing guide

:::{danger}
This driver is in beta testing and is not part of an official **AAPS** release. Not all
functionality is fully implemented or tested, and it may not work as expected. **Use it at your own
risk.**
:::

## Prerequisites (one-time)

1. **ControlX2.** Download the latest release from the
   [ControlX2 releases page](https://github.com/jwoglom/controlX2/releases), install it, and pair
   it with your pump. See [Setup](#tandem-mobi-setup).
2. **Android Studio.** Install the latest stable
   [Android Studio](https://developer.android.com/studio/releases) (Rabbit 2 at the time of
   writing).
3. **The driver source.** Clone [Andy's AndroidAPS repository](https://github.com/andyrozman/AndroidAPS)
   and check out the `andy_tandem_dev4` branch:

   ```bash
   git clone https://github.com/andyrozman/AndroidAPS.git
   cd AndroidAPS
   git checkout andy_tandem_dev4
   ```

## Building AAPS

Repeat these steps each time you update the code.

1. In Android Studio, open the folder you cloned and wait for Gradle to finish syncing.
2. Go to **Build → Generate Signed App Bundle or APK** and choose **APK**.
3. Select the module **AndroidAPS.app**.
4. Choose your keystore, or create one the first time. Keep the keystore file and its passwords:
   every later update must be signed with the same key, or Android won't install it over your
   existing **AAPS**.
5. Select the build variant **fullRelease** (or **fullDebug**) and build.
6. Copy the APK to your phone and install it.

## Prepare AAPS (one-time)

1. Open the menu in the top-left corner, go to **Maintenance → Log Settings**, and enable the
   three pump log categories: **Pump**, **PumpBtComm** and **PumpComm**. You can disable most
   others, especially any that produce a lot of logs.
2. Advanced options only work after completing the objectives. If you have **AAPS** running
   elsewhere, you can export its settings and import them here, **but update or remove the
   Nightscout URL first**, or test data will go to that instance's Nightscout.
3. Builds from this branch are development builds, so **AAPS** keeps closed loop disabled until you
   enable it. See the
   [AAPS FAQ](https://androidaps.readthedocs.io/en/latest/UsefulLinks/FAQ.html#alert-running-dev-version-closed-loop-is-disabled)
   for how.

## What to test

Test from the `andy_tandem_dev4` branch. It has the latest fixes, and it is what the developers
expect bug reports against. To update, pull the branch and [rebuild](#building-aaps):

```bash
git checkout andy_tandem_dev4
git pull
```

The branch changes often, so a new build can occasionally break something that worked before.
Report that like any other problem.

### Testing a tagged version

Tags mark specific builds of the driver (see [Release notes](phases.md#release-notes)). Only build
one if you are asked to test that version. In your clone, create a branch from the tag:

```bash
git fetch --tags
git checkout tags/<tag_name> -b <branch_name>

# For example
git checkout tags/tandem_v0.9.9.0 -b tag_tandem_v0.9.9.0
```

The branch name can be anything; the tag name must match exactly.

## Reporting problems

Follow [Where to get help](#tandem-mobi-where-to-get-help): check the
[issues page](https://github.com/andyrozman/AAPS_Tandem_Testing/issues), discuss the problem in the
**#t_mobi-test** Discord channel, and open an issue once it is confirmed as a bug. Post errors in
Discord before opening an issue, so we avoid duplicates and reports about features that aren't
developed yet.

Always include the driver version shown on the [Pump Screen](#tandem-mobi-pump-screen) (enable
[Display Driver Version](#tandem-mobi-settings)) and, for crashes, your logs.

## Collecting logs

If something crashes, connect your phone to your computer and open the **Logcat** window in
Android Studio. There will be a lot of logs; filter them with `package:mine level:info` (leave out
`level:info` for more detail).

Useful strings to filter on:

`X2`
: All logs from the [PumpX2](https://github.com/jwoglom/pumpX2) library, which handles all
  Bluetooth communication with the Mobi.

`SENT-MESSAGE` / `PARSED-MESSAGE`
: Request messages sent to the pump, and response messages received from it.
