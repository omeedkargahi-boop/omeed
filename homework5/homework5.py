# --- 2.1 Vocabulary Review ---

# 1. Git vs. GitHub: Git is a local program that tracks code edits on your machine, while GitHub is a website where you can post these changes for others to see
# 2. Terminal vs. Command Line: Terminal is the UI to type in commands, while the Command Line is the software that runs these commands on your machine
# 3. Local vs. Remote Repository: A local repositoary is a backed up version of your code on your machine, while a remote repository is a backup of your code on another server like GitHub
# 4. Version Control: a Git feature that allows developers to revert diles and collaborate with others
# 5. Staging Area: Temporary place in Git where you review changes before saving them
# 6. git add: The Git command to select what you want to backup
# 7. git commit: Saves changes to local repository before sending them out to remote repository
# 8. git push: Uploads changes to remote repository
# 9. git status: shows status of repository, and which files are being staged or tracked
# 10. git pull: The Git command to download changes from a remote repository onto your machine 
# 11. pwd: Git Bash command to print working directory
# 12. ls: Git Bash command to show all files and directories in current directory
# 13. cd: Git Bash command to change directory
# 14. nano: Git Bash command to open a file
# 15. touch: Git Bash command to create a file
# 16. mv: Git Bash command to move a file or directory to a new location
# 17. rm: Git Bash command to remove files or directories and bypass the recycle bin
# 18. cat: Git Bash command to read a file and print its contents


# --- 2.2 A Directory Tree ---

# 1. pwd
# 2. ls
# 3. cd .., cd brianna_repo, git pull origin main
# 4. cp homework.py ~/python_decal/judy_decal/homework/
# 5. cd .., cd judy_decal, cd homework
# 6. nano homework.py
# 7. git add, git commit, git push
# 8. Judy tried to push code edits to GitHub, but her remote respository has changes that she has not saved locally. I would first do git pull, then git add, commit, and push.
# 9. ~/Recent/


# --- 3.1 Data Types ---

def checkDataType(input):

    result = type(input)
    print(result)
    return result

checkDataType("hi")


# --- 3.2 Conditionals ---

def evenOrOdd(input):

    if input%2 == 0:
        return "Even"
    else:
        return "Odd"

print(evenOrOdd(34))


# --- 4.1 Loops ---

def sumWithLoop(list):
    total = 0
    for number in list:
        total = total+number
    return total

numbers = [1, 2, 3, 4, 5]

print(sumWithLoop(numbers))


# --- 5.1 Lists ---

new_list = []

def duplicatelist(list):
    position = 0
    for item in list:
        new_list.insert(position, item)
        position = position + 1
        new_list.insert(position, item)
        position = position + 1
    return new_list

letters = ["a", "b", "c"]

print(duplicatelist(letters))


# --- 5.2 Debugging ---

def square(num): # The function was missing a colon
    return num * num

print(square(11))


# --- 6.2 My Favorite Function ---

# My favorite function is by far evenOrOdd becuase I got the code right on the first try
print(evenOrOdd(3))