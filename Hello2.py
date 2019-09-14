liczba_filmów = 3
movies = []
grades = []

for i in range(liczba_filmów):
	film = input("Nazwa filmu: ")
	movies.append(film)

	ocena = int(input("Podaj ocene: "))
	grades.append(ocena)

suma = 0
for ocena in grades:
	suma = suma + ocena

avg_grades = suma/liczba_filmów

print("Srednia ocen:", avg_grades)
