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

