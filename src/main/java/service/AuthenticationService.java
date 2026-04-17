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

	public Utilisateur authenticate(String login, String password) {
		System.out.println("[AUTH] Tentative de connexion avec login: " + login);
		Utilisateur utilisateur = utilisateurDao.getByLogin(login);

		if (utilisateur != null) {
			System.out.println("[AUTH] Utilisateur trouvé: " + utilisateur.getLogin());
			if (utilisateur.getPassword().equals(password)) {
				System.out.println("[AUTH] Connexion réussie");
				return utilisateur;
			}
		} else {
			System.out.println("[AUTH] Aucun utilisateur trouvé pour le login: " + login);
		}

		return null;
	}
}
