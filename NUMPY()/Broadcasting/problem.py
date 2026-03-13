import numpy as np

# prices = [100,200,300]
# final_prices = []

# for num in prices:
#     Value = num - num/10 
#     final_prices.append(Value)

# print(final_prices)


prices = np.array([100,200,300])
discount = 10#scalar single value 

final_prices = prices - (prices * discount / 100)
print(final_prices)