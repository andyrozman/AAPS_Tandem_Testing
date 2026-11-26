# Development phases

Development is divided into five phases. After each phase there is a product that can be used
(not fully, but still usable). Detailed progress is tracked in the
[project view](https://github.com/users/andyrozman/projects/1/views/1).

The driver is currently in **Phase 5** (beta, version 0.9.x). Phase 1 started on 17 February 2025
and was completed on 4 April 2025.

**Phase 1.** Establish the driver framework, solve pairing and get communication running, and
implement basic commands: reading configuration and status (battery, remaining insulin), setting
the pump to non-Control-IQ mode, reading and setting the profile, reading and setting temp basals,
and some other settings. Pairing requires ControlX2. oref0 support only (temp basals only).

**Phase 2.** Pairing UI, cartridge change and cannula fill, and everything else needed to run the
pump fully from AAPS, built with Compose UI (this is the first AAPS driver to use Compose). Bolus
support (and oref1), and a first look at history and qualifying events (pump events).

**Phase 3.** Reading and parsing history into the AAPS database; investigating and handling
alerts and alarms (with database support); better display and storage of qualifying events; quick
bolus configuration; Pump Info UI.

**Phase 4.** Using the pump history for safety checks (for example, comparing treatments with
pump history records, and reporting to AAPS that delivery has stopped and when). Stabilization.

**Phase 5.** Release: merging into the AAPS `dev` branch and preparing documentation.

## Release notes

Tags in [Andy's AndroidAPS repository](https://github.com/andyrozman/AndroidAPS/tags), oldest
first. Testers normally build from the `andy_tandem_dev4` branch instead; see
[What to test](testing-guide.md#what-to-test).

| Tag | Date | Notes |
| --- | --- | --- |
| `tandem_0.4.9.2` | 27 Feb 2025 | Phase 1 in progress |
| `tandem_0.4.23` | 27 Mar 2025 | Temp basals (set, read, cancel), max bolus and max basal |
| `tandem_0.4.26` | 27 Mar 2025 | Same build as `tandem_0.4.23` |
| `tandem_0.4.26.1` | 5 Apr 2025 | **Phase 1 release.** Adds reading alerts and alarms |
| `tandem_0.5.28` | 13 Aug 2025 | |
| `tandem_0.6.8.8` | 22 Aug 2025 | |
| `tandem_0.6.20.0` | 30 Aug 2025 | |
| `tandem_0.6.28.1` | 11 Sep 2025 | |
| `tandem_v0_7_8_0_20260204` | 4 Feb 2026 | |
| `tandem_v0.8.13.0` | 26 Jun 2026 | |
| `tandem_v0.8.14.0` | 26 Jun 2026 | Updated for the AAPS core update |
| `tandem_v0.8.14.10` | 28 Jun 2026 | Pump Screen status banners |
| `tandem_v0.8.15.4` | 28 Jun 2026 | |
| `tandem_v0.8.19.0` | 9 Jul 2026 | Settings fixes for AAPS 4 |
| `tandem_v0.8.27.11` | 12 Aug 2026 | Wizards restyled to match AAPS |
| `tandem_v0.9.9.0` | 31 Oct 2026 | Latest tag. Support for a new PumpX2 version |

% VERIFY: notes are taken from the tag commit messages. Ask Andy for a line on the 0.5-0.8 tags.

## Version history

0.1.x – 0.3.x
: Driver framework: refactoring what was prepared for the t:slim X2 and splitting it into two
  implementations.

0.4.x
: Phase 1 implementation.

0.5.x – 0.8.x
: Phases 2 to 4 (August 2025 to August 2026).

0.9.x
: Phase 5 / Beta (current).

% VERIFY: confirm which 0.5-0.8 versions belong to which phase.
