
def view():
    
    
    
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as f:
    f.write("Name:", name+ "\n" +"Password:", pwd)




while True:
  
     
  mode = input("Do you want to create a new              password or open an existing one (view or       add) or use q to quit? ").lower
     
  if mode == "q":
    break
  if mode == "add":
    add()
  if mode == "view":
    view()
    