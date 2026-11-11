ekwipunek = {"miecz": 1, "mikstura": 3, "złoto": 50}

while True:
  print("\n--- MENU EKWIPUNKU ---")
  print("1. Pokaż przedmioty")
  print("2. Dodaj przedmiot")
  print("3. Użyj przedmiotu")
  print("4. Sprawdź przedmiot")
  print("5. Wyjście")

  wybor = input("Wybierz opcję (1-5): ")

  # pokaz
  if wybor == "1":
    print("\nTwój ekwipunek:")
    for nazwa, ilosc in ekwipunek.items():
      print(f"- {nazwa}: {ilosc}")

  # dodaj
  elif wybor == "2":
    nazwa = input("Podaj nazwę przedmiotu: ").lower()
    ilosc = int(input("Podaj ilość do dodania: "))

    if nazwa in ekwipunek:
      ekwipunek[nazwa] += ilosc
    else:
      ekwipunek[nazwa] = ilosc
    print(f"Dodano {ilosc} x {nazwa}.")

  # uzyj
  elif wybor == "3":
    nazwa = input("Jaki przedmiot chcesz użyć?: ").lower()

    if nazwa in ekwipunek:
      ekwipunek[nazwa] -= 1
      print(f"Użyto {nazwa}.")

      # jesli 0 lub mniej to usun
      if ekwipunek[nazwa] <= 0:
        del ekwipunek[nazwa]
        print(f"Przedmiot {nazwa} się skończył i został usunięty.")
    else:
      print("Nie ma takiego przedmiotu w ekwipunku.")

  # sprawdz
  elif wybor == "4":
    nazwa = input("Jaki przedmiot chcesz sprawdzić?: ").lower()

    if nazwa in ekwipunek:
      print(f"Masz {ekwipunek[nazwa]} sztuk przedmiotu: {nazwa}.")
    else:
      print("Nie masz takiego przedmiotu.")

  # wyjscie
  elif wybor == "5":
    print("Koniec programu.")
    break
  else:
    print("Błędny wybór, wpisz cyfrę od 1 do 5.")