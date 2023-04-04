firname = input("what is your first name?")
lastname = input("what is your last name?")
location = input("what is your location?")
age = input("what is your age?")

#sentence = f"Hi {firname}! Your location is {location} and you are {age} years old."
#sentence = "Hi {0} {1}! Your location is {2} and you are {3} years old.".format(firname,lastname,location,age)
sentence = "Hi " +firname+ " " + lastname + "!" + "Your name is " + location + " and you are "+age+" years old"
print(sentence)