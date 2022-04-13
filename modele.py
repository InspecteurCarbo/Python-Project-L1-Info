from tkinter import *
from functools import *
import tkinter
import random


root = Tk()

#chargement des imgaes
temp_img = PhotoImage(file='images/warship4-1-ConvertImage.png')
img1 = PhotoImage(file='images/images1.png')
img2 = PhotoImage(file='images/images2.png')
img3 = PhotoImage(file='images/images3.png')
img4 = PhotoImage(file='images/images4.png')
img5 = PhotoImage(file='images/images5.png')
img6 = PhotoImage(file='images/images6.png')
img7 = PhotoImage(file='images/images7.png')
img8 = PhotoImage(file='images/images8.png')
img9 = PhotoImage(file='images/images9.png')
img10 = PhotoImage(file='images/images10.png')
touche = PhotoImage(file='images/boom1.png')
rate = PhotoImage(file='images/splash2.png')
img11 = PhotoImage(file='images/porteavion_coule1.png')
img12 = PhotoImage(file='images/porteavion_coule2.png')
img13 = PhotoImage(file='images/croiseur_coule1.png')
img14 = PhotoImage(file='images/croiseur_coule2.png')
img15 = PhotoImage(file='images/contreTorpilleur_coule1.png')
img16 = PhotoImage(file='images/contreTorpilleur_coule2.png')
img17 = PhotoImage(file='images/torpilleur_coule1.png')
img18 = PhotoImage(file='images/torpilleur_coule2.png')

#chargement des sons
Sound2 = "son/Battleship"
Sound3 = "son/Rick-roll"
Sound4 = "son/Trololo"

#création fenêtre
cnv = Canvas(root, width=1000, height=1000)
cnv.pack()
cnv.create_image(500, 500, image=temp_img)

#création des grilles
#grille des coordonnés
for h in range (2):

    for i2 in range(10):   
        L=40
        A=(a, b)=(50+(i2*40)+h*500, 10)
        B=(a+L, b+L)
        k2=i2+1
        cnv.create_rectangle(A, B, fill='white', outline='black', width='2')
        cnv.create_text(i2*L+70+h*500, L-10, text=k2, fill="black")
        
    for i in range(10):
        L=40
        A=(a, b)=(10+h*500, 50+(i*40))
        B=(a+L, b+L)
        k=i+65
        cnv.create_rectangle(A, B, fill='white', outline='black', width='2')
        cnv.create_text(L-10+h*500, i*L+70, text=chr(k), fill="black")

#grille de l'ordi et du joueur
for h2 in range (2):
    for i3 in range (10):
        for j in range (10):
            L=40
            A=(a, b)=(50+(j*40)+h2*500, 50+(i3*40))
            B=(a+L, b+L)
            cnv.create_rectangle(A, B, outline='black', width='2')


#création des bateaux (rectangle) placés en bas + collé image dessus
porteavion_img=cnv.create_image(10, 540, image=img1, anchor='nw')
porteAvion = cnv.create_rectangle((10, 740), (50, 540), fill="red",stipple="gray12")
croiseur_img=cnv.create_image(55, 540, image=img3, anchor='nw')
croiseur = cnv.create_rectangle((55, 700), (95, 540), fill='blue',stipple="gray12")
contreTorpilleur_img=cnv.create_image(100, 540, image=img5, anchor='nw')
contreTorpilleur = cnv.create_rectangle((100, 660), (140, 540), fill='green',stipple="gray12")
sousMarin_img=cnv.create_image(145, 540, image=img7, anchor='nw')
sousMarin = cnv.create_rectangle((145, 660), (185, 540), fill='yellow',stipple="gray12")
torpilleur_img=cnv.create_image(190, 540, image=img9, anchor='nw')
torpilleur = cnv.create_rectangle((190, 620), (230, 540), fill='pink',stipple="gray12")


#création de tableau 10*10 image de où sont les bateaux
# 0 = pas de bateau
# 1 = porte-avion        11 = porte-avion touché
# 2 = croiseur           12 = croiseur touché
# 3 = contre-tropilleur  13 = contre-tropilleur touché
# 4 = sous-marin         14 = sous-marin touché
# 5 = torpilleur         15 = torpilleur touché
tab1=[[0]*11 for _ in range(11)]
tab2=[[0]*11 for _ in range(11)]

#tableau des widgets qui devront être supprimé si reset
tab1_img=[[0]*11 for _ in range(11)]
tab2_img=[[0]*11 for _ in range(11)]
tab1_coule_img=[[0]*11 for _ in range(11)]
tab2_coule_img=[[0]*11 for _ in range(11)]


#variable pour compter le nombre de bateau coulé
nb_bateau_joueur_coulé = 0
nb_bateau_ordi_coulé = 0

#fonction pour poser les bateaux de l'ordi. appelé à l'inti et si reset
creation_grille_ordi = 0 
def grille_ordi(tab2):
    hv=["horizontal", "verticale"]
    #porteAvion_ordi
    if random.choice(hv)=="horizontal":
        x=random.randint(1,5)
        y=random.randint(1,10)
        for i in range(5):
          tab2[x+i][y]=1
    else:
        x=random.randint(1,10)
        y=random.randint(1,5)
        for i in range(5):
          tab2[x][y+i]=1
    #croiseur_ordi
    if random.choice(hv)=="horizontal":
        continuer=True
        while continuer:
            x=random.randint(1,6)
            y=random.randint(1,10)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(4):
                if tab2[x+i][y]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(4):
                    tab2[x+i][y]=2
                continuer=False
    else:
        continuer=True
        while continuer:
            x=random.randint(1,10)
            y=random.randint(1,6)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(4):
                if tab2[x][y+i]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(4):
                    tab2[x][y+i]=2
                continuer=False
    #contreTorpilleur_ordi
    if random.choice(hv)=="horizontal":
        continuer=True
        while continuer:
            x=random.randint(1,7)
            y=random.randint(1,10)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(3):
                if tab2[x+i][y]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(3):
                    tab2[x+i][y]=3
                continuer=False
    else:
        continuer=True
        while continuer:
            x=random.randint(1,10)
            y=random.randint(1,7)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(3):
                if tab2[x][y+i]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(3):
                    tab2[x][y+i]=3
                continuer=False
    #sousMarin_ordi
    if random.choice(hv)=="horizontal":
        continuer=True
        while continuer:
            x=random.randint(1,7)
            y=random.randint(1,10)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(3):
                if tab2[x+i][y]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(3):
                    tab2[x+i][y]=4
                continuer=False
    else:
        continuer=True
        while continuer:
            x=random.randint(1,10)
            y=random.randint(1,7)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(3):
                if tab2[x][y+i]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(3):
                    tab2[x][y+i]=4
                continuer=False
    #torpilleur_ordi
    if random.choice(hv)=="horizontal":
        continuer=True
        while continuer:
            x=random.randint(1,8)
            y=random.randint(1,10)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(2):
                if tab2[x+i][y]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(2):
                    tab2[x+i][y]=5
                continuer=False
    else:
        continuer=True
        while continuer:
            x=random.randint(1,10)
            y=random.randint(1,8)
            #il faut poser un bateau si il n'y en a pas déajà 1 sur les cases
            ya_un_bateau=False
            for i in range(2):
                if tab2[x][y+i]!=0:
                    #y'a déjà un bateau, on recommence
                    ya_un_bateau=True
            if ya_un_bateau==False:
                #y'a pas de bateau, on plage le nouveau et on sort de la boucle
                for i in range(2):
                    tab2[x][y+i]=5
                continuer=False
    return tab2



def cherche_bateau(tab,long_bateau,type_bateau,type_joueur ,image1, image2):
    bateau_coulé=0
    nb_fois_touche=0
    #on verifie combien de fois on a le bateau touché dans le tableau
    for i in range(11):
        for j in range(11):
            if tab[i][j] ==type_bateau:
                nb_fois_touche +=1
    #si le nombre de fois touché est égal à la longueur du bateau => coulé
    if nb_fois_touche == long_bateau:
        #si un bateau a été coulé, on place l'image coulé, et on compte combien de bateau on été coulé
        bateau_coulé=1
        x=-1
        y=-1
        for i in range(11):
            for j in range(11):
                if tab[i][j]==type_bateau:
                    x=i
                    y=j
                    break
                if x != -1:
                    break
        #on verifie si le bateau est horizpntal
        if x<10 and tab[x+1][y]==type_bateau:
            #on mémorise que le bateau est coulé pour ne pas le re-coulé
            for i in range(0 , long_bateau-1):
                tab[x+i][y] = 110 + type_bateau
            if type_joueur=="ordi":
                tab1_coule_img[x][y]=cnv.create_image(10+(40*x), 10+(40*y), image=image1, anchor='nw')
            else:
                tab2_coule_img[x][y]=cnv.create_image(510+(40*x), 10+(40*y), image=image1, anchor='nw')
        else:
            for i in range(0 , 1):
                tab[x][y+i] = 110 + type_bateau
            if type_joueur=="ordi":
                tab1_coule_img[x][y]=cnv.create_image(10+(40*x), 10+(40*y), image=image2, anchor='nw')
            else:
                tab1_coule_img[x][y]=cnv.create_image(510+(40*x), 10+(40*y), image=image2, anchor='nw')
    return [tab,bateau_coulé]

