
import random
import string

def main():
    string.ascii_letters
    password = ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation ) for n in range(8)])
    print(password)
    
if __name__ == "__main__":
    main()