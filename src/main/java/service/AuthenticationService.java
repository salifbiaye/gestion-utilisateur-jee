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
		Utilisateur utilisateur = utilisateurDao.getByLogin(login);

		if (utilisateur != null) {
			if (utilisateur.getPassword().equals(password)) {
				return utilisateur;
			}
		}

		return null;
	}
}
