For this challenge, we're going to use StegoPVD (https://gist.github.com/dhondta/feaf4f5fb3ed8d1eb7515abe8cde4880), a tool developed by dhondta.
# Steganography with PNG - Pixel Value Differencing

This guide uses a ready-made script to perform steganography on PNG files using Pixel Value Differencing (PVD). It is recommended to read the script to understand its functionality.

## Prerequisites

First, install the `tinyscript` library:

```sh
pip3 install tinyscript
```

## Usage

To extract hidden data from a PNG file using the `StegoPVD` script, run the following command:

```sh
./stegopvd.py -v extract ch12.png
```

Executing this command will reveal the hidden flag.