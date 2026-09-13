# ---IMPORTS---
import tkinter as tk
from tkinter import messagebox
import webbrowser

# ---FARBEN---
HINTERGRUND = "#F2EFE9"
KARTEN = "#E8E5DF"
BUTTONS = "#607D8B"
HOVER = "#9DB7C5"
UBERSCHRIFT = "#263746"
TEXT = "#263746"
BEIGE = "#D3CEC4"

# ---HAUPTFENSTER---
fenster = tk.Tk()
fenster.configure(bg=HINTERGRUND)
fenster.title("Interaktive Bewerbung")
fenster.geometry("900x820")

katze_base64 = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABmklEQVRYR+2UMUoEQRBFZy8gGG4ixoIggpl4AD2CJt5gc2PzvYGJHkEPIGaCCIKxmGwoeAHlD/Ob3uqqrtp2kBV8yfR0/6r6W12zk06wOd3+4vpj8TbhOsqq8UsCBN/fXqf3o5OzUBLSEl81ACJJQGusawB4iVrjQMgAQDKLWsxoBlr4N/A3OoB7x6AMz+7l6SHdITg+nfXPu5v5sFNiaXb3DzFX/SCyTjoc6DdwiKccQCR+f33stnYO+ndZAHgafj1acZA2tS+Av4zI5MDTeHPQt4Yv0gCw2ptT0+T/H5qRagfGwO1AWgVNTJ8/03qxt5HWGl5xUBxGTYxRHKgCby4svPtm3vysEJHcBKgZyQsDqzhz5N0phCRyFRpW62U+6gohkOJV0UzInOtrQDptJdqF4gqkqJUmA1LwU6QJmX+9DGjutG5czq+6i9l5sSYyjl3Q8oNqezQDgMHauYyztDRmGgAyGaklje5xNn7VAI3ng1k1AKxfAPJ9TQeoBfKzBEsbmgktcdQA9rSiOcUhTKQXAyb1tF5xaL4BoFCgnevphJYAAAAQZGVCRzI5RUE1N0U4OTE2NkNFODhYw9CBAAAAAElFTkSuQmCC" 

katze_icon = tk.PhotoImage(data=katze_base64)
fenster.iconphoto(True, katze_icon)

# ---FUNKTIONEN---
def starten():
    startseite.pack_forget()
    auswahlseite.pack(fill="both", expand=True)

def zeige_me():
    auswahlseite.pack_forget()
    me_seite.pack(fill="both", expand=True)

def zurueck_auswahl_me():
    me_seite.pack_forget()
    auswahlseite.pack(fill="both", expand=True)

def zeige_staerken():
    auswahlseite.pack_forget()
    staerken_seite.pack(fill="both", expand=True)

def zurueck_zu_auswahl():
    staerken_seite.pack_forget()
    auswahlseite.pack(fill="both", expand=True)

def warum_it_anzeigen():
    auswahlseite.pack_forget()
    warum_it_seite.pack(fill="both", expand=True)

def zurueck_zu_auswahl_warum_it():
    warum_it_seite.pack_forget()
    auswahlseite.pack(fill="both", expand=True)

def mitbringen_anzeigen():
    auswahlseite.pack_forget()
    mitbringen_seite.pack(fill="both", expand=True)

def zurueck_zu_auswahl_mitbringen():
    mitbringen_seite.pack_forget()
    auswahlseite.pack(fill="both", expand=True)

def zeige_danke():
    auswahlseite.pack_forget()
    dankeseite.pack(fill="both", expand=True)

def zurueck_auswahl():
    dankeseite.pack_forget()
    auswahlseite.pack(fill="both", expand=True) 

def erstelle_box(parent):
    box = tk.Frame(
        parent,
        bg=KARTEN,
        padx=20,
        pady=20,
        highlightbackground=BEIGE,
        highlightthickness=1,
        relief="flat"
    )
    return box

def erstelle_titel(parent, text):
    label = tk.Label(
        parent,
        text=text,
        font=("Arial", 25, "bold"),
        bg=KARTEN,
        fg=UBERSCHRIFT
    )
    label.pack(pady=20)
    return label

def erstelle_untertitel(parent, text):
    label = tk.Label(
        parent,
        text=text,
        font=("Arial", 16),
        bg=KARTEN,
        fg=UBERSCHRIFT,
        anchor="w",
        justify="left"
    )
    label.pack(pady=(5), padx=20, fill="x")
    return label

def erstelle_text(parent, text):
    label = tk.Label(
        parent,
        text=text,
        font=("Arial", 12),
        wraplength=650, 
        justify="left",
        anchor="w",
        bg=KARTEN,
        fg=TEXT
    )
    label.pack(pady=(0, 15), padx=50, fill="x")
    return label

def hover_rein(event):
    event.widget.config(
        bg=HOVER,
        fg=UBERSCHRIFT
    )
def hover_raus(event):
    event.widget.config(
        bg=BUTTONS,
        fg="white"
    )

def create_main_button(parent, text, funktion):
    button = tk.Button(
        parent,
        text=text,
        font=("Arial", 12, "bold"),
        bg=BUTTONS,
        fg="white",
        bd=2,
        relief="flat",
        cursor="hand2",
        command=funktion
    )
    button.bind("<Enter>", hover_rein)
    button.bind("<Leave>", hover_raus)
    button.pack(pady=(20, 5))
    return button

def create_scnd_button(parent, text, funktion, schriftgrosse, p_x=20, p_y=10):
    rahmen = tk.Frame(
        parent,
        bg=BEIGE,
        padx=3,
        pady=3
    )
    button = tk.Button(
        rahmen,
        text=text,
        font=("Arial",schriftgrosse ,"bold"),
        padx=p_x,
        pady=p_y,
        bg=BUTTONS,
        fg="white",
        bd=0,
        relief="flat",
        cursor="hand2",
        command=funktion
    )
    button.bind("<Enter>", hover_rein)
    button.bind("<Leave>", hover_raus)
    button.pack(fill="both", expand=True)
    return rahmen

def create_zrk_button(parent, funktion):
    button = tk.Button(
        parent,
        text="❮",
        font=("Arial", 15, "bold"),
        bg=BUTTONS,
        fg="white",
        bd=2,
        relief="flat",
        cursor="hand2",
        command=funktion
    )
    button.bind("<Enter>", hover_rein)
    button.bind("<Leave>", hover_raus)
    button.place(y=20, x=20)
    return button

def umschalten_details(text_element, button_element):
    if text_element.winfo_viewable():
        text_element.pack_forget()
        button_element.config(text="Mehr Details ▾")
    else:
        text_element.pack(after=button_element, pady=(2, 8), padx=40, fill="x", anchor="w")
        button_element.config(text="Weniger Details ▴")

def umschalten_button(parent, text="Mehr Details ▾", funktion=None ):
    button = tk.Button(
        parent,
        text=text,
        bg=KARTEN,
        fg=UBERSCHRIFT,
        bd=0,
        relief="flat",
        cursor="hand2",
        anchor="w",
        justify="left",
        command=funktion
    )
    return button

def email_offnen(event=None):
    webbrowser.open("https://mail.google.com/mail/?view=cm&fs=1&to=fatmanaalgan0@gmail.com")

def kontakt_popup():
    popup = tk.Toplevel(fenster)
    popup.title("Kontakt")
    popup.geometry("400x320")
    popup.configure(bg=HINTERGRUND)
    popup.resizable(False, False)
    popup.grab_set()

    karten_frame = tk.Frame(popup, bg=KARTEN, padx=20, pady=20)
    karten_frame.pack(expand=True, fill="both", padx=20, pady=20)

    erstelle_titel(karten_frame, "Kontakt aufnehmen")

    email_label = tk.Label(
        karten_frame, 
        text="📧 fatmanaalgan0@gmail.com", 
        bg=KARTEN, 
        fg="#0066cc", 
        font=("Arial", 11, "underline"),
        cursor="hand2"
    )
    email_label.pack(pady=5)
    email_label.bind("<Button-1>", email_offnen)

    telefon_label = tk.Label(
        karten_frame, 
        text="📱 Telefon: +43 676 63 15 779", 
        bg=KARTEN,
        fg="black", 
        font=("Arial", 11)
    )
    telefon_label.pack(pady=5)


    btn_frame = tk.Frame(karten_frame, bg=KARTEN)
    btn_frame.pack(pady=10)

    btn_schliessen = tk.Button(
        btn_frame, 
        text="Schließen", 
        command=popup.destroy, 
        bg=HINTERGRUND, 
        relief="flat",
        width=12
    )
    btn_schliessen.pack(side="left", padx=5)

    btn_beenden = tk.Button(
        btn_frame, 
        text="Programm beenden", 
        command=fenster.destroy, 
        bg="#d9534f", 
        fg="white", 
        relief="flat",
        width=16
    )
    btn_beenden.pack(side="left", padx=5)

def beenden_gag():
    sicher=messagebox.askyesno(
        "Beenden",
        "Möchten Sie die Bewerbung wirklich beenden?"
    )
    if sicher:
        w_sicher=messagebox.askyesno(
            "Wirklich?",
            "Sind Sie sich wirklich sicher?"
        )
        if w_sicher:
            fenster.destroy()

# ---STARTSEITE---
startseite=tk.Frame(fenster, bg=HINTERGRUND)
startseite.pack(fill="both", expand=True)

start_box = erstelle_box(startseite)
start_box.pack(padx=20, pady=70, expand=True)

erstelle_titel(start_box, "Willkommen zu meiner Bewerbung")

untertitel = tk.Label(
    start_box,
    text="IT-Systemtechnik | Fatmana Algan",
    font=("Arial", 16),
    bg=KARTEN,
    fg=UBERSCHRIFT,
    anchor="w",
    justify="left"
)
untertitel.pack(pady=(0, 20), padx=50)


create_main_button(start_box, "Bewerbung starten ❯", starten)

# ---AUSWAHLSEITE---
auswahlseite = tk.Frame(fenster)
auswahlseite.configure(bg=HINTERGRUND)

auswahl_box = erstelle_box(auswahlseite)
auswahl_box.pack(padx=20, pady=120)

erstelle_titel(auswahl_box, "Wählen Sie einen Bereich aus")

me_button = create_scnd_button(auswahl_box, "Über mich", zeige_me, 15)
me_button.pack(fill="x", pady=10, padx=40)

staerken_button = create_scnd_button(auswahl_box, "Meine Stärken", zeige_staerken, 15)
staerken_button.pack(fill="x", pady=10, padx=40)

it_button = create_scnd_button(auswahl_box, "Warum IT?", warum_it_anzeigen, 15)
it_button.pack(fill="x", pady=10, padx=40)

mitbringen_button = create_scnd_button(auswahl_box, "Was ich mitbringe", mitbringen_anzeigen, 15)
mitbringen_button.pack(fill="x", pady=10, padx=40)

weiter_button = tk.Button(
    auswahl_box, 
        text="Weiter ❯", 
        font=("Arial", 10, "bold"),
        bg=BUTTONS,
        fg="white",
        bd=2,
        relief="flat",
        width=12,
        padx=10,
        pady=6,
        command=zeige_danke 
)
weiter_button.bind("<Enter>", hover_rein)
weiter_button.bind("<Leave>", hover_raus)
weiter_button.pack(pady=(15, 5))

# ---ÜBER MICH---
me_seite = tk.Frame(fenster)
me_seite.configure(bg=HINTERGRUND)

me_box = erstelle_box(me_seite)
me_box.pack(padx=30, pady=80)

erstelle_titel(me_box, "Über mich")

erstelle_untertitel(me_box, "Kurz zu mir")
erstelle_text(me_box, """Ich bin ein offener und wissbegieriger Mensch, der gerne Neues entdeckt und sich für unterschiedliche Themen begeistert. In meiner Freizeit verbringe ich am liebsten Zeit mit Freunden - besonders beim Volleyball oder einem gemeinsamen Spieleabend.""")

erstelle_untertitel(me_box, "Was ich gerne mache")
erstelle_text(me_box, """Neben der IT sind Videospiele ein großes Hobby von mir, besonders Spiele von Riot Games. Außerdem lese ich gerne Romance-Romane und Bücher, die zum Nachdenken anregen. Ich liebe Anime und genieße sowohl aktive Tage mit Freunden als auch ruhige Abende mit einem guten Buch.""")

erstelle_untertitel(me_box, "Fun Facts")
erstelle_text(me_box, """⚡Riesiger Potterhead - Harry Potter gehört definitiv zu meinen Favoriten.\n\n ♡ Ich liebe Hello Kitty - auch wenn man es mir vielleicht nicht sofort ansieht.\n\n ᓚᘏᗢ Ich habe eine süße Katze - die allerdings überzeugt davon ist, dass sie das Sagen hat.\n\n ❀ Ich sammle gerne Pflanzen - mein grüner Daumen hat allerdings noch etwas Luft nach oben.""")

create_zrk_button(me_box, zurueck_auswahl_me)

# ---MEINE STÄRKEN---
staerken_seite = tk.Frame(fenster)
staerken_seite.configure(bg=HINTERGRUND)

staerken_box = erstelle_box(staerken_seite)
staerken_box.pack(fill="both", expand=True, padx=40, pady=20)

erstelle_titel(staerken_box, "Meine Stärken")

# BLOCK 1
erstelle_untertitel(staerken_box, "Neugier & Lernbereitschaft")
st_text1 = erstelle_text(staerken_box, """Ich bin neugierig und lösungsorientiert. Ich möchte nicht nur wissen, dass etwas funktioniert, sondern warum.
• Hohe Motivation beim Einarbeiten in neue IT-Themen
• Tiefes Verständnis statt oberflächlichem Wissen""")
st_text1.pack_forget()
st_button1 = umschalten_button(staerken_box, funktion=lambda: umschalten_details(st_text1, st_button1))
st_button1.pack(anchor="w", padx=20, pady=(0, 2))

# BLOCK 2
erstelle_untertitel(staerken_box, "Problemlösung")
st_text2 = erstelle_text(staerken_box, """Komplexe Herausforderungen schrecken mich nicht ab. Beim Programmieren schätze ich die systematische Fehlersuche.
• Spaß am Analysieren und Beheben von Code-Fehlern
• Ausdauer und Zielstrebigkeit bis zur funktionierenden Lösung""")
st_text2.pack_forget()
st_button2 = umschalten_button(staerken_box, funktion=lambda: umschalten_details(st_text2, st_button2))
st_button2.pack(anchor="w", padx=20, pady=(0, 2))

# BLOCK 3
erstelle_untertitel(staerken_box, "Selbstständigkeit & Teamarbeit")
st_text3 = erstelle_text(staerken_box, """Ich arbeite fokussiert und eigenständig, schätze aber ebenso den aktiven Austausch im Team.
• Hohe Eigenverantwortung bei der Aufgabenbewältigung
• Freude am gemeinsamen Erarbeiten von Lösungen""")
st_text3.pack_forget()
st_button3 = umschalten_button(staerken_box, funktion=lambda: umschalten_details(st_text3, st_button3))
st_button3.pack(anchor="w", padx=20, pady=(0, 2))

# BLOCK 4
erstelle_untertitel(staerken_box, "Sorgfalt & Zuverlässigkeit")
st_txt4 = erstelle_text(staerken_box, """Aufgaben erledige ich gewissenhaft. Mir ist wichtig, Themen tiefgehend zu verstehen.
• Genaues Vorgehen und Geduld bei der Umsetzung
• Verlässliche und strukturierte Arbeitsweise""")
st_txt4.pack_forget()
st_btn4 = umschalten_button(staerken_box, funktion=lambda: umschalten_details(st_txt4, st_btn4))
st_btn4.pack(anchor="w", padx=20, pady=(0, 2))

create_zrk_button(staerken_box, zurueck_zu_auswahl)


# ---WARUM IT---
warum_it_seite = tk.Frame(fenster)
warum_it_seite.configure(bg=HINTERGRUND)

it_box = erstelle_box(warum_it_seite)
it_box.pack(fill="both", expand=True, padx=40, pady=20)

erstelle_titel(it_box, "Warum IT?")

# BLOCK 1
erstelle_untertitel(it_box, "Wie mein Interesse entstanden ist")
it_txt1 = erstelle_text(it_box, """Vor ungefähr sechs Jahren habe ich meinen ersten eigenen PC bekommen und angefangen, regelmäßig Computerspiele zu spielen. Dabei sind mit der Zeit immer mehr Fragen entstanden: Wie funktioniert das eigentlich alles? Was passiert im Hintergrund und wie können so viele verschiedene Dinge zusammenspielen? Ich fand es faszinierend und wollte nicht nur den PC und die Spiele benutzen, sondern immer mehr darüber verstehen.Gleichzeitig entstand der Wunsch, kleinere Probleme irgendwann auch selbst lösen zu können.""")
it_txt1.pack_forget()
it_btn1 = umschalten_button(it_box, funktion=lambda: umschalten_details(it_txt1, it_btn1))
it_btn1.pack(anchor="w", padx=20, pady=(0, 10))

# BLOCK 2
erstelle_untertitel(it_box, "Vom Interesse zur Begeisterung")
it_txt2 = erstelle_text(it_box, """Mein Interesse an IT ist durch mein Umfeld und meine Neugier entstanden. Je mehr ich mit Technik in Berührung kam, desto mehr wollte ich verstehen, wie Systeme funktionieren. Deshalb begann ich, mir die Grundlagen der IT und das Programmieren selbst beizubringen.\n\nHeute begeistert mich besonders die Vielfalt der IT. Neben dem Programmieren interessiert mich vor allem die IT-Sicherheit und die Frage, wie Systeme geschützt und Risiken im Internet erkannt werden.""")
it_txt2.pack_forget()
it_btn2 = umschalten_button(it_box, funktion=lambda: umschalten_details(it_txt2, it_btn2))
it_btn2.pack(anchor="w", padx=20, pady=(0, 10))

# BLOCK 3
erstelle_untertitel(it_box, "IT als berufliche Zukunft")
it_txt3 = erstelle_text(it_box, """Aus meinem ursprünglichen Interesse ist deshalb der Wunsch entstanden, IT zu meinem Beruf zu machen. Ich möchte mein bisher selbstständig erarbeitetes Wissen weiter vertiefen und die Möglichkeit bekommen, noch viel mehr über IT zu lernen und praktische Erfahrungen zu sammeln.\nFür mich ist eine Ausbildung in der IT der nächste Schritt, um aus meinem Interesse einen beruflichen Weg zu machen.""")
it_txt3.pack_forget()
it_btn3 = umschalten_button(it_box, funktion=lambda: umschalten_details(it_txt3, it_btn3))
it_btn3.pack(anchor="w", padx=20, pady=(0, 10))

create_zrk_button(it_box, zurueck_zu_auswahl_warum_it)


# ---WAS ICH MITBRINGE---
mitbringen_seite = tk.Frame(fenster)
mitbringen_seite.configure(bg=HINTERGRUND)

mitbringen_box = erstelle_box(mitbringen_seite)
mitbringen_box.pack(fill="both", expand=True, padx=20, pady=50)

erstelle_titel(mitbringen_box, "Was ich mitbringe")

# BLOCK 1
erstelle_untertitel(mitbringen_box, "Berufserfahrung")
mb_txt1 = erstelle_text(mitbringen_box, """Durch meine Tätigkeit bei Boba im Fischapark konnte ich viel Erfahrung im Kundenkontakt und im Arbeiten unter Zeitdruck sammeln. Ich habe gelernt, auch in stressigen Situationen den Überblick zu behalten, Probleme lösungsorientiert anzugehen und sowohl selbstständig als auch im Team zu arbeiten. Zusätzlich musste ich immer wieder Neues lernen, war bei den Arbeitszeiten flexibel und hatte ebenfalls schon die Aufgabe, die Einschulung neuer Mitarbeiter zu übernehmen.""")
mb_txt1.pack_forget()
mb_btn1 = umschalten_button(mitbringen_box, funktion=lambda: umschalten_details(mb_txt1, mb_btn1))
mb_btn1.pack(anchor="w", padx=20, pady=(0, 10))

# BLOCK 2
erstelle_untertitel(mitbringen_box, "IT-Kenntnisse")
mb_txt2 = erstelle_text(mitbringen_box, """Meine IT-Kenntnisse habe ich mir größtenteils selbstständig angeeignet. Dabei habe ich mich mit den Grundlagen von Hardware sowie dem Binär-, Hexadezimal- und ASCII-System beschäftigt. Außerdem lerne ich derzeit die Programmiersprache Python und erweitere meine Programmierkenntnisse kontinuierlich durch praktische Übungen und eigene Projekte. Zusätzlich habe ich erste Einblicke in die Grundlagen der IT-Sicherheit gewonnen.""")
mb_txt2.pack_forget()
mb_btn2 = umschalten_button(mitbringen_box, funktion=lambda: umschalten_details(mb_txt2, mb_btn2))
mb_btn2.pack(anchor="w", padx=20, pady=(0, 10))

# BLOCK 3
erstelle_untertitel(mitbringen_box, "Umsetzungsvermögen")
mb_txt3 = erstelle_text(mitbringen_box, """Um meine Python-Kenntnisse praktisch anzuwenden, habe ich bereits verschiedene kleine Programme und Übungen umgesetzt, darunter einen Taschenrechner und weitere kleine Anwendungen. Außerdem habe ich diese interaktive Bewerbung mit Python und Tkinter umgesetzt und dabei meine bisherigen Kenntnisse praktisch angewendet und weiter vertieft.""")
mb_txt3.pack_forget()
mb_btn3 = umschalten_button(mitbringen_box, funktion=lambda: umschalten_details(mb_txt3, mb_btn3))
mb_btn3.pack(anchor="w", padx=20, pady=(0, 10))

create_zrk_button(mitbringen_box, zurueck_zu_auswahl_mitbringen)

# ---DANKESEITE---
dankeseite = tk.Frame(fenster)
dankeseite.configure(bg=HINTERGRUND)

dankeseite_box = erstelle_box(dankeseite)
dankeseite_box.pack(padx=80, pady=120, ipady=30)

erstelle_titel(dankeseite_box, "Danke für Ihre Zeit!")
mein_txt1 = erstelle_text(dankeseite_box, """Ich hoffe, ich konnte Sie von mir überzeugen und Ihnen einen persönlichen Einblick in meine Motivation und meinen Einstieg in die IT geben.\n\nIch freue mich darauf, Sie persönlich kennenzulernen und Sie in einem Gespräch von meiner Motivation zu überzeugen.""")
mein_txt1.config(wraplength=500, justify="center", pady=15)
create_zrk_button(dankeseite_box, zurueck_auswahl)

button_rahmen = tk.Frame(dankeseite_box, bg=KARTEN)
button_rahmen.pack(pady=15)

kontakt_button = create_scnd_button(button_rahmen, "Kontakt aufnehmen :)", kontakt_popup, 12, p_x=20, p_y=10)
kontakt_button.config(width=18)
kontakt_button.pack(side="left", pady=10, padx=(5,10))

beenden_button = create_scnd_button(button_rahmen, "Beenden", beenden_gag, 12, p_x=20, p_y=10)
beenden_button.config(width=18)
beenden_button.pack(side="left", pady=10, padx=(5,10))

# ---MAINLOOP---
fenster.mainloop()