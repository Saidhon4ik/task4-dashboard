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


if __name__ == "__main__":
    tests = ["$20¢25", "29€50¢", "USD 15.", "52.99USD", "EUR37.50", "46$99¢", "€ 32.00", "36 EUR"]
    for t in tests:
        print(t, get_currency(t), get_amount(t))