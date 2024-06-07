from tkinter import *
from tkinter import ttk
from tkinter import Scrollbar
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image
from PIL import ImageTk
from tkcalendar import DateEntry
import datetime
import bcrypt
from tkinter.ttk import Combobox
import webbrowser
import pickle
import pandas as pd
import numpy as np

username = ""
result = ""

# Fonction pour crypter un mot de passe
def crypter_mot_de_passe(mot_de_passe):
    hashed_password = bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

# Fonction pour vérifier si un mot de passe correspond au mot de passe crypté
def verifier_mot_de_passe(mot_de_passe, mot_de_passe_crypte):
    return bcrypt.checkpw(mot_de_passe.encode('utf-8'), mot_de_passe_crypte.encode('utf-8'))

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        username = ""
        self.title("Nephro medicale")
        self.geometry("1200x685+50+0")
        self.configure(bg="white")
        self.resizable(False, False)
      
        # Création des cadres pour les écrans
        self.login_screen = LoginScreen(self)
        self.register_screen = RegisterScreen(self)
        self.home_screen = HomeScreen(self,username)
        self.doctor_screen = DoctorScreen(self)
        self.patient_screen = PatientScreen(self)
        self.dconsultation_screen = DconsultationScreen(self)
        self.addPatient_screen = AddPatientScreen(self)
        self.antecedant_screen = AtcdScreen(self)
        self.traitement_screen = TraitementScreen(self)
        self.dcumentation_screen = DocumentationScreen(self)
        self.examenClinique_screen = ExamenCliniqueScreen(self)
        self.prediction_screen = PredictionScreen(self)
        self.ordonnace_screen = OrdonnaceScreen(self)
        
        # Affichage de l'écran de connexion au démarrage
        self.show_screen(self.login_screen)
        
    def show_screen(self, screen):
        # Masquer tous les écrans
        self.login_screen.pack_forget()
        self.register_screen.pack_forget()
        self.home_screen.pack_forget()
        self.doctor_screen.pack_forget()
        self.patient_screen.pack_forget()
        self.dconsultation_screen.pack_forget()
        self.addPatient_screen.pack_forget()
        self.antecedant_screen.pack_forget()      
        self.traitement_screen.pack_forget()
        self.dcumentation_screen.pack_forget()
        self.examenClinique_screen.pack_forget()
        self.prediction_screen.pack_forget()
        self.ordonnace_screen.pack_forget()
        # Afficher l'écran spécifié
        screen.pack(fill=tk.BOTH, expand=True)
        
    def show_login_screen(self):
        self.show_screen(self.login_screen)
        
    def show_register_screen(self):
        self.show_screen(self.register_screen)
        
    def show_home_screen(self):

        self.show_screen(self.home_screen)
    
    def show_patient_screen(self):
        self.show_screen(self.patient_screen)  

    def show_doctor_screen(self):
        self.show_screen(self.doctor_screen)  

    def show_dconsultation_screen(self, patient_id, patient_name, patient_firstname):
        self.show_screen(self.dconsultation_screen)  

    def show_ddconsultation_screen(self):
        self.show_screen(self.dconsultation_screen)  
    
    def show_add_patient_screen(self):
        self.show_screen(self.addPatient_screen)  

    def show_antecedant_screen(self):
        self.show_screen(self.antecedant_screen)  

    def show_traitement_screen(self):
        self.show_screen(self.traitement_screen)      

    def show_dcumentation_screen(self):
        self.show_screen(self.dcumentation_screen)   

    def show_examenClinique_screen(self):
        self.show_screen(self.examenClinique_screen)    
    
    def show_prediction_screen(self):
        self.show_screen(self.prediction_screen) 

    def show_ordonnace_screen(self):
        self.show_screen(self.ordonnace_screen)    
    
    def login(self, username, password):

        # Vérifier que les champs ne sont pas vides
        if username == '' or password == '':
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return

        # Se connecter à la base de données
        try:
            # Connexion à la base de données
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="connexionbddappli"
            )
            print("Connexion avec la base de données réussie !")

            cursor = conn.cursor()

            # Vérifier les informations d'identification dans la table "utilisateur"
            query = "SELECT * FROM utilisateur WHERE nom_utilisateur = %s AND mot_passe = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                now = datetime.datetime.now()

                # Insérer la date et l'heure du dernier login dans la table utilisateur
                query = "UPDATE utilisateur SET dernier_login = %s WHERE nom_utilisateur = %s"
                cursor.execute(query, (now, username))
                conn.commit()  # Enregistrer les modifications dans la base de données
                print(now)
                messagebox.showinfo("Succès", "Bienvenue, " + username)
                self.show_home_screen()
            else:
                # Afficher un message d'erreur
                messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")

            # Fermer la connexion à la base de données
            cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Erreur de connexion", str(error))

class LoginScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        
        self.login_screen = tk.Frame(self, bg="white")
        self.login_screen.pack(fill=tk.BOTH, expand=True) 
        

        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/image1.jpg") 
        self.img = self.img.resize((550, 600), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        label = tk.Label(self, image=self.img, bg="white")
        label.place(x=70, y=50)


        frame = tk.Frame(self, width= 300, height= 350, bg= "#ffffff")
        frame.place(x=750, y=150)


        # Créer une étiquette
        heading = Label(frame, text="Connexion", fg="#57a1f8", bg= "white", font= ("microsoft yahei ui light", 23, "bold"))
        heading.place(x= 70, y= 5)


        def on_enter(e):
            self.username_entry.delete(0, "end")  

        def on_leave(e):
            name= self.username_entry.get()
            
            if name== '':
                self.username_entry.insert(0, "Nom d'utilisateur")

        # Créer les champs de saisie
        self.username_entry = Entry(frame, width= 25, fg= "black", border= 0, bg= "white", font= ("microsoft yahei ui light", 11))
        self.username_entry.place(x=30, y= 80)
        self.username_entry.insert(0, "Nom d'utilisateur")
        self.username_entry.bind("<FocusIn>", on_enter)  
        self.username_entry.bind("<FocusOut>", on_leave)  


        Frame(frame, width= 295, height= 2, bg= "black").place(x= 25, y= 107)


        def on_enter(e):
            self.password_entry.delete(0, "end")  

        def on_leave(e):
            name= self.password_entry.get()
            
            if name== '':
                self.password_entry.insert(0, "Mot de passe")

        self.password_entry = Entry(frame, width= 25, fg= "black", border= 0, bg= "white", font= ("microsoft yahei ui light", 11), show="*")
        self.password_entry.place(x=30, y= 150)
        self.password_entry.insert(0, "Mot de passe")
        self.password_entry.bind("<FocusIn>", on_enter)  
        self.password_entry.bind("<FocusOut>", on_leave)  
        Frame(frame, width= 295, height= 2, bg= "black").place(x= 25, y= 177)


        # Créer le bouton de connexion
        button_login = Button(frame, width= 39, pady= 7, text="Se connecter", fg="white", bg= "#57a1f8", border= 0, command=self.login)
        button_login.place(x= 35, y=204)


        label = Label(frame, text="Vous ne possédez pas encore de compte ?", fg="black", bg= "white", font= ("microsoft yahei ui light", 9))
        label.place(x= 0, y= 270)

        # Créer le bouton d'inscription
        button_signup = Button(frame, width=6, text="S'inscrire", fg="#57a1f8", bg="white", border=0, cursor="hand2", command=parent.show_register_screen)
        button_signup.place(x=250, y=270)



    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.master.login(username, password)

        self.parent.home_screen.set_username(username)
        self.parent.doctor_screen.set_username(username)
        self.parent.patient_screen.set_username(username)
        self.parent.dconsultation_screen.set_username(username)
        self.parent.addPatient_screen.set_username(username)
        self.parent.antecedant_screen.set_username(username)
        self.parent.traitement_screen.set_username(username)
        self.parent.dcumentation_screen.set_username(username)
        self.parent.examenClinique_screen.set_username(username)  
        self.parent.prediction_screen.set_username(username) 
        self.parent.ordonnace_screen.set_username(username) 

        #consultation_id = self.parent.dconsultation_screen.ajout_consultation()

class RegisterScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.register_screen = tk.Frame(self, bg="white")
        self.register_screen.pack(fill=tk.BOTH, expand=True) 

        frame = Frame(self, width=350, height=750, bg="white")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Créer une étiquette
        heading = Label(frame, text="Inscription", fg="#57a1f8", bg="white", font=("microsoft yahei ui light", 23, "bold"))
        heading.grid(row=0, column=0, columnspan=2, pady=(10, 0))

        ## Créer les champs de saisie
        self.entry_nom = self.create_input_entry(frame, "Nom", 1, 0)
        Frame(frame, border= 0,width= 250, height= 2, bg= "black").place(x= 235, y= 90)

        self.entry_prenom = self.create_input_entry(frame, "Prénom", 2, 0)
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 140)

        self.entry_date_naissance_label = self.create_input_label(frame, "Date de naissance", 3, 0)
        self.entry_date_naissance = DateEntry(frame, width=38, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)
        self.entry_date_naissance.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        self.entry_sexe = self.create_input_entry(frame, "Sexe", 4, 0)
        self.entry_sexe = tk.StringVar()
        self.entry_sexe.set("M")  # Valeur par défaut
        sexe_options = ["M", "F","Autre"]
        self.entry_sexe_dropdown = tk.OptionMenu(frame, self.entry_sexe, *sexe_options)
        self.entry_sexe_dropdown.config(bg="white", borderwidth=0, width=35)
        self.entry_sexe_dropdown.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.entry_email = self.create_input_entry(frame, "Email", 5, 0)
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 275)

        self.entry_telephone = self.create_input_entry(frame, "Téléphone", 6, 0)
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 320)

        self.entry_adresse = self.create_input_entry(frame, "Adresse", 7, 0)
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 365)


        self.entry_grade = self.create_input_entry(frame, "Grade", 7, 0)
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 365)

        self.entry_username = self.create_input_entry(frame, "Nom d'utilisateur", 9, 0)
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 410)

        self.entry_password = self.create_input_entry(frame, "Mot de passe", 10, 0, show='*')
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 458)


        self.entry_confirm_password = self.create_input_entry(frame, "Confirmer le mot de passe", 11, 0, show='*')
        Frame(frame, width= 250, height= 2, bg= "black").place(x= 235, y= 500)

        # Créer le bouton d'inscription
        button_signup = Button(frame, width=39, pady=7, text="S'inscrire", fg="white", bg="#57a1f8", border=0, command=self.register)
        button_signup.grid(row=12, column=0, columnspan=2, pady=(6, 0))

        label = Label(frame, text="Je possède déjà un compte", fg="black", bg="white", font=("microsoft yahei ui light", 9))
        label.grid(row=13, column=0, columnspan=2, pady=(12, 0))

        # Créer le bouton de connexion
        button_login = Button(frame, width=10, text="Se connecter", fg="#57a1f8", bg="white", border=0, command=parent.show_login_screen)
        button_login.grid(row=14, column=0, columnspan=2, pady=(5, 0))

    def create_input_entry(self, frame, placeholder, row, column, show=None):
        label = Label(frame, text=placeholder, fg="black", bg="white", font=("microsoft yahei ui light", 11, "bold"))
        label.grid(row=row, column=column, padx=10, pady=10, sticky="w")

        entry = Entry(frame, width=20, fg="black", border=0, bg="white", font=("microsoft yahei ui light", 11), relief=SOLID)
        entry.grid(row=row, column=column+1, padx=10, pady=10, sticky="w")
        entry.insert(0, placeholder)

        entry.placeholder = placeholder 

        if show:
            entry.config(show=show)

        entry.bind("<FocusIn>", self.on_enter_entry)  
        entry.bind("<FocusOut>", self.on_leave_entry)  

        return entry
    
    def create_input_label(self, frame, text, row, column):
        label = Label(frame, text=text, fg="black", bg="white", font=("microsoft yahei ui light", 11, "bold"))
        label.grid(row=row, column=column, padx=10, pady=10, sticky="w")
        return label

    def on_leave_entry(self, event):
        entry = event.widget
        if entry.get() == "":
            entry.insert(0, entry.placeholder)


    def on_enter_entry(self, event):
        entry = event.widget
        if entry.get() == entry.placeholder:
            entry.delete(0, tk.END)

    def register(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        date_naissance = self.entry_date_naissance.get()
        sexe = self.entry_sexe.get()
        email = self.entry_email.get()
        telephone = self.entry_telephone.get()
        adresse = self.entry_adresse.get()
        #role = self.entry_role.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()




        # Crypter le mot de passe
        password_crypte = crypter_mot_de_passe(password)
        confirm_crypte = crypter_mot_de_passe(confirm_password)

        # Vérifier si tous les champs sont remplis         
        if (
            nom and prenom and date_naissance and sexe and email and telephone and adresse  
            and username and password and confirm_password
        ):
            if password == confirm_password:

                with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="connexionbddappli"
                ) as conn:
                    print("Connexion avec la base de données réussie !")

                    # Insérer l'utilisateur dans la table "utilisateur"
                    query = "INSERT INTO utilisateur (nom, prenom, sexe, date_naissance, email, telephone, adresse, role, nom_utilisateur, mot_passe, confirm_mot_passe, date_inscription, dernier_login, statut) VALUES (%s, %s, %s, %s, %s, %s, %s, 'medecin', %s, %s, %s, %s, %s, %s)"
                    date_inscription = datetime.datetime.now()
                    dernier_login = datetime.datetime.now()
                    statut = "actif"
                    role = "medecin"
                    values = (nom, prenom, sexe, date_naissance, email, telephone, adresse, username, password_crypte, confirm_crypte, date_inscription, dernier_login, statut)
                    
                    
                    with conn.cursor() as cursor:
                        cursor.execute(query, values)

                    # Récupérer l'ID de l'utilisateur inséré
                    
                    id_utilisateur = cursor.lastrowid

                    print(id_utilisateur)

                    query_medecin = "INSERT INTO medecin (id_medecin, nom, prenom, nom_utilisateur, date_naissance, email, telephone, adresse) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    values_medecin = (id_utilisateur, nom, prenom, username, date_naissance, email, telephone, adresse)
                    
                    with conn.cursor() as cursor:
                        if role == "medecin":
                            cursor.execute(query_medecin, values_medecin)

                    conn.commit()
                messagebox.showinfo("Succès", "L'utilisateur a été enregistré avec succès")

            else:
                messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")

class HomeScreen(tk.Frame):
    def __init__(self, parent, username):
        tk.Frame.__init__(self, parent)    

        self.configure(bg="#57a1f8")
        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10) 


        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)


        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')


        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)

        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)
       
        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
        
        
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)

        # Créer un widget Frame pour contenir l'image et le texte
        content_frame = tk.Frame(welcome_frame, bg="white")
        content_frame.pack(padx=10, pady=50)


        # Créer un widget Frame pour contenir le texte de bienvenue
        welcome_text_frame = tk.Frame(content_frame, bg="white")
        welcome_text_frame.pack(side=tk.TOP)
      
        # Créer un widget de Bienvenue dans le cadre de bienvenue
        welcome_label1 = tk.Label(welcome_text_frame, text="Hôpital de l'EHU Oran", compound=tk.LEFT, bg="white", fg= "black", border= 0, font=("Time new roman", 20, "bold"))
        welcome_label1.pack(padx=20, pady=(20, 8))

        welcome_label2 = tk.Label(welcome_text_frame, text="Service Néphrologie", compound=tk.LEFT, bg="white", fg="gray",  border= 0, font=("Time new roman", 15, "italic"))
        welcome_label2.pack(padx=20, pady=(20, 8))

        # Charger l'image
        image = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/doctor1.jpg")
        # Redimensionner l'image si nécessaire
        image = image.resize((600, 350))
        # Convertir l'image en un format compatible avec Tkinter
        self.photo = ImageTk.PhotoImage(image)

        # Créer un widget Label pour afficher l'image dans le cadre
        image_label = tk.Label(content_frame, image=self.photo, bg="white")
        image_label.pack(side=tk.LEFT, padx=10, pady=10)

        

    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
    
    def set_username(self, username):
        self.username_label.config(text= username)

class DoctorScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=5) 

        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)

        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)

        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_home_screen)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)

        
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        #
        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)

        ########################################################################################

        spacer_label = tk.Label(welcome_frame, bg="white")
        spacer_label.pack(pady=5)


        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')
          
        # Création des libellés et des champs de saisie

        nom_label = tk.Label(welcome_frame, text="Nom :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        nom_label.pack(pady=1)
        self.nom_entry = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.nom_entry.pack(pady=1)

        prenom_label = tk.Label(welcome_frame, text="Prénom : ", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        prenom_label.pack(pady=1)
        self.prenom_entry = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.prenom_entry.pack(pady=1)

        sexe_label = tk.Label(welcome_frame, text="Sexe : ", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        sexe_label.pack(pady=1)
        self.sexe_var = tk.StringVar(welcome_frame)
        
        self.sexe_var.set("")  # Sélectionnez une valeur par défaut
        sexe_options = ["M", "F", "Autre"]
        self.sexe_entry = tk.OptionMenu(welcome_frame, self.sexe_var, *sexe_options)
        self.sexe_entry.config(bg="white", borderwidth=0, width=38)
        self.sexe_entry.pack(pady=1)

        date_naissance_label = tk.Label(welcome_frame, text="Date de Naissance :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        date_naissance_label.pack(pady=1)
        self.date_naissance_entry = DateEntry(welcome_frame, width=40, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)
        self.date_naissance_entry.pack(pady=5)

        email_label = tk.Label(welcome_frame, text="Email :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        email_label.pack(pady=1)
        self.email_entry = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.email_entry.pack(pady=1)

        telephone_label = tk.Label(welcome_frame, text="Téléphone :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        telephone_label.pack(pady=1)
        self.telephone_entry = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.telephone_entry.pack(pady=1)

        adresse_label = tk.Label(welcome_frame, text="Adresse :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        adresse_label.pack(pady=1)
        self.adresse_entry = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.adresse_entry.pack(pady=1)

        grade_label = tk.Label(welcome_frame, text="Grade :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        grade_label.pack(pady=1)
        self.grade_var = tk.StringVar(welcome_frame)
        grade_options = ["médecin généraliste", "résident(e)", "médecin spécialiste", "maître assistant(e)"]
        self.grade_entry = tk.OptionMenu(welcome_frame, self.grade_var, *grade_options)
        self.grade_entry.config(bg="white", borderwidth=0, width=40)
        self.grade_entry.pack(pady=1)

        unite_label = tk.Label(welcome_frame, text="Unité :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        unite_label.pack(pady=1)
        self.unite_var = tk.StringVar(welcome_frame)
        unite_options = ["consultation", "greffe rénale", "hémodialyse"]
        self.unite_entry = tk.OptionMenu(welcome_frame, self.unite_var, *unite_options)
        self.unite_entry.config(bg="white", borderwidth=0, width=40)
        self.unite_entry.pack(pady=1)

        specialite_label = tk.Label(welcome_frame, text="Spécialité :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        specialite_label.pack(pady=1)
        self.specialite_entry = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.specialite_entry.pack(pady=1)

        # Création du conteneur pour les boutons

        button_container = tk.Frame(welcome_frame, bg="white")
        button_container.pack(pady=10)

        #Bouton pour effacer les champs
        clear_button = tk.Button(button_container, width=10, text="Clear", fg="white", bg="#ff0000", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.clear_data)   
        clear_button.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour afficher les informations du medecin
        bouton_information = tk.Button(button_container, text="Remplir", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.get_medecin_information)
        bouton_information.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour sauvegarder les informations de la modification
        bouton_sauvegarder = tk.Button(button_container, text="Sauvegarder", fg="white", bg="#32CD32", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.save_medecin_informations)
        bouton_sauvegarder.pack(side=tk.LEFT, padx=5, pady=10)



    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
        self.username_label = Label(self, text="Nom d'utilisateur : " + username)
        self.username_label.pack()

    def clear_data(self):

        self.nom_entry.delete(0,END)
        self.prenom_entry.delete(0,END)
        self.telephone_entry.delete(0,END)
        self.adresse_entry.delete(0,END)
        self.date_naissance_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.specialite_entry.delete(0,END)

        self.sexe_var.set("")
        self.grade_var.set("")              
        self.unite_var.set("")

    def set_username(self, username):
        self.username_label.config(text= username)   

    def get_medecin_information(self):
        # Établir une connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )

        # Créer un curseur pour exécuter les requêtes
        cursor = conn.cursor()

        try:
            # Récupérer les informations du médecin
            username_medecin = self.username_label.cget("text")

            print(username_medecin)
            #query = "SELECT * FROM utilisateur WHERE nom_utilisateur = %s "
            query = """
            SELECT m.id_medecin, m.nom, m.prenom, m.sexe, m.date_naissance, m.email, m.nom_utilisateur, m.mot_de_passe,
            m.telephone, m.adresse, m.id_grade,  g.nom_grade, m.id_unite, un.nom_unite, m.id_specialite, s.nom_specialite
            FROM medecin m
            INNER JOIN utilisateur u ON m.id_medecin = u.id_utilisateur
            INNER JOIN grade g ON m.id_grade = g.id_grade
            INNER JOIN unite un ON m.id_unite = un.id_unite
            INNER JOIN specialite s ON m.id_specialite = s.id_specialite
            WHERE u.nom_utilisateur = %s
            """

            cursor.execute(query, (username_medecin, ))
            result = cursor.fetchone()

            if result:
                # Récupérer les informations de l'utilisateur
                id_medecin = result[0]
                nom = result[1]
                prenom = result[2]
                sexe = result[3]
                date_naissance = result[4]
                email = result[5]
                nom_user = result[6]
                mot_de_passe = result[7]
                telephone = result[8]
                adresse = result[9]
                id_grade = result[10]
                grade = result[11]
                id_unite = result[12]
                unite = result[13]
                id_specialite = result[14]
                specialite = result[15]


                print(sexe)

                # Afficher les informations de l'utilisateur dans les champs correspondants
                self.nom_entry.delete(0, tk.END)
                self.nom_entry.insert(tk.END, nom)

                self.prenom_entry.delete(0, tk.END)
                self.prenom_entry.insert(tk.END, prenom)

                self.sexe_var.set(sexe)
                
                self.date_naissance_entry.delete(0, tk.END)
                self.date_naissance_entry.insert(tk.END, date_naissance)

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(tk.END, email)

                self.telephone_entry.delete(0, tk.END)
                self.telephone_entry.insert(tk.END, telephone)

                self.adresse_entry.delete(0, tk.END)
                self.adresse_entry.insert(tk.END, adresse)

                self.grade_var.set(grade)

                self.unite_var.set(unite)

                self.specialite_entry.delete(0, tk.END)
                self.specialite_entry.insert(tk.END, specialite)



                print("Informations du médecin affichées avec succès")
            else:
                print("Utilisateur introuvable.")
        except mysql.connector.Error as error:
            print("Erreur lors de la récupération des informations du médecin:", error)
        finally:
            # Fermer le curseur et la connexion à la base de données
            cursor.close()
            conn.close()

    def save_medecin_informations(self):
        # Récupérer les valeurs des champs
        username = self.username_label.cget("text")
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        sexe = self.sexe_var.get()
        date_naissance_not_convert = self.date_naissance_entry.get()
        email = self.email_entry.get()
        telephone = self.telephone_entry.get()
        adresse = self.adresse_entry.get()

        # Convertir la date de naissance en objet datetime
        date_naissance = datetime.datetime.strptime(date_naissance_not_convert, "%Y-%m-%d").date()
        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        grade = self.grade_var.get()
        unite = self.unite_var.get()
        specialite = self.specialite_entry.get()


        # Récupérer les ID correspondants aux valeurs sélectionnées
        medecin_id = self.get_medecin_id(self.username_label.cget("text"))
        grade_id = self.get_grade_id(self.grade_var.get())
        unite_id = self.get_unite_id(self.unite_var.get())
        specialite_id = self.get_specialite_id(self.specialite_entry.get())

        print(unite)

        sql = "UPDATE medecin SET nom=%s, prenom=%s, sexe=%s, date_naissance=%s, email=%s, telephone=%s, adresse=%s, id_grade=%s, id_unite=%s, id_specialite=%s WHERE id_medecin=%s"
        values = (nom, prenom, sexe, date_naissance, email, telephone, adresse, grade_id, unite_id, specialite_id, medecin_id)
        cursor.execute(sql, values)

        # Valider la transaction
        conn.commit()
        messagebox.showinfo("Succès", "Modification effectuer !")
        cursor.close()
        conn.close()

    def get_medecin_id(self, username_name):
        # Récupérer l'ID du medecin à partir de la base de données
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="connexionbddappli"
        )
        cursor = conn.cursor()

        sql = "SELECT id_medecin FROM medecin WHERE nom_utilisateur = %s"
        values = (username_name,)
        cursor.execute(sql, values)

        medecin_id = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return medecin_id

    def get_grade_id(self, grade_name):
        # Récupérer l'ID du grade à partir de la base de données
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="connexionbddappli"
        )
        cursor = conn.cursor()

        sql = "SELECT id_grade FROM grade WHERE nom_grade = %s"
        values = (grade_name,)
        cursor.execute(sql, values)

        grade_id = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return grade_id

    def get_unite_id(self, unite_name):
        # Récupérer l'ID de l'unité à partir de la base de données
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="connexionbddappli"
     )
        cursor = conn.cursor()

        sql = "SELECT id_unite FROM unite WHERE nom_unite = %s"
        values = (unite_name,)
        cursor.execute(sql, values)

        unite_id = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return unite_id

    def get_specialite_id(self, specialite_name):
        # Récupérer l'ID de la spécialité à partir de la base de données
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="connexionbddappli"
        )
        cursor = conn.cursor()

        sql = "SELECT id_specialite FROM specialite WHERE nom_specialite = %s"
        values = (specialite_name,)
        cursor.execute(sql, values)

        specialite_id = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return specialite_id

class PatientScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)    
        self.parent = parent
        
        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=5) 

        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)

        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')
        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_home_screen)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
        
        
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)


       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        #
        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)

        #########################################################################################################################
        
        container = tk.Frame(welcome_frame, bg="white")
        container.pack()
        # Création du bouton pour ajouter le patient


        
        def on_entry_focus(event):
            if self.label_rechercher.get() == "Veuillez saisir par le nom ou prénom du patient":
                self.label_rechercher.delete(0, tk.END)
        
        def on_entry_leave(event):
            if self.label_rechercher.get() == "":
                self.label_rechercher.insert(0, "Veuillez saisir par le nom ou prénom du patient")



        button_container1 = tk.Frame(welcome_frame, bg="white")
        button_container1.pack(padx=10, pady=100)


        self.label_rechercher = tk.Entry(button_container1, width=80, text="Rechercher",font= ("Time new roman", 11, "italic"))
        self.label_rechercher.insert(0, "Veuillez saisir par le nom ou prénom ")
        self.label_rechercher.bind("<FocusIn>", on_entry_focus)
        self.label_rechercher.bind("<FocusOut>", on_entry_leave)
        self.label_rechercher.pack(side=tk.LEFT, padx=10)


        button_rechercher = tk.Button(button_container1, width=10, text="Rechercher", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.chercher_patient)
        button_rechercher.pack(side=tk.LEFT, padx=10)

        button_actualiser = tk.Button(button_container1, width=10,text="Actualiser",  fg="white", bg ="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.load_all_data)
        button_actualiser.pack(side=tk.LEFT, padx=5)

        # Création du Treeview pour afficher les données des patients
        frame_liste = Frame(welcome_frame, bg="white")
        frame_liste.pack()
        self.treeview = ttk.Treeview(frame_liste, columns=("id", "Nom", "Prénom", "Sexe", "Date de Naissance", "Email", "Téléphone", "Adresse", "Groupe Sanguin", "Profession", "Situation Familiale"), height=15)
        
        # Créer la barre de défilement
        scrollbar = Scrollbar(frame_liste, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("id", width=35)
        self.treeview.column("Nom", width=100)
        self.treeview.column("Prénom", width=100)
        self.treeview.column("Sexe", width=50)
        self.treeview.column("Date de Naissance", width=110)
        self.treeview.column("Email", width=50)
        self.treeview.column("Téléphone", width=70)
        self.treeview.column("Adresse", width=105)
        self.treeview.column("Groupe Sanguin", width=100)
        self.treeview.column("Profession", width=100)
        self.treeview.column("Situation Familiale", width=100)

        self.treeview.heading("#0", text="", anchor="center")
        self.treeview.heading("id", text="ID")
        self.treeview.heading("Nom", text="Nom")
        self.treeview.heading("Prénom", text="Prénom")
        self.treeview.heading("Sexe", text="Sexe")
        self.treeview.heading("Date de Naissance", text="Date de Naissance")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Téléphone", text="Téléphone")
        self.treeview.heading("Adresse", text="Adresse")
        self.treeview.heading("Groupe Sanguin", text="Groupe Sanguin")
        self.treeview.heading("Profession", text="Profession")
        self.treeview.heading("Situation Familiale", text="Situation Familiale")

        # Placer le treeview en bas

        self.treeview.pack(padx=1, pady=5)

        button_container = tk.Frame(welcome_frame, bg="white")
        button_container.pack()
        
        button_ajouter = tk.Button(button_container, width=13, text="Ajouter Patient", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=parent.show_add_patient_screen)
        button_ajouter.pack(side=tk.LEFT, padx=5, pady=15)

                
        button_info= tk.Button(button_container, width=20, text="Information Patient", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= self.infoPatient)
        button_info.pack(side=tk.LEFT, padx=5, pady=15)

        button_modifier = tk.Button(button_container, width=13, text="Modifier Patient", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.modifierPatient)
        button_modifier.pack(side=tk.LEFT, padx=5, pady=15)

        button_dconsultation = tk.Button(button_container, width=15, text="Détail consultation", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.open_consultation_details)
        button_dconsultation.pack(side=tk.LEFT, padx=5, pady=15)
       
        # Charger les données des patients au démarrage
        self.load_all_data()

        # Ajouter une ligne vide pour l'espacement
        self.rowconfigure(1, minsize=10) 

        #Selectionner un element du tableau patient 
        self.treeview.bind("<<TreeviewSelect>>")  
    def on_select(self, event):
        # Cette fonction est appelée lorsqu'un élément est sélectionné dans le Treeview
        selected_item = self.treeview.focus()
        if selected_item:
            item_data = self.treeview.item(selected_item)
            values = item_data["values"]
        if values:
            self.entry_nom.delete(0, tk.END)
            self.entry_nom.insert(0, values[1])
            self.entry_prenom.delete(0, tk.END)
            self.entry_prenom.insert(0, values[2])

            #self.optionmenu_sexe.set(values[3])
            #self.date_naissance_entry.delete(0, tk.END)
            #self.date_naissance_entry.insert(0, values[4])
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, values[5])
            self.entry_telephone.delete(0, tk.END)
            self.entry_telephone.insert(0, values[6])
            self.entry_adresse.delete(0, tk.END)
            self.entry_adresse.insert(0, values[7])
            #self.optionmenu_groupe_sanguin.set(values[8])
            self.entry_profession.delete(0, tk.END)
            self.entry_profession.insert(0, values[9])
    def load_all_data(self):
        # Supprimer toutes les lignes existantes dans le Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Se connecter à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        # Exécuter une requête SQL pour récupérer tous les patients
        query = "SELECT id_patient, nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale FROM patient"
        cursor.execute(query)

        # Récupérer les résultats de la requête
        results = cursor.fetchall()


        # Parcourir les résultats et les ajouter au Treeview
        for result in results:
            id_patient, nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale = result
            print(nom)
            self.treeview.insert("", "end", values=(id_patient,nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale))

        # Fermer le curseur et la connexion à la base de données
        cursor.close()
        conn.close()
    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()
    def set_username(self, username):
        self.username_label.config(text= username)   
    def chercher_patient(self):
        # Se connecter à la base de données

        self.treeview.delete(*self.treeview.get_children())

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        # Créer un curseur pour exécuter des requêtes SQL
        cursor = mydb.cursor()

        # Exécuter une requête SQL pour rechercher le patient
        champs_rechercher = self.label_rechercher.get()

           # Vérifier si le champ de recherche est vide
        if champs_rechercher == "":
             messagebox.showerror("Erreur", "Veuillez saisir dans le champs !")
             return
        
        query = "SELECT * FROM patient WHERE nom LIKE %s OR prenom LIKE %s"
        param = (f"%{champs_rechercher}%", f"%{champs_rechercher}%")


        # Exécuter la requête SQL
        cursor.execute(query, param)

        # Récupérer les résultats de la requête
        results = cursor.fetchall()


        # Afficher les résultats dans le TreeView
        if results:
            for result in results:
                self.treeview.insert("", "end", values=result)
        else:
            # Afficher un message indiquant l'absence de résultats
            messagebox.showerror("Erreur", "Patient introuvable.")

        # Fermer le curseur et la connexion à la base de données
        cursor.close()
        mydb.close()       
    def open_consultation_details(self):
        # Récupérer l'élément sélectionné dans le Treeview
        selected_item = self.treeview.focus()

        id_medecin  =  self.get_medecin_id(self.username_label.cget("text"))

        if selected_item:
            # Obtenir les données du patient sélectionné
            patient_data = self.treeview.item(selected_item)

            # Vérifier si les valeurs sont présentes et s'assurer qu'il y a suffisamment d'éléments
            if "values" in patient_data and len(patient_data["values"]) >= 3:
                patient_id = patient_data["values"][0]
                patient_name = patient_data["values"][1]
                patient_firstname = patient_data["values"][2]

                # Récupérer l'ID d'orientation à partir de l'ID du patient
                orientation_id = self.get_orientation_id(patient_id)


                #print(orientation_id)

                # Afficher les informations du patient dans l'écran "dconsultation_screen"
                self.parent.dconsultation_screen.display_patient_info(patient_id, patient_name, patient_firstname,id_medecin,orientation_id)
                self.parent.dconsultation_screen.affiche_historique_consultation()
                # Afficher l'écran "dconsultation_screen"
                self.parent.show_dconsultation_screen(patient_id, patient_name, patient_firstname)
            else:
                print("Les données du patient sont incomplètes.")
        else:
            print("Aucun patient sélectionné.")
    def get_orientation_id(self, id_patient):
        # Établir une connexion à la base de données
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        # Créer un curseur pour exécuter des requêtes
        cursor = connection.cursor()

        # Exécuter la requête SQL pour récupérer l'id_orientation
        query = "SELECT id_orientation FROM orientation WHERE id_patient = %s"
        cursor.execute(query, (id_patient,))

        # Récupérer le résultat de la requête
        result = cursor.fetchone()

        # Fermer le curseur et la connexion à la base de données
        cursor.close()
        connection.close()

        # Vérifier si un résultat a été obtenu et renvoyer l'id_orientation correspondant
        if result:
            orientation_id = result[0]
            return orientation_id
        else:
            return None    
    def get_medecin_id(self, username_name):
        # Récupérer l'ID du medecin à partir de la base de données
        #username  = self.username_label.cget("text")

        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="connexionbddappli"
        )
        cursor = conn.cursor()

        sql = "SELECT id_medecin FROM medecin WHERE nom_utilisateur = %s"
        values = (username_name ,)
        cursor.execute(sql, values)

        medecin_id = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return medecin_id
    def infoPatient(self):
        # Récupérer l'élément sélectionné dans le Treeview
        selected_item = self.treeview.focus()

        if selected_item:
            # Obtenir les données du patient sélectionné
            patient_data = self.treeview.item(selected_item)

            # Vérifier si les valeurs sont présentes et s'assurer qu'il y a suffisamment d'éléments
            if "values" in patient_data and len(patient_data["values"]) >= 3:
                patient_id = patient_data["values"][0]
                patient_name = patient_data["values"][1]
                patient_firstname = patient_data["values"][2]


        # Récuprer les informations personnelles du patient 

        # Création de la fenêtre principale
        top_level = tk.Toplevel()
        top_level.configure(background="white")
        
        # Création d'un Notebook avec un style personnalisé
        style = ttk.Style()
        style.configure("Custom.TNotebook.Tab", foreground="#57a1f8", background="white", font=("Time new roman", 10, "bold"))

        notebook = ttk.Notebook(top_level, style="Custom.TNotebook")
        notebook.pack(pady=10, expand=True)

        # Personnalisation du style des cadres
        style = ttk.Style()
        # Changer la couleur du fond du cadre
        style.configure("Custom.TFrame", background="white")  
        # Changer la couleur du fond lorsqu'il est sélectionné
        style.map("Custom.TFrame", background=[('selected', "white")])  

        # Création des frames pour les onglets
        frame1 = ttk.Frame(notebook, width=800, height=550)
        frame2 = ttk.Frame(notebook, width=800, height=550)
        frame3 = ttk.Frame(notebook, width=800, height=550)

        # Appliquer le style personnalisé aux cadres
        frame1.configure(style="Custom.TFrame")
        frame2.configure(style="Custom.TFrame") 
        frame3.configure(style="Custom.TFrame") 

        # Ajout des frames au notebook
        notebook.add(frame1, text='Information Personelle')
        notebook.add(frame2, text='Antécedant')
        notebook.add(frame3, text='Symptome')


        #Informations personnelles du patient
        #####################################################################################

        # Création des labels pour afficher les informations du patient dans frame1
        label_id_patient = tk.Label(frame1, text="ID Patient : ", bg="white", font=("Time new roman", 12))
        label_nom = tk.Label(frame1, text="Nom : ", bg="white", font=("Time new roman", 12))
        label_prenom = tk.Label(frame1, text="Prénom : ", bg="white", font=("Time new roman", 12))
        label_sexe = tk.Label(frame1, text="Sexe : ", bg="white", font=("Time new roman", 12))
        label_date_naissance = tk.Label(frame1, text="Date de Naissance : ", bg="white", font=("Time new roman", 12))
        label_email = tk.Label(frame1, text="Email : ", bg="white", font=("Time new roman", 12))
        label_telephone = tk.Label(frame1, text="Téléphone : ", bg="white", font=("Time new roman", 12))
        label_adresse = tk.Label(frame1, text="Adresse : ", bg="white", font=("Time new roman", 12))
        label_groupe_sanguin = tk.Label(frame1, text="Groupe Sanguin : ", bg="white", font=("Time new roman", 12))
        label_profession = tk.Label(frame1, text="Profession : ", bg="white", font=("Time new roman", 12))
        label_situation_familiale = tk.Label(frame1, text="Situation Familiale : ", bg="white", font=("Time new roman", 12))

        # Placement des labels
        label_id_patient.pack(anchor="w", padx=10, pady=5)
        label_nom.pack(anchor="w", padx=10, pady=5)
        label_prenom.pack(anchor="w", padx=10, pady=5)
        label_sexe.pack(anchor="w", padx=10, pady=5)
        label_date_naissance.pack(anchor="w", padx=10, pady=5)
        label_email.pack(anchor="w", padx=10, pady=5)
        label_telephone.pack(anchor="w", padx=10, pady=5)
        label_adresse.pack(anchor="w", padx=10, pady=5)
        label_groupe_sanguin.pack(anchor="w", padx=10, pady=5)
        label_profession.pack(anchor="w", padx=10, pady=5)
        label_situation_familiale.pack(anchor="w", padx=10, pady=5)

         # Se connecter à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        query = """
            SELECT *
            FROM patient
            WHERE id_patient = %s
            """  
        
        cursor.execute(query, (patient_id,))

        # Récupérer les résultats de la requête
        results = cursor.fetchall()
        
        for result in results:

            id_patient, nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale = result

        label_id_patient.config(text="ID Patient : " + str(id_patient))
        label_nom.config(text="Nom : " + nom)
        label_prenom.config(text="Prénom : " + prenom)
        label_sexe.config(text="Sexe : " + sexe)
        label_date_naissance.config(text="Date de Naissance : " + str(date_naissance))
        label_email.config(text="Email : " + email)
        label_telephone.config(text="Téléphone : " + str(telephone))
        label_adresse.config(text="Adresse : " + adresse)
        label_groupe_sanguin.config(text="Groupe Sanguin : " + groupe_sanguin)
        label_profession.config(text="Profession : " + profession)
        label_situation_familiale.config(text="Situation Familiale : " + situation_familiale)

        cursor.close()
        conn.close()
        
        #Antécedant médicaux du patient
        #####################################################################################
        # Créer un Frame pour encapsuler le Treeview
        treeview_frame = tk.Frame(frame2)
        treeview_frame.pack(fill="both", expand=True)

        # Création des labels pour afficher les informations du patient dans frame2
        label_ant = tk.Label(frame2, text="Antécedant medicaux : ", bg="white", font=("Time new roman", 12,"bold"))
        label_ant.pack(anchor="w", padx=10, pady=5)

        treeview1_frame = tk.Frame(frame2, height=5, bg= "white")
        treeview1_frame.pack(anchor="w", padx=10)  
      
        # Créer les widgets Treeview pour afficher les antécédents
        treeview1 = ttk.Treeview(treeview1_frame, height=5)
        treeview1["columns"] = ("Nom Maladie", "Date Début", "Date Fin")

        # Label pour le deuxième Treeview
        label_chru2 = tk.Label(frame2, text="Antécédant chirurgicaux : ", bg="white", font=("Time new roman", 12, "bold"))
        label_chru2.pack(anchor="w", padx=10, pady=5)

        treeview2_frame = tk.Frame(frame2, height=5, bg= "white")
        treeview2_frame.pack(anchor="w", padx=10)  

        treeview2 = ttk.Treeview(treeview2_frame, height=5)
        treeview2["columns"] = ("Nom chirurgie", "Date Début", "Lieu")

        # Label pour le 3eme Treeview
        label_fam = tk.Label(frame2, text="Antécédant familiaux : ", bg="white", font=("Time new roman", 12, "bold"))
        label_fam.pack(anchor="w", padx=10, pady=5)

        treeview3_frame = tk.Frame(frame2, height=5, bg= "white")
        treeview3_frame.pack(anchor="w", padx=10)           

        treeview3 = ttk.Treeview(treeview3_frame, height=5)
        treeview3["columns"] = ("Nom Maladie", "Date Début", "Date Fin")

        # Ajouter des en-têtes de colonnes
        treeview1.heading("#0", text="ID")
        treeview1.heading("Nom Maladie", text="Nom Maladie")
        treeview1.heading("Date Début", text="Date Début")
        treeview1.heading("Date Fin", text="Date Fin")

        treeview1.column("#0", width=50)
        treeview1.column("Nom Maladie", width=150)
        treeview1.column("Date Début", width=150)
        treeview1.column("Date Fin", width=150)

        treeview2.heading("#0", text="ID")
        treeview2.heading("Nom chirurgie", text="Nom chirurgie")
        treeview2.heading("Date Début", text="Date Début")
        treeview2.heading("Lieu", text="Lieu")

        treeview2.column("#0", width=50)
        treeview2.column("Nom chirurgie", width=150)
        treeview2.column("Date Début", width=150)
        treeview2.column("Lieu", width=150)

        treeview3.heading("#0", text="ID")
        treeview3.heading("Nom Maladie", text="Nom Maladie")
        treeview3.heading("Date Début", text="Date Début")
        treeview3.heading("Date Fin", text="Date Fin")

        treeview3.column("#0", width=50)
        treeview3.column("Nom Maladie", width=150)
        treeview3.column("Date Début", width=150)
        treeview3.column("Date Fin", width=150)

        treeview1.pack(side="left", padx=10, pady=(5, 50), fill="both", expand=True)
        treeview2.pack(side="left", padx=10, pady=(5, 50), fill="both", expand=True)
        treeview3.pack(side="left", padx=10, pady=(5, 50), fill="both", expand=True)

        treeview_frame.pack(fill="both", expand=True)

         # Se connecter à la base de données
        conn2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor2 = conn2.cursor()

        query2 = """
            SELECT am.nom_maladie, am.date_debut, am.date_fin
            FROM consultation c
            INNER JOIN antecedentmedicaux am ON c.id_consultation = am.id_consultation
            WHERE c.id_patient = %s
            """  
        
        cursor2.execute(query2, (patient_id,))

        # Récupérer les résultats de la requête
        results2 = cursor2.fetchall()

        for i, result in enumerate(results2):

            maladie, debut, fin = result

            treeview1.insert(parent="", index="end", iid=i, text=str(i), values=(maladie, debut, fin))

        cursor2.close()
        conn2.close()

        # Se connecter à la base de données
        conn3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor3 = conn3.cursor()

        query3 = """
            SELECT am.nom_chirurgie, am.date_debut, am.lieu
            FROM consultation c
            INNER JOIN antecedentchirurgicaux am ON c.id_consultation = am.id_consultation 
            WHERE c.id_patient = %s
            """  
        
        cursor3.execute(query3, (patient_id,))

        # Récupérer les résultats de la requête
        results3 = cursor3.fetchall()

        for i, result in enumerate(results3):

            maladie, debut, lieu = result

            treeview2.insert(parent="", index="end", iid=i, text=str(i), values=(maladie, debut, lieu))

        cursor3.close()
        conn3.close()

        # Se connecter à la base de données
        conn4 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor4 = conn4.cursor()

        query4 = """
            SELECT am.nom_maladie, am.date_debut, am.date_fin
            FROM consultation c
            INNER JOIN antecedentfamiliaux am ON c.id_consultation = am.id_consultation
            WHERE c.id_patient = %s
            """  
        
        cursor4.execute(query4, (patient_id,))

        # Récupérer les résultats de la requête
        results4 = cursor4.fetchall()

        for i, result in enumerate(results4):

            maladie, debut, fin = result

            treeview3.insert(parent="", index="end", iid=i, text=str(i), values=(maladie, debut, fin))

        cursor4.close()
        conn4.close()

        # Ajouter pour chaque Treeview dans le cadre avec une barre de défilement vertical
        # Créer une barre de défilement verticale et l'associer au Treeview
        treeview_scrollbar1 = tk.Scrollbar(treeview1_frame, orient="vertical", command=treeview1.yview)
        treeview1.configure(yscrollcommand=treeview_scrollbar1.set)
        treeview_scrollbar1.pack(side="right", fill="y")

        treeview_scrollbar2 = tk.Scrollbar(treeview2_frame, orient="vertical", command=treeview2.yview)
        treeview2.configure(yscrollcommand=treeview_scrollbar2.set)
        treeview_scrollbar2.pack(side="right", fill="y")

        treeview_scrollbar3 = tk.Scrollbar(treeview3_frame, orient="vertical", command=treeview3.yview)
        treeview3.configure(yscrollcommand=treeview_scrollbar3.set)
        treeview_scrollbar3.pack(side="right", fill="y")

        #Symptome du patient
        #####################################################################################

        treeviews_frame = tk.Frame(frame3, height= 7, bg = "white")
        treeviews_frame.pack(fill="both", expand=True)

        # Création des labels pour afficher les informations des symptomes du patient dans frame3
 
        # Créer les widgets Treeview pour afficher les antécédents
        treeviews = ttk.Treeview(treeviews_frame)
        treeviews["columns"] = ("Type symptome", "Gravite", "Date")

        # Ajouter des en-têtes de colonnes
        treeviews.heading("#0", text="ID")
        treeviews.heading("Type symptome", text="Type symptome")
        treeviews.heading("Gravite", text="Gravite")
        treeviews.heading("Date", text="Date")

        treeviews.column("#0", width=50)
        treeviews.column("Type symptome", width=200)
        treeviews.column("Gravite", width=100)
        treeviews.column("Date", width=150)

        # Se connecter à la base de données
        conn5 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor5 = conn5.cursor()

        query5 = """
            SELECT ts.nom_type_symptome, g.nom_gravite_sympthome, s.date_symptome
            FROM consultation c
            INNER JOIN symptome s ON c.id_consultation = s.id_consultation  
            INNER JOIN type_symptome ts ON ts.id_type_symptome  = s.id_type_symptome
            INNER JOIN gravite_sympthome g ON g.id_gravite_sympthome = s.id_gravite_symptome
            WHERE c.id_patient = %s
            """  

        cursor5.execute(query5, (patient_id,))

        # Récupérer les résultats de la requête
        results5 = cursor5.fetchall()

        for i, result in enumerate(results5):

            symptome, gravite, date = result
            treeviews.insert(parent="", index="end", iid=i, text=str(i), values=(symptome, gravite, date))


        treeviews.pack(side="left", padx=10, pady=(5, 50), fill="both", expand=True)
        treeviews_scrollbar = tk.Scrollbar(treeviews_frame, orient="vertical", command=treeviews.yview)
        treeviews.configure(yscrollcommand=treeviews_scrollbar.set)
        treeviews_scrollbar.pack(side="right", fill="y")


        cursor5.close()
        conn5.close()

        #Récuperer la logueur et largeur de la fentre et la centrer 
        top_level.update_idletasks()
        width = top_level.winfo_width()
        height = top_level.winfo_height()

        x = (top_level.winfo_screenwidth() // 2) - (width // 2)
        y = (top_level.winfo_screenheight() // 2) - (height // 2)
        top_level.geometry(f"{width}x{height}+{x}+{y}")


        #top_level.mainloop()
    def modifierPatient(self):
         # Récupérer l'élément sélectionné dans le Treeview
        selected_item = self.treeview.focus()

        if selected_item:
            # Obtenir les données du patient sélectionné
            patient_data = self.treeview.item(selected_item)

            # Vérifier si les valeurs sont présentes et s'assurer qu'il y a suffisamment d'éléments
            if "values" in patient_data and len(patient_data["values"]) >= 3:
                patient_id = patient_data["values"][0]
                patient_name = patient_data["values"][1]
                patient_firstname = patient_data["values"][2]


        # Création de la fenêtre principale
        top_level = tk.Toplevel()
        top_level.configure(background="white")
        top_level.title("Modifier informations personnel du patient")


        # Modifier Informations personnelles du patient
        #####################################################################################

        labels = [
            "ID Patient :",
            "Nom :",
            "Prénom :",
            "Sexe :",
            "Date de Naissance :",
            "Email :",
            "Téléphone :",
            "Adresse :",
            "Groupe Sanguin :",
            "Profession :",
            "Situation Familiale :"
            ]
        # Se connecter à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        
        cursor = conn.cursor()

        query = """
            SELECT *
            FROM patient
            WHERE id_patient = %s
        """  
        
        cursor.execute(query, (patient_id,))

        # Récupérer les résultats de la requête
        results = cursor.fetchall()

        for result in results:
            id_patient, nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale = result

            for label_text in labels:
                label_frame = tk.Frame(top_level, bg="white")
                label_frame.pack(anchor="w", padx=10, pady=5)

                label = tk.Label(label_frame, text=label_text, bg="white", font=("Time new roman", 12))
                label.pack(side="left")

                if label_text == "ID Patient :":
                    id_patient_entry = tk.Entry(label_frame, text=id_patient, width=38, font=("Time new roman", 11))
                    id_patient_entry.insert(0, str(id_patient))
                    id_patient_entry.configure(state="disabled")
                    id_patient_entry.pack(side = "left")
                elif label_text == "Nom :":
                    nom_entry = tk.Entry(label_frame, text=nom, width=38, font=("Time new roman", 11))
                    nom_entry.insert(0, nom)
                    nom_entry.pack(side="left")
                elif label_text == "Prénom :":
                    prenom_entry = tk.Entry(label_frame, text=prenom, width=38, font=("Time new roman", 11))
                    prenom_entry.insert(0, prenom)
                    prenom_entry.pack(side="left")
                elif label_text == "Sexe :":
                    sexe_var = tk.StringVar(label_frame)
                    sexe_var.set(sexe)  # Sélectionnez une valeur par défaut
                    sexe_options = ["homme", "femme", "autre"]
                    sexe_entry = tk.OptionMenu(label_frame, sexe_var, *sexe_options)
                    sexe_entry.config(bg="white", borderwidth=0, width=38)
                    sexe_entry.pack(side="left")
                elif label_text == "Date de Naissance :":

                    date_naissance_entry = DateEntry(label_frame, text=date_naissance, width=40, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)
                    date_naissance_entry.set_date(date_naissance)
                    date_naissance_entry.pack(side="left")

                    print(date_naissance)
                elif label_text == "Email :":
                    email_entry = tk.Entry(label_frame, text=email, width=38, font=("Time new roman", 11))
                    email_entry.insert(0, email)
                    email_entry.pack(side="left")
                elif label_text == "Téléphone :":
                    telephone_entry = tk.Entry(label_frame, text=telephone, width=38, font=("Time new roman", 11))
                    telephone_entry.insert(0, telephone)
                    telephone_entry.pack(side="left")
                elif label_text == "Adresse :":
                    adresse_entry = tk.Entry(label_frame, text=adresse, width=38, font=("Time new roman", 11))
                    adresse_entry.insert(0, adresse)
                    adresse_entry.pack(side="left")
                elif label_text == "Groupe Sanguin :":
                    var_groupe_sanguin = StringVar(label_frame)
                    var_groupe_sanguin.set(groupe_sanguin)
                    optionmenu_groupe_sanguin = OptionMenu(label_frame, var_groupe_sanguin, "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
                    optionmenu_groupe_sanguin.config(bg="white", borderwidth=0, width=38)
                    optionmenu_groupe_sanguin.pack(side="left")
                elif label_text == "Profession :":
                    profession_entry = tk.Entry(label_frame, text=profession, width=38, font=("Time new roman", 11))
                    profession_entry.insert(0, profession)
                    profession_entry.pack(side="left")
                elif label_text == "Situation Familiale :":
                    var_situation_familiale = StringVar(label_frame)
                    var_situation_familiale.set(situation_familiale)
                    optionmenu_situation_familiale = OptionMenu(label_frame, var_situation_familiale, "Célibataire", "Marié(e)", "Divorcé(e)")
                    optionmenu_situation_familiale.config(bg="white", borderwidth=0, width=38)
                    optionmenu_situation_familiale.pack(side="left")
            
   
            def modifier():

                # Connexion à la base de données
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="connexionbddappli"
                )
                cursor = conn.cursor()

                nom = nom_entry.get()
                prenom = prenom_entry.get()
                sexe = sexe_var.get()
                date_naissance = date_naissance_entry.get_date()
                email = email_entry.get()
                telephone = telephone_entry.get()
                adresse = adresse_entry.get()
                groupe_sanguin = var_groupe_sanguin.get()
                profession = profession_entry.get()
                situation_familiale = var_situation_familiale.get()


                sql = "UPDATE patient SET nom=%s, prenom=%s, sexe=%s, date_naissance=%s, email=%s, telephone=%s, adresse=%s, groupe_sanguin=%s, profession=%s, situation_familiale=%s WHERE id_patient=%s"
                values = (nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale, id_patient)
                cursor.execute(sql, values)

                # Valider la transaction
                conn.commit()
                messagebox.showinfo("Succès", "Modification effectuer !")
                cursor.close()
                conn.close()

        cursor.close()
        conn.close()

        button_modifier = tk.Button(top_level, text="Modifier", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=modifier)
        button_modifier.pack(pady=10)
    
        top_level.update_idletasks()
        width = top_level.winfo_width()
        height = top_level.winfo_height()
        x = (top_level.winfo_screenwidth() // 2) - (width // 2)
        y = (top_level.winfo_screenheight() // 2) - (height // 2)
        top_level.geometry(f"{width}x{height}+{x}+{y}")

class AddPatientScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent) 

        self.parent = parent

        self.id_patient = None

        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10) 


        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)


        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)


        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)


        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
        
        
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)


        ##############################################################################################################

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')
        


        frame1 = Frame(welcome_frame, bg="white")
        frame1.pack(anchor='w', padx=50, pady=1)

        self.image_retour = tk.PhotoImage(file="C:/Users/KAWTHER/VsCode/Doc/Images/previous.png")


        retour_button = tk.Button(frame1, bg="white", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= parent.show_patient_screen, image= self.image_retour)   
        # Ajuster l'apparence du bouton
        retour_button.config(compound=tk.LEFT, padx=5, pady=1)

        # Afficher le bouton
        retour_button.pack(side=tk.LEFT)

        ##############################################################################################################
        #Pour les champs de saisie 

        self.champ_label = tk.Label(welcome_frame, text="Ajout patient ", fg="black", font=("Times New Roman", 14, "bold"), bg="white")
        self.champ_label.pack(side="top")


         # Création des labels et des champs de saisie pour les informations du patient
        self.label_nom = Label(welcome_frame, text="Nom :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold")) 
        self.label_nom.pack(pady=1)
        self.entry_nom = Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_nom.pack(pady=1)

        self.label_prenom = Label(welcome_frame, text="Prénom :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_prenom.pack(pady=1)
        self.entry_prenom = Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_prenom.pack(pady=1)


        self.label_sexe = Label(welcome_frame, text="Sexe :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_sexe.pack(pady=1)
        self.var_sexe = StringVar(welcome_frame)
        self.var_sexe.set("")
        self.optionmenu_sexe = OptionMenu(welcome_frame, self.var_sexe, "femme", "homme", "autre")
        self.optionmenu_sexe.config(bg="white", borderwidth=0, width=38)
        self.optionmenu_sexe.pack(pady=1)


        self.label_date_naissance = Label(welcome_frame, text="Date de Naissance :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.date_naissance_entry = DateEntry(welcome_frame, width=40, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)

        self.label_email = Label(welcome_frame, text="Email :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_email.pack(pady=1)
        self.entry_email = Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_email.pack(pady=1)


        self.label_telephone = Label(welcome_frame, text="Téléphone :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_telephone.pack(pady=1)
        self.entry_telephone = Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_telephone.pack(pady=1)


        self.label_adresse = Label(welcome_frame, text="Adresse :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_adresse.pack(pady=1)
        self.entry_adresse = Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_adresse.pack(pady=1)


        self.label_groupe_sanguin = Label(welcome_frame, text="Groupe sanguin :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_groupe_sanguin.pack(pady=1)

        self.var_groupe_sanguin = StringVar(welcome_frame)
        self.var_groupe_sanguin.set("A+")
        self.optionmenu_groupe_sanguin = OptionMenu(welcome_frame, self.var_groupe_sanguin, "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        self.optionmenu_groupe_sanguin.config(bg="white", borderwidth=0, width=38)
        self.optionmenu_groupe_sanguin.pack(pady=1)

        self.label_profession = Label(welcome_frame, text="Profession :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_profession.pack(pady=1)
        self.entry_profession = Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_profession.pack(pady=1)

        self.label_situation_familiale = Label(welcome_frame, text="Situation familiale :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        self.label_situation_familiale.pack(pady=1)
        self.var_situation_familiale = StringVar(welcome_frame)
        self.var_situation_familiale.set("Célibataire")
        self.optionmenu_situation_familiale = OptionMenu(welcome_frame, self.var_situation_familiale, "Célibataire", "Marié(e)", "Divorcé(e)")
        self.optionmenu_situation_familiale.config(bg="white", borderwidth=0, width=38)
        self.optionmenu_situation_familiale.pack(pady=1)

        #################################################################################################################

        # Création du conteneur pour les boutons

        button_container = tk.Frame(welcome_frame, bg="white")
        button_container.pack(pady=20)

        #Bouton pour effacer les champs
        clear_button = tk.Button(button_container, width=10, text="Clear", fg="white", bg="#ff0000", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.clear_data)   
        clear_button.pack(side=tk.LEFT, padx=5, pady=20)

        #Bouton pour sauvegarder les informations de la modification
        bouton_sauvegarder = tk.Button(button_container, text="Sauvegarder", fg="white", bg="#32CD32", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command = self.ajouter_patient)
        bouton_sauvegarder.pack(side=tk.LEFT, padx=5, pady=20)


        #Bouton pour sauvegarder les informations de la modification
        bouton_orientation = tk.Button(button_container, text="Orientation", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command = self.orientation)
        bouton_orientation.pack(side=tk.LEFT, padx=5, pady=20)
    
    
    def orientation(self):
        if self.id_patient is not None:        
            add_orientation(self.id_patient)
        else:
            messagebox.showerror("Erreur", "Aucun ID de patient disponible")

    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
    
    def set_username(self, username):
        self.username_label.config(text= username)  

    def clear_data(self):

        self.entry_nom.delete(0,END)
        self.entry_prenom.delete(0,END)
        self.var_sexe.set("")

    def ajouter_patient(self):
        # Récupérer les valeurs saisies dans les champs de saisie
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        sexe = self.var_sexe.get()
        date_naissance = self.date_naissance_entry.get()
        email = self.entry_email.get()
        telephone = self.entry_telephone.get()
        adresse = self.entry_adresse.get()
        groupe_sanguin = self.var_groupe_sanguin.get()
        profession = self.entry_profession.get()
        situation_familiale = self.var_situation_familiale.get()

        # Ajouter le code pour enregistrer les informations du patient dans la base de données
        # Vérifier que les champs ne sont pas vides
        if not all((nom, prenom, date_naissance, sexe, telephone)):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return

        # Insérer les données dans la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()
        sql = "INSERT INTO patient (nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, sexe, date_naissance, email, telephone, adresse, groupe_sanguin, profession, situation_familiale)
        cursor.execute(sql, values)

        id_patient = cursor.lastrowid 
        self.id_patient = id_patient 

        conn.commit()
        cursor.close()
        conn.close()

        self.parent.patient_screen.load_all_data()

        # Afficher un message de confirmation
        messagebox.showinfo("Confirmation", "Le patient a été ajouté avec succès")

        # Effacer les champs de saisie après l'ajout du patient
        self.entry_nom.delete(0, tk.END)
        self.entry_prenom.delete(0, tk.END)
        self.var_sexe.set("")
        self.entry_email.delete(0, tk.END)
        self.entry_telephone.delete(0, tk.END)
        self.entry_adresse.delete(0, tk.END)
        self.var_groupe_sanguin.set("")
        self.entry_profession.delete(0, tk.END)
        self.var_situation_familiale.set("")

    def set_id_patient(self, id_patient):     
        self.id_patient = id_patient

    def get_id_patient(self):
        return self.id_patient

def add_orientation(id_patient) :

    add_orientation_window = tk.Toplevel(bg="white")
    add_orientation_window.title("Ajout orienttaion")

    label_id_patient = Label(add_orientation_window, text="ID patient :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
    label_id_patient .pack(pady=5)

    l_id_patient = Label(add_orientation_window, text= id_patient, bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
    l_id_patient .pack(pady=5)

    label_date_orientation = Label(add_orientation_window, text="Date orientation :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
    label_date_orientation.pack(pady=5)
    
    date_orientation_entry = DateEntry(add_orientation_window, width=25, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)
    date_orientation_entry.pack(pady=5)
    
    label_type_orientation = Label(add_orientation_window, text="Type orientation :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
    label_type_orientation.pack(pady=5)
    
    var_type_orientation = StringVar(add_orientation_window)
    var_type_orientation.set("")

    type_orientation_option = OptionMenu(add_orientation_window, var_type_orientation, "externe", "interne", "urgence")
    type_orientation_option.config(bg="white", borderwidth=0, width=25)
    type_orientation_option.pack(pady=1)

    valeurs_service = [
    "Néphrologie",
    "Urologie",
    "Dermatologie",
    "Epidémiologie",
    "Gastro-entérologie",
    "Gynécologie-obstétrique",
    "Hématologie",
    "Histologie",
    "Maladies infectieuses",
    "Médecine du travail",
    "Médecine interne",
    "Chirurgie hépatobiliaire",
    "Neurologie",
    "Chirurgie thoracique",
    "Oncologie médicale",
    "Urgences",
    "Orl",
    "Orthopédie",
    "Pneumologie",
    "Psychiatrie",
    "Rhumatologie",
    "Médecine légale",
    "Chirurgie maxilo-faciale",
    "Chirurgie générale",
    "Néphrologie",
    "Cardiologie",
    "Endocrinologie",
    "Pharmacologie",
    "Transfusion sanguine",
    "Maternité",
    "Ophtalmologie"
    ]

    label_service_origine= Label(add_orientation_window, text="Service d'origine :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
    label_service_origine.pack(pady=5)
    
    service_origine = Combobox(add_orientation_window, values=valeurs_service)
    service_origine.pack(pady=5)

    label_service_destination = Label(add_orientation_window, text="Service destination :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
    label_service_destination.pack(pady=5)
    

    service_destination = Combobox(add_orientation_window, values=valeurs_service)
    service_destination.pack(pady=5)


    def ajout():

        date_orientation = date_orientation_entry.get_date()
        t_orientation = var_type_orientation.get()
        s_destination = service_destination.get()
        s_origine = service_origine.get()


        print(t_orientation)

        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT id_service_origine FROM service_origine  WHERE nom_service = %s", (s_origine,))
        id_service_origine = cursor.fetchone()[0]

        cursor.execute("SELECT id_service  FROM service_destination   WHERE nom_service = %s", (s_destination,))
        id_service_destination = cursor.fetchone()[0]

        cursor.execute("INSERT INTO orientation (date_orientation, type_orientation, id_service_origine, id_service_destination, id_patient) VALUES (%s, %s, %s, %s, %s)",
                       (date_orientation, t_orientation, id_service_origine, id_service_destination, id_patient))

        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Ajout de l'orientation du patient")

    button_ajout = tk.Button(add_orientation_window, text="Ajout orientation", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=ajout)
    button_ajout.pack(pady=10)
    
    add_orientation_window.update_idletasks()
    width = 600
    height = 500
    x = (add_orientation_window.winfo_screenwidth() // 2) - (width // 2)
    y = (add_orientation_window.winfo_screenheight() // 2) - (height // 2)
    add_orientation_window.geometry(f"{width}x{height}+{x}+{y}")

class DconsultationScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)    
        self.parent = parent

        self.configure(bg="#57a1f8")
        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=5) 

        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)

        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)


        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=0)

        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)



        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')

        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_home_screen)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
               
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)

        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        #
        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)

        ###############################################


        self.champ_label = tk.Label(welcome_frame, text="Détail consultataion ", fg="#57a1f8", font=("Times New Roman", 15, "bold"), bg="white")
        self.champ_label.pack(side="top")
        
        frame_container = tk.Frame(welcome_frame, bg="white")
        frame_container.pack(side="top", padx=10, pady=10, anchor="w")

        main_frame = tk.Frame(frame_container, bg="white")
        main_frame.pack(side="left")

        # Créer un cadre pour le label et l'entry du patient ID
        frame1 = tk.Frame(main_frame, bg="white")
        frame1.pack(side="top", anchor="w")

        label_patient_id = tk.Label(frame1, text="ID du patient :", font=("Time new roman", 12), bg="white")
        label_patient_id.pack(side="left", padx=10, pady=10)

        self.entry_patient_id = tk.Entry(frame1, font=("Time new roman", 12), width=30, background='white')
        self.entry_patient_id.pack(side="left", padx=5, pady=5)

        # Créer un cadre pour le label et l'entry du nom du patient
        frame2 = tk.Frame(main_frame, bg="white")
        frame2.pack(side="top", anchor="w")

        label_patient_name = tk.Label(frame2, text="Nom du patient :", font=("Time new roman", 12), bg="white")
        label_patient_name.pack(side="left", padx=10, pady=10)

        self.entry_patient_name = tk.Entry(frame2, font=("Time new roman", 12), width=28,background='white')
        self.entry_patient_name.pack(side="left", padx=5, pady=5)
        
        # Créer un cadre pour le label et l'entry du prenom du patient
        frame3 = tk.Frame(main_frame, bg="white")
        frame3.pack(side="top", anchor="w")

        label_patient_firstname = tk.Label(frame3, text="Prénom du patient :", font=("Time new roman", 12), bg="white")
        label_patient_firstname.pack(side="left", padx=5, pady=5)

        self.entry_patient_firstname = tk.Entry(frame3, font=("Time new roman", 12), width=27,background='white')
        self.entry_patient_firstname.pack(side="left", padx=5, pady=5)

        # Créer un cadre pour le label et l'entry du id du medecin
        frame4 = tk.Frame(main_frame, bg="white")
        frame4.pack(side="top", anchor="w")

        # Labels pour afficher les informations supplémentaires
        label_id_medecin = tk.Label(frame4, text="ID medecin :", font=("Time new roman", 12), bg="white")
        label_id_medecin.pack(side="left", padx=5, pady=5)

        # Entrées pour afficher les valeurs des informations supplémentaires
        self.entry_id_medecin = tk.Entry(frame4, font=("Time new roman", 12), width=32,background='white')
        self.entry_id_medecin.pack(side="left", padx=5, pady=5)

        frame5 = tk.Frame(main_frame, bg="white")
        frame5.pack(side="top", anchor="w")

        label_date_or = tk.Label(frame5, text="Date orientation :", font=("Time new roman", 12), bg="white")
        label_date_or.pack(side="left", padx=5, pady=5)

        self.entry_date_or = tk.Entry(frame5, font=("Time new roman", 12), width=30)
        self.entry_date_or.pack(side="left", padx=5, pady=5)


        frame6 = tk.Frame(main_frame, bg="white")
        frame6.pack(side="top", anchor="w")


        label_type_orientation = tk.Label(frame6, text="Type orientation :", font=("Time new roman", 12), bg="white")
        label_type_orientation.pack(side="left", padx=5, pady=5)

        self.entry_type_orientation = tk.Entry(frame6, font=("Time new roman", 12), width=30)
        self.entry_type_orientation.pack(side="left", padx=5, pady=5)

        frame7 = tk.Frame(main_frame, bg="white")
        frame7.pack(side="top", anchor="w")

        label_service_origine = tk.Label(frame7, text="Service origine :", font=("Time new roman", 12), bg="white")
        label_service_origine.pack(side="left", padx=5, pady=5)

        self.entry_service_origine = tk.Entry(frame7, font=("Time new roman", 12), width=30)
        self.entry_service_origine.pack(side="left", padx=5, pady=5)

        main_frame2 = tk.Frame(frame_container, bg="white")
        main_frame2.pack(side="right", padx=10, fill="both", expand=True)

        frame8 = tk.Frame(main_frame2, bg="white")
        frame8.pack(side="top", anchor="ne", padx=5, pady=5)

        label_date_consultation = tk.Label(frame8, text="Date consultation :", font=("Time new roman", 12), bg="white")
        label_date_consultation.pack(side="left", padx=5, pady=5)

        self.entry_date_consultation = DateEntry(frame8, font=("Time new roman", 12), width=25, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)
        self.entry_date_consultation.pack(side="left", padx=5, pady=5)
  

        # Créer un cadre pour le label et l'entry de la remarque
        frame9 = tk.Frame(main_frame2, bg="white")
        frame9.pack(side="top", padx=5, pady=5)

        label_remarques = tk.Label(frame9, text="Remarques :", font=("Time new roman", 12), bg="white")
        label_remarques.pack(side="left", padx=5, pady=5)

        self.entry_remarques = tk.Entry(frame9, font=("Time new roman", 12), width=30, state="normal")
        self.entry_remarques.pack(side="left", padx=5, pady=5)


        # Créer un cadre pour le label et l'entry de la remarque
        frame10 = tk.Frame(main_frame2, bg="white")
        frame10.pack(side="top", padx=5, pady=5)

        button_cs = tk.Button(frame10, width=17, text="Ajouter consultation", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command = self.ajout_consultation)
        button_cs.pack(padx=5, pady=5)
       

        ########################################################################################
        # Pour la liste des consultations du patient

        frame_liste = Frame(welcome_frame, bg="white")
        frame_liste.pack(padx=20, pady=20, anchor="w")

        frame_treeview = Frame(frame_liste)
        frame_treeview.pack(side="left", padx=10)

        self.treeview = ttk.Treeview(frame_treeview, columns=("id_consultation","id_medecin", "nom_medecin", "date_consultation", "heure_consultation", "remarques"), height=10)
        self.treeview.pack(fill="both", expand=True)

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("id_consultation", width=100)
        self.treeview.column("id_medecin", width=100)
        self.treeview.column("nom_medecin", width=100)
        self.treeview.column("date_consultation", width=100)
        self.treeview.column("heure_consultation", width=110)
        self.treeview.column("remarques", width=200)

        self.treeview.heading("#0", text="", anchor="center")
        self.treeview.heading("id_consultation", text="id_consultation")
        self.treeview.heading("nom_medecin", text="nom_medecin")
        self.treeview.heading("id_medecin", text="id_medecin")
        self.treeview.heading("date_consultation", text="date_consultation")
        self.treeview.heading("heure_consultation", text="heure_consultation")
        self.treeview.heading("remarques", text="remarques")
       
        # Placer le treeview en bas
        self.treeview.pack()
      
        scrollbar = Scrollbar(frame_liste, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="left", fill="y")

        frame_button = Frame(frame_liste, background = "white")
        frame_button.pack(side="right", padx=3, pady=5)

        button_afficher = Button(frame_button, text="Afficher Ordonnance", width = 20, fg="white", bg="#57a1f8", border=0, cursor="hand2", font= ("Time new roman", 11, "bold"), command=self.afficher_id_consultation)
        button_afficher.pack(padx=3, pady=5)

        # Création du conteneur pour les boutons
        button_container = tk.Frame(welcome_frame, bg="white")
        button_container.pack(pady=10)

        #Bouton pour les antécedants
        button_Antécedant = tk.Button(button_container, width=10, text="Antécedant", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command = parent.show_antecedant_screen)   
        button_Antécedant.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour les symtomes
        bouton_exClinique = tk.Button(button_container, text="Examen clinique", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= parent.show_examenClinique_screen)
        bouton_exClinique.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour le traitement
        bouton_traitement = tk.Button(button_container, text="Traitement", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=parent.show_traitement_screen)
        bouton_traitement.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour cunsuite à tenir 
        bouton_indication= tk.Button(button_container, text="Conduire à tenir", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"))
        bouton_indication.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour Diagnostique 
        bouton_Diagnostique = tk.Button(button_container, text="Diagnostique", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"))
        bouton_Diagnostique.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour ordonnance
        bouton_ordonnance = tk.Button(button_container, text="Ordonnance", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command = parent.show_ordonnace_screen)
        bouton_ordonnance.pack(side=tk.LEFT, padx=5, pady=10)

        #Bouton pour lettre orientation
        bouton_orientation = tk.Button(button_container, text="Orientation autre service", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.login)
        bouton_orientation.pack(side=tk.LEFT, padx=5, pady=10)

    def login(self):
        login_screen = LoginScreen()
        username, password = login_screen.login()
        print(username)  # Affiche le nom d'utilisateur
        print(password)  # Affiche le mot de passe
        self.display_user_info(username)

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
        self.username_label = Label(self, text="Nom d'utilisateur : " + username)
        self.username_label.pack()

    def set_username(self, username):
        self.username_label.config(text= username)

    def display_patient_info(self, patient_id, patient_name, patient_firstname,id_medecin,orientation_id):
        
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="connexionbddappli"
                )
        cursor = conn.cursor()


        query = "SELECT type_orientation, date_orientation, id_service_origine FROM orientation WHERE id_orientation = %s"
        cursor.execute(query, (orientation_id,))
        result = cursor.fetchone()


        cursor.execute("SELECT nom_service FROM service_origine WHERE id_service_origine  = %s", (result[2],))
        nom_service = cursor.fetchone()[0]

        cursor.close()
        conn.close()


        self.entry_type_orientation.config(state="normal")
        self.entry_type_orientation.delete(0, tk.END)
        self.entry_type_orientation.insert(0, result[0])
        self.entry_type_orientation.config(state="readonly")


        self.entry_date_or.config(state="normal")
        self.entry_date_or.delete(0, tk.END)
        self.entry_date_or.insert(0, result[1])
        self.entry_date_or.config(state="readonly")



        self.entry_service_origine.config(state="normal")
        self.entry_service_origine.delete(0, tk.END)
        self.entry_service_origine.insert(0, nom_service)
        self.entry_service_origine.config(state="readonly")
        
        
        self.entry_id_medecin.config(state="normal")
        self.entry_id_medecin.delete(0, tk.END)
        self.entry_id_medecin.insert(0, id_medecin)
        self.entry_id_medecin.config(state="readonly")
       
       
        self.entry_patient_id.config(state="normal")
        self.entry_patient_id.delete(0, tk.END)
        self.entry_patient_id.insert(0, patient_id)
        self.entry_patient_id.config(state="readonly")

        self.entry_patient_name.config(state="normal")
        self.entry_patient_name.delete(0, tk.END)
        self.entry_patient_name.insert(0, patient_name)
        self.entry_patient_name.config(state="readonly")

        self.entry_patient_firstname.config(state="normal")
        self.entry_patient_firstname.delete(0, tk.END)
        self.entry_patient_firstname.insert(0, patient_firstname)
        self.entry_patient_firstname.config(state="readonly")
        
    def ajout_consultation(self):

        id_medecin = self.entry_id_medecin.get()
        id_patient = self.entry_patient_id.get()
        date_consultation = self.entry_date_consultation.get()
        heure_consultation = datetime.datetime.now().strftime("%H:%M:%S")
        remarques =  self.entry_remarques.get()

        # Se connecter à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        query = "INSERT INTO consultation (id_patient, id_medecin, date_consultation, heure_consultation, remarques) VALUES (%s, %s, %s, %s, %s)"
        values = (id_patient, id_medecin, date_consultation, heure_consultation, remarques)

        cursor.execute(query, values)
        conn.commit()
        consultation_id = cursor.lastrowid  #Prendre l'ID deriner de consultation
        cursor.close()
        conn.close()

        self.parent.antecedant_screen.set_consultation_id(consultation_id)
        self.parent.examenClinique_screen.set_consultation_id(consultation_id)
        self.parent.traitement_screen.set_consultation_id(consultation_id)
        self.parent.ordonnace_screen.set_consultation_id(consultation_id)
        
        print(consultation_id)
        messagebox.showinfo("Succès", "Consultation ajoutée avec succès")
        self.parent.dconsultation_screen.affiche_historique_consultation()


        return consultation_id 

    def set_consultation_id(self, consultation_id):     
        self.consultation_id = consultation_id

    def get_consultation_id(self):
        return self.consultation_id
      
    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def affiche_historique_consultation(self):

        patient_name = self.entry_patient_name.get()
        patient_firstname = self.entry_patient_firstname.get()
        id_medecin = self.entry_id_medecin.get()
        id_patient = self.entry_patient_id.get()
        #print(id_patient, id_medecin)

        self.treeview.delete(*self.treeview.get_children())

        # Se connecter à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        query = """
            SELECT c.id_consultation, c.id_medecin, m.nom, c.date_consultation, c.heure_consultation, c.remarques
            FROM consultation c
            INNER JOIN medecin m ON c.id_medecin = m.id_medecin
            WHERE c.id_patient = %s
            ORDER BY c.id_consultation ASC
            """
        
        # Exécuter une requête SQL pour récupérer tous les patients        
        #query = "SELECT id_consultation, id_patient, id_medecin, date_consultation, heure_consultation, remarques FROM consultation WHERE id_patient = %s"
        cursor.execute(query, (id_patient,))

        # Récupérer les résultats de la requête
        results = cursor.fetchall()


        # Parcourir les résultats et les ajouter au Treeview
        for result in results:
            id_consultation, id_patient, id_medecin, date_consultation, heure_consultation, remarques = result
            self.treeview.insert("", "end", values=(id_consultation, id_patient, id_medecin, date_consultation, heure_consultation, remarques))

        # Fermer le curseur et la connexion à la base de données
        cursor.close()
        conn.close()

    def afficher_id_consultation(self):
        selected_item = self.treeview.focus()
        if selected_item:
            item_data = self.treeview.item(selected_item)
            id_consultation = item_data["values"][0]
            self.show_id_consultation(id_consultation)

    def show_id_consultation(self, id_consultation):
        
        top_level = Toplevel(background="white")
        label = Label(top_level, text="Ordonnance de la consultation N°: {}".format(id_consultation), font=("Time new roman", 10), bg="white")
        label.pack()

        # Création du Label pour afficher le nom du médecin
        label_patient = tk.Label(top_level, text="Nom et prénom patient : ", font=("Time new roman", 10), bg="white")
        label_patient.pack()

        label_medecin = tk.Label(top_level, text="Nom médecin : ", font=("Time new roman", 10), bg="white")
        label_medecin.pack()


        # Se connecter à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        valeur_medicament_actuel ="prescrit"
        query = """
            SELECT t.id_medicament, m.nom_medicament, m.id_voie, v.nom_voie, c.id_patient, p.nom, med.id_medecin, med.nom, p.prenom
            FROM consultation c
            INNER JOIN traitement t ON c.id_consultation = t.id_consultation
            INNER JOIN medicament m ON t.id_medicament = m.id_medicament
            INNER JOIN voie v ON m.id_voie = v.id_voie
            INNER JOIN patient p ON c.id_patient = p.id_patient
            INNER JOIN medecin med ON c.id_medecin = med.id_medecin
            WHERE c.id_consultation = %s AND t.medicament_actuel = %s
            """       
        # Exécuter une requête SQL pour récupérer tous les patients        
        cursor.execute(query, (id_consultation,valeur_medicament_actuel, ))

        # Récupérer tous les résultats de la requête
        results = cursor.fetchall()

        # Création du Treeview pour afficher les résultats des médicaments et des voies
        treeview = ttk.Treeview(top_level, columns=("Nom Médicament", "Voie d'administration"))
        treeview.heading("#0", text="ID Médicament")
        treeview.heading("Nom Médicament", text="Nom Médicament")
        treeview.heading("Voie d'administration", text="Voie d'administration")

        scrollbar = Scrollbar(top_level, orient="vertical", command = treeview.yview)
        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        treeview.pack()

        # Initialisation des variables
        noms_medecins = []
        noms_patients = []
        prenoms_patients = []
        nom_medecin = ""
        nom_patient = ""
        prenom_patient = ""

        # Parcours des résultats et insertion dans le Treeview
        for row in results:
            id_medicament = row[0]
            nom_medicament = row[1]
            nom_voie = row[3]
            nom_medecin_actuel = row[7]
            nom_patient_actuel = row[5]
            prenom_patient_actuel = row[8]

            print(nom_medecin_actuel)

            # Vérifier si le nom du médecin a déjà été ajouté à la liste
            if nom_medecin_actuel not in noms_medecins and nom_patient_actuel not in noms_patients and prenom_patient_actuel not in prenoms_patients :
                # Mettre à jour le nom du médecin et du patient
                nom_medecin = nom_medecin_actuel
                nom_patient = nom_patient_actuel
                prenom_patient = prenom_patient_actuel
                # Ajouter le nom du médecin et du patient à leurs listes respectives
                noms_medecins.append(nom_medecin_actuel)
                noms_patients.append(nom_patient_actuel)
                prenoms_patients.append(nom_patient_actuel)


            treeview.insert("", "end", text=str(id_medicament), values=(nom_medicament, nom_voie))

        # Affichage du nom du médecin et le nom et prenom du patient dans le Label
        label_patient.config(text="Nom et prénom patient : " + nom_patient + ' ' + prenom_patient)
        label_medecin.config(text="Nom médecin : " + nom_medecin)

        # Configurer le redimensionnement de la fenêtre
        top_level.pack_propagate(False)

        top_level.update_idletasks()
        width = 620
        height = 300
        x = (top_level.winfo_screenwidth() // 2) - (width // 2)
        y = (top_level.winfo_screenheight() // 2) - (height // 2)
        top_level.geometry(f"{width}x{height}+{x}+{y}")

class AtcdScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10) 


        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)


        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)


        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)


        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
              
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

 
       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)

        ##############################################################################################################

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')
        
        frame_retour = Frame(welcome_frame, bg="white")
        frame_retour.pack(anchor='w', padx=50, pady=1)

        self.image_retour = tk.PhotoImage(file="C:/Users/KAWTHER/VsCode/Doc/Images/previous.png")


        retour_button = tk.Button(frame_retour, bg="white", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= parent.show_ddconsultation_screen, image= self.image_retour)   
        # Ajuster l'apparence du bouton
        retour_button.config(compound=tk.LEFT, padx=5, pady=1)

        # Style des widgets ttk
        style = ttk.Style()
        style.configure("Custom.TLabel", font=("Times New Roman", 11, "bold"), background="white")
        style.configure("Custom.TEntry", font=("Times New Roman", 11), background="white")
        style.configure("Custom.TButton", font=("Times New Roman", 11),fg="white")
        style.configure("Custom.TCheckbutton", font=("Times New Roman", 11, "bold"), background="white")

        self.consultation_label = tk.Label(welcome_frame, text="ID de la consultation :", fg="#57a1f8", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_label.pack(side="top")

        self.consultation_id_label = tk.Label(welcome_frame, text="", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_id_label.pack(side="top")

        # Afficher le bouton
        retour_button.pack(side=tk.LEFT)


        # Création des conteneurs pour chaque partie
        frame1 = tk.Frame(welcome_frame, bg="white")
        frame1.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        frame2 = tk.Frame(welcome_frame, bg="white")
        frame2.pack(side="left",expand=True,  fill="both", padx=10, pady=10)
        frame3 = tk.Frame(welcome_frame, bg="white")
        frame3.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        frame4 = tk.Frame(welcome_frame, bg="white")
        frame4.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        # Antécédents médicaux
        label_medical = ttk.Label(frame1, text="Antécédents Médicaux", style="Custom.TLabel")
        label_medical.pack(pady=10)

        label_nom_maladie = ttk.Label(frame1, text="Nom de la maladie:", style="Custom.TLabel")
        label_nom_maladie.pack(pady=10)
        self.entry_nom_maladie = ttk.Entry(frame1, style="Custom.TEntry")
        self.entry_nom_maladie.pack(pady=10)

        label_date_debut_medical = ttk.Label(frame1, text="Date de début:", style="Custom.TLabel")
        label_date_debut_medical.pack(pady=10)
        self.entry_date_debut_medical = DateEntry(frame1, style="Custom.TEntry",width=20, date_pattern="yyyy-mm-dd")
        self.entry_date_debut_medical.pack(pady=10)

        label_date_fin_medical = ttk.Label(frame1, text="Date de fin:", style="Custom.TLabel")
        label_date_fin_medical.pack(pady=10)
        self.entry_date_fin_medical = DateEntry(frame1, style="Custom.TEntry",width=20, date_pattern="yyyy-mm-dd")
        self.entry_date_fin_medical.pack(pady=10)

        label_remarque_medical = ttk.Label(frame1, text="Remarque:", style="Custom.TLabel")
        label_remarque_medical.pack(pady=10)
        self.entry_remarque_medical = ttk.Entry(frame1, style="Custom.TEntry")
        self.entry_remarque_medical.pack(pady=10)

        button_ajouter_medical = ttk.Button(frame1, text="Ajouter antécédent médical", style="Custom.TButton", command=self.ajouter_antecedent_medical)
        button_ajouter_medical.pack(pady=10)


        # Antécédents chirurgicaux
        label_chirurgical = ttk.Label(frame2, text="Antécédents Chirurgicaux", style="Custom.TLabel")
        label_chirurgical.pack(pady=10)

        label_nom_chirurgie = ttk.Label(frame2, text="Nom de la chirurgie:", style="Custom.TLabel")
        label_nom_chirurgie.pack(pady=10)
        self.entry_nom_chirurgie = ttk.Entry(frame2, style="Custom.TEntry")
        self.entry_nom_chirurgie.pack(pady=10)

        label_date_debut_chir = ttk.Label(frame2, text="Date de début:", style="Custom.TLabel")
        label_date_debut_chir.pack(pady=10)
        self.entry_date_debut_chir = DateEntry(frame2, style="Custom.TEntry",width=20, date_pattern="yyyy-mm-dd")
        self.entry_date_debut_chir.pack(pady=10)

        label_lieu = ttk.Label(frame2, text="Lieu:", style="Custom.TLabel")
        label_lieu.pack(pady=10)
        self.entry_lieu = ttk.Entry(frame2, style="Custom.TEntry")
        self.entry_lieu.pack(pady=10)

        label_remarque_chir = ttk.Label(frame2, text="Remarque:", style="Custom.TLabel")
        label_remarque_chir.pack(pady=10)
        self.entry_remarque_chir = ttk.Entry(frame2, style="Custom.TEntry")
        self.entry_remarque_chir.pack(pady=10)

        button_ajouter_chirurgical = ttk.Button(frame2, text="Ajouter antécédent chirurgical", style="Custom.TButton", command=self.ajouter_antecedent_chirurgical)
        button_ajouter_chirurgical.pack(pady=10)

        # Antécédents familiaux
        label_familial = ttk.Label(frame3, text="Antécédents Familiaux", style="Custom.TLabel")
        label_familial.pack(pady=10)

        label_nom_maladie_fam = ttk.Label(frame3, text="Nom de la maladie:", style="Custom.TLabel")
        label_nom_maladie_fam.pack(pady=10)
        self.entry_nom_maladie_fam = ttk.Entry(frame3, style="Custom.TEntry")
        self.entry_nom_maladie_fam.pack(pady=10)

        label_date_debut_fam = ttk.Label(frame3, text="Date de début:", style="Custom.TLabel")
        label_date_debut_fam.pack(pady=10)
        self.entry_date_debut_fam = DateEntry(frame3, style="Custom.TEntry",width=20, date_pattern="yyyy-mm-dd")
        self.entry_date_debut_fam.pack(pady=10)

        label_date_fin_fam = ttk.Label(frame3, text="Date de fin:", style="Custom.TLabel")
        label_date_fin_fam.pack(pady=10)
        self.entry_date_fin_fam = DateEntry(frame3, style="Custom.TEntry",width=20, date_pattern="yyyy-mm-dd")
        self.entry_date_fin_fam.pack(pady=10)

        label_remarque_fam = ttk.Label(frame3, text="Remarque:", style="Custom.TLabel")
        label_remarque_fam.pack(pady=10)
        self.entry_remarque_fam = ttk.Entry(frame3, style="Custom.TEntry")
        self.entry_remarque_fam.pack(pady=10)

        button_ajouter_familial = ttk.Button(frame3, text="Ajouter antécédent familial", style="Custom.TButton", command=self.ajouter_antecedent_familial)
        button_ajouter_familial.pack(pady=10)

        # Habitudes de vie
        label_habitude = ttk.Label(frame4, text="Habitudes de vie", style="Custom.TLabel")
        label_habitude.pack(pady=10)

        # Checkbox for smoking
        self.smoking_var = tk.IntVar()
        self.check_smoking = ttk.Checkbutton(frame4, text="Tabagisme", variable=self.smoking_var, style="Custom.TCheckbutton")
        self.check_smoking.pack(pady=10)

        # Checkbox for drug use
        self.drug_var = tk.IntVar()
        self.check_drug = ttk.Checkbutton(frame4, text="Drogue", variable=self.drug_var, style="Custom.TCheckbutton")
        self.check_drug.pack(pady=10)

        # Checkbox for alcohol consumption
        self.alcohol_var = tk.IntVar()
        self.check_alcohol = ttk.Checkbutton(frame4, text="Alcool", variable=self.alcohol_var, style="Custom.TCheckbutton")
        self.check_alcohol.pack(pady=10)
        
        label_description = ttk.Label(frame4, text="Description:", style="Custom.TLabel")
        label_description.pack(pady=10)
        self.entry_description = ttk.Entry(frame4, style="Custom.TEntry")
        self.entry_description.pack(pady=10)

        button_ajouter_habitude = ttk.Button(frame4, text="Ajouter habitude de vie", style="Custom.TButton", command=self.ajouter_habitude_vie)
        button_ajouter_habitude.pack(pady=10)
     
    def ajouter_antecedent_medical(self):
        nom_maladie = self.entry_nom_maladie.get()
        date_debut = self.entry_date_debut_medical.get() 
        date_fin = self.entry_date_fin_medical.get()
        remarque = self.entry_remarque_medical.get()
        id_consultation = self.consultation_id_label.cget("text")



        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        # Insertion des données dans la table "antecedentmedicaux"
        query = "INSERT INTO antecedentmedicaux (id_consultation, nom_maladie, date_debut, date_fin, remarque) VALUES (%s, %s, %s, %s, %s)"
        values = (id_consultation, nom_maladie, date_debut, date_fin, remarque)

        cursor.execute(query, values)

        # Validation de la transaction et fermeture de la connexion
        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Ajout antecedent medicaux" )


        # Effacer les champs de saisie
        self.entry_nom_maladie.delete(0, tk.END)
        self.entry_date_debut_medical.delete(0, tk.END)
        self.entry_date_fin_medical.delete(0, tk.END)
        self.entry_remarque_medical.delete(0, tk.END)

    def ajouter_antecedent_chirurgical(self):
        
        # Récupérer les valeurs des champs
        nom_chirurgie = self.entry_nom_chirurgie.get()
        date_debut = self.entry_date_debut_chir.get() 
        lieu = self.entry_lieu.get()
        remarque = self.entry_remarque_chir.get()
        id_consultation = self.consultation_id_label.cget("text")


        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()


        query = "INSERT INTO antecedentchirurgicaux (id_consultation, nom_chirurgie, date_debut, lieu, remarque) VALUES (%s, %s, %s, %s, %s)"
        values = (id_consultation, nom_chirurgie, date_debut, lieu, remarque)
        cursor.execute(query, values)

        # Validation de la transaction et fermeture de la connexion
        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Ajout antecedent chirurgicaux" )

        # Réinitialiser les champs après l'ajout des données
        self.entry_nom_chirurgie.delete(0, tk.END)
        self.entry_date_debut_chir.delete(0, tk.END)
        self.entry_lieu.delete(0, tk.END)
        self.entry_remarque_chir.delete(0, tk.END)

    def ajouter_antecedent_familial(self):
       
        # Récupérer les valeurs des champs
        nom_maladie = self.entry_nom_maladie.get()
        date_debut = self.entry_date_debut_fam.get()
        date_fin = self.entry_date_fin_fam.get()
        remarque = self.entry_remarque_fam.get()
        id_consultation = self.consultation_id_label.cget("text")


        
        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        
        # Insertion des données dans la table "antecedentfamiliaux"
        query = "INSERT INTO antecedentfamiliaux (id_consultation, nom_maladie, date_debut, date_fin, remarque) VALUES (%s, %s, %s, %s, %s)"
        values = (id_consultation, nom_maladie, date_debut, date_fin, remarque)

        cursor.execute(query, values)


        # Validation de la transaction et fermeture de la connexion
        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Ajout antecedent familiaux" )

        # Réinitialiser les champs après l'ajout des données
        self.entry_nom_maladie.delete(0, tk.END)
        self.entry_date_debut_fam.delete(0, tk.END)
        self.entry_date_fin_fam.delete(0, tk.END)
        self.entry_remarque_fam.delete(0, tk.END)

    def ajouter_habitude_vie(self):
        
        # Récupérer les valeurs des habitudes de vie
        smoking = self.smoking_var.get()
        drug = self.drug_var.get()
        alcohol = self.alcohol_var.get()
        description = self.entry_description.get()
        id_consultation = self.consultation_id_label.cget("text")


        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        # Add code to save the lifestyle habit to the database
        if smoking:
            values = (id_consultation, 1,  description)  # ID de l'option "Tabagisme" dans la table option_habitudes
            query = "INSERT INTO habitudevie (id_consultation, id_option_habitude, description) VALUES (%s, %s, %s)"
            cursor.execute(query, values)

        if drug:
            values = (id_consultation, 3, description)  # ID de l'option "Drogue" dans la table option_habitudes
            query = "INSERT INTO habitudevie (id_consultation, id_option_habitude, description) VALUES (%s, %s, %s)"
            cursor.execute(query, values)

        if alcohol:
            values = (id_consultation, 2, description)  # ID de l'option "Alcool" dans la table option_habitudes
            query = "INSERT INTO habitudevie (id_consultation, id_option_habitude, description) VALUES (%s, %s, %s)"
            cursor.execute(query, values)

        conn.commit()
        conn.close()

        messagebox.showinfo("Succès", "Ajout habitude de vie")

        # Clear the input fields
        self.entry_nom_habitude.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)
        self.smoking_var.set(0)
        self.drug_var.set(0)
        self.alcohol_var.set(0)

    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()
  
    def set_username(self, username):
        self.username_label.config(text= username)
    
    def set_consultation_id(self, consultation_id):
        self.consultation_id_label.config(text=consultation_id)

class TraitementScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10) 


        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)


        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)


        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)


        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
        
        
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)




        ##############################################################################################################

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')
        


        frame1 = Frame(welcome_frame, bg="white")
        frame1.pack(anchor='w', padx=50, pady=1)

        self.image_retour = tk.PhotoImage(file="C:/Users/KAWTHER/VsCode/Doc/Images/previous.png")


        retour_button = tk.Button(frame1, bg="white", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= parent.show_ddconsultation_screen, image= self.image_retour)   
        # Ajuster l'apparence du bouton
        retour_button.config(compound=tk.LEFT, padx=5, pady=1)

        # Afficher le bouton
        retour_button.pack(side=tk.LEFT)



        # Création des widgets de l'écran de traitement
        label = tk.Label(welcome_frame, text="Traitement médical du patient", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        label.pack()

        cont_frame = tk.Frame(welcome_frame, bg="white")
        cont_frame.pack(pady=5)

        self.consultation_label = tk.Label(cont_frame, text="ID de la consultation :", fg="#57a1f8", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_label.pack(side=tk.LEFT)

        self.consultation_id_label = tk.Label(cont_frame, text="", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_id_label.pack(side=tk.RIGHT)

    
        # Style des widgets ttk
        style = ttk.Style()
        style.configure("Custom.TEntry", font=("Times New Roman", 11), background="white")
        style.configure("Custom.TButton", font=("Times New Roman", 11),fg="white")
        style.configure("Custom.TCheckbutton", font=("Times New Roman", 11, "bold"), background="white")

        ##############################################################################################################
        #Pour les champs de saisie         
        # Création des étiquettes et des champs de saisie pour chaque information du médicament
        label_nom_medicament = tk.Label(welcome_frame, text="Nom du médicament :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_nom_medicament.pack()
        self.entry_nom_medicament = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_nom_medicament.pack()

        label_dosage = tk.Label(welcome_frame, text="Dosage:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_dosage.pack()
        self.entry_dosage = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_dosage.pack()

        label_nom_compro = tk.Label(welcome_frame, text="Nom commercial :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_nom_compro.pack()
        self.entry_nom_compro = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_nom_compro.pack()

        #label_taille = tk.Label(welcome_frame, text="Taille :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        #label_taille.pack()
        #self.entry_taille = Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        #self.entry_taille.pack()


        #label_atc = tk.Label(welcome_frame, text="ATC :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        #label_atc.pack()
        #self.entry_atc = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        #self.entry_atc.pack()

        label_voie = tk.Label(welcome_frame, text="Voie d'administration :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_voie.pack()

        # Options pour la liste déroulante de voie d'administration
        options_voie = [
            "Orale",
            "Itramusculaire",
            "Intraveineuse",
            "Rectale",
            "Sous-cutanée",
            "Sublinguale",
            "Transdermique"
        ]

        self.combobox_voie = Combobox(welcome_frame, values=options_voie)
        self.combobox_voie.pack()

        label_date_debut = tk.Label(welcome_frame, text="Date de début:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_date_debut.pack()
        self.entry_date_debut = DateEntry(welcome_frame,width=20, date_pattern="yyyy-mm-dd")  
        self.entry_date_debut.pack()

        label_date_fin = tk.Label(welcome_frame, text="Date de fin:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_date_fin.pack()
        self.entry_date_fin = DateEntry(welcome_frame,width=20, date_pattern="yyyy-mm-dd") 
        self.entry_date_fin.pack()

        label_duree_prise = tk.Label(welcome_frame, text="Durée de prise:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_duree_prise.pack()
        self.entry_duree_prise = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_duree_prise.pack()

        label_medicament_actuel = tk.Label(welcome_frame, text="Médicament actuel:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_medicament_actuel.pack()

        # Variable pour stocker la valeur du choix (1 pour "oui", 0 pour "non")
        self.medicament_actuel_var = tk.IntVar()

        # Création des boutons de sélection
        radio_oui = tk.Radiobutton(welcome_frame, text="Oui", variable=self.medicament_actuel_var, value=1, bg="white",  font=("Time new roman", 11))
        radio_oui.pack()

        radio_non = tk.Radiobutton(welcome_frame, text="Non", variable=self.medicament_actuel_var, value=0, bg="white", font=("Time new roman", 11))
        radio_non.pack()


        # Création d'un bouton pour sauvegarder les informations
        bouton_sauvegarder = tk.Button(welcome_frame, text="Sauvegarder", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.sauvegarder)
        bouton_sauvegarder.pack()


    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
        self.username_label = Label(self, text="Nom d'utilisateur : " + username)
        self.username_label.pack()

    def sauvegarder(self):
        # Récupérer les valeurs saisies par l'utilisateur
        nom_medicament = self.entry_nom_medicament.get()
        dosage = self.entry_dosage.get()
        nom_compro = self.entry_nom_compro.get()
        voie_administration = self.combobox_voie.get()
        date_debut = self.entry_date_debut.get()
        date_fin = self.entry_date_fin.get()
        duree_prise = self.entry_duree_prise.get()
        medicament_actuel = "Oui" if self.medicament_actuel_var.get() == 1 else "Non"
        id_consultation = self.consultation_id_label.cget("text")


        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()


        # Insérer la voie d'administration dans la table "voie" si elle n'existe pas déjà
        #cursor.execute("INSERT IGNORE INTO voie (nom_voie) VALUES (%s)", (voie_administration,))
        cursor.execute("SELECT id_voie FROM voie WHERE nom_voie = %s", (voie_administration,))
        id_voie = cursor.fetchone()[0]

        # Insérer les informations du médicament dans la table "medicaments"
        cursor.execute("INSERT INTO medicament (nom_medicament, dosage, nom_compro, id_voie) VALUES (%s, %s, %s, %s)",
                       (nom_medicament, dosage, nom_compro, id_voie))
        
        id_medicament = cursor.lastrowid 

        cursor.execute("INSERT INTO traitement (id_medicament, id_consultation, medicament_actuel, date_debut, date_fin, duree_prise) VALUES (%s, %s, %s, %s, %s, %s)",
                       (id_medicament, id_consultation, medicament_actuel, date_debut, date_fin, duree_prise))

        # Valider les modifications et fermer la connexion à la base de données
        conn.commit()
        conn.close()

        self.entry_nom_medicament.delete(0, tk.END)
        self.entry_dosage.delete(0, tk.END)
        self.entry_nom_compro.delete(0, tk.END)
        self.entry_duree_prise.delete(0, tk.END)
        self.entry_date_fin.delete(0, tk.END)
        self.entry_date_debut.delete(0, tk.END)



        messagebox.showinfo("Succès", "Ajout du medicament du patient")

    def set_username(self, username):
        self.username_label.config(text= username)

    def set_consultation_id(self, consultation_id):
        self.consultation_id_label.config(text=consultation_id)

class OrdonnaceScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10) 


        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)


        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)


        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)


        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
        
        
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)




        ##############################################################################################################

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')
        


        frame1 = Frame(welcome_frame, bg="white")
        frame1.pack(anchor='w', padx=50, pady=1)

        self.image_retour = tk.PhotoImage(file="C:/Users/KAWTHER/VsCode/Doc/Images/previous.png")


        retour_button = tk.Button(frame1, bg="white", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= parent.show_ddconsultation_screen, image= self.image_retour)   
        # Ajuster l'apparence du bouton
        retour_button.config(compound=tk.LEFT, padx=5, pady=1)

        # Afficher le bouton
        retour_button.pack(side=tk.LEFT)



        # Création des widgets de l'écran de traitement
        label = tk.Label(welcome_frame, text="Ordonnance du patient", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        label.pack()

        cont_frame = tk.Frame(welcome_frame, bg="white")
        cont_frame.pack(pady=5)

        self.consultation_label = tk.Label(cont_frame, text="ID de la consultation :", fg="#57a1f8", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_label.pack(side=tk.LEFT)

        self.consultation_id_label = tk.Label(cont_frame, text="", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_id_label.pack(side=tk.RIGHT)

    
        # Style des widgets ttk
        style = ttk.Style()
        style.configure("Custom.TEntry", font=("Times New Roman", 11), background="white")
        style.configure("Custom.TButton", font=("Times New Roman", 11),fg="white")
        style.configure("Custom.TCheckbutton", font=("Times New Roman", 11, "bold"), background="white")

        ##############################################################################################################
        #Pour les champs de saisie         
        # Création des étiquettes et des champs de saisie pour chaque information du médicament
        label_nom_medicament = tk.Label(welcome_frame, text="Nom du médicament :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_nom_medicament.pack()
        self.entry_nom_medicament = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_nom_medicament.pack()


        # Création d'un bouton pour sauvegarder les informations
        bouton_interaction = tk.Button(welcome_frame, text="Interaction médicament", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.interaction_medicament)
        bouton_interaction.pack()

        label_dosage = tk.Label(welcome_frame, text="Dosage:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_dosage.pack()
        self.entry_dosage = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_dosage.pack()

        label_nom_compro = tk.Label(welcome_frame, text="Nom commercial :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_nom_compro.pack()
        self.entry_nom_compro = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_nom_compro.pack()

        label_voie = tk.Label(welcome_frame, text="Voie d'administration :", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_voie.pack()

        # Options pour la liste déroulante de voie d'administration
        options_voie = [
            "Orale",
            "Itramusculaire",
            "Intraveineuse",
            "Rectale",
            "Sous-cutanée",
            "Sublinguale",
            "Transdermique"
        ]

        self.combobox_voie = Combobox(welcome_frame, values=options_voie)
        self.combobox_voie.pack()

        label_date_debut = tk.Label(welcome_frame, text="Date de début:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_date_debut.pack()
        self.entry_date_debut = DateEntry(welcome_frame,width=20, date_pattern="yyyy-mm-dd")  
        self.entry_date_debut.pack()

        label_date_fin = tk.Label(welcome_frame, text="Date de fin:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_date_fin.pack()
        self.entry_date_fin = DateEntry(welcome_frame,width=20, date_pattern="yyyy-mm-dd") 
        self.entry_date_fin.pack()

        label_duree_prise = tk.Label(welcome_frame, text="Durée de prise:", bg="white",fg= "#57a1f8",font= ("Time new roman", 11, "bold"))
        label_duree_prise.pack()
        self.entry_duree_prise = tk.Entry(welcome_frame, width=38 ,font=("Time new roman", 11))
        self.entry_duree_prise.pack()

        # Création d'un bouton pour sauvegarder les informations
        bouton_sauvegarder = tk.Button(welcome_frame, text="Sauvegarder", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.sauvegarder)
        bouton_sauvegarder.pack()


    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
        self.username_label = Label(self, text="Nom d'utilisateur : " + username)
        self.username_label.pack()

    def sauvegarder(self):
        # Récupérer les valeurs saisies par l'utilisateur
        nom_medicament = self.entry_nom_medicament.get()
        dosage = self.entry_dosage.get()
        nom_compro = self.entry_nom_compro.get()
        voie_administration = self.combobox_voie.get()
        date_debut = self.entry_date_debut.get()
        date_fin = self.entry_date_fin.get()
        duree_prise = self.entry_duree_prise.get()
        medicament_actuel = "prescrit"
        id_consultation = self.consultation_id_label.cget("text")


        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()


        # Insérer la voie d'administration dans la table "voie" si elle n'existe pas déjà
        #cursor.execute("INSERT IGNORE INTO voie (nom_voie) VALUES (%s)", (voie_administration,))
        cursor.execute("SELECT id_voie FROM voie WHERE nom_voie = %s", (voie_administration,))
        id_voie = cursor.fetchone()[0]

        # Insérer les informations du médicament dans la table "medicaments"
        cursor.execute("INSERT INTO medicament (nom_medicament, dosage, nom_compro, id_voie) VALUES (%s, %s, %s, %s)",
                       (nom_medicament, dosage, nom_compro, id_voie))
        
        id_medicament = cursor.lastrowid 

        cursor.execute("INSERT INTO traitement (id_medicament, id_consultation, medicament_actuel, date_debut, date_fin, duree_prise) VALUES (%s, %s, %s, %s, %s, %s)",
                       (id_medicament, id_consultation, medicament_actuel, date_debut, date_fin, duree_prise))

        # Valider les modifications et fermer la connexion à la base de données
        conn.commit()
        conn.close()

        self.entry_nom_medicament.delete(0, tk.END)
        self.entry_dosage.delete(0, tk.END)
        self.entry_nom_compro.delete(0, tk.END)
        self.entry_duree_prise.delete(0, tk.END)
        self.entry_date_fin.delete(0, tk.END)
        self.entry_date_debut.delete(0, tk.END)



        messagebox.showinfo("Succès", "Ajout du medicament au patient")

    def set_username(self, username):
        self.username_label.config(text= username)

    def interaction_medicament(self):
        # Récupérer les valeurs saisies par l'utilisateur
        nom_medicament = self.entry_nom_medicament.get()

        # Connexion à la base de données MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT médicament1 AS medicament, catégorie1 AS categorie, niveau "
               "FROM interaction_entre_medicaments "
               "WHERE médicament2 = %s "
               "UNION "
               "SELECT médicament2 AS medicament, catégorie2 AS categorie, niveau "
               "FROM interaction_entre_medicaments "
               "WHERE médicament1 = %s "
               "GROUP BY medicament, categorie, niveau",
               (nom_medicament, nom_medicament))
        
        interactions = cursor.fetchall()


        if interactions:
            afficher_interactions(interactions)
        else:
            messagebox.showinfo("Interactions possibles", "Le médicament ne présente pas d'interactions connues.")
    
    def set_consultation_id(self, consultation_id):
        self.consultation_id_label.config(text=consultation_id)

def afficher_interactions(interactions):
    # Créer une nouvelle fenêtre
    interactions_window = tk.Toplevel(bg="white")
    interactions_window.title("Interactions possibles")
   
    search_label = tk.Label(interactions_window, text="Recherche d'interaction :",fg= "black",bg="white",font= ("Time new roman", 11, "bold"))
    search_label.pack(pady=5)

    search_frame = tk.Frame(interactions_window, bg="white")
    search_frame.pack(pady=5)

    # Créer une boîte de recherche
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT)
    
    # Fonction de recherche
    def rechercher():
        search_text = search_entry.get().lower()
        interactions_table.delete(*interactions_table.get_children())
        for interaction in interactions:
            if search_text in interaction[0].lower() or search_text in interaction[1].lower() or search_text in interaction[2].lower():
                interactions_table.insert('', tk.END, values=(interaction[0], interaction[1], interaction[2]))

    # Bouton de recherche
    search_button = tk.Button(search_frame, text="Rechercher", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 8, "bold"), command=rechercher)
    search_button.pack(pady=5)
    
    # Créer un tableau pour afficher les interactions
    interactions_table = ttk.Treeview(interactions_window, columns=("Médicament", "Catégorie", "Niveau"), show="headings")
    interactions_table.pack(fill=tk.BOTH, expand=True)


    # Ajouter des en-têtes de colonnes
    interactions_table.heading("Médicament", text="Médicament")
    interactions_table.heading("Catégorie", text="Catégorie")
    interactions_table.heading("Niveau", text="Niveau")


    # Ajouter des colonnes à la taille appropriée
    interactions_table.column("Médicament", width=100)
    interactions_table.column("Catégorie", width=100)
    interactions_table.column("Niveau", width=100)


    # Créer la barre de défilement
    scrollbar = ttk.Scrollbar(interactions_window, orient="vertical", command=interactions_table.yview)
    interactions_table.configure(yscrollcommand=scrollbar.set)

    # Placer la table et la scrollbar en utilisant le gestionnaire de positionnement pack
    interactions_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.LEFT, fill=tk.Y)

    # Configurer le redimensionnement de la fenêtre
    interactions_window.pack_propagate(False)

    # Afficher les interactions dans le tableau
    for interaction in interactions:
        interactions_table.insert('', tk.END, values=(interaction[0], interaction[1], interaction[2]))


    interactions_window.update_idletasks()
    width = 600
    height = 500
    x = (interactions_window.winfo_screenwidth() // 2) - (width // 2)
    y = (interactions_window.winfo_screenheight() // 2) - (height // 2)
    interactions_window.geometry(f"{width}x{height}+{x}+{y}")

class DocumentationScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=5)

        # Image de logo
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png")
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8")
        self.label.pack(anchor=tk.CENTER, padx=5)

        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8", text="Nephro Med", fg="white",
                              font=("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        # Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')
        
        # Créer le bouton de acceuil  
         # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
        
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)


       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)

        # Espacement entre logout et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8", text="Version 1.0", fg="white",
                                font=("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)

        links = [
            ("The Renal Drug Handbook","https://www.medicinainterna.net.pe/sites/default/files/The_Renal_Drug_Handbook_The_Ultimate.pdf"),
            ("Kidney International", "https://www.kidney-international.org/"),
            ("American Society of Nephrology (ASN)", "https://www.asn-online.org/"),
            ("National Kidney Foundation (NKF)", "https://www.kidney.org/"),
            ("Renal Association (UK)", "https://renal.org/"),
            ("UpToDate", "https://www.uptodate.com/home"),
            ("PubMed", "https://pubmed.ncbi.nlm.nih.gov/"),
            ("European Renal Association-European Dialysis and Transplant Association (ERA-EDTA)",
             "https://www.era-edta.org/"),
            ("American Journal of Kidney Diseases (AJKD)", "https://www.ajkd.org/"),
            ("Nephrology, Dialysis, Transplantation (NDT)", "https://academic.oup.com/ndt"),
            ("International Society of Nephrology (ISN)", "https://www.theisn.org/"),
            ("British Renal Society (BRS)", "https://www.britishrenal.org/"),
            ("The Renal Fellow Network", "https://renalfellow.blogspot.com/"),
            ("National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)",
             "https://www.niddk.nih.gov/"),
            ("Kidney Research UK", "https://www.kidneyresearchuk.org/"),
        ]

        for link_label, link_url in links:
            documentation_button = tk.Button(
                welcome_frame,
                width=80,
                pady=5,
                text=link_label,
                fg="#ffffff",  # Couleur de texte blanche
                bg="#57a1f8",
                activebackground="#7ca9f9",  # Couleur de surbrillance
                borderwidth=2,
                relief="solid",
                highlightthickness=0,
                highlightbackground="#1e5799" , # Couleur de contour
                font=("microsoft yahei ui light", 8, "bold italic"),
                border=0,
                command=lambda url=link_url: self.open_link(url)
            )
            documentation_button.pack(pady=5, padx=10, anchor='center')

    def open_link(self, url):
        webbrowser.open(url)

    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
        self.username_label = Label(self, text="Nom d'utilisateur : " + username)
        self.username_label.pack()


    def set_username(self, username):
        self.username_label.config(text=username)     

class ExamenCliniqueScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)    
        self.parent = parent
        

        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10) 


        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)


        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)


        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)


        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command= self.parent.show_patient_screen)
        medecin_button.pack(pady=5)


        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)
              
        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)


       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)

        ##############################################################################################################

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')

        frame1 = Frame(welcome_frame, bg="white")
        frame1.pack(anchor='w', padx=50, pady=1)
        self.image_retour = tk.PhotoImage(file="C:/Users/KAWTHER/VsCode/Doc/Images/previous.png")

        retour_button = tk.Button(frame1, bg="white", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= parent.show_ddconsultation_screen, image= self.image_retour)   
        # Ajuster l'apparence du bouton
        retour_button.config(compound=tk.LEFT, padx=5, pady=1)
        # Afficher le bouton
        retour_button.pack(side=tk.LEFT)


        self.consultation_label = tk.Label(welcome_frame, text="ID de la consultation :", fg="#57a1f8", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_label.pack(side="top")

        self.consultation_id_label = tk.Label(welcome_frame, text="", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        self.consultation_id_label.pack(side="top")


        style = ttk.Style()
        style.configure("Custom.TLabel", font=("Times New Roman", 11, "bold"), background="white")
        style.configure("Custom.TEntry", font=("Times New Roman", 11), background="white")
        style.configure("Custom.TButton", font=("Times New Roman", 11),fg="white")
        style.configure("Custom.TCheckbutton", font=("Times New Roman", 11, "bold"), background="white")


        self.examen_label = tk.Label(welcome_frame, text="Examens cliniques :", fg="#57a1f8", font=("Times New Roman", 14, "bold"), bg="white")
        self.examen_label.pack()

        # Création des conteneurs pour chaque partie
        frame1 = tk.Frame(welcome_frame, bg="white")
        frame1.pack(side="left", expand=True, fill="both",padx=5, pady=10)
        frame2 = tk.Frame(welcome_frame, bg="white")
        frame2.pack(side="left", expand=True, fill="both", padx=(0, 5), pady=10)



        # Champ d'entrée pour le nom de l'examen clinique
        nom_examen_label = tk.Label(frame1, text="Nom de l'examen :", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        nom_examen_label.pack(pady=10)
        self.nom_examen_var = tk.StringVar()
        self.nom_examen_dropdown = ttk.Combobox(frame1, textvariable=self.nom_examen_var, values=[
            "Poids",
            "Labstix",
            "Glycémie",
            "Tension"
        ])
        self.nom_examen_dropdown.pack()

        # Champ d'entrée pour la description de l'examen
        description_label = tk.Label(frame1, text="Description de l'examen :", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        description_label.pack(pady=10)
        self.description_entry = tk.Entry(frame1, width=25)
        self.description_entry.pack(pady=10)

        # Champ d'entrée pour la date de l'examen
        date_examen_label = tk.Label(frame1, text="Date de l'examen :", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        date_examen_label.pack(pady=10)
        self.date_examen_entry = DateEntry(frame1,width=20, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)
        self.date_examen_entry.pack(pady=10)

        # Champ d'entrée pour le résultat de l'examen
        resultat_label = tk.Label(frame1, text="Résultat de l'examen :", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        resultat_label.pack(pady=10)
        self.resultat_entry = tk.Entry(frame1, width=25)
        self.resultat_entry.pack(pady=10)

        # Bouton pour sauvegarder les informations dans la base de données
        save_button = tk.Button(frame1, text="Ajouter examen ", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"),command=self.sauvegarder_examen)
        save_button.pack(pady=10)


        # Champ d'entrée pour le symptôme
        symptome_label = tk.Label(frame2, text="Symptôme :", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        symptome_label.pack(pady=10)


        self.symptome_var = tk.StringVar()
        self.symptome_dropdown = ttk.Combobox(frame2, textvariable=self.symptome_var, values=[
            "Anurie",
            "Arthralgie",
            "Battements cardiaques rapides",
            "Bourdonnements d'oreilles",
            "Bouffissure de visage",
            "Brûlure mictionnelle",
            "Confusion",
            "Constipation",
            "Convulsions ou crises convulsives",
            "Crampes musculaires",
            "Diarrhée",
            "Difficulté à parler ou à comprendre la parole",
            "Difficulté à respirer ou respiration sifflante",
            "Douleurs abdominales",
            "Douleurs abdominales intenses",
            "Douleurs articulaires",
            "Douleurs lombaires",
            "Douleurs musculaires",
            "Douleurs pelviennes",
            "Douleurs thoraciques",
            "Douleurs à la poitrine",
            "Démangeaisons",
            "Engourdissement ou faiblesse soudaine d'un côté du corps",
            "Essoufflement",
            "Essoufflement au repos",
            "Essoufflement intense",
            "Éruptions cutanées",
            "Éruptions cutanées sévères ou éruptions cutanées généralisées",
            "Étourdissements sévères ou perte de conscience",
            "Évanouissements",
            "Fatigue persistante et sensation de faiblesse",
            "Fièvre",
            "Frissons",
            "Gonflement des pieds et des chevilles (œdème)",
            "Hypertension artérielle (pression artérielle élevée)",
            "Lombalgie",
            "Mal de gorge",
            "Maux de tête",
            "Maux de tête sévères",
            "Mictions fréquentes",
            "Nausées",
            "Palpitations cardiaques",
            "Perte d'appétit",
            "Perte de poids",
            "Pic d'HTA (hypertension artérielle)",
            "Protéinurie",
            "Pâleur de la peau",
            "Problèmes de concentration et de mémoire",
            "Sensation de brûlure en urinant",
            "Soif excessive",
            "Troubles du sommeil",
            "Urines fréquentes et abondantes ou, au contraire, diminution de la quantité d'urine",
            "Urines mousseuses ou présence de sang dans les urines",
            "Vertiges",
            "Yeux rouges",
            "Vision floue"
        ])
        self.symptome_dropdown.pack(pady=10)


        # Champ d'entrée pour la gravité
        gravite_label = tk.Label(frame2, text="Gravité :", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        gravite_label.pack(pady=10)
        self.gravite_var = tk.StringVar()
        self.gravite_dropdown = ttk.Combobox(frame2, textvariable=self.gravite_var, values=[
            "Légère",
            "Modérée",
            "Sévère",
            "Critique"
        ])
        self.gravite_dropdown.pack(pady=10)

        # Champ d'entrée pour la date du symptôme
        date_label = tk.Label(frame2, text="Date du symptôme :", fg="black", font=("Times New Roman", 12, "bold"), bg="white")
        date_label.pack(pady=10)
        self.date_entry = DateEntry(frame2, width=20, date_pattern="yyyy-mm-dd",background='white', foreground='black', borderwidth=0)
        self.date_entry.pack(pady=10)

        # Bouton pour soumettre les informations
        submit_button = tk.Button(frame2, text="Ajouter symptôme",  fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command= self.ajouter_symptome)
        submit_button.pack(pady=10)


    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
        self.username_label = Label(self, text="Nom d'utilisateur : " + username)
        self.username_label.pack()

    def set_consultation_id(self, consultation_id):
        self.consultation_id_label.config(text=consultation_id)
    
    def set_username(self, username):
        self.username_label.config(text= username)

    def sauvegarder_examen(self):
        # Récupérer les valeurs des champs
        nom_examen = self.nom_examen_var.get()
        description = self.description_entry.get()
        date_examen = self.date_examen_entry.get_date()
        resultat = self.resultat_entry.get()
        id_consultation = self.consultation_id_label.cget("text")


        # Insérer les données dans la base de données
        try:
            # Établir une connexion à la base de données
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="connexionbddappli"
            )

            # Créer un curseur pour exécuter les requêtes
            cursor = conn.cursor()

            # Insérer les données dans la table nom_examen
            insert_nom_examen_query = "INSERT INTO nom_examen (nom) VALUES (%s)"
            cursor.execute(insert_nom_examen_query, (nom_examen,))
            conn.commit()

            # Récupérer l'ID de l'examen inséré
            id_nom_examen = cursor.lastrowid

            # Insérer les données dans la table examen_clinique
            insert_examen_query = "INSERT INTO examen_clinique (id_nom_examen, description, date_examen, resultat, id_consultation) VALUES (%s, %s, %s, %s, %s)"
            examen_values = (id_nom_examen, description, date_examen, resultat, id_consultation)
            cursor.execute(insert_examen_query, examen_values)
            conn.commit()

            # Fermer le curseur et la connexion à la base de données
            cursor.close()
            conn.close()
            
            messagebox.showinfo("Succès", "Ajout de l'examen")

            # Réinitialiser les champs après la sauvegarde
            self.nom_examen_var.set('')
            self.description_entry.delete(0, tk.END)
            self.date_examen_entry.delete(0, tk.END)
            self.resultat_entry.delete(0, tk.END)

        except mysql.connector.Error as error:
            # Gérer les erreurs de connexion à la base de données
            print("Erreur lors de la connexion à la base de données:", error)

    def ajouter_symptome(self):
        symptome = self.symptome_dropdown.get()
        gravite = self.gravite_dropdown.get()
        date_symptome = self.date_entry.get()
        id_consultation = self.consultation_id_label.cget("text")


        # Connexion à la base de données
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="connexionbddappli"
        )
        cursor = conn.cursor()

        # Récupérer l'id du type de symptôme en fonction du nom du type de symptôme saisi
        select_type_query = "SELECT id_type_symptome FROM type_symptome WHERE nom_type_symptome = %s"
        cursor.execute(select_type_query, (symptome,))
        type_symptome = cursor.fetchone()

        # Récupérer l'id de la gravité du symptôme en fonction du nom de la gravité saisie
        select_gravite_query = "SELECT id_gravite_sympthome  FROM gravite_sympthome WHERE nom_gravite_sympthome = %s"
        cursor.execute(select_gravite_query, (gravite,))
        gravite_symptome = cursor.fetchone()

        if type_symptome and gravite_symptome:
            # Insérer le symptôme dans la table "symptome" avec les clés étrangères
            insert_query = "INSERT INTO symptome (id_type_symptome, id_gravite_symptome, date_symptome, id_consultation) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (type_symptome[0], gravite_symptome[0], date_symptome, id_consultation))
            conn.commit()
            messagebox.showinfo("Succès", "Symptôme ajouté avec succès.")
        else:
            messagebox.showerror("Erreur", "Le symptôme ou la gravité du symptôme est introuvable.")

        cursor.close()
        conn.close()

        # Réinitialiser les champs d'entrée après la soumission
        self.symptome_dropdown.set('')
        self.gravite_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

class PredictionScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)    
        self.parent = parent

        self.configure(bg="#57a1f8")

        # Création du conteneur principal
        self.home_screen = tk.Frame(self, bg="#57a1f8")
        self.home_screen.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10) 


        # Image de logo 
        self.img = Image.open("C:/Users/KAWTHER/VsCode/Doc/Images/kidney.png") 
        self.img = self.img.resize((150, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.home_screen, image=self.img, bg="#57a1f8") 
        self.label.pack(anchor=tk.CENTER, padx=5)


        # Créer un widget de Bienvenue
        self.label = tk.Label(self.home_screen, bg="#57a1f8",text="Nephro Med", fg="white" ,font= ("microsoft yahei ui light", 23, "bold"))
        self.label.pack(anchor=tk.CENTER)

        #Trait de séparation entre les frames
        separator = tk.Frame(self, bg="#57a1f8", width=1)
        separator.pack(side=tk.LEFT, fill=tk.Y, padx=10)


        # Création du cadre de bienvenue
        welcome_frame = tk.Frame(self, bg="white")
        welcome_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Espacement entre Nephro Med et le bouton Consultation
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=25)


        # Créer le bouton de acceuil  
        acceuil_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Acceuil", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=self)
        acceuil_button.pack(pady=5)
        
        # Créer le bouton de consultation  
        medecin_button = tk.Button(self.home_screen, width= 20, pady= 7,text="Consultation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0, command=parent.show_patient_screen)
        medecin_button.pack(pady=5)

        # Créer le bouton de prediction  
        prediction_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Prediction", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_prediction_screen)
        prediction_button.pack(pady=5)

        # Créer le bouton de paramètre  
        parametre_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Paramètre", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_doctor_screen)
        parametre_button.pack(pady=5)

       # Créer le bouton de statistique  
        statistique_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Statistiques", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0)
        statistique_button.pack(pady=5)

        # Créer le bouton de documentation
        documentation_button = tk.Button(self.home_screen, width= 20, pady= 7, text="Documentation", fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,command=parent.show_dcumentation_screen)
        documentation_button.pack(pady=5)

        # Créer le bouton de déconnexion
        logout_button = tk.Button(self.home_screen,  width= 20, pady= 7, fg="white", bg= "#57a1f8", font= ("microsoft yahei ui light", 11, "bold"), border= 0,text="Se déconnecter", command=self.logout)
        logout_button.pack(pady=5)


        # Espacement entre lougout  et la version
        spacer_label = tk.Label(self.home_screen, bg="#57a1f8")
        spacer_label.pack(pady=20)

        self.version = tk.Label(self.home_screen, bg="#57a1f8",text="Version 1.0", fg="white" ,font= ("microsoft yahei ui light", 9, "bold"))
        self.version.pack(anchor=tk.CENTER)


        ##############################################################################################################

        username =""

        frame = Frame(welcome_frame)
        frame.pack(anchor='ne', padx=40, pady=10)

        self.label = tk.Label(frame, text= "Bienvenue, " , bg="white",fg= "black", border= 0,font= ("Time new roman", 11, "bold"))
        self.label.pack(side='left')

        self.username_label = tk.Label(frame, text= username , bg="white",fg= "#57a1f8", border= 0,font= ("Time new roman", 11, "bold"))
        self.username_label.pack(side='left')



        ###############################################

        frame = tk.Frame(welcome_frame, bg="white")
        frame.pack(side="top")

        self.champ_label = tk.Label(frame, text="Prédiction du niveau de risque  avec une précision de :", fg="#57a1f8", font=("Times New Roman", 15, "bold"), bg="white")        
        self.precision_label = tk.Label(frame, text="84 %", fg="#32CD32", font=("Times New Roman", 15, "bold"), bg="white")

        self.champ_label.pack(side="left")
        self.precision_label.pack(side="left")
        
        frame1 = tk.Frame(welcome_frame, bg="white")
        frame1.pack(side="top",  pady=10)

        label_contre = tk.Label(frame1, text="Contre indication :", font=("Time new roman", 12), bg="white")
        label_contre.pack(side="left", padx=5, pady=10)

        # Chargement des options depuis le fichier Excel
        data1 = pd.read_excel("Files/dataset.xlsx", sheet_name="Feuil3")
        filtered_data1 = data1['Contre indication'].drop_duplicates().tolist()
        
        def filter_options1(*args):
            search_text = self.combobox_contre.get()
            filtered_values1 = [value for value in filtered_data1 if search_text.lower() in value.lower()]
            self.combobox_contre.configure(values=filtered_values1)

        # Création du Combobox  
        self.combobox_contre = ttk.Combobox(frame1, font=("Time new roman", 12), width=30)
        self.combobox_contre.pack(side="left", padx=5, pady=10)
        self.combobox_contre["values"] = filtered_data1
        self.combobox_contre.bind("<<ComboboxSelected>>")
        self.combobox_contre.bind("<KeyRelease>", filter_options1)
             
        frame2 = tk.Frame(welcome_frame, bg="white")
        frame2.pack(side="top",  pady=10)
        
        label_type = tk.Label(frame2, text="Type indication :", font=("Time new roman", 12), bg="white")
        label_type.pack(side="left", padx=5, pady=10)

        values = ["Antécédant", "Syndrome", "Symptome","Situation particulière"]
   

        #Filtre sur le Combobox
        def filter_options2(*args):
            search_text = self.combobox_type.get()
            filtered_values = [value for value in values  if search_text.lower() in value.lower()]
            self.combobox_type.configure(values=filtered_values)

        # Création du Combobox  
        self.combobox_type = ttk.Combobox(frame2, font=("Time new roman", 12), width=30, values=values)
        self.combobox_type.pack(side="left", padx=5, pady=10)
        self.combobox_type.bind("<<ComboboxSelected>>")
        self.combobox_type.bind("<KeyRelease>", filter_options2)

        frame3 = tk.Frame(welcome_frame, bg="white")
        frame3.pack(side="top",  pady=10)

        label_medicament = tk.Label(frame3, text="Médicament :", font=("Time new roman", 12), bg="white")
        label_medicament.pack(side="left", padx=5, pady=10)


        # Chargement des options depuis le fichier Excel
        data = pd.read_excel("Files/dataset.xlsx", sheet_name="Feuil2")
        filtered_data = data['Nom medicament'].drop_duplicates().tolist()
        
        def filter_options3(*args):
            search_text = self.combobox_medicament.get()
            filtered_values = [value for value in filtered_data if search_text.lower() in value.lower()]
            self.combobox_medicament.configure(values=filtered_values)


        # Création du Combobox  
        self.combobox_medicament = ttk.Combobox(frame3, font=("Time new roman", 12), width=30)
        self.combobox_medicament.pack(side="left", padx=5, pady=10)
        self.combobox_medicament["values"] = filtered_data
        self.combobox_medicament.bind("<<ComboboxSelected>>")
        self.combobox_medicament.bind("<KeyRelease>", filter_options3)


        frame4 = tk.Frame(welcome_frame, bg="white")
        frame4.pack(side="top",  pady=10)

        label_categorie = tk.Label(frame4, text="Catégorie  :", font=("Time new roman", 12), bg="white")
        label_categorie.pack(side="left", padx=5, pady=10)

        # Chargement des options depuis le fichier Excel
        data4 = pd.read_excel("Files/dataset.xlsx", sheet_name="Feuil4")
        filtered_data4 = data4['Catégorie'].drop_duplicates().tolist()
        
        def filter_options4(*args):
            search_text = self.combobox_categorie.get()
            filtered_values4 = [value for value in filtered_data4 if search_text.lower() in value.lower()]
            self.combobox_categorie.configure(values=filtered_values4)

        # Création du Combobox  
        self.combobox_categorie = ttk.Combobox(frame4, font=("Time new roman", 12), width=30)
        self.combobox_categorie.pack(side="left", padx=5, pady=10)
        self.combobox_categorie["values"] = filtered_data4
        self.combobox_categorie.bind("<<ComboboxSelected>>")
        self.combobox_categorie.bind("<KeyRelease>", filter_options4)


        frame5 = tk.Frame(welcome_frame, bg="white")
        frame5.pack(side="top",  pady=10)
     
        label_voie = tk.Label(frame5, text="Voie d'administration  :", font=("Time new roman", 12), bg="white")
        label_voie.pack(side="left", padx=5, pady=10)


        values5 = ["orale", "injectable", "extracorporelle", "intraveineuse", "sous-cutanée",
          "Injectable", "ophtalmique", "inhalée", "systémique", "cutanée",
          "intrapéritonéale", "intraveineuse", "intramusculaire-intraveineuse (en perfusion)",
          "auriculaire"]

        
        def filter_options5(*args):
            search_text = self.combobox_voie.get()
            filtered_values = [value for value in values5  if search_text.lower() in value.lower()]
            self.combobox_voie.configure(values=filtered_values)


        # Création du Combobox  
        self.combobox_voie = ttk.Combobox(frame5, font=("Time new roman", 12), width=30, values=values5)
        self.combobox_voie.pack(side="left", padx=5, pady=10)
        self.combobox_voie.bind("<<ComboboxSelected>>")
        self.combobox_voie.bind("<KeyRelease>", filter_options5)

        button_container = tk.Frame(welcome_frame, bg="white")
        button_container.pack(pady=10)

        #Bouton pour les antécedants
        button_verifier = tk.Button(button_container, width=10, text="Vérifier", fg="white", bg="#57a1f8", border=0, cursor="hand2",font= ("Time new roman", 11, "bold"), command=self.encodage)   
        button_verifier.pack(side=tk.LEFT, padx=5, pady=10)


    def logout(self):
        # Réinitialiser l'état de l'application ou effectuer d'autres actions de déconnexion
        self.reset_application_state()
        # Retourner à la page de connexion
        self.parent.show_login_screen()

    def reset_application_state(self):
        # Fermer l'interface et se déconnecter
        self.master.destroy()
        self.username_label = Label(self, text="Nom d'utilisateur : " + username)
        self.username_label.pack()
   
    def set_username(self, username):
        self.username_label.config(text= username)
    
    def encodage(self):

        contre = self.combobox_contre.get()
        type = self.combobox_type.get()
        medicament = self.combobox_medicament.get()
        categorie  = self.combobox_categorie.get()
        voie  = self.combobox_voie.get()
        

        if not contre or not type or not medicament or not categorie or not voie:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

        else : 
            #Importer le modèle sauvgarder
            with open('Files/Random_forest.pkl', 'rb') as file:
                loaded_model = pickle.load(file)
        
            #Importer le label encodeur sauvgrader        
            with open('Files/label_encoders.pkl', 'rb') as file:
                label_encoders = pickle.load(file)  
        
            new = np.array([[contre,type,medicament,categorie ,voie]])


            new2 = pd.DataFrame(new, columns=['Contre indication', 
            'Type Contre indication', 'Nom medicament',
            'Catégorie',
            'Voie'])
        
            #Encodage 

            for col in new2.columns:
                if col in label_encoders:
                    le = label_encoders[col]
                    new_values = []
                    for value in new2[col]:
                        if value in le.classes_:
                            new_values.append(le.transform([value])[0])
                        else:
                            # Si la valeur est nouvelle, assigner un nouvel encodage
                            max_label = max(le.transform(le.classes_), default=-1) + 1
                            le.classes_ = np.append(le.classes_, value)
                            le_mapping = dict(zip(le.classes_, range(len(le.classes_))))
                            new_values.append(le_mapping[value])
                    new2[col] = new_values


            # Appliquer le modèle de Random Forest 
            predictions = loaded_model.predict(new2)
            risk_levels = ['Modéré', 'Haut', 'Critique']
            predicted_labels = [risk_levels[prediction] for prediction in predictions]
        
            # Enlever les ' et [] du résulat de predicted_labels
            predicted_labels_string = ', '.join(predicted_labels)


            niveau_window = tk.Toplevel(bg="white", width= 500, height= 500)
            niveau_window.title("Niveau de risque")


            # Obtenez la taille de la fenêtre principale
            window_width = self.winfo_width()
            window_height = self.winfo_height()

            # Obtention de la largeur et longueur du Toplevel
            toplevel_width = niveau_window.winfo_width()
            toplevel_height = niveau_window.winfo_height()

            # Calculer les coordonnées x et y pour centrer le Toplevel
            x = self.winfo_x() + (window_width // 2) - (toplevel_width // 2)
            y = self.winfo_y() + (window_height // 2) - (toplevel_height // 2)

            # Définir la géométrie du Toplevel pour le centrer
            niveau_window.geometry(f"+{x}+{y}")

            label = tk.Label(niveau_window, text= "Le niveau de risque entre  : ", fg= "black",bg="white",font= ("Time new roman", 12, "italic"))
            label.pack(pady=5)

            label_contre = tk.Label(niveau_window, text= contre, fg= "black",bg="white",font= ("Time new roman", 12, "italic"))
            label_contre.pack(pady=5)
        
            label_medicament = tk.Label(niveau_window, text= medicament, fg= "black",bg="white",font= ("Time new roman", 12, "italic"))
            label_medicament.pack(pady=5)

            if predicted_labels_string == 'Modéré':
                niveau_label = tk.Label(niveau_window, text= predicted_labels_string, fg= "#FFD700",bg="white",font= ("Time new roman", 11, "bold"))
                niveau_label.pack(pady=5)
            else :
                if predicted_labels_string == 'Haut':
                    niveau_label = tk.Label(niveau_window, text= predicted_labels_string, fg= "orange",bg="white",font= ("Time new roman", 11, "bold"))
                    niveau_label.pack(pady=5)
                else :
                    niveau_label = tk.Label(niveau_window, text= predicted_labels_string, fg= "red",bg="white",font= ("Time new roman", 11, "bold"))
                    niveau_label.pack(pady=5)

app = Application()
app.mainloop()    