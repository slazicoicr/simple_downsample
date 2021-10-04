# Simple Downsampling

## Usage
```
simple_downsample --help
usage: simple_downsample [-h] [--seed SEED] downsample_to file

Simplified interface to the samtools downsampling algorithm.

positional arguments:
  downsample_to  How many reads to downsample to.
  file           Path to BAM file.

optional arguments:
  -h, --help     show this help message and exit
  --seed SEED    Seed for the downsampling.
```

## Requirements
* Python 3.8 or greater
* samtools 1.10 or greater

## Installation
Clone repository and within cloned folder run `pip install .`
