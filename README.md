# py-etherscan-api module
EtherScan.io API python bindings

## Description
This module is written as an effort to provide python bindings to the EtherScan.io API, which can be found at: 
https://etherscan.io/apis
In order to use this, you must attain an Etherscan user account, and generate an API key.

The API variable name `key` needs to be stored in a file named `api_key.py` in the base module directory.  This will be
sorted out to be more user friendly later.

## Available bindings
Currently, only the following Etherscan.io API modules are available:

- accounts
- stats
- tokens

The remaining available modules provided by Etherscan.io will be added shortly

## Examples
All possible calls have an associated example file in the examples folder to show how to call the binding

These of course will be fleshed out with more details and explanation in time

## TODO:

- Package and submit to PyPI
- Add the following modules:
    - event logs
    - geth proxy
    - websockets
- Add robust documentation
- Add unit test suite
- Add requests.session as a connection option
    - include request throttling based on Etherscan's suggestions
- jupyter notebook examples

## Holla at ya' boy
BTC: 16Ny72US78VEjL5GUinSAavDwARb8dXWKG

ETH: 0x5E8047fc033499BD5d8C463ADb29f10f11165ed0
