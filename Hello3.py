def ask_user():
	counter = int(input("Ile chcesz dodać filmów?: "))
	print("Ile filmów: ", counter)

	list_movies = []
	list_grades = []

	for i in range(counter):
		film = input("Podaj tytuł filmu: ")
		grade = float(input("Podaj ocenę filmu: "))

		list_movies.append(film)
		list_grades.append(grade)

	return list_movies, list_grades
user_movies, user_grades = ask_user()
print(user_movies)
print(user_grades)

index = int(input("Podaj numer filmu do sprawdzenia: ")



print(user_movies[index-1],":",user_grades[index-1])