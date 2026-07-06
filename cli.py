import argparse
from bots.logging_config import logger
from bots.orders import place_order
from bots.validators import VALIDATE_SIDE,VALIDATE_TYPE ,validate_quantity,validate_price,validate_side,validate_order_type,validate_symbol


def main():
    parser = argparse.ArgumentParser(description=" Trading Bot")


    parser.add_argument(
        "--symbol" ,
        required=True,
        help="Add Trading Symbol (i.e. BTCUSDT )"
    )

    parser.add_argument(
        "--side",
        choices=VALIDATE_SIDE,
        required=True,
        help="Add BUY or SELL"
    )

    parser.add_argument(
        "--type",
        choices=VALIDATE_TYPE,
        required=True,
        help="Order type i.e. MARKET OR LIMIT"
    )
    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Add order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Add the price to place the order"
    )


    args = parser.parse_args()
    
    args.quantity = validate_quantity(args.quantity)
    args.symbol = validate_symbol(args.symbol)
    
    if args.price is not None:
        args.price = validate_price(args.price)

    logger.info("............ORDER REQUEST SUMMARY ................")
    logger.info(f"Symbol      : {args.symbol}")
    logger.info(f"Side        : {args.side}")
    logger.info(f"Order Type  : {args.type}")
    logger.info(f"Quantity    : {args.quantity}")
    logger.info(f"Price       : {args.price}")

    try:
        place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )
        logger.info(f"Order placed successfully")
    except Exception as e:
        logger.exception(f"Order Place is Failed")
        exit(1)


if __name__ == "__main__":
    main()