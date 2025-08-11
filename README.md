# Bitcoin Investment Calculator

A Python script that calculates the returns on Bitcoin investments using historical price data. Enter any past date and investment amount to see what your Bitcoin would be worth today.

## Features
- **Historical Price Lookup**: Uses local CSV data to find Bitcoin prices on any given date.
- **Flexible Date Matching**: If exact date not available, uses closest earlier trading day.
- **Comprehensive Output**: Shows purchase details, Bitcoin units acquired, current value, and profit/loss.
- **Clean Interface**: Simple command-line prompts with input validation.

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
