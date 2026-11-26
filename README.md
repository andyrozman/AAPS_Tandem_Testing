# AAPS Tandem Mobi testing

Testing and documentation for the Tandem Mobi pump driver for
[AndroidAPS](https://github.com/nightscout/AndroidAPS) (AAPS).

> [!CAUTION]
> This driver is in beta testing and is not part of an official AAPS release. Not all
> functionality is fully implemented or tested, and it may not work as expected.
> **Use it at your own risk.**

## Documentation

The full documentation is at **https://andyrozman.github.io/AAPS_Tandem_Testing/**. It covers:

- **Tandem Mobi:** setting up and using the pump with AAPS.
- **Testing guide:** building AAPS with the driver, what to test, and collecting logs.
- **Development phases:** the plan, release tags and version history.

## Status

The driver is in Phase 5 (beta, version 0.9.x), built from the `andy_tandem_dev4` branch of
[Andy's AndroidAPS repository](https://github.com/andyrozman/AndroidAPS). The plan is to merge it
into the official AAPS repository for the Christmas 2026 release, or the nearest release after it.
Progress is tracked in the [project view](https://github.com/users/andyrozman/projects/1/views/1).

## Getting help and reporting problems

1. Check the [issues](https://github.com/andyrozman/AAPS_Tandem_Testing/issues) to see whether the
   problem is already known.
2. If not, post in the **#t_mobi-test** channel on the
   [We Are Not Waiting Discord](https://discord.gg/4fQUWHZ4Mw), so we can discuss whether it is a
   bug or how the driver works.
3. Once it is confirmed as a bug, open an issue here, with your driver version and logs.

## Contributing to the docs

The documentation is written in MyST Markdown in `docs_src/` and built with Sphinx. See
[Contributing to these docs](docs_src/contributing/docs.md) for how to build, preview and publish
it.
