class Wunschmaschine:
    def __init__(self):
        self.ziel = ""
        self.essenz_check = ""
        self.kausal_check = ""
        self.energie_check = ""
        self.physisch_check = ""
        self.ergebnis = ""

    def ziel_eingeben(self):
        self.ziel = input("Was möchtest du manifestieren? ")
    
    def essenz_pruefung(self):
        print("\nEssenz-Ebene: Ist das Ziel wirklich dein tiefstes Seelenziel?")
        antwort = input("(ja/nein): ")
        if antwort.lower() == "ja":
            self.essenz_check = "✅ Dein Ziel entspricht deinem wahren Seelenwunsch."
        else:
            self.essenz_check = "⚠️ Dein Ziel könnte aus Ego-Wünschen stammen. Überlege, was du wirklich willst."

    def kausal_pruefung(self):
        print("\nKausale Ebene: Welche Überzeugung hast du zu diesem Ziel?")
        antwort = input("Glaubst du, dass du es leicht erreichen kannst? (ja/nein): ")
        if antwort.lower() == "ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt das Ziel."
        else:
            self.kausal_check = "⚠️ Du hast blockierende Glaubenssätze. Arbeite an deiner inneren Einstellung."
    
    def energie_pruefung(self):
        print("\nEnergie-Ebene: Fühlst du dich bereits so, als hättest du dein Ziel erreicht?")
        antwort = input("(ja/nein): ")
        if antwort.lower() == "ja":
            self.energie_check = "✅ Deine energetische Ausstrahlung stimmt mit deinem Ziel überein."
        else:
            self.energie_check = "⚠️ Visualisiere und spüre dein Ziel als bereits erfüllt, um deine Frequenz anzuheben."
    
    def physisch_pruefung(self):
        print("\nPhysische Ebene: Welche konkreten Schritte hast du schon unternommen?")
        antwort = input("Hast du bereits eine Handlung ausgeführt? (ja/nein): ")
        if antwort.lower() == "ja":
            self.physisch_check = "✅ Du bist aktiv in der Umsetzung. Sehr gut!"
        else:
            self.physisch_check = "⚠️ Manifestation benötigt physische Handlungen. Setze einen ersten konkreten Schritt!"
    
    def manifestieren(self):
        self.ziel_eingeben()
        self.essenz_pruefung()
        self.kausal_pruefung()
        self.energie_pruefung()
        self.physisch_pruefung()
        
        print("\n--- WUNSCHMASCHINEN-ANALYSE ---")
        print(f"\n🎯 Ziel: {self.ziel}")
        print(self.essenz_check)
        print(self.kausal_check)
        print(self.energie_check)
        print(self.physisch_check)
        
        if "⚠️" not in (self.essenz_check + self.kausal_check + self.energie_check + self.physisch_check):
            self.ergebnis = "🌟 Dein Ziel ist im vollständigen Alignment! Es wird sich schnell materialisieren. 🌟"
        else:
            self.ergebnis = "🔍 Es gibt Blockaden. Arbeite an den Bereichen mit ⚠️ für eine schnellere Manifestation."
        
        print("\n📌 Fazit: ", self.ergebnis)

# Anwendung der Wunschmaschine
if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()
