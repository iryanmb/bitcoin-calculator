# Bitcoin Return Calculator

## Overview
This Python command-line program calculates the current value of a past Bitcoin investment using historical daily closing price data from a local CSV file.

The user enters:
1. A **buy date** (YYYY-MM-DD)  
2. An **amount in USD**  

The program then:
- Loads Bitcoin historical prices from `bitcoin_historical_data.csv`
- Finds the closing price on the given date, or the closest earlier date available
- Calculates the amount of BTC that could have been purchased at that time
- Uses the most recent price in the dataset to determine the investment’s current value
- Displays the final value, profit or loss in USD, and percentage return

No fees, taxes, or inflation adjustments are included.

---

## Skills Demonstrated
-Object-Oriented Programming
-Data parsing using Pandas and datetime objects
-Working with time-series financial data
