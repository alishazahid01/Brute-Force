# Brute force password Cracker
# Importing itertools
import itertools

class PasswordCracker:
    
    # Constructor (Dunder Method)
    def __init__(self, password, file_path, num_list, lowercase_list, uppercase_list, special_char, length):
        self.password = password
        self.file_path = file_path
        self.num_list = num_list
        self.lowercase_list = lowercase_list
        self.uppercase_list = uppercase_list
        self.special_char = special_char
        self.length = length

    # Dictionary attack 
    def dictionary_attack(self):
        # Open Password dictionary file
        with open(self.file_path, "r") as file:
            # Reading each line
            for line in file:
                line = line.strip()
                if line == self.password:
                    return True, line
        return False, None
        
    # Exhaustive attack
    def exhaustive_attack(self):
        for combination in itertools.product(self.num_list, self.lowercase_list, self.uppercase_list, self.special_char, repeat=self.length):
            cracked_pass = ''.join(combination)
            if cracked_pass == self.password:
                return True, cracked_pass
        return False, None

def main():
    # Input password
    password = input("Enter the password: ")
    length = int(input("Enter the length of password: "))
    file_path = "pwd_dict.txt"

    # Exhaustive attack by trying every combination
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char = ['@', '#', '$', '*', '?']

    # Performing dictionary attack
    pwd_obj = PasswordCracker(password, file_path, num_list, lowercase_list, uppercase_list, special_char, length)
    dict_attack, matched = pwd_obj.dictionary_attack()

    # Checking if the password found or not using dictionary attack
    if dict_attack:
        print("Password Found using dictionary attack:", matched)
    else:
        print("Password not found using dictionary attack")
        print("Trying Exhaustive attack...... ")
        check, cracked_password = pwd_obj.exhaustive_attack()

        # Conditions
        if check:
            print("Password Found using exhaustive attack:", cracked_password)
        else:
            print("Password not found using exhaustive attack")

if __name__ == "__main__":
    main()
