# Tandem Mobi driver for AAPS

**Driver version:** {{ version }} (Phase 5 / Beta)

:::{danger}
**Important safety note.** This driver is in beta testing and is not part of an official **AAPS**
release. Not all functionality is fully implemented or tested, and it may not work as expected.
**Use it at your own risk.**
:::

The full pump documentation is on one page, laid out like the other pump pages in the
[AAPS documentation](https://androidaps.readthedocs.io/), so it can move there when the driver is
released: **[Tandem Mobi](CompatiblePumps/TandemMobi.md)**.

## Beta testing

The driver is in beta, but a few things still need to be done. Everything that is missing is
listed as a feature request on the
[AAPS_Tandem_Testing issues page](https://github.com/andyrozman/AAPS_Tandem_Testing/issues),
along with all known bugs.

To start testing, follow the [Testing guide](testing/testing-guide.md). If something doesn't work,
check the issues page first. If it isn't there, post in the **#t_mobi-test** Discord channel so we
can discuss whether it is a bug or just how the driver works, and open an issue once it is
confirmed. See [Where to get help](#tandem-mobi-where-to-get-help).

The current plan is to finalize changes by the end of 2026 and then merge the driver into the
official AAPS repository, ready for the Christmas release or the nearest release after it.

:::{important}
Please read the whole [Tandem Mobi](CompatiblePumps/TandemMobi.md) page before you start testing.
It explains how the Mobi works and how this driver works, which will also help you decide how to
set up the pump. In some cases you may need to restart AAPS after setting up your pump for the
first time.
:::

```{toctree}
:maxdepth: 2
:caption: Pump

CompatiblePumps/TandemMobi
```

```{toctree}
:maxdepth: 2
:caption: Testers

testing/testing-guide
testing/phases
```

```{toctree}
:maxdepth: 1
:caption: Project

contributing/docs
archive/phase-1
```

```{toctree}
:maxdepth: 1
:caption: Todo

TODO
```
