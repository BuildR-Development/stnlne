# Development

## Overview

This project is currently under active development. The main goal is to experiment with modular systems, audio processing, and various hidden features without locking the architecture down too early.

## Project Structure

```text
/
├── src/
├── data/
├── cache/
├── logs/
├── config.json
├── main.py
└── DEVELOPMENT.md
```

## Running Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then start the development build:

```bash
python main.py
```

The default development configuration uses `127.0.0.1` and should not require an external connection.

## Development Notes

The codebase is intentionally experimental. APIs and internal structures may change without notice.

Some features are disabled by default because they are incomplete or are only useful for testing:

* Experimental audio processing
* Spectrogram decoding
* Automatic recovery
* Hidden/debug modes

## Logging

Runtime logs are stored in:

```text
logs/runtime.log
```

Use the `debug` option in `config.json` when additional diagnostic information is required.

## TODO

* [ ] Improve error handling
* [ ] Add configuration validation
* [ ] Implement proper module discovery
* [ ] Expand audio processing support
* [ ] Add automated tests
* [ ] Document the internal API
* [ ] Clean up experimental code

## Warning

Development builds may contain unfinished functionality. Do not assume that configuration values or internal APIs will remain compatible between versions.
