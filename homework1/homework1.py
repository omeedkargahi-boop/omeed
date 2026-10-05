# File: homework1.py

# --- Variables and Data Types ---

a=10
print (a)
print(type(a)) # a is an integer, a whole number

b=1.5
print (b)
print(type(b)) # b is a float, a number followed by a decimal

c=3j
print (c)
print(type(c)) # c is a complex number, a number followed by an imaginary number

d="hello" 
print (d)
print(type(d)) # d is a string, which is a text or sequence of words

e=[1,2,3]
print (e)
print(type(e)) # e is a list

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print(type(f)) # f is a dict

g=(1,2)
print (g)
print(type(g)) # g is a tuple

h = ["apple", "banana", "strawberry"]
print (h)
print(type(h)) # h is a list

i = True
print (i)
print(type(i)) # i is a bool

j = None
print (j)
print(type(j)) # j is a NoneType

k = [True, "blue", 12]
print (k)
print(type(k)) # k is a list

l = str(14)
print (l)
print(type(l)) # l is a string

m = 1e4
print (m)
print(type(m)) # m is a float

# --- Booleans ---
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, it is a string with something in it
print(bool(123)) # True, it is an integer with something in it
print(bool(["apple", "cherry", "banana"])) # True, it is a list with something in it
print(bool(True)) # True, True is always True
print(bool(False)) # False, False is always False
print(bool(0)) # False, Zero repsents nothing
print(bool("")) # False, an empty value is always false
print(bool(" ")) # True, the space counts as a character
print(bool(())) # False, an empty value is always false
print(bool([])) # False, an empty value is always false
print(bool({})) # False, an empty value is always false
print(bool(True and False)) # False, "and" requires two True values to be True
print(bool(True and True)) # True, "and" requires two True values to be True
print(bool(False and False)) # False, "and" requires two False values to be False
print(bool(True or False)) # True, "or" only requires one value to be True to be True
print(bool(True or True)) # True, "or" only requires one value to be True to be True
print(bool(False or False)) # False, "or" only requires one value to be False to be False
print(bool(not(False))) # True, being not False is the same as True
print(bool(not(True))) # False, being not True is the same as False


# True usually represents something that is there, while False represents the lack of something
# print print(bool(" ")), I didn't think a space would be considered a charcter
z=10
y=11
print(bool(z < y)) # This is True, because it compares the variables z and y, and confirms that z is smaller
print(bool(z > y)) # This is False, becuase it compares the varibale y to z and confirms that y is larger

# --- Operators ---
print(10 + 5) # 15, + performs addition
print (10-5) # 5, - performs subtraction
print(2 * 4) # 8, * perfoms multiplication
print(6 / 3) # 2, / perfoms division
print(5 % 2) # 2, 1 returns remainder
print(3 ** 2) # 9, ** acts as an exponential
print(15 // 2) # 7, // divides and rounds
print(5 == 2) # False, == is "equals"
print(10 != 10) # False, =! is "not equal"
print(2 < 5) # True, < is less than
print(12 > 5) # True, > is greater than
print(5 <= 6) # True, >= is les than or equal to
print(1 >= 10) # False, >= is greater than or equal to

x=5
x += 5 # Adds 5 to x, saves value
x -= 4 # Subtracts 4 from x, ssaves value
x *= 3 # Multiplies x by 3, saves value

# and requires all condtions to be true
print(10 == 10 and 11 == 11) # retunrs True
print(10 == 10 and 10 == 11) # returns False

# or requires at least one condition to be 
print(10 == 10 or 10 == 11) # returns True
print(11 == 10 or 10 == 11) # returns False

# not reverses a condtion
print(not(10 == 11)) # returns True
print(not(11 == 11)) # retuns False

# / simply divides, while // divides and rounds
# % divides and retunrs remainder, while // divides and rounds
# I would use % when looking for remained
print(15%4) # prints 3 as a remainder
# Assignment operators work by evaluting an expression, and storing the value of it as a variable for future use

# --- Strings ---
my_string = "hello"
print(my_string) # prints: hello
print(my_string[0])  # prints: h
print(my_string[1]) # prints: e
print(my_string[2])  # prints: l
print(my_string[3]) # prints: l
print(my_string[4])  # prints: o
print(my_string[-1])  # prints: o
print(my_string[1:3])  # prints: el
print(my_string[0:5:2])  # prints: hlo
print(len(my_string)) # prints: 5
print(my_string + "goodbye") # prints: hellogoodbye
print(7 * my_string)  # prints: hellohellohellohellohellohellohello

# I scliced lines 8 and 0 becuase : chooses certain letters to use
name = "Oski"
print("Hello, my name is", name) # results in "Hello, my name is Oski" becuase name was already defined as a variable and was printed
name = "Oski"
print(f"Hello, my name is {name}") # results in the same thing as above but embeds the "name" variable in the string rather than keeping it separate
# The line above usues an f-string (formatted string) which allows you to put variables directly inside a text string

# --- Terminal Commands ---
# cd
# Changes directory, use to move between folders
# Example, cd Downloads

# ls
# lists all files and folders in current directory
# ls

# ls -a
# lists every single files and folder including hidden ones in your current directory
# ls -1

# mkdir
# creates a new directory
# mkdir ExampleFolder

# cat
# displays text of a file on your terminal
# cat pythonproject.py

# pwd
# prints current directory's path back to root directory
# pwd

# cd . .
# moves you into the parent directory of your current diretory
# cd . . could move you from grandparent/parent/child to grandparent/parent

# cd . 
# tells scripts to look at your current folder
# cd . 

# cd~
# sends you back to home directory
# cd ~

# cp
# copies a file and sends to a destination
# cp lecturenotes.txt backup.txt

# mv
# moves a file to a new folder
# mv lecturenotes.txt booknotes.txt

# rm
# permenantly deletes file, bypassing recyle bin
# rm lecturenotes.txt

# clear
# clears your terminal
# clear

# grep
# searches inside text files for specific word
# grep "photosynthesis" lecturenotes.txt


# touch
# creates brand new, empty file instantly without opening editor
# "touch" followed by file name
# touch novel.txt

# head
# displays first 10 lines of text file
# "head" followed by file name
# head novel.txt

# man
# opens built in refernce guide for any command
# "man" folowed by command you want to explore
# man head

# ls only lists standard, visible files, while ls -a reveals hidden files as well
# A hidden file is a file that is hidden from your directory GUI because they hold sensitive software or background settings

#Three useful flags
# -lh  shows files in a detailed list, sorting by whatever you want. To use, type "ls -lh"
# rm is used to delete a directory and all subdirectories, and it is used by typing "rm -r files_for_deletion"
# -i makes a search non case sensitive, and you use it by typing "grep -i "Banana" bionotes.txt" and it returns Banana, banana, BANANA
