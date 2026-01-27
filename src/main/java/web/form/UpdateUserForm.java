package web.form;

import java.util.Map;

public class UpdateUserForm extends AbstractUserForm {

	private String id;
	private static final String INVALID_ID_ERROR_MESSAGE = "L'ID doit être un nombre valide";

	public UpdateUserForm(String id, String nom, String prenom, String login, String password) {
		super(nom, prenom, login, password);
		this.id = id;
	}

	public UpdateUserForm(Map<String, String[]> map) {
		super(map);
		this.id = map.get("id") != null ? map.get("id")[0] : null;
	}

	@Override
	protected void checkEmptyFields() {
		super.checkEmptyFields();
		if (id == null || id.isBlank()) {
			errors.put("id", EMPTY_FIELD_ERROR_MESSAGE);
		}
	}

	public void checkIdValidity() {
		if (id != null && !id.isBlank()) {
			try {
				Integer.parseInt(id);
			} catch (NumberFormatException e) {
				errors.put("id", INVALID_ID_ERROR_MESSAGE);
			}
		}
	}

	public boolean isValid() {
		checkEmptyFields();
		checkIdValidity();

		if (errors.isEmpty()) {
			return this.status = true;
		}

		this.statusMessage = "Saisie incomplète";
		return status = false;
	}

	public static UpdateUserForm fromMap(Map<String, String[]> map) {
		return new UpdateUserForm(map);
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}
}