import re


def get_currency(text):
    """Return 'EUR' or 'USD' for a messy price string."""
    if "EUR" in text or "€" in text:
        return "EUR"
    return "USD"


def get_amount(text):
    """Return the price as a number, for example '$20¢25' -> 20.25."""
    groups = re.findall(r"\d+", text)
    if len(groups) == 1:
        return float(groups[0])
    return float(groups[0] + "." + groups[1])

def add_price_columns(orders):
    """Add 'currency' and 'amount' columns parsed from 'unit_price'."""
    orders = orders.copy()
    orders["currency"] = orders["unit_price"].map(get_currency)
    orders["amount"] = orders["unit_price"].map(get_amount)
    return orders

if __name__ == "__main__":
    tests = ["$20¢25", "29€50¢", "USD 15.", "52.99USD", "EUR37.50", "46$99¢", "€ 32.00", "36 EUR"]
    for t in tests:
        print(t, get_currency(t), get_amount(t))