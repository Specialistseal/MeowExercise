# Exercise 15: Reverse Word Order
def reverse_word(given_str):
    #this function will reversre the word order of the givenstring
    given_str = given_str.split(" ")
    return " ".join(given_str[::-1])


sentence = input("pleses write a small sentence and i wil reverse the word order. \n")
print(reverse_word(sentence))