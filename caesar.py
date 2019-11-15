'''Caesarian Cipher Program
    Created: Nov. 1, 2019
    Creator: MDube
    Language: Python
    IDE: PyCharm
'''

def encrypt(my_string, count_num):
    encrypted = '' #new cipher
    for letter in my_string:
        if letter.isalpha(): #if character is a letter
            new_letter = chr(ord(letter) + count_num) #adds the count of the cipher to the letter char
            if ord(new_letter) <= 90: #ASCII 90 is Z, so capital letter must be <= 90
                encrypted += str(new_letter) #adds letter to encrypted string
            else: #if the char goes over 90, which would lead to lower case letters
                back_num = ord(new_letter) - 25 #goes back to the beginning after passing Z
                new_letter = chr(back_num)
                encrypted += str(new_letter)
        else:
            encrypted += str(letter)
    return encrypted

if __name__ == '__main__':
    print('This program will encrypt whatever text you would like to encrypt with a specific count of your choosing.')
    decrypted = input('Type what you would like encrypted in a caesar cipher:\n')
    count = int(input('Please input a non-negative number for the count of your encryption:\n'))
    print(encrypt(decrypted.upper(), count)) #decrypted is now all uppercase letters