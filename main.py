
responses = [
    "Milk - $3.50 ",
    "Computer - $250",
    "Cereal - $3 ",
    "Chips - $5"
  ]

def store_hours():
  user_input = input("Hello, how can I help you?\n ")
  if user_input == 'store hours':
    print("9am to 5pm")
  if user_input == 'location':
    print("San Diego, Los Angels ")
  if user_input == 'avaible products':
      print(responses)
    
store_hours()