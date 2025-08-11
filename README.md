# Bitcoin Investment Calculator

A Python script that calculates the returns on Bitcoin investments using historical price data. Enter any past date and investment amount to see what your Bitcoin would be worth today.

## Features
- **Historical Price Lookup**: Uses local CSV data to find Bitcoin prices on any given date.
- **Flexible Date Matching**: If exact date not available, uses closest earlier trading day.
- **Comprehensive Output**: Shows purchase details, Bitcoin units acquired, current value, and profit/loss.
- **Command Line Interface**: Simple command-line prompts with input validation.

## How It Works
1. **Input**: Enter a buy date (`YYYY-MM-DD`) and investment amount in USD.  
2. **Price Lookup**: Script finds the closing price on your specified date (or nearest earlier date).  
3. **Calculation**: Determines how much BTC you could have purchased and its current value.  
4. **Results**: Displays profit/loss in both absolute dollars and percentage terms.

## CSV Data Format
Expected CSV structure:
- **Start**: Date column (YYYY-MM-DD format)  
- **Close**: Bitcoin closing price in USD  

## Code Structure

### BitcoinData Class
- Loads and processes CSV data.  
- Provides date-based price lookups.  
- Handles missing dates with fallback logic.  

### Key Functions
- `parse_buy_date()` — Validates date input format.  
- `parse_amount()` — Handles USD amount parsing with comma support.  
- `price_on_or_before()` — Finds closest available trading day.  
- `format_money()` — Consistent currency formatting.  

## Error Handling
- **Invalid Dates**: Prompts for correct YYYY-MM-DD format.  
- **Out of Range**: Validates dates against available data range.  
- **Missing Data**: Uses nearest earlier date when exact match unavailable.  
- **Invalid Amounts**: Requires positive numerical input.  

## Example Output
=== Bitcoin Return Calculator (CSV, no fees) ===
Data range: 2014-09-17 to 2024-12-15
Latest Close (sell price): $43,256.78 on 2024-12-15

Enter buy date (YYYY-MM-DD): 2017-12-15
Enter amount invested in USD (e.g., 1000): 5000

--- Result ---
Buy date entered: 2017-12-15
Buy date used: 2017-12-15 (exact match)
Buy Close price: $17,900.00
Sell date used: 2024-12-15 (latest in CSV)
Sell Close: $43,256.78
BTC units: 0.27932961
Final value: $12,080.45
Gain/Loss: $7,080.45 (141.61%)

## Limitations
- No transaction fees — calculations assume zero trading fees.    
- Historical data only — limited to dates within CSV dataset.  
- USD only — input and output in U.S. dollars.  

## Use Cases
- **Investment Analysis**: Evaluate past Bitcoin investment opportunities.  
- **Educational Tool**: Understand Bitcoin's historical performance.   
- **Market Research**: Analyze Bitcoin price trends over time.  

