def caesar(user_need,text, shift):
    maxi=len(text)
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    elif not(shift > 1 or shift < maxi):
        return 'Shift must be an integer between 1 and '+ str(maxi)
    else:
        if user_need=="D":
            shift=-shift

        alphabet = 'abcdefghijklmnopqrstuvwxyz'    
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
        encrypted_text = text.translate(translation_table)
        return encrypted_text

user_need=input('do you wanna encrypt(E) or decrypt(D)')
user_need=user_need.upper()
if user_need=="E":
    text=input('Enter the text that needs to be encrypted :     ')
    shift=int(input('write the shift that needs to be done(this should be same while decrepting)')
    print (caesar(user_need, text ,shift))
elif user_need=='D':
    text=input('Enter the text that needs to be decrepted:     ')
    shift=int(input('write the shift that needs to be done(this should be same as encrypting)'))
    print (caesar(user_need, text ,shift))
else:
    print('you need to enter either "E" or "D"')
x=input('press enter to exit from program....')