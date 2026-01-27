package service;

import beans.Utilisateur;
import dao.UtilisateurDao;

public class AuthenticationService {

	private UtilisateurDao utilisateurDao;

	public AuthenticationService() {
		this.utilisateurDao = new UtilisateurDao();
	}

	public AuthenticationService(UtilisateurDao utilisateurDao) {
		this.utilisateurDao = utilisateurDao;
	}

	public boolean authenticate(String login, String password) {
		Utilisateur utilisateur = utilisateurDao.getByLogin(login);

		if (utilisateur != null && utilisateur.getPassword().equals(password)) {
			return true;
		}

		return false;
	}
}