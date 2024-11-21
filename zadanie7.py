import random

# Losowanie, czy pada (True = pada, False = nie pada)
pogoda = random.choice([True, False])

while True:
    # Pytanie do użytkownika
    odpowiedz = input("Czy pada deszcz? (tak/nie): ").lower()

    # Sprawdzenie odpowiedzi użytkownika
    if odpowiedz == "tak" and pogoda:
        print("Brawo! Zgadłeś! Pada deszcz.")
        break  # Przerywa pętlę, jeśli odpowiedź jest poprawna
    elif odpowiedz == "nie" and not pogoda:
        print("Brawo! Zgadłeś! Nie pada deszcz.")
        break  # Przerywa pętlę, jeśli odpowiedź jest poprawna
    else:
        print("Niestety, spróbuj jeszcze raz.")
