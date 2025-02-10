# Project 5 By FA24-BCS-110
story = """
On a sunny (), a curious [] named {} went on an adventure. 
First, {} decided to visit the {} in search of a magical {}. 
Along the way, {} met a friendly {} named {}. They decided to {} together and stumbled upon a {} that could {}!
Excited, they rushed to tell everyone in the {}, especially {}'s best friend, {}. 
Together, they all celebrated with a huge {} and lived {} ever after.
"""

place = input("Enter a place: ")
character_type = input("Enter a character type (e.g., wizard, dragon): ")
character_name = input("Enter the name of the character: ")
friend_name = input("Enter the name of a friend: ")
magical_object = input("Enter a magical object: ")
activity = input("Enter an activity: ")
strange_thing = input("Enter a strange thing (e.g., talking tree): ")
ability = input("Enter an ability (e.g., fly, sing): ")
celebration = input("Enter a type of celebration: ")
adjective = input("Enter an adjective: ")

filled_story = story.replace("()", place).replace("[]", character_type).replace("{}", character_name, 1).replace("{}", character_name, 1).replace("{}", place, 1).replace("{}", magical_object, 1).replace("{}", character_name, 1).replace("{}", character_type, 1).replace("{}", friend_name, 1).replace("{}", activity, 1).replace("{}", strange_thing, 1).replace("{}", ability, 1).replace("{}", place, 1).replace("{}", character_name, 1).replace("{}", friend_name, 1).replace("{}", celebration, 1).replace("{}", adjective, 1)

print(filled_story)