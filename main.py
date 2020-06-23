

def price_difference(high, low):
    """A simple calculation on the increase / decrease of crypto price."""
    diff = (high - low) / low
    return diff

# main #
high = float(input('Give me the price high.'))
low = float(input('Gime me the price low.'))

diff = price_difference(high, low)
diff_in_percentage = diff * 100
print(diff_in_percentage)