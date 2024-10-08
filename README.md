# AIPI 510 Pre-Module Assignment

This tool is used to process csv files and display them to the user and it contains tests to ensure proper functionality

## Installation

This guide assumes you already have Git and at least Python 3.11.9 installed and configured on your machine and bash is used to execute all commands.

Clone this repo into your machine

```bash
git clone https://github.com/laxman-22/AIPI-510-Pre-module-Assignment.git

```

Please ensure you are using the correct version of Python to use this tool which is **Python 3.11.9** for this tool.

Also install the required dependencies. Make sure the following versions are used for Pandas, Pytest, and Pip.

**Pandas: 2.2.2**

**Pytest: 8.3.2**

```bash
pip install pandas==2.2.2
pip install -U pytest==8.3.2
```

Ensure the correct versions are installed

Look for pandas and pytest after running this command
```bash
pip list
```


## Usage

In order to use the CLI tool, open the directory that contains the process_csv.py file and run the tool

```bash
cd AIPI-510-Pre-module-Assignment/
```
**Note: If you are using Linux, please use python3 instead of python in the below commands.**
```bash
python process_csv.py
```
In order to run the unit tests created to test this tool, execute the following command in the directory

```bash
python -m pytest -v
```

