# secret code project 
while True :
    print('''secret_code''')
    choice = input("Type 'code' to encrypt, 'decode' to decrypt, or 'quit' to exit: ")
    if choice == 'quit':
        print('exit programe')
        break
    elif  choice == "code":
        word= input('enter code to encrypt')
    if len(word) >= 3:
             secret_code = "abc" + word[1:] + word[0] + "xyz"
             print(f"Encrypted message: {secret_code}")
    else:
         secret_code = word[::-1]
    print(f"Encrypted message: {secret_code}")

   
