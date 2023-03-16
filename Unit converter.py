num = input("Insert the value you want to convert: ")
while True:
    def unit_converter(num):
 
    mode = input("What is the initial unit?[M - metre, Km - Kilometer, Cm - centimeter] ").lower()
    new_mode = input("What unit do you want to convert it to? [M - metre, Km - Kilometer, Cm - centimeter]")
    
        if mode =="cm" and new_mode == "m":
             answer = int(num )* 100
             print(answer)
       elif mode =="m" and new_mode == "cm":
              answer = int(num )/100
              print(answer)
      elif mode =="m" and new_mode == "km":
             answer = int(num )*1000
             print(answer)
    elif mode =="km" and new_mode == "m":
        answer = int(num )/1000
        print(answer)
    else:
        print("Invalid Unit!")
        
unit_converter(num)