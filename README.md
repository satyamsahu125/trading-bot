# Binance Futures Testnet Trading Bot

A simple Python CLI application to place **MARKET** and **LIMIT** orders on the Binance Futures Testnet (USDT-M). The project follows a clean and reusable structure with input validation, logging, and exception handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Support BUY and SELL sides
- Command Line Interface (CLI) using argparse
- Input validation
- Structured project architecture
- Logging of requests, responses, and errors
- Exception handling
- Binance Futures Testnet integration

---

## Project Structure

```
trading-bot/
│
├── bots/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── .env
├── requirements.txt
└── README.md
```

---

# Prerequisites

- Python 3.10+
- Binance Futures Testnet Account
- Binance Testnet API Key & Secret
- pip

---

# Setup

## 1. Clone Repository

```bash
git clone https://github.com/<your-username>/trading-bot.git

cd trading-bot
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create .env

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
BASE_URL=https://testnet.binancefuture.com
```

Generate your API keys from:

https://testnet.binancefuture.com

---

# Running the Application

## MARKET Order

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.01
```

---

## LIMIT Order

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type LIMIT \
--quantity 0.01 \
--price 50000
```

---

# Example Output

```
========== ORDER REQUEST SUMMARY ==========
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.01

Creating Binance Client...

========== ORDER RESPONSE ==========
Order ID      : 123456789
Status        : NEW
Executed Qty  : 0.0000
Average Price : N/A

Order placed successfully.
```

---

# Logging

All API requests, responses and errors are automatically stored in:

```
logs/trading_bot.log
```

The log contains:

- Order Request Summary
- API Response
- Errors
- Exceptions

---

# Validation

The application validates:

- Trading Symbol
- BUY / SELL
- MARKET / LIMIT
- Quantity > 0
- Price > 0
- Price required for LIMIT orders

---

# Assumptions

- User has a Binance Futures Testnet account.
- Valid API credentials are configured in the `.env` file.
- Internet connection is available.
- Only MARKET and LIMIT orders are implemented.
- Quantity and price values are positive numbers.

---

# Tech Stack

- Python 3
- python-binance
- argparse
- python-dotenv
- logging

---

# Future Improvements

- Stop-Limit Orders
- OCO Orders
- Interactive CLI
- Unit Tests
- Docker Support

---

# Author

Satyam Sahu
