
str_order = list() 

def select_meal():
  isDone = False
  while isDone == False:
    user_input = input("Hello, would you like a pizza or a salad?\n")
    if (user_input == "done"):
      isDone = True
      break 
    if (user_input == "pizza"):
      str_order.append(pizza())
    if (user_input == "salad"):
      str_order.append(salad())
    print("You ordered a "+ " and a ".join(str_order)+ ". Place another order or say 'done'.\n") 
  if isDone == True:
    print("Your order has been placed. Goodbye!")

def pizza(): 
  pizza_order = ""
  ask_user = input("Small, medium, or large?\n")
  pizza_order += ask_user + " pizza"
  pizza_order += toppings() 
  return pizza_order

def toppings(): 
  cnt = 0
  str_toppings = ""
  noMore = False
  while noMore == False:
    ask_toppings = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done'.\n")
    cnt += 1 
    if (ask_toppings == "done"): 
      return str_toppings
      noMore = True
    if cnt == 1:
      str_toppings += " with"
    if cnt > 1:
      str_toppings += " and"
    str_toppings += " " + ask_toppings 
  return str_toppings
  
def salad():
  salad_order = ""
  ask_user = input("Would you like a garden salad or greek salad?\n")
  salad_order += ask_user + " salad"
  salad_order += dressing()
  return salad_order
  
def dressing():
  ask_dressing = input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon\n")
  return " with "+ ask_dressing + " dressing"

select_meal()