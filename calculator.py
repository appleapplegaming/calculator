on = 1
question = input("what do you want to do:\n1.multiplication\n2.division\n3.addition\n4.subtraction\n5.exit \n>")
def function(question):
    if question == "1":
        return "division"
    elif question == "2":
        return "multiplication"
    else:
        return "Invalid option silly"
value = function(question)
print(function(question))
while on == 1:
    if value == "1":
        answer1 = int(input("enter your first number"))
        answer2 = int(input("enter your second number"))
        print(answer1 / answer2)
        on = 0