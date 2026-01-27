package service;

import java.util.ArrayList;

import beans.Utilisateur;
import dao.UtilisateurDao;

public class UserService {

	private UtilisateurDao dao;

	public UserService(UtilisateurDao dao) {
		this.dao = dao;
	}

	public UserService() {
		this.dao = new UtilisateurDao();
	}

	public Utilisateur ajouter(Utilisateur utilisateur) {

		Utilisateur user = dao.getByLogin(utilisateur.getLogin());
		if (user != null) {
			throw new RuntimeException("Un utilisateur avec ce login existe déjà");
		} else if (dao.ajouter(utilisateur)) {
			return utilisateur;
		} else {
			throw new RuntimeException("Une erreur inattendue s'est produite");
		}
	}

	public ArrayList<Utilisateur> lister() {
		return dao.lister();
	}

	public Utilisateur getUser(int id) {
		return dao.get(id);

	}

	public Utilisateur modifier(Utilisateur utilisateur) {

		Utilisateur existant = dao.get(utilisateur.getId());
		if (existant == null) {
			throw new RuntimeException("Utilisateur introuvable");
		}

		Utilisateur userAvecMemeLogin = dao.getByLogin(utilisateur.getLogin());
		if (userAvecMemeLogin != null && userAvecMemeLogin.getId() != utilisateur.getId()) {
			throw new RuntimeException("Ce login est déjà utilisé par un autre utilisateur");
		}

		if (dao.modifier(utilisateur)) {
			return utilisateur;
		} else {
			throw new RuntimeException("Erreur lors de la modification");
		}
	}

	public void supprimer(int id) {

		Utilisateur existant = dao.get(id);
		if (existant == null) {
			throw new RuntimeException("Utilisateur introuvable");
		}

		if (!dao.supprimer(id)) {
			throw new RuntimeException("Erreur lors de la suppression");
		}
	}
}
