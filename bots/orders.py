from binance.exceptions import BinanceAPIException


from bots.client import get_client
from bots.logging_config import logger

from bots.validators import *
def place_order(symbol, side, order_type, quantity, price=None):
    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)

        client = get_client()

        logger.info(
            f"Order Request -> Symbol={symbol}, Side={side}, "
            f"Type={order_type}, Quantity={quantity}, Price={price}"
        )

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=float(quantity)
            )
        else:
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=float(quantity),
                price=str(price),
                timeInForce="GTC"
            )

        logger.info("========== ORDER RESPONSE ==========")
        logger.info(f"Order ID      : {response['orderId']}")
        logger.info(f"Status        : {response['status']}")
        logger.info(f"Executed Qty  : {response['executedQty']}")
        logger.info(f"Average Price : {response.get('avgPrice', 'N/A')}")
        
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        raise

    except Exception:
        logger.exception("Unexpected error while placing order")
        raise