"""
1. Product Review Analysis

Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
"""

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
     ]

def capitalize_words(reviews):
    keywords = ["good", "excellent", "bad", "Poor", "average"]
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)

capitalize_words(reviews)

print("\n")

split_reviews = [review.split() for review in reviews]

def word_counter(split_reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    positive_count = 0
    negative_count = 0

    for words in split_reviews:
        for word in words:
            word_lower = word.lower().strip(".,!?")
            if word_lower in positive_words:
                positive_count += 1
            elif word_lower in negative_words:
                negative_count += 1

    return positive_count, negative_count

postive_count, negative_count = word_counter(split_reviews)

print(f" There are {postive_count} postive words.")
print(f" There are {negative_count} negative words.")

"""
2. User Input Data Processor
Objective: The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. 
If not, print an error message.
"""

def length_validator(first_name, last_name):
    if len(first_name) > 2:
        return len(first_name)
    elif len(last_name) > 2:
        return len(last_name)
    else:
        print("Please enter a name that is more than 2 characters long")
    
while True:
    first_name_input = input("Please enter your first name: ")
    last_name_input = input("Please enter your last name: ")

    name_length = length_validator(first_name_input, last_name_input)

    print(f"Your first name is: {len(first_name_input)} characters long and your last name is: {len(last_name_input)} long.")

    continue_input = input("Would you like to enter another name? (yes/no): ")
    if continue_input != 'yes':
        break
