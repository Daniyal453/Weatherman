
# Weatherman

This project will generate reports for highest lowest temperature and average of particular month or year text files. 

## Prerequisites

- [argparse](https://docs.python.org/3/library/argparse.html)
- [CSV](https://docs.python.org/3/library/csv.html)
- [Python3](https://www.python.org/downloads/)


## Things You Will Have To Change:
 In weatherman.py, path_to_file_directory is the location path where your text files are stored.


## Installation

All you need is to clone this project and in the terminal you have to write input commands like:

```bash
  python3 main.py path_to_file_directory -a 2012/3 # For Month

```
```bash  
  python3 main.py path_to_file_directory -e 2012 # For Year
```
```bash
  python3 main.py path_to_file_directory -c 2012/4 # For Month Horizontal Bars
```
```bash
  python3 main.py path_to_file_directory -e 2012 -a 2012/4 -c 2015/6 # For Month, Year and Month Horizontal
```

