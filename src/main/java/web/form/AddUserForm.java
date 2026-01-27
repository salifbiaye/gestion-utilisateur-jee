package web.form;

import java.util.Map;

public class AddUserForm extends AbstractUserForm {

	private String passwordBis;

	private static final String DIFFERENT_PASSWORDS_ERROR_MESSAGE = "Les mots de passe ne sont pas conformes ";

	public AddUserForm(String nom, String prenom, String login, String password, String passwordBis) {
		super(nom, prenom, login, password);
		this.passwordBis = passwordBis;
	}

	protected void checkEmptyFields() {
		super.checkEmptyFields();
		if (passwordBis == null || passwordBis.isBlank()) {
			errors.put("passwordBis", EMPTY_FIELD_ERROR_MESSAGE);
		}
	}

	public void checkPasswordConformity() {
		if (password != null && !password.equals(passwordBis)) {
			errors.put("passwordBis", DIFFERENT_PASSWORDS_ERROR_MESSAGE);
		}
	}

	@Override
	public boolean isValid() {

		checkEmptyFields();
		checkPasswordConformity();

		if (errors.isEmpty()) {
			return this.status = true;
		}

		this.statusMessage = "Saisie incomplète";
		return status = false;
	}

	public AddUserForm(Map<String, String[]> map) {
		super(map);
		this.passwordBis = map.get("passwordBis") != null ? map.get("passwordBis")[0] : null;
	}

	public static AddUserForm fromMap(Map<String, String[]> map) {
		return new AddUserForm(map);
	}

	public String getPasswordBis() {
		return passwordBis;
	}

	public void setPasswordBis(String passwordBis) {
		this.passwordBis = passwordBis;
	}

}
