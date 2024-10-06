italian_food = [
  "Pasta Bolognese",
  "Pepperoni pizza",
  "Margherita pizza",
  "Lasagna"
]

def find_meal(name, menu):
  return name if name in menu else None

def select_meal(name):
  return find_meal(name, italian_food)

def display_available_meals():
  print("Available Italian Meals:")
  for meal in italian_food:
    print(meal)

def create_summary(name, amount):
  order = select_meal(name)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
display_available_meals()

name_input = input("Choose your meal: ")
amount_input = input("Order Quantity: ")

result = create_summary(name_input, amount_input)
print(result)