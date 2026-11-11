import random

# Początkowy ekwipunek (każdy przedmiot ma ilość, wagę i wartość)
ekwipunek = {
    "miecz": {"ilosc": 1, "waga": 5, "wartosc": 100},
    "mikstura": {"ilosc": 3, "waga": 1, "wartosc": 20},
    "złoto": {"ilosc": 50, "waga": 0, "wartosc": 1},
}

MAKS_WAGA = 20  # Maksymalna waga, jakiej nie można przekroczyć


# Funkcja pomocnicza licząca aktualną wagę ekwipunku
def oblicz_wage():
  suma_wagi = 0
  for nazwa, dane in ekwipunek.items():
    if nazwa != "złoto":  # Złoto pomijamy w wadze
      suma_wagi += dane["ilosc"] * dane["waga"]
  return suma_wagi


# Opcja 1: Wyświetla nazwy, ilości, wagę i wartość
def pokaz_przedmioty(eq):
  print("\n--- TWÓJ EKWIPUNEK ---")
  if not eq:
    print("Ekwipunek jest pusty.")
    return

  akt_waga = oblicz_wage()
  print(f"Aktualna waga ekwipunku: {akt_waga} / {MAKS_WAGA}")

  for nazwa, dane in eq.items():
    print(
        f"- {nazwa.capitalize()}: ilość: {dane['ilosc']}, waga: {dane['waga']},"
        f" wartość: {dane['wartosc']}"
    )
  print("------------------------")


# Opcja 2: Dodaj / Kup przedmiot[cite: 1]
def dodaj_przedmiot(eq):
  print("\n--- SKLEP / DODAWANIE PRZEDMIOTU ---")
  nazwa = input("Podaj nazwę przedmiotu: ").lower()

  # Pobieranie lub losowanie wartości i wagi
  try:
    wartosc = int(input("Podaj wartość przedmiotu (lub wpisz losową, np. 0): "))
    if wartosc <= 0:
      wartosc = random.randint(10, 30)
      print(f"Wylosowano wartość: {wartosc}")
  except ValueError:
    wartosc = random.randint(10, 30)
    print(f"Wylosowano wartość: {wartosc}")

  try:
    waga = int(input("Podaj wagę przedmiotu (lub wpisz 0, aby wylosować): "))
    if waga <= 0:
      waga = random.randint(1, 5)
      print(f"Wylosowano wagę: {waga}")
  except ValueError:
    waga = random.randint(1, 5)
    print(f"Wylosowano wagę: {waga}")

  try:
    ilosc = int(input("Podaj ilość: "))
  except ValueError:
    ilosc = 1

  koszt = wartosc * ilosc

  # Sprawdzenie czy gracza stać na zakup (jeśli to nie złoto)
  if "złoto" in eq and nazwa != "złoto":
    if eq["złoto"]["ilosc"] < koszt:
      print(
          f"Nie masz wystarczająco złota! Potrzebujesz {koszt}, a masz"
          f" {eq['złoto']['ilosc']}."
      )
      return
    # Odejmujemy złoto za zakup
    eq["złoto"]["ilosc"] -= koszt

  # Sprawdzenie maksymalnej wagi
  akt_waga = oblicz_wage()
  if akt_waga + (waga * ilosc) > MAKS_WAGA:
    print(
        "Przekroczysz maksymalną wagę ekwipunku! Zakup/dodanie anulowane."
       [cite: 1]
    )
    if "złoto" in eq and nazwa != "złoto":
      eq["złoto"]["ilosc"] += koszt  # Zwrot złota
    return

  # Dodanie przedmiotu do słownika lub zwiększenie ilości
  if nazwa in eq:
    eq[nazwa]["ilosc"] += ilosc
  else:
    eq[nazwa] = {"ilosc": ilosc, "waga": waga, "wartosc": wartosc}

  print(f"Sukces! Dodano {ilosc} x {nazwa} do ekwipunku.")


# Opcja 3: Użyj lub sprzedaj przedmiot[cite: 1]
def uzyj_przedmiotu(eq):
  print("\n--- UŻYJ / SPRZEDAJ PRZEDMIOT ---")
  nazwa = input("Jaki przedmiot chcesz użyć lub sprzedać?: ").lower()

  if nazwa not in eq:
    print("Nie ma takiego przedmiotu w ekwipunku.")
    return

  print("1. Użyj (zmniejsz ilość o 1)")
  print("2. Sprzedaj (odzyskaj połowę wartości)")
  wybor = input("Wybierz opcję (1/2): ")

  if wybor == "1":
    eq[nazwa]["ilosc"] -= 1
    print(f"Użyto przedmiotu: {nazwa}.")
  elif wybor == "2":
    zysk = eq[nazwa]["wartosc"] // 2
    eq[nazwa]["ilosc"] -= 1
    if "złoto" in eq:
      eq["złoto"]["ilosc"] += zysk
    else:
      eq["złoto"] = {"ilosc": zysk, "waga": 0, "wartosc": 1}
    print(f"Sprzedano {nazwa}. Otrzymano {zysk} złota.")
  else:
    print("Nieprawidłowy wybór.")
    return

  # Jeśli ilość spadła do 0, usuń wpis całkowicie[cite: 1]
  if eq[nazwa]["ilosc"] <= 0:
    del eq[nazwa]
    print(f"Przedmiot {nazwa} się skończył i został usunięty z ekwipunku.")


# Opcja 4: Sprawdź obecność przedmiotu[cite: 1]
def sprawdz_przedmiot(eq):
  print("\n--- SPRAWDŹ PRZEDMIOT ---")
  nazwa = input("Jaki przedmiot chcesz sprawdzić?: ").lower()

  if nazwa in eq:
    dane = eq[nazwa]
    print(
        f"Znaleziono! {nazwa.capitalize()} -> Ilość: {dane['ilosc']}, Waga:"
        f" {dane['waga']}, Wartość: {dane['wartosc']}"
    )
  else:
    print(f"Przedmiot '{nazwa}' nie znajduje się w ekwipunku.")


# Główna pętla programu z menu[cite: 1]
def main():
  while True:
    print("\n=== MENU EKWIPUNKU ===")
    print("1. Pokaż przedmioty")
    print("2. Dodaj / Kup przedmiot")
    print("3. Użyj / Sprzedaj przedmiot")
    print("4. Sprawdź przedmiot")
    print("5. Wyjście")

    wybor = input("Wybierz opcję (1-5): ")

    if wybor == "1":
      pokaz_przedmioty(ekwipunek)
    elif wybor == "2":
      dodaj_przedmiot(ekwipunek)
    elif wybor == "3":
      uzyj_przedmiotu(ekwipunek)
    elif wybor == "4":
      sprawdz_przedmiot(ekwipunek)
    elif wybor == "5":
      print("Koniec programu. Do zobaczenia!")
      break  # Przerywa pętlę while i kończy działanie[cite: 1]
    else:
      print("Nie ma takiej opcji! Wybierz liczbę od 1 do 5.")


# Uruchomienie programu
if __name__ == "__main__":
  main()