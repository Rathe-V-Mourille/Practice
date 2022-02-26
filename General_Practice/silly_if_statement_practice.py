ages = [19, 38, 24, 57, 33, 31, 95]

for age in ages:
    if age <= 32:
        print(f"{age}! You're a spring chicken, that you are!")
    elif age == 33:
        print(f"""
{age}! Congratulations! 
It's all downhill from here...\n""")
        break    
    else:
        print(f"""
{age}! You're quite over the hill...
In fact, I can't even see the top of your head anymore!\n""")