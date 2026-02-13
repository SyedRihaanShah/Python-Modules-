from forex_python.converter import CurrencyRates

c = CurrencyRates()
# rate = c.get_rate('USD', 'INR') #gives the value of 1 USD in INR
# rate = c.convert('USD', 'INR', 100) # converts 100 usd into inr 
rates = c.get_rates('USD') # gives all the rates of the given currency
# print(rate)
print(rates)