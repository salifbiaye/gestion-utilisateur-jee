package web.form;

import java.util.HashMap;
import java.util.Map;

public abstract class AbstractUserForm {
	protected String nom;
	protected String prenom;
	protected String login;
	protected String password;
	protected Map<String, String> errors;
	protected boolean status;
	protected String statusMessage;
	protected static final String EMPTY_FIELD_ERROR_MESSAGE = "Vous devez renseigner ce champ";

	public AbstractUserForm(String nom, String prenom, String login, String password) {
		super();
		this.nom = nom;
		this.prenom = prenom;
		this.login = login;
		this.password = password;
		this.errors = new HashMap<>();
	}

	public AbstractUserForm(Map<String, String[]> map) {
		this(map.get("nom") != null ? map.get("nom")[0] : null, map.get("prenom") != null ? map.get("prenom")[0] : null,
				map.get("login") != null ? map.get("login")[0] : null,
				map.get("password") != null ? map.get("password")[0] : null);
	}

	protected void checkEmptyFields() {
		if (nom == null || nom.isBlank()) {
			errors.put("nom", EMPTY_FIELD_ERROR_MESSAGE);
		}
		if (prenom == null || prenom.isBlank()) {
			errors.put("prenom", EMPTY_FIELD_ERROR_MESSAGE);
		}
		if (login == null || login.isBlank()) {
			errors.put("login", EMPTY_FIELD_ERROR_MESSAGE);
		}
		if (password == null || password.isBlank()) {
			errors.put("password", EMPTY_FIELD_ERROR_MESSAGE);
		}
	}

	public abstract boolean isValid();

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getPrenom() {
		return prenom;
	}

	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}

	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Map<String, String> getErrors() {
		return errors;
	}

	public void setErrors(Map<String, String> errors) {
		this.errors = errors;
	}

	public boolean isStatus() {
		return status;
	}

	public void setStatus(boolean status) {
		this.status = status;
	}

	public String getStatusMessage() {
		return statusMessage;
	}

	public void setStatusMessage(String statusMessage) {
		this.statusMessage = statusMessage;
	}
}