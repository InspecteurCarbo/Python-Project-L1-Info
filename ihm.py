from tkinter import messagebox
from modele import *
import winsound
import time


#init des variables
old=[None, None]  #position des la souris
bateau=""         #bateauu sélectionné
x_bateau = [0,0]  #coordonnées du bateau sélectionné
y_bateau = [0,0]  #coordonnées du bateau sélectionné
long_bateau = 0   #longueur du bateau sélectionné
larg_bateau = 0   #largeur du bateau sélectionné
ok_bateau = 0     #bateau sélectionné placé sur la grille
x_final = [0,0]   #coordonnées du bateau sélectionné placé sur la grille
y_final = [0,0]   #coordonnées du bateau sélectionné placé sur la grille
nb_de_0 = -1
grille_ok = 0
son = "none"


#tableau pour dire comment l'ordi choisit les cases lorsqu'il joue.
List_alea = [i for i in range(0, 99)]
random.shuffle(List_alea)

def clic(event):
  global compteur, compteur_prec, grille_ok
  old[0]=event.x
  old[1]=event.y

  # en mode init, on sélectionne le bateau à placer et on créé la grille de l'ordi
  if etape.get()==0:
    # reconaissance du bateau
    global bateau
    global x_bateau, y_bateau
            
    # on regarde si les coordonnées de la soursi sont sur 1 des 5 bateaux
    # si oui, on sélectionne le bateau et ses coordonnées
    if cnv.coords(porteAvion)[0]<=old[0]<=cnv.coords(porteAvion)[2] and cnv.coords(porteAvion)[1]<=old[1]<=cnv.coords(porteAvion)[3]:
      bateau="porteAvion"
      x_bateau = (cnv.coords(porteAvion)[0] , cnv.coords(porteAvion)[2])
      y_bateau = (cnv.coords(porteAvion)[1] , cnv.coords(porteAvion)[3])
      #si le bateau est sélectionné, on le supprime de la grille joueur parce qu'il va être replacé
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==1:
            tab1[i][j]=0
    elif cnv.coords(croiseur)[0]<=old[0]<=cnv.coords(croiseur)[2] and cnv.coords(croiseur)[1]<=old[1]<=cnv.coords(croiseur)[3]:
      bateau="croiseur"
      x_bateau = (cnv.coords(croiseur)[0] , cnv.coords(croiseur)[2])
      y_bateau = (cnv.coords(croiseur)[1] , cnv.coords(croiseur)[3])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==2:
            tab1[i][j]=0
    elif cnv.coords(contreTorpilleur)[0]<=old[0]<=cnv.coords(contreTorpilleur)[2] and cnv.coords(contreTorpilleur)[1]<=old[1]<=cnv.coords(contreTorpilleur)[3]:
      bateau="contreTorpilleur"
      x_bateau = (cnv.coords(contreTorpilleur)[0] , cnv.coords(contreTorpilleur)[2])
      y_bateau = (cnv.coords(contreTorpilleur)[1] , cnv.coords(contreTorpilleur)[3])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==3:
            tab1[i][j]=0
    elif cnv.coords(sousMarin)[0]<=old[0]<=cnv.coords(sousMarin)[2] and cnv.coords(sousMarin)[1]<=old[1]<=cnv.coords(sousMarin)[3]:
      bateau="sousMarin"
      x_bateau = (cnv.coords(sousMarin)[0] , cnv.coords(sousMarin)[2])
      y_bateau = (cnv.coords(sousMarin)[1] , cnv.coords(sousMarin)[3])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==4:
            tab1[i][j]=0
    elif cnv.coords(torpilleur)[0]<=old[0]<=cnv.coords(torpilleur)[2] and cnv.coords(torpilleur)[1]<=old[1]<=cnv.coords(torpilleur)[3]:
      bateau="torpilleur"
      x_bateau = (cnv.coords(torpilleur)[0] , cnv.coords(torpilleur)[2])
      y_bateau = (cnv.coords(torpilleur)[1] , cnv.coords(torpilleur)[3])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==5:
            tab1[i][j]=0
            
    #lors du premier clic ou après un reset; on place les bateaux de l'ordi
    global creation_grille_ordi, son
    compteur = -1
    compteur_prec = -1
    if creation_grille_ordi ==0:
      grille_ordi(tab2)
      creation_grille_ordi += 1

  # en mode jeu, on vérifie si le joueur à toucher un bateau, puis on fait jouer l'ordi
  if etape.get()==1 and grille_ok==1 :
    global nb_bateau_joueur_coulé, nb_bateau_ordi_coulé
    

    #le joueur attaque
    #position de la souris
    xg2 =int((old[0]-510) / 40)
    yg2 =int((old[1]-10) / 40)
    #si le joueur a cliqué sur la grille de l'ordi
    if 0 < xg2 < 11  and 0 < yg2 < 11 :
      #si la valeur dans le tableau est comprise entre 1 et 5, c'est qu'on a trouché un bateau (pas encore touchée)
      if 0 < tab2[xg2][yg2] < 6:
        #image et son comme quoi on a touché
        tab2_img[xg2][yg2]=cnv.create_image(510+(40*xg2), 10+(40*yg2), image=touche, anchor='nw')
        #on mémorise que cette case a été touchée
        tab2[xg2][yg2] += 10

        #on vérifie si un bateau a été coulé
        #porteavion
        nb_bateau_ordi_coulé = nb_bateau_ordi_coulé + cherche_bateau(tab2,5,11,"joueur",img11,img12)[1]
        #croiseur
        nb_bateau_ordi_coulé = nb_bateau_ordi_coulé + cherche_bateau(tab2,4,12,"joueur",img13,img14)[1]
        #contretorpilleur
        nb_bateau_ordi_coulé = nb_bateau_ordi_coulé + cherche_bateau(tab2,3,13,"joueur",img15,img16)[1]
        #sousmarin
        nb_bateau_ordi_coulé = nb_bateau_ordi_coulé + cherche_bateau(tab2,3,14,"joueur",img15,img16)[1]
        #torpilleur
        nb_bateau_ordi_coulé = nb_bateau_ordi_coulé + cherche_bateau(tab2,2,15,"joueur",img17,img18)[1]

        #on incrémente le compteur qui autorise l'ordi à jouer
        compteur += 1

      elif tab2[xg2][yg2]==0:
        #si pas de bateau touché
        tab2_img[xg2][yg2]=cnv.create_image(510+(40*xg2), 10+(40*yg2), image=rate, anchor='nw')
        tab2[xg2][yg2] = 10
        #on incrémente le compteur qui autorise l'ordi à jouer
        compteur += 1

    #l'ordi_attaque
    #l'irdi attaque que si le joueur a joué une case valide
    if compteur != compteur_prec:
      compteur_prec = compteur
      #on prend une case aléatoire
      global List_alea
      List_alea[compteur]

      #les dizaine, c'est les x, les unités, c'est les y
      xgo = int (List_alea[compteur]/10)+1
      ygo = (List_alea[compteur]%10)+1

      #on vérifie si dans le tableau joueur il y a un bateau dans la case sélectionnée
      if 0 < tab1[xgo][ygo] < 6:
        #alors on place image et son "touché"
        tab1_img[xgo][ygo] = cnv.create_image(10+(40*xgo), 10+(40*ygo), image=touche, anchor='nw')
        
        #on mémorise que cette case a été touchée
        tab1[xgo][ygo] +=10

        #on vérifie si un bateau a été coulé
        #porteavion
        nb_bateau_joueur_coulé = nb_bateau_joueur_coulé + cherche_bateau(tab1,5,11,"ordi",img11,img12)[1]
        #croiseur
        nb_bateau_joueur_coulé = nb_bateau_joueur_coulé + cherche_bateau(tab1,4,12,"ordi",img13,img14)[1]
        #contretorpilleur
        nb_bateau_joueur_coulé = nb_bateau_joueur_coulé + cherche_bateau(tab1,3,13,"ordi",img15,img16)[1]
        #sousmarin
        nb_bateau_joueur_coulé = nb_bateau_joueur_coulé + cherche_bateau(tab1,3,14,"ordi",img15,img16)[1]
        #torpilleur
        nb_bateau_joueur_coulé = nb_bateau_joueur_coulé + cherche_bateau(tab1,2,15,"ordi",img17,img18)[1]

      elif tab1[xgo][ygo]==0:
        tab1_img[xgo][ygo] = cnv.create_image(10+(40*xgo), 10+(40*ygo), image=rate, anchor='nw')
    #décision du gagnant
    if nb_bateau_joueur_coulé == 5:
      messagebox.showinfo("résultat", "tu as perdu")
      winsound.PlaySound(Sound4,winsound.SND_FILENAME| winsound.SND_LOOP)
      etape.set(2)
    elif nb_bateau_ordi_coulé == 5:
      messagebox.showinfo("résultat", "tu as gagné ")
      winsound.PlaySound(Sound3,winsound.SND_FILENAME| winsound.SND_LOOP)
      
      etape.set(2)
  elif etape.get()==1 and grille_ok==0:
    messagebox.showinfo("erreur", "il doit y avoir une erreur dans le placement de tes bateaux !!      Si le problème persiste appuie sur le bouton reset")
    etape.set(0)
    

def glisser(event):

  if etape.get()==0:
    global bateau
    global old  
    global x_bateau, y_bateau
    global long_bateau, larg_bateau
    global ok_bateau , x_final, y_final
    
    # de combien on va bouger
    delta_x = event.x-old[0]
    delta_y = event.y-old[1]

    larg_bateau = (x_bateau[1] - x_bateau[0]) / 40
    long_bateau = (y_bateau[1] - y_bateau[0]) / 40

    # on verifie que la future position est dans la fenetre, sinon, on borne
    if x_bateau[0] + delta_x  < 10:
    # trop à gauche
      delta_x = 10-x_bateau[0]
    else:
      if x_bateau[1] + delta_x > 900-(40*larg_bateau):
      # trop à droite
        delta_x = 900-(40*larg_bateau)-x_bateau[1]
    if y_bateau[0] + delta_y < 10:
      # trop haut
      delta_y = 10 - y_bateau[0]
    else:
      if y_bateau[1] + delta_y > 900 - (40*long_bateau):
        # trop bas
        delta_y = 900 - (40*long_bateau) - y_bateau[1]
  
    x_bateau = (x_bateau[0]+delta_x , x_bateau[0]+delta_x + (40*larg_bateau)) 
    y_bateau = (y_bateau[0]+delta_y , y_bateau[0]+delta_y + (40*long_bateau))

    #position au-dessus de la grille
    xg =int((x_bateau[0]-10) / 40)
    yg =int((y_bateau[0]-10) / 40)

    if 0 < xg < 11 and 0 < xg + larg_bateau -1 < 11 and 0 < yg < 11 and 0 < yg + long_bateau-1  < 11:
      #on vérifie qu'il n'y a pas déjà un bateau
      ya_un_bateau=False
      for i in range(int(larg_bateau)):
        for j in range(int(long_bateau)):
          if tab1[xg+i][yg+j]!=0:
            ya_un_bateau=True
      if ya_un_bateau == False:
        ok_bateau = 1
        x_final = xg
        y_final = yg
      else:
        ok_bateau = 0
    else:
        ok_bateau = 0

    if bateau=="porteAvion":
      cnv.move(porteAvion, delta_x, delta_y)
      cnv.coords(porteavion_img,cnv.coords(porteAvion)[0],cnv.coords(porteAvion)[1])    
    if bateau=="croiseur":
      cnv.move(croiseur, delta_x, delta_y)
      cnv.coords(croiseur_img,cnv.coords(croiseur)[0],cnv.coords(croiseur)[1])
    if bateau=="contreTorpilleur":
      cnv.move(contreTorpilleur, delta_x, delta_y)
      cnv.coords(contreTorpilleur_img,cnv.coords(contreTorpilleur)[0],cnv.coords(contreTorpilleur)[1])
    if bateau=="sousMarin":
      cnv.move(sousMarin, delta_x, delta_y)
      cnv.coords(sousMarin_img,cnv.coords(sousMarin)[0],cnv.coords(sousMarin)[1])
    if bateau=="torpilleur":
      cnv.move(torpilleur, delta_x, delta_y)
      cnv.coords(torpilleur_img,cnv.coords(torpilleur)[0],cnv.coords(torpilleur)[1])

    old[0]=event.x
    old[1]=event.y


def on_release(event):
  if etape.get()==0:
    global bateau, grille_ok, nb_de_0
    global ok_bateau , x_final, y_final
    global x_bateau , y_bateau
      
    delta_x = (40*x_final +10) - x_bateau[0]
    delta_y = (40*y_final +10) - y_bateau[0]

    if ok_bateau==1:
      # faire glisser le bateau
      if bateau=="porteAvion":
        cnv.move(porteAvion, delta_x, delta_y)   
        cnv.coords(porteavion_img,cnv.coords(porteAvion)[0],cnv.coords(porteAvion)[1]) 
        for i in range(int(larg_bateau)):
          for j in range(int(long_bateau)):
            tab1[x_final+i][y_final+j]=1
      if bateau=="croiseur":
        cnv.move(croiseur, delta_x, delta_y)
        cnv.coords(croiseur_img,cnv.coords(croiseur)[0],cnv.coords(croiseur)[1])
        for i in range(int(larg_bateau)):
          for j in range(int(long_bateau)):
            tab1[x_final+i][y_final+j]=2    
      if bateau=="contreTorpilleur":
        cnv.move(contreTorpilleur, delta_x, delta_y)
        cnv.coords(contreTorpilleur_img,cnv.coords(contreTorpilleur)[0],cnv.coords(contreTorpilleur)[1])
        for i in range(int(larg_bateau)):
          for j in range(int(long_bateau)):
            tab1[x_final+i][y_final+j]=3      
      if bateau=="sousMarin":
        cnv.move(sousMarin, delta_x, delta_y)
        cnv.coords(sousMarin_img,cnv.coords(sousMarin)[0],cnv.coords(sousMarin)[1])
        for i in range(int(larg_bateau)):
          for j in range(int(long_bateau)):
            tab1[x_final+i][y_final+j]=4
      if bateau=="torpilleur":
        cnv.move(torpilleur, delta_x, delta_y)
        cnv.coords(torpilleur_img,cnv.coords(torpilleur)[0],cnv.coords(torpilleur)[1])
        for i in range(int(larg_bateau)):
          for j in range(int(long_bateau)):
            tab1[x_final+i][y_final+j]=5 
    else:
      #si bateau mal placé dans la grille, on le remt en bas
      if bateau=="porteAvion":
        larg=cnv.coords(porteAvion)[2] - cnv.coords(porteAvion)[0]
        long=cnv.coords(porteAvion)[3] - cnv.coords(porteAvion)[1]
        cnv.coords(porteAvion,10 ,540 ,10+larg, 540+long)
        cnv.coords(porteavion_img,cnv.coords(porteAvion)[0],cnv.coords(porteAvion)[1])
      if bateau=="croiseur":
        larg=cnv.coords(croiseur)[2] - cnv.coords(croiseur)[0]
        long=cnv.coords(croiseur)[3] - cnv.coords(croiseur)[1]
        cnv.coords(croiseur,55 ,540 ,55+larg, 540+long)
        cnv.coords(croiseur_img,cnv.coords(croiseur)[0],cnv.coords(croiseur)[1])
      if bateau=="contreTorpilleur":
        larg=cnv.coords(contreTorpilleur)[2] - cnv.coords(contreTorpilleur)[0]
        long=cnv.coords(contreTorpilleur)[3] - cnv.coords(contreTorpilleur)[1]
        cnv.coords(contreTorpilleur,100 ,540 ,100+larg, 540+long)
        cnv.coords(contreTorpilleur_img,cnv.coords(contreTorpilleur)[0],cnv.coords(contreTorpilleur)[1])    
      if bateau=="sousMarin":
        larg=cnv.coords(sousMarin)[2] - cnv.coords(sousMarin)[0]
        long=cnv.coords(sousMarin)[3] - cnv.coords(sousMarin)[1]
        cnv.coords(sousMarin,145 ,540 ,145+larg, 540+long)
        cnv.coords(sousMarin_img,cnv.coords(sousMarin)[0],cnv.coords(sousMarin)[1])    
      if bateau=="torpilleur":
        larg=cnv.coords(torpilleur)[2] - cnv.coords(torpilleur)[0]
        long=cnv.coords(torpilleur)[3] - cnv.coords(torpilleur)[1]
        cnv.coords(torpilleur,190 ,540 ,190+larg, 540+long)
        cnv.coords(torpilleur_img,cnv.coords(torpilleur)[0],cnv.coords(torpilleur)[1])    
      bateau=""
      x_bateau = [0,0]
      y_bateau = [0,0]
    
    #fonctionnement du bouton start si tous les bateaux sur la grille
    for i in range (11):
          for j in range (11):
            if tab1[i][j]==0:
              nb_de_0 += 1  
    print(nb_de_0)
    
    if nb_de_0!=103:
      nb_de_0 = -1
      grille_ok = 0
    else:
      grille_ok = 1


def clic_droit (event):
  if etape.get()==0:
    old[0]=event.x
    old[1]=event.y
      
    if cnv.coords(porteAvion)[0]<=old[0]<=cnv.coords(porteAvion)[2] and cnv.coords(porteAvion)[1]<=old[1]<=cnv.coords(porteAvion)[3]:
      bateau="porteAvion"
      larg=cnv.coords(porteAvion)[2] - cnv.coords(porteAvion)[0]
      long=cnv.coords(porteAvion)[3] - cnv.coords(porteAvion)[1]
      cnv.coords(porteAvion,10 ,540 ,10+long, 540+larg)
      if larg > long:
        cnv.itemconfigure(porteavion_img,image=img1)
      else:
        cnv.itemconfigure(porteavion_img,image=img2)
      cnv.coords(porteavion_img,cnv.coords(porteAvion)[0],cnv.coords(porteAvion)[1])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==1:
            tab1[i][j]=0
    elif cnv.coords(croiseur)[0]<=old[0]<=cnv.coords(croiseur)[2] and cnv.coords(croiseur)[1]<=old[1]<=cnv.coords(croiseur)[3]:
      bateau="croiseur"
      larg=cnv.coords(croiseur)[2] - cnv.coords(croiseur)[0]
      long=cnv.coords(croiseur)[3] - cnv.coords(croiseur)[1]
      cnv.coords(croiseur, 10 ,590 ,10+long, 590+larg)
      if larg > long:
        cnv.itemconfigure(croiseur_img,image=img3)
      else:
        cnv.itemconfigure(croiseur_img,image=img4)
      cnv.coords(croiseur_img,cnv.coords(croiseur)[0],cnv.coords(croiseur)[1])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==2:
            tab1[i][j]=0
    elif cnv.coords(contreTorpilleur)[0]<=old[0]<=cnv.coords(contreTorpilleur)[2] and cnv.coords(contreTorpilleur)[1]<=old[1]<=cnv.coords(contreTorpilleur)[3]:
      bateau="contreTorpilleur"
      larg=cnv.coords(contreTorpilleur)[2] - cnv.coords(contreTorpilleur)[0]
      long=cnv.coords(contreTorpilleur)[3] - cnv.coords(contreTorpilleur)[1]
      cnv.coords(contreTorpilleur,10 ,640 ,10+long, 640+larg)
      if larg > long:
        cnv.itemconfigure(contreTorpilleur_img,image=img5)
      else:
        cnv.itemconfigure(contreTorpilleur_img,image=img6)
      cnv.coords(contreTorpilleur_img,cnv.coords(contreTorpilleur)[0],cnv.coords(contreTorpilleur)[1])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==3:
            tab1[i][j]=0
    elif cnv.coords(sousMarin)[0]<=old[0]<=cnv.coords(sousMarin)[2] and cnv.coords(sousMarin)[1]<=old[1]<=cnv.coords(sousMarin)[3]:
      bateau="sousMarin"
      larg=cnv.coords(sousMarin)[2] - cnv.coords(sousMarin)[0]
      long=cnv.coords(sousMarin)[3] - cnv.coords(sousMarin)[1]
      cnv.coords(sousMarin,10 ,690 ,10+long, 690+larg)
      if larg > long:
        cnv.itemconfigure(sousMarin_img,image=img7)
      else:
        cnv.itemconfigure(sousMarin_img,image=img8) 
      cnv.coords(sousMarin_img,cnv.coords(sousMarin)[0],cnv.coords(sousMarin)[1])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==4:
            tab1[i][j]=0
    elif cnv.coords(torpilleur)[0]<=old[0]<=cnv.coords(torpilleur)[2] and cnv.coords(torpilleur)[1]<=old[1]<=cnv.coords(torpilleur)[3]:
      bateau="torpilleur"
      larg=cnv.coords(torpilleur)[2] - cnv.coords(torpilleur)[0]
      long=cnv.coords(torpilleur)[3] - cnv.coords(torpilleur)[1]
      cnv.coords(torpilleur,10 ,740 ,10+long, 740+larg)
      if larg > long:
        cnv.itemconfigure(torpilleur_img,image=img9)
      else:
        cnv.itemconfigure(torpilleur_img,image=img10)
      cnv.coords(torpilleur_img,cnv.coords(torpilleur)[0],cnv.coords(torpilleur)[1])
      for i in range(1,10):
        for j in range(1,10):
          if tab1[i][j]==5:
            tab1[i][j]=0


# étape du jeu
# 0 = init ou bouton reset - le joueur place les bateaux
# 1 = start - joueur joue, puis l'ordi
etape = tkinter.IntVar()
etape.set(0)
def debut_jeu():
  global son
  son = winsound.PlaySound(Sound2,winsound.SND_FILENAME| winsound.SND_ASYNC | winsound.SND_LOOP)
  etape.set(1)
  print(etape.get())
  return

def reset():
    #on replace les bateaux en bas
    cnv.coords(porteAvion,10 ,740 ,50, 540)
    cnv.itemconfigure(porteavion_img,image=img1)
    cnv.coords(porteavion_img,cnv.coords(porteAvion)[0],cnv.coords(porteAvion)[1])
    cnv.coords(croiseur, 55 ,700 ,95, 540)
    cnv.itemconfigure(croiseur_img,image=img3)
    cnv.coords(croiseur_img,cnv.coords(croiseur)[0],cnv.coords(croiseur)[1])
    cnv.coords(contreTorpilleur,100 ,660 ,140, 540)
    cnv.itemconfigure(contreTorpilleur_img,image=img5)
    cnv.coords(contreTorpilleur_img,cnv.coords(contreTorpilleur)[0],cnv.coords(contreTorpilleur)[1])
    cnv.coords(sousMarin,145 ,660 ,185 , 540)
    cnv.itemconfigure(sousMarin_img,image=img7)
    cnv.coords(sousMarin_img,cnv.coords(sousMarin)[0],cnv.coords(sousMarin)[1])
    cnv.coords(torpilleur,190 ,620 ,230 , 540)
    cnv.itemconfigure(torpilleur_img,image=img9)
    cnv.coords(torpilleur_img,cnv.coords(torpilleur)[0],cnv.coords(torpilleur)[1])
    winsound.PlaySound(None, winsound.SND_ASYNC)
    
    for i in range(11):
        for j in range(11):
            #on remet les grilles joueur et ordi de jeu à 0
            tab1[i][j]=0
            tab2[i][j]=0
            #on supprime les widget touché/splash/coulé
            cnv.delete(tab1_img[i][j])
            cnv.delete(tab2_img[i][j])
            cnv.delete(tab1_coule_img[i][j])
            cnv.delete(tab2_coule_img[i][j])
    #on remet le jeu en mode init pour que le joueur replace les bateaux
    etape.set(0)
    #on remet à 0 la creation de la grille ordi pour qu'elle soit recalculée
    global creation_grille_ordi
    creation_grille_ordi=0
    #on remet à 0 le nombre de bateau coulé
    global nb_bateau_joueur_coulé , nb_bateau_ordi_coulé, nb_de_0, grille_ok, son
    nb_bateau_joueur_coulé = 0
    nb_bateau_ordi_coulé = 0
    nb_de_0 = -1
    grille_ok = 0
    son="none"
    return


#placement des boutons
btn = Button(root, text="Start", width=40, command=debut_jeu)
btn_w = cnv.create_window(480, 600, window=btn)

btn2 = Button(root, text="Reset", width=40, command=reset)
btn_w = cnv.create_window(480, 640, window=btn2)

btn3 = Button(root, text="Option", width=40)
btn_w = cnv.create_window(480, 680, window=btn3)



cnv.bind("<Button-1>",clic)
cnv.bind("<B1-Motion>",glisser)
cnv.bind("<ButtonRelease-1>", on_release)
cnv.bind("<ButtonRelease-3>",clic_droit)
  
