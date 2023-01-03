# Write a program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>
            You are selected!
            <|date|>'''
name= input("Enter your name: ")
date= input("Enter date: ")
letter= letter.replace("<|Name|>",name)
letter= letter.replace("<|date|>",date)
print(letter)