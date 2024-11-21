Napisz program, który obliczy sumę wszystkich liczb, które są podzielne przez 3 lub 5, w zakresie od 1 do 1000.
ODPOWIEDZ:
suma = 0

for i in range(1, 1001):  # Przechodzimy przez liczby od 1 do 1000
    if i % 3 == 0 or i % 5 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 3 lub 5
        suma += i  # Dodajemy liczbę do sumy

print(f"Suma liczb podzielnych przez 3 lub 5 w zakresie od 1 do 1000 wynosi: {suma}")
