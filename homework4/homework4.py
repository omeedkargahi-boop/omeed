# --- 3.1 List Operations ---


my_favorite_foods = ["fries", "tacos", "mangos", "donuts", "chicken"] # A list with my favorite foods
print(my_favorite_foods[-1]) # Prints last item with negative indexing

my_favorite_foods.append("pizza") # Adds "pizza" to the list
# I encountered this error: NameError: name 'pizza' is not defined
# Originally, I failed to put pizza in qutations
# I fixed this by adding quotations to indicate it's a string

my_favorite_foods.insert(0, "apple") # Inserts "apple" at the start of the list
my_favorite_foods.remove("tacos") # Removes the third item from the list
print(len(my_favorite_foods)) # Prints length of the list

for food in my_favorite_foods: # Prints each food in uppercase
    print(food.upper())

new_foods_list = my_favorite_foods[0], my_favorite_foods[5] # Creates new list only with first and last values of previous list
print(new_foods_list)

count = 0
for food in my_favorite_foods: # A function that checks the list for potatoes
    if food == "potato":
        count = count + 1
if count > 0:
    print("A potato!")
else:
    print("No potato!")

# An bug I initially encountered was that it would print "No Potato!" for every food in the list rather than for the list as a whole
# I fixed this by adding a count an if else statments after the loop had run to determine if any potatoes where detected


# --- 3.2 Slicing and Striding ---


twenty_numbers = list(range(21)) # Creates a list of numbers 0-20
print(twenty_numbers)

def get_first_15(twenty_numbers): # Takes a list of numbers and returns the first 15 elements 
    return twenty_numbers[0:15]

step1 = get_first_15(twenty_numbers) 
print(step1)

def get_every_fifth(get_first_15): # Takes the list from get_first_15() and returns every 5th element from it
    return get_first_15[::5]

step2 = get_every_fifth(step1)
print(step2)

# I got repeated syntax errors when trying to call a function inside a function
# To solve this, I called each function after defining it and set it equal to a variable (step 1, 2, 3), which I could then use to represent the functions return

def reverse_and_stride(get_every_fifth): # Takes the list from get_every_5th() and reverses and returns every 3rd element
    get_every_fifth.reverse()
    return get_every_fifth[::3]

step3 = reverse_and_stride(step2)
print(step3)


# --- 3.3 Nested Lists ---


numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2]) # Prints the third row

# I recieved [IndexError: list index out of range] becuase I lowkey forgot that indexing starts at 0
# I fixed this by changing my intial index of [3] to [2] to actually index the third item

print(numbers[1][1]) # Print the second item in the second row.

numbers.append([10, 11, 12]) # Add [10, 11, 12] as a new row using .append()

def sum_nested(selected_list): # Writes a function called sum nested() that loops through each row, sums all numbers, and returns the total.
    total = 0
    for set in selected_list:
        for individual_number in set:
            total = total + individual_number
    return total

print(sum_nested(numbers))


# --- 3.4 Create a 5x5 List ---


my_list = []
def create5x5(new_list): # Function that creates a 5x5 list
    beginning = 1
    
    for set in range(5):
        row = list(range(beginning, beginning + 5))
        new_list.append(row)
        beginning = beginning + 5
    return new_list

result1 = (create5x5(my_list))
print(result1)


def multiples_of_three(given_list): # Writes a function that replaces all multiples of 3 with “?”. Stores the updated 5x5 list in a new variable.
    for row in given_list:
        for number in range(len(row)):
            if row[number] % 3 == 0:
                row[number] = "?"
    return given_list

result2 = multiples_of_three(result1)
print(result2)

# A huge problem I had was that I forgot the difference between a lists value and it's index

# I tried an if statement like: 
# if (number % 3) == 0:
#   row[number] = "?"

# Which doesn't work becuase the [number] in the second line actually represnets an index, not a value, and python got confused once I was trying to index a [6] in a list of 5 values
# So I would get a lot of IndexErrors (and some other ones too)

def not_equal_to_questionmark(given_list): # Writes a function that adds all elements not equal to “?” and returns the sum. Saves the result in a variable.
    total = 0

    for row in given_list:
        for number in range(len(row)):
            if row[number] != "?":
                total = total + row[number]

    return total

print(not_equal_to_questionmark(result2))


# --- 4.1 Dictionary Operations ---


ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"]) # Print “Katie”’s age.

ages["Mira"] = 100 # Change Mira’s age to 100.

ages["Milana"] = 52 # Add ‘‘Milana" with an age of 52

del ages["Mariam"]  # Remove ‘‘Mariam" from the dictionary.

for name in ages: # Use a for loop to print out each person’s name and age.
    print(name,",", ages[name])


# --- My Favorite Function ---

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

def sum_nested(selected_list): # Writes a function called sum nested() that loops through each row, sums all numbers, and returns the total.
    total = 0
    for set in selected_list:
        for individual_number in set:
            total = total + individual_number
    return total

print(sum_nested(numbers))