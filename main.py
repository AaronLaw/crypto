from crypto.crypto import Price

# main #
high = input('Give me the price high.')
low = input('Gime me the price low.')

high_price = Price(high)
low_price = Price(low)

diff = low_price.price_difference(high_price)
diff_in_percentage = diff * 100
print(diff_in_percentage)