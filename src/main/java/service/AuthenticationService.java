package service;

import beans.Utilisateur;
import dao.UtilisateurDaoBdd;

public class AuthenticationService {

	private UtilisateurDaoBdd utilisateurDao;

	public AuthenticationService() {
		this.utilisateurDao = new UtilisateurDaoBdd();
	}

	public AuthenticationService(UtilisateurDaoBdd utilisateurDao) {
		this.utilisateurDao = utilisateurDao;
	}

	public boolean authenticate(String login, String password) {
		System.out.println("[AUTH] Tentative de connexion avec login: " + login);
		Utilisateur utilisateur = utilisateurDao.getByLogin(login);

		if (utilisateur != null) {
			System.out.println("[AUTH] Utilisateur trouvé: " + utilisateur.getLogin());
			System.out.println("[AUTH] Password BDD: '" + utilisateur.getPassword() + "' vs saisi: '" + password + "'");
			if (utilisateur.getPassword().equals(password)) {
				System.out.println("[AUTH] Connexion réussie");
				return true;
			}
		} else {
			System.out.println("[AUTH] Aucun utilisateur trouvé pour le login: " + login);
		}

		return false;
	}
}