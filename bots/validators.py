from decimal import Decimal

VALIDATE_SIDE = ["BUY" , "SELL"]
VALIDATE_TYPE = ["MARKET","LIMIT"]




def validate_symbol(symbol : str):
    if not symbol:
        raise ValueError("")
    
    return symbol.upper()

def validate_side(side : str):

    side  = side.upper()


    if side not in VALIDATE_SIDE:
        raise ValueError(f"Invalid side , USE ONLY : {VALIDATE_SIDE}")
    
    return side


def validate_order_type(order_type : str):

    order_type = order_type.upper()

    if order_type not in VALIDATE_TYPE:
        raise ValueError(f"INvalid order type  USE ONLY :{VALIDATE_TYPE}")
    return order_type

def validate_quantity(quantity):
    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price):
    if price is None:
        raise ValueError("Price is required")

    price = float(price)

    if price <= 0:
        raise ValueError("Price must be greater than 0")

    return price