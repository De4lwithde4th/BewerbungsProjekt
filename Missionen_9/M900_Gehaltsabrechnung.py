# 1.
# Definiere eine Klasse Mitarbeiter.
# Ein Mitarbeiter besitzt eine eindeutige Nummer (id) und einen Namen (name).
# Die ID des Mitarbeiters soll durch die Klasse selbst fortlaufend nummeriert werden.
# Der erste Mitarbeiter hat also die ID 1, der zweite Mitarbeiter die ID 2 usw.
# Füge der Klasse sinnvolle Getter- und Setter-Methoden hinzu
# und definiere zudem eine __str__()-Methode,
# die die ID und den Mitarbeiternamen als String zurückliefert.
# 2.
# Schreibe eine Klasse PersonalVerwaltung.
# Diese Klasse hat eine Mitarbeiterliste (mitarbeiterListe, Typ: list).
# Sie hält Methoden zum Hinzufügen und zum Entfernen von Mitarbeitern bereit.
# Außerdem benötigt sie eine Methode list_mitarbeiter(),
# um alle Mitarbeiter auf der Konsole aufzulisten.
#
# 3.
# Füge der Klasse PersonalVerwaltung eine Methode sort_mitarbeiter() hinzu.
# Diese Methode soll die Mitarbeiter mittels Bubblesort sortieren.
# Zu diesem Zweck muss in der Klasse Mitarbeiter
# eine Methode boolean ist_kleiner(Mitarbeiter m) hinzugefügt werden.
# Sie ist von Bubblesort zu verwenden, um die Rangfolge unter den Mitarbeitern zu erkennen.
# Die sort_mitarbeiter()-Methode soll dazu führen,
# dass die Mitarbeiter alphabetisch nach ihren Namen sortiert werden.

class Mitarbeiter:
    _id_counter = 0  # Klassenvariable zur Verwaltung der IDs
    
    def __init__(self, name):
        Mitarbeiter._id_counter += 1  # ID hochzählen
        self._id = Mitarbeiter._id_counter
        self._name = name
    
    # Getter-Methoden
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    # Setter-Methode für den Namen
    def set_name(self, name):
        self._name = name

    # Methode zum Vergleich: Gibt True zurück, wenn der aktuelle Mitarbeiter
    # alphabetisch (case-insensitive) vor dem anderen Mitarbeiter liegt.
    def ist_kleiner(self, anderer):
        return self._name.lower() < anderer._name.lower()
    
    # String-Darstellung
    def __repr__(self):
        return f"Mitarbeiter-ID: {self._id}, Name: {self._name}"


class PersonalVerwaltung:
    def __init__(self):
        self.mitarbeiterListe = []  # Liste zur Speicherung der Mitarbeiter
        
    def add_mitarbeiter(self, mitarbeiter):
        """Fügt einen Mitarbeiter der Liste hinzu."""
        self.mitarbeiterListe.append(mitarbeiter)
        
    def remove_mitarbeiter(self, mitarbeiter):
        """Entfernt einen Mitarbeiter aus der Liste, falls vorhanden."""
        if mitarbeiter in self.mitarbeiterListe:
            self.mitarbeiterListe.remove(mitarbeiter)
            
    def list_mitarbeiter(self):
        """Gibt alle Mitarbeiter in der Konsole aus."""
        for m in self.mitarbeiterListe:
            print(m)
            
    def sort_mitarbeiter(self):
        """Sortiert die Mitarbeiterliste alphabetisch nach den Namen mittels Bubblesort."""
        n = len(self.mitarbeiterListe)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Wenn das Element an der Stelle j nicht kleiner ist als das folgende,
                # werden die beiden Elemente getauscht.
                if not self.mitarbeiterListe[j].ist_kleiner(self.mitarbeiterListe[j+1]):
                    self.mitarbeiterListe[j], self.mitarbeiterListe[j+1] = self.mitarbeiterListe[j+1], self.mitarbeiterListe[j]


# Beispielhafte Nutzung:
if __name__ == '__main__':
    pv = PersonalVerwaltung()
    m1 = Mitarbeiter("Charlie")
    m2 = Mitarbeiter("Alice")
    m3 = Mitarbeiter("Bob")
    
    pv.add_mitarbeiter(m1)
    pv.add_mitarbeiter(m2)
    pv.add_mitarbeiter(m3)
    
    print("Unsortierte Mitarbeiterliste:")
    pv.list_mitarbeiter()
    
    pv.sort_mitarbeiter()
    
    print("\nSortierte Mitarbeiterliste:")
    pv.list_mitarbeiter()


