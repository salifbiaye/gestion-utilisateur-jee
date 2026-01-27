package dao;

import java.util.ArrayList;

import beans.Utilisateur;

public class UtilisateurDao {
	private static final ArrayList<Utilisateur> utilisateurs = new ArrayList<Utilisateur>();
//	static {
//		utilisateurs.add(new Utilisateur(1, "Biaye", "Salif", "sbiaye", "password123"));
//	}
	private static int count = 1;

	public boolean ajouter(Utilisateur utilisateur) {
		utilisateur.setId(++count);
		utilisateurs.add(utilisateur);
		return true;
	}

	public boolean modifier(Utilisateur utilisateur) {
		for (Utilisateur u : utilisateurs) {
			if (u.getId() == utilisateur.getId()) {
				u.setNom(utilisateur.getNom());
				u.setPrenom(utilisateur.getPrenom());
				u.setLogin(utilisateur.getLogin());
				if (utilisateur.getPassword() != null) {
					u.setPassword(utilisateur.getPassword());
				}

				return true;
			}

		}

		return false;
	}

	public boolean supprimer(int id) {
		for (Utilisateur u : utilisateurs) {
			if (u.getId() == id) {
				utilisateurs.remove(u);
				return true;
			}
		}

		return false;
	}

	public ArrayList<Utilisateur> lister() {
		return utilisateurs;
	}

	public Utilisateur get(int id) {
		for (Utilisateur u : utilisateurs) {
			if (u.getId() == id) {

				return u;
			}

		}

		return null;
	}

	public Utilisateur getByLogin(String login) {
		for (Utilisateur u : utilisateurs) {
			if (u.getLogin() != null && u.getLogin().equals(login)) {

				return u;
			}

		}

		return null;
	}

}
