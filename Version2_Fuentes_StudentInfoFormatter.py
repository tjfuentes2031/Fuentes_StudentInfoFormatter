firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
section = input("Enter section: ")
favoriteSubject = input("Enter favorite subject: ")

fullName = firstName + " " + lastName

cleanName = fullName.strip().title()
cleanSection = section.strip().title()
cleanFavoriteSubject = favoriteSubject.strip().title()

print("\nFormatted Output: ")
print(f"Name: {cleanName}")
print(f"Name Code: {cleanName.upper()}")
print(f"Section: {cleanSection.upper()}")
print(f"Favorite subject: {cleanFavoriteSubject}")
print(f"Character Count: {len(cleanName)}")
