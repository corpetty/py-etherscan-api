# py-etherscan-api module

[![Build Status](https://secure.travis-ci.org/corpetty/py-etherscan-api.png?branch=master)](http://travis-ci.org/corpetty/py-etherscan-api) [![Join the chat at https://gitter.im/py-etherscan/Lobby](https://badges.gitter.im/py-etherscan/Lobby.svg)](https://gitter.im/py-etherscan/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

EtherScan.io API python bindings

## Description

This module is written as an effort to provide python bindings to the EtherScan.io API, which can be found at:
https://etherscan.io/apis. If you are interacting with a contract on the Ropsten Testnet please use
https://ropsten.etherscan.io/apis.
In order to use this, you must attain an Etherscan user account, and generate an API key.

In order to use the API, you must provide an API key at runtime, which can be found at the Etherscan.io API website.
If you'd like to use the provided examples without altering them, then the JSON file `api_key.json` must be stored in
the base directory. Its format is as follows:

    { "key" : "YourApiKeyToken" }

with `YourApiKeyToken` is your provided API key token from EtherScan.io

## Installation

To install the package to your computer, simply run the following command in the base directory:

    python3 -m pip install py-etherscan-api

## Available bindings

Currently, only the following Etherscan.io API modules are available:

- accounts
- contracts
- stats
- tokens
- proxies
- blocks
- transactions

The remaining available modules provided by Etherscan.io will be added eventually...

## Available Networks

Currently, this works for the following networks:

- Mainnet
- Ropsten

## Examples

All possible calls have an associated example file in the examples folder to show how to call the binding

These of course will be fleshed out with more details and explanation in time

Jupyter notebooks area also included in each directory to show all examples

## TODO:

- Package and submit to PyPI
- Add the following modules:
  - event logs
  - geth proxy
  - websockets
- Add robust documentation
- Add unit test suite
- Add request throttling based on Etherscan's suggestions

## Holla at ya' boy

BTC: 16Ny72US78VEjL5GUinSAavDwARb8dXWKG

ETH: 0x5E8047fc033499BD5d8C463ADb29f10f11165ed0
