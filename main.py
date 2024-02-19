users = [{"username": "axel", "password": "123"}, {"username": "john", "password": "password"}]

def register_user(username, password):
  for user in users:
    if user["username"] == username:
      return False
  users.append({"username": username, "password": password})
  return True


def login_user(username, password):
  for user in users:
    if user["username"] == username:
      if user["password"] == password:
        return {"message": "Login successful"}
      else:
        return {"message": "Wrong password"}
  return {"message": "User not found"}

while True:
  print("1. Register")
  print("2. Login")
  print("3. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    username = input("Enter username: ")
    password = input("Enter password: ")
    if register_user(username, password):
      print("Registration successful")
    else:
      print("Registration failed")
  elif choice == "2":
    count = 0
    while True:
      
      if count == 3:
        print("Too many attempts. Exiting...")
        break
      
      count += 1
      
      username = input("Enter username: ")
      password = input("Enter password: ")
      response = login_user(username, password)
      
      if response["message"] == "User not found":
        print(response["message"])
      elif response["message"] == "Wrong password":
        print(response["message"])
      else:
        print("Welcome, " + username)
        break
    break
  else:
    break