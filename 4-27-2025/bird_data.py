# ---------------------------------------
# Computer Science
# Program 13: Bird Targets
# Your Name
# Last Modified: 
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------


import string  # import string module 

# Function to print the menu options
def print_menu():
    print("\nTarget Bird List Menu")
    print("1. Print Target List")
    print("2. Lookup by Name")
    print("3. Lookup by Number")
    print("4. How Many Birds?")
    print("5. How Many in Family?")
    print("6. Exit\n")

# Function to print all birds in the target list
def print_target_list(targets):
    print("\nTarget List\n")
    for number in targets.keys():  # go through all bird numbers sorted numerically
        print(f"-----------");
        bird = targets[number]
        print(f"Number: {number}, Name: {bird[0]} ({bird[1]}), Family: {bird[2]}, Frequency: {bird[3]} occurrence")
    print("-----------\nEnd Target List")


# Function to search for a bird by its common name
def lookup_by_name(targets, name):
    count = 0
    found = False  # flag to check if bird was found
    for bird in targets.values():  # search through all bird entries
        count += 1
        if bird[0].lower() == name.lower():  # make case-insensitive comparison
            print(f"Number: {count}, Name: {bird[0]} ({bird[1]}), Family: {bird[2]}, Frequency: {bird[3]}\n")
            found = True
            break  # stop looping once found
    if not found:
        print(f"\n{name} not found in the target list.\n")



# Function to search for a bird by its number
def lookup_by_number(targets, number):
    if number in targets:  # check if bird number exists
        bird = targets[number]
        print(f"Number: {number}, {bird[0]} ({bird[1]}), Family: {bird[2]}, Frequency: {bird[3]}\n")
    else:
        print(f"Error: Target number {number} does not exist.\n")

# Function to count and print how many birds are in the list
def how_many_birds(targets):
    print(f"There are {len(targets)} different target birds.\n")

# Function to count how many birds belong to a specific family
def how_many_in_family(targets, family):
    count = 0
    for bird in targets.values():
        if bird[2].lower() == family.lower():  # compare family names case-insensitively
            count += 1
    print(f"There are {count} target birds in the family {family}.\n")

    
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_targets(filename):
    targets = {}
    file = open(filename, "r")
    
    for bird in file:
        birdlist = bird.strip().split(",")
        index = int(birdlist.pop(0))
        targets[index] = [birdlist.pop(0)]          # common name
        targets[index] += [birdlist.pop(0)]         # scientific name
        targets[index] += [birdlist.pop(0)]         # family
        targets[index] += [birdlist.pop(0)]         # frequency of occurrence on eBird checklists

    file.close()
    return targets

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

targets = create_targets("birddata.txt")

choice = 0
while choice != 6:
    print_menu()
    choice = get_choice(1, 6, "Enter a menu option: ")
    if choice == 1:    
        print_target_list(targets)
    elif choice == 2:
        name = input("Enter a bird name: ")
        name = name.capitalize()
        lookup_by_name(targets, name)
    elif choice == 3:
        number = get_choice(1, 100, "Enter a item number: ")
        lookup_by_number(targets, number)
    elif choice == 4:
        how_many_birds(targets)
    elif choice == 5:
        family = input("Enter a family name: ")
        how_many_in_family(targets, family)
print("Thank you.  Goodbye!")
