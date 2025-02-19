import streamlit as st

class Wunschmaschine:
    def __init__(self):
        self.ziel = ""
        self.essenz_check = ""
        self.kausal_check = ""
        self.energie_check = ""
        self.physisch_check = ""
        self.ergebnis = ""

    def ziel_eingeben(self):
        self.ziel = st.text_input("Was möchtest du manifestieren?")
    
    def essenz_pruefung(self):
        antwort = st.radio("Essenz-Ebene: Ist das Ziel wirklich dein tiefstes Seelenziel?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.essenz_check = "✅ Dein Ziel entspricht deinem wahren Seelenwunsch."
        else:
            self.essenz_check = "⚠️ Dein Ziel könnte aus Ego-Wünschen stammen. Überlege, was du wirklich willst."

    def kausal_pruefung(self):
        antwort = st.radio("Kausale Ebene: Glaubst du, dass du es leicht erreichen kannst?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt das Ziel."
        else:
            self.kausal_check = "⚠️ Du hast blockierende Glaubenssätze. Arbeite an deiner inneren Einstellung."
    
    def energie_pruefung(self):
        antwort = st.radio("Energie-Ebene: Fühlst du dich bereits so, als hättest du dein Ziel erreicht?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.energie_check = "✅ Deine energetische Ausstrahlung stimmt mit deinem Ziel überein."
        else:
            self.energie_check = "⚠️ Visualisiere und spüre dein Ziel als bereits erfüllt, um deine Frequenz anzuheben."
    
    def physisch_pruefung(self):
        antwort = st.radio("Physische Ebene: Hast du bereits eine Handlung ausgeführt?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.physisch_check = "✅ Du bist aktiv in der Umsetzung. Sehr gut!"
        else:
            self.physisch_check = "⚠️ Manifestation benötigt physische Handlungen. Setze einen ersten konkreten Schritt!"
    
    def manifestieren(self):
        st.title("✨ Wunschmaschine ✨")
        self.ziel_eingeben()
        if self.ziel:
            self.essenz_pruefung()
            self.kausal_pruefung()
            self.energie_pruefung()
            self.physisch_pruefung()

            st.subheader("--- WUNSCHMASCHINEN-ANALYSE ---")
            st.write(f"🎯 Ziel: {self.ziel}")
            st.write(self.essenz_check)
            st.write(self.kausal_check)
            st.write(self.energie_check)
            st.write(self.physisch_check)
            
            if "⚠️" not in (self.essenz_check + self.kausal_check + self.energie_check + self.physisch_check):
                self.ergebnis = "🌟 Dein Ziel ist im vollständigen Alignment! Es wird sich schnell materialisieren. 🌟"
            else:
                self.ergebnis = "🔍 Es gibt Blockaden. Arbeite an den Bereichen mit ⚠️ für eine schnellere Manifestation."
            
            st.success(self.ergebnis)

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()
