# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox

#Création interface
interface_crypto = Tk()
interface_crypto.title('[NSI : MP1] Crypto System By [JE NE VOUS LE DIRAI PAS!!]')
interface_crypto.geometry("500x500")
interface_crypto.resizable(0, 0)

#Cryptage avec clé
def crypto(chaine: str, cle: int) -> str:
    #Sécurité
    cle = abs(cle) % 26
    #Alphabet plus position conversion de A
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posA = abs(cle)
    #Output var
    out = ""
    #Bouclage de conversion
    for i in chaine:
        pre = 0
        pos = 0
        for j in range(26):
            if i == alphabet[j]:
                pre = 1
                pos = j
        if pre == 1:
            out += alphabet[(posA + pos)%26]
        else:
            out += i
    return out

#Partie 1 de l'interface
    #Label
message1 = Label(interface_crypto,text='Entrée texte à crypter\nEntrée clé de cryptage')
message1.pack()
    #Entrée
crypto_b = Entry(interface_crypto)
crypto_b.pack()
crypto_key_b = Entry(interface_crypto)
crypto_key_b.pack()
message_out1 = Label(interface_crypto,text="Sortie")
message_out1.pack()
crypto_out = Entry(interface_crypto)
crypto_out.pack()
    #Méthode
def cryptoB():
    Ans = crypto(crypto_b.get(), int(crypto_key_b.get()))
    crypto_out.delete(0,END)
    crypto_out.insert(0,Ans)
    tkinter.messagebox.showinfo(title="Crypto",message=Ans)

    #Bouton
button_crypto = Button(interface_crypto, text="1-Cryptage d'un texte à partir d'une clé fournie", command = cryptoB)
button_crypto.pack()


#Décrytage avec une clé
def decrypto(chaine: str, cle: int) -> str:
    #Sécurité
    cle = abs(cle) % 26
    #Alphabet plus position conversion de A
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posA = abs(26 - cle)
    #Output var
    out = ""
    #Bouclage de conversion
    for i in chaine:
        pre = 0
        pos = 0
        for j in range(26):
            if i == alphabet[j]:
                pre = 1
                pos = j
        if pre == 1:
            out += alphabet[(posA + pos)%26]
        else:
            out += i
    return out

#Partie 2 de l'interface
    #Label
message2 = Label(interface_crypto,text='\nEntrée texte à décrypter\nEntrée clé de décryptage')
message2.pack()
    #Entrée
decrypto_b = Entry(interface_crypto)
decrypto_b.pack()
decrypto_key_b = Entry(interface_crypto)
decrypto_key_b.pack()
message_out2 = Label(interface_crypto,text="Sortie")
message_out2.pack()
crypto_out2 = Entry(interface_crypto)
crypto_out2.pack()
    #Méthode
def decryptoB():
    Ans = decrypto(decrypto_b.get(), int(decrypto_key_b.get()))
    crypto_out2.delete(0,END)
    crypto_out2.insert(0,Ans)
    tkinter.messagebox.showinfo(title="Decrypto",message=Ans)

    #Bouton
button_decrypto = Button(interface_crypto, text="2-Décryptage d'un texte à partir d'une clé fournie", command = decryptoB)
button_decrypto.pack()

#Partie 3 de l'interface
    #Label
message3 = Label(interface_crypto,text='\nEntrée texte à décrypter')
message3.pack()
    #Entrée
decrypto_b_2 = Entry(interface_crypto)
decrypto_b_2.pack()
    #Méthode
def decryptoB2():
    decrypto_brute(decrypto_b_2.get())

message_out3 = Label(interface_crypto,text="Sortie")
message_out3.pack()
crypto_out3 = Entry(interface_crypto)
crypto_out3.pack()

    #Bouton
button_decrypto = Button(interface_crypto, text="3-Décryptage d'un texte sans la clé", command = decryptoB2)
button_decrypto.pack()


#Décrytage par force brute
def decrypto_brute(chaine: str) -> str:
    index = 1
    status = True
    while status and index < 27:
        Ans = decrypto(chaine, index)
        crypto_out3.delete(0,END)
        crypto_out3.insert(0,Ans)
        tkinter.messagebox.showinfo(title="Decrypto Brute",message="Essai avec une clé de "+str(index)+"\n"+Ans)
        changer = tkinter.messagebox.askyesno(message="\nSi vous visualisez le texte en clair cliquer 'yes'/'oui' sinon 'no'/'non'\n")
        if changer:
            status = False
        else:
            index += 1
    if status:
        crypto_out3.delete(0,END)
        tkinter.messagebox.showinfo(message="\nDésolé, vous avez essayé toutes les valeurs de clé, le texte a été crypté selon une méthode non mono-alphabétique")



#Fermeture/Partie 4 de l'interface
message4 = Label(interface_crypto,text='\nFin programme')
message4.pack()
end_button = Button(interface_crypto, text='4-fin du programme', command =  interface_crypto.destroy)
end_button.pack()

interface_crypto.mainloop()
