# Zmienna do liczenia odpowiedzi "nie"
nie_count = 0

while True:
    odpowiedz = input("Czy pada deszcz? (tak/nie/nie wiem): ").lower()

    if odpowiedz == "tak":
        print(f"Zakończono. Udzieliłeś {nie_count} odpowiedzi 'nie'.")
        break  # Zakończenie pętli, gdy użytkownik odpowie 'tak'
    
    elif odpowiedz == "nie":
        nie_count += 1  # Zwiększamy licznik odpowiedzi 'nie'
    
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    
    else:
        print("Proszę odpowiedz 'tak', 'nie' lub 'nie wiem'.")
