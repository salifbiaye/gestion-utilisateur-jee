package mapper;

import beans.Utilisateur;
import web.form.AddUserForm;
import web.form.UpdateUserForm;

public class UserMapper {

	public static Utilisateur toUser(AddUserForm form) {
		Utilisateur utilisateur = new Utilisateur();
		utilisateur.setNom(form.getNom());
		utilisateur.setPrenom(form.getPrenom());
		utilisateur.setLogin(form.getLogin());
		utilisateur.setPassword(form.getPassword());
		utilisateur.setRole(form.getRole() != null ? form.getRole() : "user");
		return utilisateur;
	}

	public static UpdateUserForm toUpdateUserForm(Utilisateur utilisateur) {
		UpdateUserForm form = new UpdateUserForm(String.valueOf(utilisateur.getId()), utilisateur.getNom(),
				utilisateur.getPrenom(), utilisateur.getLogin(), utilisateur.getPassword());
		form.setRole(utilisateur.getRole() != null ? utilisateur.getRole() : "user");
		return form;
	}

	public static Utilisateur toUserFromUpdate(UpdateUserForm form) {
		Utilisateur u = new Utilisateur(Integer.parseInt(form.getId()), form.getNom(), form.getPrenom(),
				form.getLogin(), form.getPassword());
		u.setRole(form.getRole() != null ? form.getRole() : "user");
		return u;
	}

}
