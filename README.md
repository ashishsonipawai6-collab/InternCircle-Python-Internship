# Personal Expense Tracker with CSV

## Project Overview
A beginner-friendly Python application to manage daily expenses and store them permanently in a CSV file.

## Features
- Add new expenses
- View all expenses
- Filter expenses by category
- Calculate category-wise totals
- Store data using CSV files
- Validate dates and amounts

## Technologies Used
- Python
- CSV Module
- File Handling
- Dictionaries
- Functions
- Exception Handling

## How to Run
1. Download the project files.
2. Open the project folder in VS Code.
3. Run:

`python expense_tracker.py`

## Files
- expense_tracker.py – Main Python program
- expenses.csv – Sample expense records

## Problem Fixed
Initially, CSV file handling on Windows can create unwanted blank lines. I fixed this by opening CSV files with `newline=''`.

## Sample Data
The expenses.csv file contains 10 sample expense records using fictional data.