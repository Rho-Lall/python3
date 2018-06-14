## Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest (normal, drone, premium) and how much it will cost to ship their package using Sal's Shippers.

def priceline(weight):
## A parent function that will use two child functions.

## Each child will store pricing and calculate prices based on weight for each shipping method: Normal/Premium, & Drone. Each child will return: Shipping_Method, Cost 

##The parent will run both child functions and then use logic to pick the cheapest option. 

  drone_price = price_by_drone(weight)
  ground_price = price_by_ground(weight) 
  
  if drone_price > ground_price:
    return ground_price
  else:
    return drone_price
	

## First child. Calculates cheapest ground/premium rate.
def price_by_ground(weight):
  if weight >=10:
    cost = 4.75*weight + 20
  elif weight >=6:
    cost = 4.00*weight + 20  
  elif weight >=2:
    cost = 3.00*weight + 20
  else:
    cost = 1.50*weight + 20
    
  premium = 125  
 
  if premium > cost:
    shipping_method = "Ground"
    return cost, shipping_method
  else:
    shipping_method = "Premium"
    return premium, shipping_method
  
## Test Print Statment
##print(price_by_ground(23))


## Second Child. Calculates best drone price.

def price_by_drone(weight):
  shipping_method = "Drone"
  if weight > 10:
    cost = 14.25*weight
  elif weight > 6:
    cost = 12*weight
  elif weight > 2:
    cost = 9*weight
  else:
    cost = 4.5*weight
    
  return cost, shipping_method

## Test Print Statment

print(priceline(10))