import sys
import re
print("\n\nBienvenue sur notre repertoire de gestion de contacts")
print("Pour commencer vous devez choisir parmis les indices de notre menu\n")
def menu():
    
    print("                                           *     MENU GESTION DE CONTACTS     *")
    print("                                           ************************************")
    print("******************************************* 1=> AFFICHER LA LISTE DES CONTACTS ******************************************")
    print("******************************************* 2=> RECHERCHE DE CONTACT           ******************************************")
    print("******************************************* 3=> POUR L'AJOUT DE CONTACT        ******************************************")    
    print("******************************************* 4=> MODIFIER UN CONTACT            ******************************************")
    print("******************************************* 5=> SUPPRIMER UN CONTACT           ******************************************")
    print("******************************************* 6=> SUPPRIMER TOUT LES CONTACT     ******************************************")
    print("******************************************* 7=> QUITTER                        ******************************************")
    print("                                           ************************************")
    print("\nMerci de faire votre choix?\n")
    choix=input(">>>>>")
    if choix=="1":
        Lister_Contact()
    elif choix=="2":
        Rechercher_Contact()
    elif choix=="3":
        Ajouter_Contact()
    elif choix=="4":
        Modifier_contact()
    elif choix=="5":
        Supprimer_Contact()
    elif choix=="6":
        Supprimer_Tout_Contact()
    elif choix=="7":
        print("Merci pour votre visite\nA la prochaine bye!!!!")
        sys.exit()
    else:
        print("Choix non disponible")
        
        
    

repertoire="repertoire.txt"
def Supprimer_Tout_Contact():
    f = open(repertoire, 'w')
    f.write("")
    f.close()
    
"""
Fonction permettant de faire l'ajout dans 
"""
def Ajouter_Contact():
    test_nom=re.compile("^[a-zA-Z0-9_ ]*$")
    test_tel=re.compile("^[0-9]*$")
    print("***************Ajout contact********************")
    nom=input("Votre nom \n")
    while test_nom.findall(nom)==[]:
        nom=input("Nom incorrect \n")
    if nom=="":
        nom="vide"
    """
    On vérifie si le contact a ajouter existe dans le repertoire
    """
    resultat_recherche=[]
    indice=[]
    f = open(repertoire, 'r')
    i=-1
    for ligne in f:
        i=i+1
        contact=ligne.split("   ")
        if contact[0]==nom:
            resultat_recherche.append(contact)
            indice.append(i)
    if len(resultat_recherche)>=1:
        print("Le nom que vous souhaitez ajoutez dans le repertoire existe deja \n")
        for result in resultat_recherche:
            print("Détails {} ".format(result))
        rep=input("Souhaitez vous faire une mise à jour \ntapez \n1. Pour faire une mise à jour \n2. Pour un nouveau ajout\n")
        if rep=="2":
            numero=input("Votre numero\n")
            while test_tel.findall(numero)==[] or numero=="":
                print("numero incorrect")
                numero=input("Votre numero\n")              
            rep_tel2=input("Voulez ajoutez un autre numero O/N?\n")
            choix_rep_tel2=["o","O","oui","","Oui","OUI"]
            if rep_tel2 in choix_rep_tel2:
                tel2=input("Saisir le numéro\n")
                while test_tel.findall(tel2)==[] or tel2=="":
                    tel2=input("numéro incorrect\n")
                new_Contact=nom+"   "+numero+"/"+tel2
            else:
                new_Contact=nom+"   "+numero
            f = open(repertoire, 'a')
            f.write(new_Contact)
            f.write("\n")
            f.close()
            print("Ajout avec succes")
        elif rep=="1":
            for resulta,j in zip(resultat_recherche,indice):
                res=result[1].strip("\n")
                f = open(repertoire, 'r')
                m=f.read()
                pos=m.split("\n")
                modif_tel_existant=input("Souhaitez vous modifier le téléphone existant O/N?\n")
                choix_modif_tel_existant=["o","O","oui","","Oui","OUI"]
                if modif_tel_existant in choix_modif_tel_existant:
                    tel=input("Entrez le nouveau téléphone\n")
                    while test_tel.findall(tel)==[]or tel=="":
                        tel=input("numéro incorrect\n")
                else:
                    tel=res
                ajout_tel2=input("Voulez vous ajoutez un deuxieme numero a ce contact O/N?\n")
                if ajout_tel2 in choix_modif_tel_existant:
                    tel2=input("Entrez le second numéro\n")
                    while test_tel.findall(tel2)==[]or tel2=="":
                        tel2=input("numéro incorrect\n")
                    pos[j]=nom+"    "+tel+"/"+tel2
                else:
                    pos[j]=nom+"    "+tel
                es=""
                es="\n".join(pos)
                f.close()
                l = open(repertoire, 'w')
                l.write(es)
                l.close()
                print("\nMis à jour réussit")
    else:
        
        numero=input("Votre numero\n")
        while test_tel.findall(numero)==[]or numero=="":
            numero=input("numéro incorrect\n")
        rep_tel2=input("Voulez ajoutez un autre numero O/N?\n")
        choix_rep_tel2=["o","O","oui","","Oui","OUI"]
        if rep_tel2 in choix_rep_tel2:
            tel2=input("Saisir le numéro\n")
            while test_tel.findall(tel2)==[]or tel2=="":
                tel2=input("numéro incorrect\n")
            new_Contact=nom+"   "+numero+"/"+tel2
        else:
            new_Contact=nom+"   "+numero
        f = open(repertoire, 'a')
        f.write(new_Contact)
        f.write("\n")
        f.close()
        print("Ajout avec succes")
       
"""
Cette fonction permet de faire une recherche
suivant le nom ou le numero de téléphne
"""
def Rechercher_Contact():
    resultat_recherche=[]
    print("*****************Menu de recherche*********")
    cherche=input("Saisir le nom à rechercher\n")
    f = open(repertoire, 'r')
    for ligne in f:
        contact=ligne.split("   ")
        if cherche in str(contact):
            resultat_recherche.append(contact)
    if len(resultat_recherche)>=1:
        print("On a {0} résultats associé(s) au contact {1} ".format(len(resultat_recherche),cherche))
        print("Voici les details de la recherche :\n")
        for result in resultat_recherche:
            print("Nom : {0}\nTéléphone : {1} ".format(result[0],result[1]))
    else:
        print("Le contact {} n'existe pas ".format(cherche))
    f.close() 
        
    #print("Nom : {0} Téléphone : {1} ".format(contact[0],contact[1]))
    f.close()
"""
Fonction permettant de faire la suppression de contact
"""
def Supprimer_Contact():
    print("*****************Supprimer de recherche*********\n")
    resultat_recherch_sup=[]
    indice=[]
    sup=input("Saisir le nom du contact à suppprimer\n")
    f = open(repertoire, 'r+')
    i=-1
    for ligne in f.readlines():
        i=i+1
        s=ligne.split("   ")
        if sup == s[0]:
            resultat_recherch_sup.append(ligne)
            indice.append(i)
            #resultat_recherch_sup.append(contact)
            #break
    f.close()  
    if len(resultat_recherch_sup)==1:
        print("Il y a {0} numero(s) associé(s) au contact {1} \n".format(len(resultat_recherch_sup),sup))
        for result in resultat_recherch_sup:
            result= result.split("  ")
            print("Nom : {0} Téléphone : {1} ".format(result[0],result[1]))
            t = open(repertoire, 'r')
            m=t.read()
            m=m.split("\n")
            m.pop(indice[0])
            es=""
            es="\n".join(m)
            t.close()
            l = open(repertoire, 'w')
            l.write(es)
            l.close()
            print("\nsupression réeussit")
    elif len(resultat_recherch_sup)>1:
        print("Il y a {0} numero(s) associé(s) au contact {1} ".format(len(resultat_recherch_sup),sup))
        for result,j in zip(resultat_recherch_sup,indice):
            result= result.split("  ")
            print("Position {2} Nom : {0} Téléphone : {1}  ".format(result[0],result[1],j))
        num=eval(input("veuillez saisir la position du contact à supprimer\n"))
        if num in indice:
            t = open(repertoire, 'r')
            m=t.read()
            m=m.split("\n")
            m.pop(num)
            es=""
            es="\n".join(m)
            t.close()
            l = open(repertoire, 'w')
            l.write(es)
            l.close()
            print("supression réeussit")
        #num_sup=input("Choisir le numero associé")
        #for num in resultat_recherch_sup:       
            
    else:
        print("Le contact {} n'existe pas dans la liste des contacts".format(sup))
    
"""
Fonction permettant d'afficher la liste des contacts
"""
def Lister_Contact():
    print("Menu de contact")
    f = open(repertoire, 'r')
    for ligne in f:
        contact=ligne.split("   ")
        c="{0}  : {1} ".format(contact[0],contact[1])
        print (c.rstrip())
    f.close()
"""
    Fonction permettant de modifier un contact
"""
def Modifier_contact():
    test_nom=re.compile("^[a-zA-Z0-9_ ]*$")
    test_tel=re.compile("^[0-9]*$")
    resultat_recherch_sup=[]
    indice=[]
    sup=input("\nSaisir le nom du contact à modifier\n")
    f = open(repertoire, 'r+')
    i=-1
    for ligne in f.readlines():
        i=i+1
        if sup in str(ligne):
            resultat_recherch_sup.append(ligne)
            indice.append(i)
            #resultat_recherch_sup.append(contact)
            #break
    f.close()  
    if len(resultat_recherch_sup)==1:
        rep="O"
        print("Il y a {0} numero(s) associé(s) au contact {1} ".format(len(resultat_recherch_sup),sup))
        for result,j in zip(resultat_recherch_sup,indice):
            result=result.split("   ")
            print("Nom : {0} Téléphone : {1} ".format(result[0],result[1]))
            f = open(repertoire, 'r')
            m=f.read()
            pos=m.split("\n")
            res=result[1].strip("\n")
            menu_mod=input("Tappez \n1. Pour modifier {0}\n2. Pour modifier {1}3. Pour ajouter un nouveau numéro\n4. pour modifier toutes les données.\n5. Pour retourner au menu principal\n".format(result[0],result[1]))
            if menu_mod=="1":
                nom=input("Entrez le nouveau nom\n")
                while test_nom.findall(nom)==[]:
                    nom=input("nom incorrect\n")
                if nom=="":
                    nom="vide"
                telephone=res
                pos[j]=nom+"    "+telephone
            if menu_mod=="2":
                telephone=input("Entrez le nouveau numéro\n")
                while test_tel.findall(telephone)==[]or telephone=="":
                    telephone=input("numéro incorrect\n")
                nom=result[0]
                pos[j]=nom+"    "+telephone
            if menu_mod=="3":
                tel2=input("Entrez le nouveau numéro\n")
                nom=result[0]
                telephone=res
                pos[j]=nom+"    "+telephone+"/"+tel2
            if menu_mod=="4":                
                nom=input("Entrez le nouveau nom\n")
                while test_nom.findall(nom)==[]:
                    nom=input("nom incorrect\n")
                telephone=input("Entrez le nouveau numéro\n")
                while test_tel.findall(telephone)==[]or telephone=="":
                    telephone=input("numéro incorrect\n")
                pos[j]=nom+"    "+telephone
            if menu_mod=="5":
                menu()
            #ajout_tel2=input("Voulez vous ajoutez un deuxieme numero a ce contact O/N?\n")
            #choix_modif_tel_existant=["o","O","oui","","Oui","OUI"]
            #if ajout_tel2 in choix_modif_tel_existant:
            #    tel2=input("Entrez le second numéro\n")
            #    pos[j]=nom+"    "+telephone+"/"+tel2
            #else:
            #    pos[j]=nom+"    "+telephone
            es=""
            es="\n".join(pos)
            f.close()
            l = open(repertoire, 'w')
            l.write(es)
            l.close()
            print("\nMis à jour réussit")
    elif len(resultat_recherch_sup)>1:
        rep="O"
        print("Il y a {0} numero(s) associé(s) au contact {1} ".format(len(resultat_recherch_sup),sup))
        for result,j in zip(resultat_recherch_sup,indice):
            result=result.split("   ")
            print("Position {2} Nom : {0} Téléphone : {1}  ".format(result[0],result[1],j))
        try:
            num=eval(input("\nveuillez saisir la position du contact à modifier\n"))
            if num in indice:
                f = open(repertoire, 'r')
                m=f.read()
                pos=m.split("\n")
                nom=input("\nEntrez le nouveau nom\n")
                telephone=input("Entrez le nouveau téléphone\n")         
                while test_tel.findall(telephone)==[]or telephone=="":
                    telephone=input("numéro incorrect\n")
                ajout_tel2=input("Voulez vous ajoutez un deuxieme numero a ce contact O/N?\n")
                choix_modif_tel_existant=["o","O","oui","","Oui","OUI"]
                if ajout_tel2 in choix_modif_tel_existant:
                    tel2=input("Entrez le second numéro\n")
                    while test_tel.findall(tel2)==[]or tel2=="":
                        tel2=input("numéro incorrect\n")
                    pos[num]=nom+"    "+telephone+"/"+tel2
                else:
                    pos[num]=nom+"    "+telephone
                es=""
                es="\n".join(pos)
                f.close()
                l = open(repertoire, 'w')
                l.write(es)
                l.close()
                print("Mis à jour réussit")
        except:
            print("numero incorrect")
            menu()
    else:
        rep=input("{} n'existe pas dans la liste des contacts|n Souhaitez vous enregister un nouveau contact O/N\n".format(sup))
        if rep=="O" or rep=="o" or rep=="oui" or rep=="OUI" or rep=="Oui":
            Ajouter_Contact()
        else:
            menu()
        
            
while True:
    menu()

