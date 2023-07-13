on = 1
question = input("what do you want to do:\n1.multiplication\n2.division\n3.addition\n4.subtraction\n5.exit \n> ")
def function(question):
    if question == "2":
        return "division"
    elif question == "1":
        return "multiplication"
    else:
        return "Invalid option silly"
value = function(question)
print(function(question))
while on == 1:
    if value == "division":
        answer1 = int(input("enter your first number\n> "))
        answer2 = int(input("enter your second number\n> "))
        print(answer1 / answer2)
        on = 0