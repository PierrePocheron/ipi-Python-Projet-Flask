DROP TABLE IF EXISTS utilisateur;
DROP TABLE IF EXISTS produit;
DROP TABLE IF EXISTS panier;
DROP TABLE IF EXISTS produit_panier;
DROP TABLE IF EXISTS commande;


CREATE TABLE utilisateur (
  idUtilisateur INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE produit (
  idProduit INTEGER PRIMARY KEY AUTOINCREMENT,
  code INTEGER NOT NULL,
  marque TEXT NOT NULL,
  prix INTEGER NOT NULL,
  image TEXT
);

CREATE TABLE panier (
  idPanier INTEGER PRIMARY KEY AUTOINCREMENT,
  idUtilisateur INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (idUtilisateur) REFERENCES utilisateur (idUtilisateur)
);

CREATE TABLE produit_panier (
  idProduitPanier INTEGER PRIMARY KEY AUTOINCREMENT,
  idProduit INTEGER NOT NULL,
  idPanier INTEGER NOT NULL,
  quantité INTEGER,
  FOREIGN KEY (idProduit) REFERENCES produit (idProduit),
  FOREIGN KEY (idPanier) REFERENCES panier (idPanier)
);

CREATE TABLE commande (
  idCommande INTEGER PRIMARY KEY AUTOINCREMENT,
  idUtilisateur INTEGER NOT NULL,
  idPanier INTEGER NOT NULL,
  dateCommande TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  prixTotal INTEGER NOT NULL,
  FOREIGN KEY (idUtilisateur) REFERENCES utilisateur (idUtilisateur),
  FOREIGN KEY (idPanier) REFERENCES panier (idPanier)
);