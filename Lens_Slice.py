# Your code below:
toppings = ["Pepperoni", "Pineapple", "Cheese", "Sausage", "Olives", "Anchovies", "Mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(num_pizzas)

num_pizzas = "We Sell " + str (num_pizzas) + " different kinds of Pizzas"

# print(num_pizzas)

pizza_and_prices = [[2, "Pepperoni"], [6, "Pineapple"], [1, "Cheese"], [3, "Sausage"], [2, "Olives"], [7, "Anchovies"], [2, "Mushrooms"]] 

# print(pizza_and_prices)

pizza_and_prices.sort()

print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]

print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]

print(priciest_pizza)
pizza_and_prices.pop()
print(pizza_and_prices)
pizza_and_prices.append([2.5, "Peppers"])
pizza_and_prices.sort()
three_cheapest = pizza_and_prices[:3]
print(pizza_and_prices)
print(three_cheapest)


