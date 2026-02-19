full_dot = '●'
empty_dot = '○'
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_character(name,strength,intelligence,charisma):
    if type(name) is not str:
        return('The character name should be a string')
    if name=="":
        return ('The character should have a name')
    if len(name)>10:
        return ('The character name is too long')
    if ' ' in name:
        return('The character name should not contain spaces')
    if not isinstance(strength,int) or not isinstance(charisma,int) or not isinstance (intelligence, int):
        return ('All stats should be integers')
    if strength < 1 or intelligence<1 or charisma<1:
        return ('All stats should be no less than 1')
    if strength>4 or intelligence>4 or charisma>4:
        return('All stats should be no more than 4')
    if sum([strength,intelligence,charisma])!=7:
        return ('The character should start with 7 points')
 
    return (
        f"{name}\n"
        f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
        f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
        f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    )

ch_name=input('Enter character name     :')
ch_strength=input('Enter character strength :')
ch_intelligence= input('Enter character intelligence :')
ch_charisma=input('Enter character charisma     :')
# Call the function to clear the screen
clear_screen()   
ch_charisma=int (ch_charisma)
ch_intelligence=int(ch_intelligence)
ch_strength=int(ch_strength)
print(create_character(ch_name,ch_strength,ch_intelligence,ch_charisma))
x=input('press enter to exit from program....')