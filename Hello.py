movie = input("Tytuł filmu: ")
grade = int(input("Ocena filmu w skali 1 - 10: "))

print("Film pt. " + movie)
print("Oceniasz na ", grade)

if grade > 7:
	print("Very good")
elif grade > 5:
	print("Typical")
else:
	print("Crap")