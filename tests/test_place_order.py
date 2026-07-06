from bots.orders import place_order


def test_market_order():
    try:
        response = place_order(
            symbol="BTCUSDT",
            side="BUY",
            order_type="MARKET",
            quantity=0.001
        )

        print("\n===== MARKET ORDER SUCCESS =====")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Average Price : {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\nMARKET ORDER FAILED\n{e}")


def test_limit_order():
    try:
        response = place_order(
            symbol="BTCUSDT",
            side="BUY",
            order_type="LIMIT",
            quantity=0.001,
            price=50000
        )

        print("\n===== LIMIT ORDER SUCCESS =====")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Price         : {response.get('price')}")

    except Exception as e:
        print(f"\nLIMIT ORDER FAILED\n{e}")


if __name__ == "__main__":
    print("Testing Binance Futures Testnet...\n")

    test_market_order()
    print("-" * 50)
    test_limit_order()