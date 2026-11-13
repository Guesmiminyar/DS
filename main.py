ventes = []
prochain_id = 1

# Nombre de jours de chaque mois (février corrigé plus bas si bissextile)
JOURS_PAR_MOIS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    # ----------------------------- MENU -----------------------------
    print("\n===== GESTION DES VENTES =====")
    print("1. Ajouter une vente")
    print("2. Afficher les ventes")
    print("3. Rechercher des ventes")
    print("4. Modifier une vente")
    print("5. Supprimer une vente")
    print("0. Quitter")
    choix = input("Votre choix : ").strip()

    # ----------------------------- AJOUT ----------------------------
    if choix == "1":
        print("\n--- Ajout d'une vente ---")

        while True:
            produit = input("Produit : ").strip()
            if produit != "":
                break
            print("Erreur : ce champ ne peut pas être vide.")

        while True:
            categorie = input("Catégorie : ").strip()
            if categorie != "":
                break
            print("Erreur : ce champ ne peut pas être vide.")

        # Quantité : entier strictement positif
        while True:
            texte = input("Quantité : ").strip()
            if texte.isdecimal() and int(texte) > 0:
                quantite = int(texte)
                break
            print("Erreur : entrez un nombre entier strictement positif.")

        # Prix : réel strictement positif (un seul point ou une seule virgule)
        # prix unitaire est le prix d'un seul article
        while True:
            texte = input("Prix unitaire : ").strip().replace(",", ".")
            if texte.replace(".", "", 1).isdecimal() and float(texte) > 0:
                prix = float(texte)
                break
            print("Erreur : entrez un nombre strictement positif (ex : 12.5).")

        # Date : format AAAA-MM-JJ vérifié à la main
        # la date est le jour ou la vente a ete fait
        while True:
            date = input("Date (AAAA-MM-JJ) : ").strip()
            if (len(date) == 10 and date[4] == "-" and date[7] == "-"
                    and date[:4].isdecimal() and date[5:7].isdecimal()
                    and date[8:].isdecimal()):
                annee = int(date[:4])
                mois = int(date[5:7])
                jour = int(date[8:])
                jours_max = list(JOURS_PAR_MOIS)
                if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
                    jours_max[1] = 29
                if 1 <= mois <= 12 and 1 <= jour <= jours_max[mois - 1]:
                    break
            print("Erreur : date invalide. Format attendu : AAAA-MM-JJ.")

        ventes.append({
            "id": prochain_id,
            "produit": produit,
            "categorie": categorie,
            "quantite": quantite,
            "prix_unitaire": prix,
            "date": date,
        })
        print(f"Vente n°{prochain_id} ajoutée avec succès.")
        prochain_id += 1

    # --------------------------- AFFICHAGE --------------------------
    elif choix == "2":
        if len(ventes) == 0:
            print("Aucune vente à afficher.")
        else:
            print(f"\n{'ID':<4} {'Produit':<15} {'Catégorie':<15} "
                  f"{'Qté':>5} {'Prix U.':>9} {'Date':<12}")
            print("-" * 66)
            for v in ventes:
                print(f"{v['id']:<4} {v['produit']:<15} {v['categorie']:<15} "
                      f"{v['quantite']:>5} {v['prix_unitaire']:>9.2f} "
                      f"{v['date']:<12}")

    # --------------------------- RECHERCHE --------------------------
    elif choix == "3":
        print("\n--- Recherche ---")
        print("1. Par produit")
        print("2. Par catégorie")
        sous_choix = input("Votre choix : ").strip()

        if sous_choix == "1":
            champ = "produit"
        elif sous_choix == "2":
            champ = "categorie"
        else:
            print("Choix invalide.")
            continue

        terme = input(f"Entrez le {champ} à rechercher : ").strip().lower()
        if terme == "":
            print("Erreur : la recherche ne peut pas être vide.")
            continue

        resultats = [v for v in ventes if terme in v[champ].lower()]

        if len(resultats) == 0:
            print("Aucun résultat trouvé.")
        else:
            print(f"{len(resultats)} résultat(s) trouvé(s).")
            print(f"\n{'ID':<4} {'Produit':<15} {'Catégorie':<15} "
                  f"{'Qté':>5} {'Prix U.':>9} {'Date':<12}")
            print("-" * 66)
            for v in resultats:
                print(f"{v['id']:<4} {v['produit']:<15} {v['categorie']:<15} "
                      f"{v['quantite']:>5} {v['prix_unitaire']:>9.2f} "
                      f"{v['date']:<12}")

    # --------------------------- MODIFICATION -----------------------
    elif choix == "4":
        print("\n--- Modification d'une vente ---")
        if len(ventes) == 0:
            print("Aucune vente à modifier.")
            continue

        texte = input("ID de la vente à modifier : ").strip()
        if not texte.isdecimal():
            print("Erreur : veuillez entrer un nombre entier.")
            continue
        id_vente = int(texte)

        vente = None
        for v in ventes:
            if v["id"] == id_vente:
                vente = v
                break

        if vente is None:
            print("Erreur : ID introuvable.")
            continue

        print("Laissez vide pour conserver la valeur actuelle.")

        nouveau = input(f"Produit [{vente['produit']}] : ").strip()
        if nouveau != "":
            vente["produit"] = nouveau

        nouveau = input(f"Catégorie [{vente['categorie']}] : ").strip()
        if nouveau != "":
            vente["categorie"] = nouveau

        while True:
            nouveau = input(f"Quantité [{vente['quantite']}] : ").strip()
            if nouveau == "":
                break
            if nouveau.isdecimal() and int(nouveau) > 0:
                vente["quantite"] = int(nouveau)
                break
            print("Erreur : entrez un nombre entier strictement positif.")

        while True:
            nouveau = input(f"Prix unitaire [{vente['prix_unitaire']}] : ")
            nouveau = nouveau.strip().replace(",", ".")
            if nouveau == "":
                break
            if nouveau.replace(".", "", 1).isdecimal() and float(nouveau) > 0:
                vente["prix_unitaire"] = float(nouveau)
                break
            print("Erreur : entrez un nombre strictement positif.")

        while True:
            nouveau = input(f"Date [{vente['date']}] : ").strip()
            if nouveau == "":
                break
            if (len(nouveau) == 10 and nouveau[4] == "-" and nouveau[7] == "-"
                    and nouveau[:4].isdecimal() and nouveau[5:7].isdecimal()
                    and nouveau[8:].isdecimal()):
                annee = int(nouveau[:4])
                mois = int(nouveau[5:7])
                jour = int(nouveau[8:])
                jours_max = list(JOURS_PAR_MOIS)
                if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
                    jours_max[1] = 29
                if 1 <= mois <= 12 and 1 <= jour <= jours_max[mois - 1]:
                    vente["date"] = nouveau
                    break
            print("Erreur : date invalide. Format attendu : AAAA-MM-JJ.")

        print("Vente modifiée avec succès.")

    # --------------------------- SUPPRESSION ------------------------
    elif choix == "5":
        print("\n--- Suppression d'une vente ---")
        if len(ventes) == 0:
            print("Aucune vente à supprimer.")
            continue

        texte = input("ID de la vente à supprimer : ").strip()
        if not texte.isdecimal():
            print("Erreur : veuillez entrer un nombre entier.")
            continue
        id_vente = int(texte)

        vente = None
        for v in ventes:
            if v["id"] == id_vente:
                vente = v
                break

        if vente is None:
            print("Erreur : ID introuvable.")
            continue

        confirmation = input(f"Supprimer '{vente['produit']}' (ID {id_vente}) ? (o/n) : ").strip().lower()
        if confirmation == "o":
            ventes.remove(vente)
            print("Vente supprimée.")
        else:
            print("Suppression annulée.")

    # ----------------------------- QUITTER --------------------------
    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Choix invalide, entrez un nombre entre 0 et 5.")