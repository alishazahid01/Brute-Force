# Brute-Force
# Brute Force Password Cracker

![Python](https://img.shields.io/badge/Python-3.x-blue)

This Python script is a basic brute force password cracker that attempts to crack a given password using two methods: dictionary attack and exhaustive attack. It allows users to input a password, its length, and performs these attacks to find the password.

## Code Structure and Functionality

The code is organized into functions and a main section, each with specific roles:

### PasswordCracker Class

The class represents a password cracker.

#### Constructor (__init__)

- Initializes the password to be cracked, file path to a password dictionary, character lists (numbers, lowercase, uppercase, special characters), and the desired password length.

#### dictionary_attack Method

- Performs a dictionary attack by checking if the given password matches any line in a password dictionary file.
- Returns True and the matched password if found; otherwise, returns False.

#### exhaustive_attack Method

- Performs an exhaustive attack by generating all possible combinations of characters based on the provided character lists and length.
- Compares each generated combination with the given password.
- Returns True and the cracked password if found; otherwise, returns False.

### Main Function

- Accepts user input for the target password and desired password length.
- Specifies the password dictionary file path and character lists.
- Initiates a PasswordCracker object with the provided parameters.
- Performs a dictionary attack and checks if the password is found. If not, it proceeds to an exhaustive attack.
- Prints the results of both attacks.

## How the Code Works

The script begins by defining the PasswordCracker class, which encapsulates the password cracking logic.

In the main function:

- The user is prompted to enter the target password and desired password length.
- A password dictionary file path and character lists (numbers, lowercase, uppercase, special characters) are specified.
- A PasswordCracker object is created with the provided input and character lists.
- The script attempts to crack the password using a dictionary attack first:
  - It checks if the target password matches any line in the password dictionary file.
  - If a match is found, it prints the result and ends the script.
  - If no match is found, it proceeds to an exhaustive attack.

In the exhaustive attack:

- The script generates all possible combinations of characters of the specified length.
- Each generated combination is compared to the target password.
- If a match is found, it prints the result and ends the script.
- If no match is found, it prints that the password was not found using exhaustive attack.

Overall, this script is a basic demonstration of password cracking techniques, including dictionary and exhaustive attacks. It can be further expanded and enhanced for more complex scenarios and security testing.

## Usage

To use the script, follow these steps:

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Follow the prompts to input the target password, password length, and other options.

## Disclaimer

This script is intended for educational and testing purposes. Unauthorized use of this script for malicious activities is strictly prohibited. Always obtain proper authorization and adhere to legal and ethical standards when conducting security testing.

## License

This project is licensed under the MIT License. 

