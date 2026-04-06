-- Création de la table utilisateur si elle n'existe pas
CREATE TABLE IF NOT EXISTS utilisateur (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    login VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

-- Insertion de quelques données de test (optionnel)
INSERT INTO utilisateur (nom, prenom, login, password) VALUES
('Dupont', 'Jean', 'jdupont', 'password123'),
('Martin', 'Marie', 'mmartin', 'password456'),
('Bernard', 'Pierre', 'pbernard', 'password789');
