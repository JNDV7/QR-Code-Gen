import qrcode
import tkinter
from tkinter import messagebox


# def de la fonction pour crée le QR Code
def MakeQRcode():
    QRcode = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    QRcode.add_data(lien.get())
    QRcode.make(fit=True)
    QRcode = QRcode.make_image(fill_color=liste_variable.get(), back_color=liste_variable_fond.get())
    if liste_variable_fond.get() == liste_variable.get():
        messagebox.showerror(title="Erreur couleur", message="Veuillez ne pas chosir la même couleur pour le QR Code et le fond !")
        return;
    elif nom.get() == "":
        messagebox.showerror(title="Nom manquant" , message="Veuillez entré un nom de fichier pour votre QRcode !")
        return;
    elif lien.get() == "":
        messagebox.showerror(title="Lien manquant" , message="Veuillez entré un lien pour votre QRcode !")
        return;
    QRcode.save("C:/Users/Heiden/Desktop/" + nom.get() + ".png")
    messagebox.showinfo(title="QRcode crée", message=f"Votre QR Code a bien été generé et placer sur votre bureau au nom de : {nom.get()}")

# Création de l'app avec ces valeurs
app = tkinter.Tk()
app.title("QRcode Generator")
app.geometry("720x480")
app.resizable(width=False, height=False)
app.iconbitmap("icon.ico")

C = tkinter.Canvas(app, background="blue", height=250, width=300)
filename = tkinter.PhotoImage(file="image_fond.gif")
background_label = tkinter.Label(app, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# placement des labels et des entrys
label_lien = tkinter.Label(text="Lien : ", background="#000000", foreground="#0411A6", font="5")
label_lien.place(x=250, y=5)
lien = tkinter.Entry()
lien.place(y=5, x=300)

label_nom = tkinter.Label(text="Nom : ", background="#000000", foreground="#0411A6", font="5")
label_nom.place(x="250", y="35")
nom = tkinter.Entry()
nom.place(y=40, x=300)


# création du menu pour le choix de couleur du QR Code
liste_couleurs = [
"blue",
"white",
"red",
"black",
"yellow",
"green",
"purple",
"orange",
"brown",
"pink",
]

liste_variable = tkinter.StringVar(app)
liste_variable.set(liste_couleurs[1])

opt = tkinter.OptionMenu(app, liste_variable, *liste_couleurs)
opt.config(width=10, height=1, background="#0411A6", activebackground="#0411A6", activeforeground="#F70303")
opt.place(x=50, y=20)

label_couleurs = tkinter.Label(text="Choisissez une couleur pour le QR Code", foreground="#FFFFFF", background="#15D606")
label_couleurs.place(x=0, y=0)

# création du menu pour le choix de la couleurde fond du QR Code
liste_couleurs_fond = [
"blue",
"red",
"white",
"black",
"yellow",
"green",
"purple",
"orange",
"brown",
"pink",
]

liste_variable_fond = tkinter.StringVar(app)
liste_variable_fond.set(liste_couleurs_fond[3])

opt_fond = tkinter.OptionMenu(app, liste_variable_fond, *liste_couleurs_fond)
opt_fond.config(width=10, height=1, background="#0411A6", activebackground="#0411A6", activeforeground="#F70303")
opt_fond.place(x=530, y=20)

label_couleur_fond = tkinter.Label(text="Choisissez une couleur de fond pour le QR Code", foreground="#FFFFFF", background="#15D606")
label_couleur_fond.place(x=460, y=0)

# création du boutton de validation et placement
w = tkinter.Button(app, command=MakeQRcode, text="Créer le QRcode", background="#15D606", activebackground="#0A6303", justify="center")
w.pack(side="bottom", fill="x")

app.mainloop()