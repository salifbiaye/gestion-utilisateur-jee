# Docker Compose Setup für GesUsers2

## Configuration

Un fichier `docker-compose.yml` a été créé avec:

- **MySQL 8.0**: Base de données `gesusers`
  - Utilisateur: `root`
  - Mot de passe: `passer123`
  - Port: `3306`

- **Adminer**: Interface web pour gérer la base de données
  - URL: `http://localhost:8080`
  - Connexion: Server=`mysql`, User=`root`, Password=`passer123`, Database=`gesusers`

## Démarrage

```bash
# Démarrer les services
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down

# Arrêter et supprimer les données
docker-compose down -v
```

## Configuration dans l'application

Pour utiliser la base de données MySQL au lieu du stockage en mémoire:

1. Ouvrez `src/main/java/service/UserService.java`
2. Changez la ligne 17 de:
   ```java
   private UtilisateurDao dao = new UtilisateurDao();
   ```
   à:
   ```java
   private UtilisateurDao dao = new UtilisateurDaoBdd();
   ```

3. Faites la même modification dans `src/main/java/service/AuthenticationService.java` ligne 11

4. Vérifiez les paramètres de connexion dans `src/main/java/dao/UtilisateurDaoBdd.java`:
   ```java
   String url = "jdbc:mysql://localhost:3306/gesusers";
   String user = "root";
   String password = "passer123";
   ```

## Accès Adminer

Ouvrez votre navigateur et accédez à: **http://localhost:8080**

Connectez-vous avec:
- Server: `mysql`
- Username: `root`
- Password: `passer123`
- Database: `gesusers`

Vous devriez voir la table `utilisateur` avec les données de test.
