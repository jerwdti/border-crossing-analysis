# Border Crossing Analysis
**Author: Chengtian Deng**

## Table of Contents
1. [Description](README.md#Description)
1. [Steps to solve this problem](README.md#Steps-to-solve-this-problem)
1. [Language and Pakage used](README.md#Language-and-Pakage-used)
1. [Discussion](README.md#Discussion)
1. [To Run](README.md#To-Run)
1. [Reference](README.md#Reference)

## Description
The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.

**For this challenge, The program takes input of border crossing data statistics to calculate the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. It also outputs monthly average of total number of crossings for that type of crossing and border.**

## Steps to solve this problem
This program uses list and csv file manipulation to pursuit the result.
* Sort the list
* Create tempory list to check duplicated record based on 3 citerias: Border, Date, Measure
* Sum up the crossing number if entries of border are duplicated
* Traverse the list and calculated count of previous months passed and the total crossing
* Calculate and store the average entry
* Sort again and write to disk

## Language and  Pakage used 
*Bash==4.4
*Python==3.7.4 (source code)
    *math -- using for rounding up the float valute to nearest integer
    *argparse -- to link the argument to python source code
    *csv -- used to read and write csv files

## Discussion 
This program can be solved using list manipulation, or sql query. Since the approach of this program is to analysis a csv data tabel. It would also be effcient to use sql languages to reach the solution by creating script to update the csv tabel into database and using query to generate new tabels. In this solution, I took an approach of using list manipulation. The whole program consist of 4 loop inside the file reader and 1 loop inside the writer loop. Two sort algorithms are used. In worst case this would take O(n log n) complexity to run while reading the file and O(n) while writing the file to the disk.

### Assumptions
* Input file and output file are successfuoly passed into python3 using run.sh. 
* Each record in input file are recorded by month and are recorded in the first day of the month
* Values entries inside the input file can be converted to integer

## To Run 
- bash run.py

### run time
*The run time on [Here](https://data.transportation.gov/api/views/keg4-3bc2/rows.csv?accessType=DOWNLOAD) with 351605 data entry is
real    3m37.549s
user    3m35.916s
sys    0m0.668s
using macOs==10.15.1 processor 1.3 Ghz Dual-Core Intel Core m7f

## Reference
https://docs.python.org/2/howto/argparse.html
https://unix.stackexchange.com/questions/52313/how-to-get-execution-time-of-a-script-effectively
https://stackoverflow.com/questions/8528178/list-of-zeros-in-python
https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-this-python-sort-method
https://stackoverflow.com/questions/5850986/joining-pairs-of-elements-of-a-list-python
