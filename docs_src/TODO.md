(todo)=
# Todo

Working list for these docs: screenshots still to capture, open questions about the driver, and
the remaining steps before publishing. The source is `docs_src/TODO.md`; tick items there as you
go.

**Screenshots: 17 / 43 done** (as of November 6, 2026).

## How to capture

- Use the same phone for every shot, AAPS in dark theme, no personal notifications in the status bar.
  `python docs_src/tools/screenshots.py demo on` gives a clean status bar (fixed clock, full battery) on phones that support it.
- Capture with the phone's screenshot button, or over USB with `python docs_src/tools/screenshots.py capture <name>`, which saves straight to `docs_src/images/tandem/` (needs `adb`).
- Black out serial numbers, Bluetooth addresses and pairing data. `python docs_src/tools/screenshots.py redact FILE X Y W H` does it, or use any image editor.
- Never include the AAPS home screen: it shows live glucose, heart rate and steps. Crop to the dialog instead.
- Save to `docs_src/images/tandem/` with the file name below. *Refresh* items keep their current name, so the new file overwrites the old one.
- Run `python docs_src/tools/screenshots.py normalize docs_src/images/tandem/<file>` to resize to 1080 px wide and compress.
- On the page (`CompatiblePumps/TandemMobi.md`), point the image at the new file and delete its `% SCREENSHOT:` comment. `grep -rn "% SCREENSHOT" docs_src` lists the ones left.

## Screenshots

### Setup and pairing

Page section: [Setup](#tandem-mobi-setup)

- [ ] **ControlX2 pump search, no pump found** — `controlx2_pairing_stuck.png` · ControlX2
  - Where: ControlX2 → pairing wizard → pump search (stage 1 of 7).
  - Set up: Pump not in pairing mode, so the search keeps running.
- [ ] **ControlX2 App info entry** — `controlx2_appinfo_1.png` · ControlX2
  - Where: Recent apps → tap the ControlX2 icon → menu with App info.
- [ ] **ControlX2 App info screen** — `controlx2_appinfo_2.png` · ControlX2
  - Where: Android Settings → Apps → ControlX2.
- [ ] **ControlX2 permissions, all allowed** — `controlx2_appinfo_3.png` · Retake (old UI)
  - Where: App info → Permissions.
  - Set up: Allow every permission, including Location. The current image shows Location under “Not allowed”, which contradicts the text.
- [ ] **ControlX2 View Pump State** — `controlx2_view_pump_state.jpg` · New
  - Where: ControlX2 → Settings → Debug → View Pump State.
  - Set up: Pump paired. Make sure the Save to Clipboard option is visible.
  - **Redact:** The whole JSON body. It contains the pairing data.
- [ ] **Overview with the Pair Pump button** — `v4_overview_pair_button.jpg` · New
  - Where: AAPS → Mobi overview.
  - Set up: Use Shared Connection and Hide Pump Pair Button in Overview both off, so Pair Pump shows.
  - **Redact:** Serial number and Bluetooth address.
- [ ] **AAPS pairing wizard, every step** — `v4_pairing_wizard_1.jpg, _2.jpg, …` · New
  - Where: Mobi overview → Pair Pump (or Mobi settings → Tandem Pump Connection Wizard).
  - Set up: One screenshot per wizard step, numbered in order: Begin Pairing, device list, PIN entry, connecting, Successfully Connected.
  - **Redact:** Serial number, Bluetooth address and PIN.

### Pump Screen and bolus

Page sections: [Pump Screen](#tandem-mobi-pump-screen), [Bolus progress](#tandem-mobi-bolus-progress)

- [x] **Mobi overview** — `v4_overview.jpg`, replaces `overview_v2.jpg` · Retake (old UI)
- [x] **Overview while a bolus runs** — `v4_overview_bolus.jpg` · New
- [x] **Bolus progress dialog** — `v4_bolus_progress.jpg` · New
- [ ] **Overview with highlighted data labels** *(optional)* — `v4_overview_indicators.jpg` · New
  - Where: AAPS → Mobi overview.
  - Set up: New items so NOTIFICATION, EVENTS and HISTORY are colored (red, green, blue).
  - **Redact:** Serial number and Bluetooth address.
- [ ] **Overview with a driver error** *(optional)* — `v4_overview_error.jpg` · New
  - Where: AAPS → Mobi overview.
  - Set up: Section 5 visible, e.g. move the pump out of Bluetooth range until the connection drops.
  - **Redact:** Serial number and Bluetooth address.

### Mobi settings

Page section: [Mobi settings](#tandem-mobi-settings)

- [x] **Preferences, top** — `v4_preferences_top.jpg`, replaces `pref_v2_1.jpg` · Retake (old UI)
- [x] **Preferences, bottom** — `v4_preferences_bottom.jpg`, replaces `pref_v2_2.jpg` · Retake (old UI)
- [ ] **Preferences with shared connection on** — `v4_preferences_shared.jpg` · New
  - Where: Mobi overview → gear icon.
  - Set up: Use Shared Connection on, so Shared Connection Data shows.
  - **Redact:** Shared Connection Data if it shows anything other than asterisks.

### Actions

Page section: [Actions](#tandem-mobi-actions)

- [x] **Actions, delivery suspended** — `v4_insulin_start_before.jpg` · Refresh (already v4)
- [x] **Actions, delivery running** — `v4_insulin_stop_before.jpg` · Refresh (already v4)
- [x] **Resume insulin confirmation** — `v4_insulin_start.jpg` · Refresh (already v4)
- [x] **Stop insulin confirmation** — `v4_insulin_stop.jpg` · Refresh (already v4)
- [x] **Actions while a temp basal runs** — `v4_actions_tbr_running.jpg` · New
- [x] **Stop Temp Rate confirmation** — `v4_stop_temp_rate.jpg` · New
- [ ] **Cartridge Setup screen** — `v4_cartridge_setup.jpg` · Refresh (already v4)
  - Where: Actions → Cartridge/Cannula Setup.
  - Set up: Ideally with some steps checked.
- [ ] **Change Cartridge, step 1** — `v4_change_cart_step1.jpg` · Refresh (already v4)
  - Where: Cartridge Setup → Change Cartridge.
  - Set up: Delivery stopped, no active notifications.
- [ ] **Change Cartridge, step 2** — `v4_change_cart_step2.jpg` · Refresh (already v4)
  - Where: After Begin Change Cartridge.
  - Set up: Cartridge unlocked.
- [ ] **Change Cartridge, step 3** — `v4_change_cart_step3.jpg` · New
  - Where: After Cartridge Inserted.
  - Set up: The in-progress screen. It can be brief, so be ready to capture.
- [ ] **Change Cartridge, step 4** — `v4_change_cart_step4.jpg` · Refresh (already v4)
  - Where: End of the change.
  - Set up: Status: Cartridge change complete.
- [ ] **Fill Tubing, step 1** — `v4_filltubing_step1.jpg` · Refresh (already v4)
  - Where: Cartridge Setup → Fill Tubing.
  - Set up: No active notifications.
- [ ] **Fill Tubing, step 2 (filling)** — `v4_filltubing_step2a.jpg` · Refresh (already v4)
  - Where: After Begin Fill Tubing.
  - Set up: Before pressing the pump button.
- [ ] **Fill Tubing, step 2 (button released)** — `v4_filltubing_step2b.jpg` · Refresh (already v4)
  - Where: After releasing the pump button.
  - Set up: Yes/No prompt with Restart Fill and Complete Fill.
- [ ] **Fill Tubing, step 3** — `v4_filltubing_step3.jpg` · New
  - Where: After Complete Fill.
  - Set up: Moves on automatically, so capture quickly.
- [ ] **Fill Tubing, step 4** — `v4_filltubing_step4.jpg` · Refresh (already v4)
  - Where: End of the fill.
  - Set up: Status: connect the infusion site.
- [ ] **Fill Cannula, enter amount** — `v4_fill_cannula_1.jpg` · New
  - Where: Cartridge Setup → Fill Cannula.
  - Set up: Amount entered, before tapping Fill Cannula.
- [ ] **Fill Cannula, complete** — `v4_fill_cannula_2.jpg` · New
  - Where: After Fill Cannula.
  - Set up: Completed state.
- [ ] **Change Cartridge blocked by a notification** *(optional)* — `v4_notification_blocking.jpg` · New
  - Where: Cartridge Setup → Change Cartridge.
  - Set up: An unacknowledged notification on the pump.
- [ ] **Site Reminder** — `v4_site_reminder.jpg`, replaces `site_reminder.jpg` · Retake (old UI)
  - Where: Cartridge Setup → Site Reminder.
  - Set up: A preset selected, date and time showing.
- [x] **Pump Info** — `v4_pump_info.jpg`, replaces `pump_info.jpg` · Retake (old UI)

### Data

Page section: [Data](#tandem-mobi-pump-data)

- [x] **Data screen** — `v4_data_main.jpg`, replaces `data_main.jpg` · Retake (old UI)
- [x] **Notifications** — `v4_data_notifications.jpg`, replaces `data_notifications.jpg` · Retake (old UI)
- [x] **Events** — `v4_data_events.jpg`, replaces `data_events.jpg` · Retake (old UI)
- [x] **Pump History list** — `v4_data_history.jpg`, replaces `data_pump_history.jpg` · Retake (old UI)
- [x] **History Log Details** — `v4_data_history_details.jpg`, replaces `data_pump_history_details.jpg` · Retake (old UI)

### Archive (Phase 1)

Page: [Phase 1 documentation](archive/phase-1.md)

- [ ] **Phase 1 T:MOBI tab** — `mobi_driver_overview_v1.jpg` · Keep (historical)
  - Where: Historical image.
  - Set up: No retake. The old UI no longer exists.
- [ ] **Phase 1 preferences** — `mobi_driver_prefs_v1.jpg` · Keep (historical)
  - Where: Historical image.
  - Set up: No retake. The old UI no longer exists.

## Open questions

Each open one also has a `% VERIFY:` comment on its page. List them with `grep -rn "% VERIFY" docs_src`.

- [ ] [Pump Screen fields](#tandem-mobi-pump-screen): Does the top command card also list queued commands?
- [ ] [Pump Screen fields](#tandem-mobi-pump-screen): How does the driver reconnect after losing the pump? The old text said auto-reconnect was coming in Phase 3; the source now has auto-reconnect in the PumpX2 layer.
- [ ] [Pump Screen fields](#tandem-mobi-pump-screen): Document the banner shown when the pump can't be reached and the warning when it is suspended (added in v0.8.14.10)?
- [ ] [Mobi settings](#tandem-mobi-settings), Auto confirm Low Basal Delivery Alert: What is the actual threshold for the Low Basal Delivery Alert? The old text said “less than 50% ??”.
- [ ] [B) Pairing with AAPS only](#tandem-mobi-pair-aaps): Check the wizard steps (written from the source strings) against a real pairing.
- [ ] [Events](#tandem-mobi-events): Is event support in the PumpX2 library still incomplete?
- [ ] [Pump history](#tandem-mobi-history-reading): Phase 4 uses history for safety checks. Is “history is not used by the driver” still true?
- [ ] [Troubleshooting](#tandem-mobi-troubleshooting): Does the Bluetooth off/on tip from the Phase 1 docs still apply?
- [ ] [Troubleshooting](#tandem-mobi-troubleshooting), pump powered down: Is a full cartridge change and fill needed, or only a restart of delivery?
- [ ] [Development phases](testing/phases.md): Short notes for the 0.5–0.8 tags, and which versions belong to which phase.

Resolved:

- [x] Pairing button name: it is **Pair Pump** on the Pump Screen; the wizard also opens from **Tandem Pump Connection Wizard** in the settings. The wizard needs the 6-digit PIN from inside the cartridge bay.
- [x] **Debug Commands**: a developer tool that sends raw PumpX2 messages; documented with a warning.
- [x] **Stop Insulin** while a temp basal runs: still refused (“Before stopping delivery, you need to stop the active Temp Basal Rate”).
- [x] Capabilities bullets for pump history and cartridge/cannula: confirmed in the driver.
- [x] Tags since Phase 1: listed on [Development phases](testing/phases.md).
- [x] Safety banner: all pages now use the README's beta / “use at your own risk” wording.
- [x] Testing from the branch vs. tags: the branch is the default; issues are welcome from either once confirmed in Discord.

## Before publishing

- [ ] Change the push trigger in `.github/workflows/docs.yml` back from `[testing_v4]` to `[testing]` before merging upstream.
- [ ] Work-in-progress preview on the fork (stavlor.github.io/AAPS_Tandem_Testing): enable Actions and set Pages source to GitHub Actions in the fork, then push to `testing_v4` (the branch the workflow builds for now).
- [ ] On the upstream repo, set GitHub Pages source to **GitHub Actions** (Settings → Pages), so the workflow can deploy.
- [x] Delete the old images left directly in `docs_src/images/` (superseded, no longer referenced).
- [ ] Once the Sphinx site is live upstream, delete the old hand-written site: `docs/index.html`, `docs/index_phase_1.html` and `docs/pics/`. Its images were either copied to `docs_src/images/tandem/` or superseded by v4 shots (`pref_v2_up/down.jpg`, `SiteReminder.jpg`, `start_pump.png`, `cartridge_actions.png`).
- [ ] Import the repo on Read the Docs (readthedocs.org → Add project → AAPS_Tandem_Testing). Needs admin rights on the GitHub repo for automatic builds on push, so Andy may need to do it or add you as a maintainer.
- [ ] On Read the Docs, set the default branch to `testing` and turn on pull request previews (Settings → Pull request builds).
- [ ] Decide which site is the main one (GitHub Pages or Read the Docs) and point README.md's documentation link at it.
