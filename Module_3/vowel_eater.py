# The program will remove and print uneaten consonants (non-vowels).

#takes the input from user
user_word = input("Enter word to eat here: ")
#changes the input to upper_case
user_word = user_word.upper()
#
for letter in user_word:
    if letter in "AEIOU":
        continue
    print("Your eaten consonant is", letter)
