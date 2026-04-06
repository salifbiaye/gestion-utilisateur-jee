# Gestion Utilisateurs - Application Java EE

Une application web complète de gestion d'utilisateurs développée avec Java EE (Jakarta EE), permettant l'authentification, les opérations CRUD et la personnalisation de thème.

## 📋 Fonctionnalités

### Authentification
- Connexion sécurisée avec login et mot de passe
- Inscription de nouveaux utilisateurs
- Déconnexion avec préservation du thème
- Protection des routes par filtre d'authentification

### Gestion des Utilisateurs (CRUD)
- **Créer** : Ajouter de nouveaux utilisateurs avec validation
- **Lire** : Afficher la liste complète des utilisateurs
- **Modifier** : Mettre à jour les informations d'un utilisateur
- **Supprimer** : Supprimer un utilisateur avec confirmation

### Personnalisation
- Basculer entre thème clair et thème sombre
- Thème persistant en session (conservé même après déconnexion)

### Validation
- Validation côté serveur des formulaires
- Messages d'erreur contextuels en français
- Vérification de l'unicité des logins
- Affichage des messages de succès/erreur

## 🛠️ Technologies Utilisées

| Technologie | Version | Usage |
|------------|---------|-------|
| Java | 17 | Langage principal |
| Jakarta Servlet | 6.1 | Gestion des requêtes HTTP |
| JSP | - | Vues dynamiques |
| JSTL | 2.0 | Logique dans les vues |
| Apache Tomcat | 11.0 | Serveur d'application |
| MySQL | - | Base de données (optionnel) |
| JDBC | - | Accès aux données |

## 📦 Prérequis

- **Java Development Kit (JDK)** : Version 17 ou supérieure
- **Apache Tomcat** : Version 11.0
- **IDE** : Eclipse IDE for Enterprise Java and Web Developers (recommandé)
- **MySQL** : Version 8.0+ (optionnel, pour la persistance en base de données)

## 🚀 Installation et Configuration

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd gesusers2
```

### 2. Configuration dans Eclipse

1. Ouvrir Eclipse IDE
2. Importer le projet : `File > Import > Existing Projects into Workspace`
3. Sélectionner le dossier du projet
4. Cliquer sur `Finish`

### 3. Configuration du serveur Tomcat

1. Dans Eclipse, ouvrir la vue `Servers` : `Window > Show View > Servers`
2. Clic droit > `New > Server`
3. Sélectionner `Apache > Tomcat v11.0 Server`
4. Spécifier le répertoire d'installation de Tomcat
5. Ajouter le projet `gesusers2` au serveur

### 4. Configuration de la base de données (optionnel)

Par défaut, l'application utilise un stockage **en mémoire** (ArrayList). Les données sont perdues au redémarrage du serveur.

Pour activer la **persistance MySQL** :

#### a. Créer la base de données

```sql
CREATE DATABASE gestion_utilisateurs;
USE gestion_utilisateurs;

CREATE TABLE utilisateur (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    login VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

#### b. Configurer la connexion

Modifier le fichier `src/main/java/dao/UtilisateurDaoBdd.java` (lignes 17-19) :

```java
String url = "jdbc:mysql://localhost:3306/gestion_utilisateurs";
String user = "votre_user_mysql";
String password = "votre_password_mysql";
```

#### c. Basculer vers le DAO base de données

Modifier `src/main/java/service/UserService.java` (ligne 17) :

```java
// Avant
this.dao = new UtilisateurDao();

// Après
this.dao = new UtilisateurDaoBdd();
```

Faire de même dans `src/main/java/service/AuthenticationService.java` (ligne 11).

### 5. Démarrer l'application

1. Clic droit sur le projet > `Run As > Run on Server`
2. Sélectionner le serveur Tomcat configuré
3. L'application démarre sur : `http://localhost:8080/gesusers2/`

## 📖 Utilisation

### Première connexion

Avec le stockage en mémoire par défaut, un utilisateur de test est créé automatiquement.
Identifiants: `test` / `password`

### Routes disponibles

| Route | Méthode | Description | Authentification |
|-------|---------|-------------|------------------|
| `/login` | GET/POST | Page de connexion | Non |
| `/logout` | GET | Déconnexion | Oui |
| `/list` | GET | Liste des utilisateurs | Oui |
| `/add` | GET/POST | Ajouter un utilisateur | Oui |
| `/update?id={id}` | GET/POST | Modifier un utilisateur | Oui |
| `/delete?id={id}` | GET | Supprimer un utilisateur | Oui |
| `/theme` | POST | Basculer le thème | Non |

### Workflow typique

1. **Se connecter** : Authentification via `/login` avec les identifiants `test` / `password`
2. **Gérer les utilisateurs** : Ajouter, modifier, supprimer via `/list`
4. **Personnaliser** : Changer le thème avec le bouton en haut à droite
5. **Se déconnecter** : Via `/logout`

## 📁 Structure du Projet

```
gesusers2/
├── src/main/java/
│   ├── beans/
│   │   └── Utilisateur.java          # Modèle de données utilisateur
│   ├── dao/
│   │   ├── UtilisateurDao.java       # DAO en mémoire (par défaut)
│   │   └── UtilisateurDaoBdd.java    # DAO MySQL
│   ├── service/
│   │   ├── UserService.java          # Logique métier CRUD
│   │   └── AuthenticationService.java # Logique d'authentification
│   ├── web/
│   │   ├── controller/
│   │   │   ├── ListUserServlet.java
│   │   │   ├── AddUserServlet.java
│   │   │   ├── UpdateUserServlet.java
│   │   │   ├── RemoveUserServlet.java
│   │   │   ├── AuthenticationController.java
│   │   │   └── ThemeController.java
│   │   └── form/
│   │       ├── AbstractUserForm.java  # Classe de base validation
│   │       ├── AddUserForm.java
│   │       └── UpdateUserForm.java
│   ├── mapper/
│   │   └── UserMapper.java            # Conversion Form ↔ Entity
│   └── filter/
│       └── AuthenticationFilter.java  # Filtre de sécurité
├── src/main/webapp/
│   ├── WEB-INF/
│   │   ├── web.xml                    # Descripteur de déploiement
│   │   ├── lib/                       # Bibliothèques JSTL
│   │   ├── login.jsp
│   │   ├── listerUtilisateurs.jsp
│   │   ├── ajouterUtilisateur.jsp
│   │   └── modifierUtilisateur.jsp
│   ├── inc/
│   │   ├── header.jsp                 # En-tête commun
│   │   └── footer.jsp                 # Pied de page commun
│   └── css/
│       ├── light/                     # Styles thème clair
│       └── dark/                      # Styles thème sombre
└── build/                             # Classes compilées
```

## 🏗️ Architecture

L'application suit une architecture **3-tiers** classique :

```
┌─────────────────────────────────────┐
│   Couche Présentation (JSP)        │
│   - Vues JSP avec JSTL              │
│   - Servlets (Contrôleurs)          │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Couche Service                    │
│   - UserService                     │
│   - AuthenticationService           │
│   - Validation métier               │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Couche Accès Données (DAO)       │
│   - UtilisateurDao (mémoire)        │
│   - UtilisateurDaoBdd (MySQL)       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Stockage                          │
│   - ArrayList (par défaut)          │
│   - MySQL (optionnel)               │
└─────────────────────────────────────┘
```

### Patterns implémentés

- **MVC** : Séparation Modèle-Vue-Contrôleur
- **DAO Pattern** : Abstraction de l'accès aux données
- **Service Layer** : Encapsulation de la logique métier
- **Form Object Pattern** : Gestion de la validation
- **Filter Pattern** : Authentification et autorisation

## 🔐 Sécurité

⚠️ **Note importante** : Cette application est destinée à des fins **éducatives**.

**Limitations de sécurité actuelles** :
- Mots de passe stockés en clair (non hashés)
- Pas de protection CSRF
- Pas de validation côté client
- Session sans timeout configuré

**Pour un environnement de production**, il faudrait :
- Hasher les mots de passe (BCrypt, PBKDF2)
- Ajouter une protection CSRF
- Implémenter HTTPS
- Ajouter une validation côté client
- Configurer des timeouts de session
- Utiliser des PreparedStatements (déjà fait)

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Forker le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commiter vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pousser vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est un projet éducatif.

## 👤 Auteur

Projet développé dans le cadre d'un apprentissage Java EE.

## 📞 Support

Pour toute question ou problème, n'hésitez pas à ouvrir une issue sur le repository.

---

Développé avec ☕ et Java
