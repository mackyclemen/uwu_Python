def uwu(word):
    return word.replace('r', 'w') \
               .replace('l', 'w') \
               .replace('R', 'W') \
               .replace('L', 'W') \
               .replace('mo', 'myo') \
               .replace('mo', 'Myo') \
               .replace('no', 'nyo') \
               .replace('No', 'Nyo') \
           + ' uwu'


if __name__ == "__main__":
    print("Welcome to the uwu translator!")
    user_input = input("Enter text to translate: ")
    print(">" + uwu(user_input))
