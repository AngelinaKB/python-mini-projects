detective = input("Enter a detective's name: ")
snack = input("Enter a type of snack: ")
location = input("Enter a location: ")
adjective = input("Enter an adjective: ")
suspect = input("Enter a suspect's name: ")
object_found = input("Enter an object found at the scene: ")

story = f"""
Detective {detective} was called to {location} to investigate a mysterious case:
someone had stolen a {snack} right out of the fridge.

The only clue? A {adjective} {object_found} lying next to the empty plate.

After interrogating {suspect}, who looked suspiciously full, Detective {detective} cracked the case.

Justice was served. But the {snack} was not.
"""

print(f"\n{story}")
