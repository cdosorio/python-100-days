# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

true_t = name1.count("t") + name2.count("t")
true_r = name1.count("r") + name2.count("r")
true_u = name1.count("u") + name2.count("u")
true_e = name1.count("e") + name2.count("e")

love_l = name1.count("l") + name2.count("l")
love_o = name1.count("o") + name2.count("o")
love_v = name1.count("v") + name2.count("v")
love_e = name1.count("e") + name2.count("e")

score_as_string = str(true_t + true_r + true_u + true_e) + str(love_l + love_o + love_v + love_e)
score = int(score_as_string)

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else :
    print(f"Your score is {score}.")
