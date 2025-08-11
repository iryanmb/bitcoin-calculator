"""
Description:
    This script calculates how much your Bitcoin investment would be worth today,
    based on historical daily closing prices from a local CSV file.

How It Works:
    1. You enter:
       - A buy date (YYYY-MM-DD)
       - An amount in USD
    2. The program:
       - Loads 'bitcoin_historical_data.csv'
       - Finds the closing price on the given date (or the nearest earlier date)
       - Calculates how much BTC you could have purchased
       - Uses the most recent closing price to determine current value
       - Displays your profit/loss in USD and percentage
"""

import pandas as pd
from datetime import datetime, date


CSV_PATH = "bitcoin_historical_data.csv"  


# ---------------------------
# Data loading and lookups
# ---------------------------

class BitcoinData:
    """
    Holds the Bitcoin daily price table and provides simple lookups.
    We assume the CSV has 'Start' and 'Close' columns.
    """

    def __init__(self, csv_path: str):
        # Load and normalize the two columns we care about into a simple table:
        #   date: Python date objects
        #   close: float USD
        self.df = self._load_csv(csv_path)

        # Useful cached values
        self.min_date: date = self.df["date"].min()
        self.max_date: date = self.df["date"].max()
        self.latest_day: date = self.df.iloc[-1]["date"]
        self.latest_close: float = float(self.df.iloc[-1]["close"])

    def _load_csv(self, csv_path: str) -> pd.DataFrame:
        # Read file
        raw = pd.read_csv(csv_path)

        # Keep only the columns we need
        df = raw[["Start", "Close"]].copy()

        # Convert 'Start' from text to real Python dates
        df["Start"] = pd.to_datetime(df["Start"], utc=True, errors="coerce").dt.date

        # Rename to consistent names and sort by date (earliest → latest)
        df = (
            df.rename(columns={"Start": "date", "Close": "close"})
              .sort_values("date")
              .reset_index(drop=True)
        )

        return df

    def price_on_or_before(self, d: date) -> tuple[date, float] | None:
        """
        Return (date_used, close_price). If there's no exact match for d,
        use the closest earlier date. If none exists (d < min_date), return None.
        """
        # Take all rows with date <= d
        sub = self.df[self.df["date"] <= d]
        if sub.empty:
            return None
        row = sub.iloc[-1]
        return row["date"], float(row["close"])

    def latest_price(self) -> tuple[date, float]:
        """Return (latest_day, latest_close) from the table."""
        row = self.df.iloc[-1]
        return row["date"], float(row["close"])


# ---------------------------
# Small helpers (parsing/formatting)
# ---------------------------

def parse_buy_date(text: str) -> date | None:
    """Parse 'YYYY-MM-DD' into a Python date, or return None if invalid."""
    try:
        dt = datetime.strptime(text.strip(), "%Y-%m-%d")
        return date(dt.year, dt.month, dt.day)
    except ValueError:
        return None


def parse_amount(text: str) -> float | None:
    """Parse a positive float amount in USD (commas allowed)."""
    try:
        x = float(text.replace(",", "").strip())
        return x if x > 0 else None
    except Exception:
        return None


def format_money(x: float) -> str:
    return f"${x:,.2f}"


# ---------------------------
# Main program flow
# ---------------------------

def main() -> None:
    print("=== Bitcoin Return Calculator (CSV, no fees) ===\n")

    data = BitcoinData(CSV_PATH)

    # Show the valid date range and the "sell today" price
    print(f"Data range: {data.min_date} to {data.max_date}")
    print(f"Latest Close (sell price): {format_money(data.latest_close)} on {data.latest_day}\n")

    # 1) Ask for buy date
    while True:
        buy_text = input("Enter buy date (YYYY-MM-DD): ").strip()
        buy_date = parse_buy_date(buy_text)
        if buy_date is None:
            print("  -> Invalid date format. Example: 2017-12-15")
            continue
        if buy_date < data.min_date:
            print(f"  -> Too early. Earliest supported date is {data.min_date}.")
            continue
        if buy_date > data.max_date:
            print(f"  -> Too late. Latest supported date is {data.max_date}.")
            continue

        found = data.price_on_or_before(buy_date)
        if found is None:
            print("  -> No data on or before that date. Try another date.")
            continue

        buy_day, buy_close = found
        break  # valid buy date acquired

    # 2) Ask for amount in USD
    while True:
        amt_text = input("Enter amount invested in USD (e.g., 1000): ").strip()
        amount_usd = parse_amount(amt_text)
        if amount_usd is None:
            print("  -> Amount must be a positive number.")
            continue
        break  # valid amount acquired

    # 3) Core math (coin method)
    btc_units = amount_usd / buy_close
    final_value = btc_units * data.latest_close
    abs_gain = final_value - amount_usd
    pct_gain = (abs_gain / amount_usd) * 100.0

    # 4) Output
    print("\n--- Result ---")
    print(f"Buy date entered: {buy_date}")
    if buy_day != buy_date:
        print(f"Buy date used:    {buy_day} (closest earlier date)")
    else:
        print(f"Buy date used:    {buy_day} (exact match)")
    print(f"Buy Close price:  {format_money(buy_close)}")
    print(f"Sell date used:   {data.latest_day} (latest in CSV)")
    print(f"Sell Close:       {format_money(data.latest_close)}")
    print(f"BTC units:        {btc_units:,.8f}")
    print(f"Final value:      {format_money(final_value)}")
    print(f"Gain/Loss:        {format_money(abs_gain)} ({pct_gain:,.2f}%)\n")


if __name__ == "__main__":
    main()
