

# main #
def price_difference(high, low):
    """A simple calculation on the increase / decrease of crypto price."""
    diff = (high - low) / low
    return diff