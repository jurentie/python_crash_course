guest_list = ["Elon Musk", "David Bowie", "Barack Obama"]

print("Dear: " + guest_list[0] + ", please come to my dinner party.")
print("Dear: " + guest_list[1] + ", please come to my dinner party.")
print("Dear: " + guest_list[2] + ", please come to my dinner party.")

print()

print(guest_list[0] + " can't make it.")

print()

guest_list[0] = "George Takei"

print("Dear: " + guest_list[0] + ", please come to my dinner party.")
print("Dear: " + guest_list[1] + ", please come to my dinner party.")
print("Dear: " + guest_list[2] + ", please come to my dinner party.")

print()

print("I have found a bigger dinner table!")

print()

# Add guest to beginning of list
guest_list.insert(0, "Colton Haynes")

#Add guest to middle of list
guest_list.insert(2, "RuPaul")

# Add guest to end of list
guest_list.append("Shakespear")

print("Dear: " + guest_list[0] + ", please come to my dinner party.")
print("Dear: " + guest_list[1] + ", please come to my dinner party.")
print("Dear: " + guest_list[2] + ", please come to my dinner party.")
print("Dear: " + guest_list[3] + ", please come to my dinner party.")
print("Dear: " + guest_list[4] + ", please come to my dinner party.")
print("Dear: " + guest_list[5] + ", please come to my dinner party.")

print()

print("I can only invite two people to dinner...")

print()

# Remove four people from the list and print a message apologizing.
print("Sorry " + guest_list.pop() + " that I can't invite you to dinner.")
print("Sorry " + guest_list.pop() + " that I can't invite you to dinner.")
print("Sorry " + guest_list.pop() + " that I can't invite you to dinner.")
print("Sorry " + guest_list.pop() + " that I can't invite you to dinner.")

print()

# Print message to remaining guests letting them know they are still invited.
print(guest_list[0] + " you are still invited.")
print(guest_list[1] + " you are still invited.")

print()

# Delete remaining people in list so I have an empty list.
del guest_list[1]
del guest_list[0]

# Make sure list is empty
print(guest_list)