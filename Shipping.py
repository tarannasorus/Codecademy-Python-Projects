def gship(weight):
  if weight < 2:
    return (weight * 1.5) + 20
  elif (weight > 2) and (weight < 6):
    return (weight *3) + 20
  elif (weight > 6) and (weight < 10):
    return (weight * 4) + 20
  else:
    return (weight * 4.75) + 20
  
premium = 125.00
  
def drone(weight):
  if weight < 2:
    return weight * 4.50
  elif (weight > 2) and (weight < 6):
    return weight * 9
  elif (weight > 6) and (weight < 10):
    return weight * 12
  else:
    return weight * 14.25
  

    
def cheapest(weight):
  if (drone(weight)) < (gship(weight)):
    return " You should ship using drone shipping, it will cost $" + str(drone(weight))
  elif (gship(weight)) < (premium):
    return "You should ship using ground shipping, it will cost $" + str(gship(weight))
  else:
    return "You should ship using premium ground shipping, it will cost $" + str(premium)
  
print(cheapest(26))
  


  