import random
import string

def generate_password(lenght):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation

    characters = uppercase + lowercase + numbers + special_chars

    passwort = [
        random.choice(uppercase),
        random.choice(lowercase),        
        random.choice(numbers),
        random.choice(special_chars)
    ]


    while len(passwort) < lenght:
        passwort.append(random.choice(characters))

    random.shuffle(passwort)

    return "".join(passwort)

if __name__ == "__main__":
    n = int(input("Bitte Passwortlänge eingeben: "))
    passwort = generate_password(n)
    print("Generiertes Passwort ist: ", passwort)