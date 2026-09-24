import tkinter
import json
indeksedycji = None
zadania = []
#region .json
def zapiszdane():
        with open("Zadania.json", "w", encoding="utf-8") as plik:
            json.dump(zadania, plik, ensure_ascii=False, indent=4)
def wczytajdane():
    try:
        with open("Zadania.json", "r", encoding="utf-8") as plik:
            zadania.extend(json.load(plik))
            odswiezliste()
    except FileNotFoundError:
        pass
#endregion
#region Definicje
def dodajzadanie():
    if pole.get() != "":
        tresc = pole.get()
        pole.delete(0, tkinter.END)
        priorytety = priorytet.get()
        wykonane = False
        zadanie = {
            "treść": tresc,
            "priorytet": priorytety,
            "wykonane": wykonane,
        }
        zadania.append(zadanie)
        błąd.pack_forget()
        zapiszdane()
        odswiezliste()
    else:
        bladedycji.pack_forget()
        błąd.pack()
def usunzadanie():
    try:
        indeks = lista.curselection()[0]
        zadania.pop(indeks)
        błąd.pack_forget()
        zapiszdane()
        odswiezliste()
    except IndexError:
        bladedycji.pack_forget()
        błąd.pack()
def zadaniedone():
    try:
        indeks = lista.curselection()[0]
        if not zadania[indeks]["wykonane"]:
            zadania[indeks]["wykonane"] = True
            błąd.pack_forget()
            zapiszdane()
            odswiezliste()
    except IndexError:
        bladedycji.pack_forget()
        błąd.pack()
def edytuj():
    try:
        global indeksedycji
        indeksedycji = indeks = lista.curselection()[0]
        zadanie = zadania[indeks]
        if not zadanie["wykonane"]:
            pole.delete(0, tkinter.END)
            pole.insert(0, zadanie["treść"])
            priorytet.set(zadanie["priorytet"])
            zapisedycji.pack()
            przyciskedycji.pack_forget()
            błąd.pack_forget()
            bladedycji.pack_forget()
        else:
            błąd.pack_forget()
            bladedycji.pack()
    except IndexError:
        błąd.pack()
        bladedycji.pack_forget()
def zapiszedycje():
    try:
        global indeksedycji
        if indeksedycji is not None:
            nowytekst = pole.get()
            if nowytekst != "":
                zadania[indeksedycji]["treść"] = nowytekst
                zadania[indeksedycji]["priorytet"] = priorytet.get()
                pole.delete(0, tkinter.END)
                zapisedycji.pack_forget()
                indeksedycji = None
                błąd.pack_forget()
                przyciskedycji.pack()
                zapiszdane()
                odswiezliste()
    except IndexError:
        bladedycji.pack_forget()
        błąd.pack()
def odswiezliste():
    lista.delete(0, tkinter.END)
    for i in zadania:
        if i["wykonane"] == True:
            lista.insert(tkinter.END, f"✓ {i["treść"]} — {i["priorytet"]}")
        else:
            lista.insert(tkinter.END, f" {i["treść"]} — {i["priorytet"]}")
#endregion
#region GUI
okno = tkinter.Tk()
okno.title("Projekt_3")
okno.geometry("400x600")
napis = tkinter.Label(okno, text="INTELIGENTNY PLANNER v0.1")
napis.pack()
pole = tkinter.Entry(okno, width=25)
pole.pack()
priorytet = tkinter.StringVar(value="Średni")
wybórpriorytetu = tkinter.OptionMenu(okno, priorytet, "Niski", "Średni", "Wysoki")
wybórpriorytetu.config(width=18)
wybórpriorytetu.pack()
przycisk = tkinter.Button(okno, text="Dodaj zadanie", command=dodajzadanie, width=20)
przycisk.pack()
zapisedycji = tkinter.Button(okno, text="Zapisz zmiany", command=zapiszedycje, width=20)
lista = tkinter.Listbox(okno, width=25)
lista.pack()
lista.delete(0, tkinter.END)
wczytajdane()
przyciskusuwan = tkinter.Button(okno, text="Usuń zaznaczone", command=usunzadanie, width=20)
przyciskusuwan.pack()
przyciskdone = tkinter.Button(okno, text="Zadanie wykonanane", command=zadaniedone, width=20)
przyciskdone.pack()
przyciskedycji = tkinter.Button(okno, text="Edytuj", command=edytuj, width=20)
przyciskedycji.pack()
błąd = tkinter.Label(okno, text="Błąd")
bladedycji = tkinter.Label(okno, text="Zadanie wykonane. Nie możesz edytować wykonanych zadań.")
bladedycji.pack_forget()
błąd.pack_forget()
okno.mainloop()
#endregion 
