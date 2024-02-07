#!/bin/bash

# Nom du fichier contenant les données de vente
fichier_ventes="ventes.txt"

# Calcul du chiffre d'affaires total et recherche du produit le plus rentable
resultat=$(awk 'BEGIN { maxCA=0; produit=""; }
                {
                    CA = $2 * $3;
                    if (CA > maxCA) {
                        maxCA = CA;
                        produit = $1;
                    }
                    totalCA += CA;
                }
                END { print produit " " totalCA; }' "$fichier_ventes")

# Affichage du produit le plus rentable et du chiffre d'affaires total
echo "Le produit le plus rentable et son chiffre d'affaires total sont :"
echo "$resultat"
