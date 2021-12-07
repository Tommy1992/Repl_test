# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
msg= "Not leap year."

# def function(year):
    # if year % 4 == 0:
    #     msg= "Leap year."
    #     if year % 100 == 0:
    #        msg= "Not leap year"
    #     else: print ("Leap year")
    #     return
    #     if year % 400 == 0:
    #         print (msg= "Leap year.")
    #     else: print ("Not leap year.")
    #     return
    # else: print ("Not leap year.")
    # print (msg)

if year % 4 == 0:
    msg= "Leap year."
    if year % 100 == 0:
        msg= "Not leap year"
    else:
      print ("Leap year.")
      exit()
    if year % 400 == 0:
      msg= "Leap year."
    else:
      print ("Not leap year.")
      exit()
print (msg)

