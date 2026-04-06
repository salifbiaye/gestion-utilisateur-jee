package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import beans.Utilisateur;

public class UtilisateurDaoBdd {

	// Méthode pour obtenir la connexion
	private Connection getConnection() throws SQLException {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			throw new SQLException("Driver MySQL introuvable", e);
		}
		String url = "jdbc:mysql://localhost:3306/gesusers";
		String user = "root";
		String password = "passer123";
		return DriverManager.getConnection(url, user, password);
	}

	public boolean ajouter(Utilisateur utilisateur) {
		String sql = "INSERT INTO utilisateur (nom, prenom, login, password) VALUES (?, ?, ?, ?)";

		try (Connection conn = getConnection();
				PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

			pstmt.setString(1, utilisateur.getNom());
			pstmt.setString(2, utilisateur.getPrenom());
			pstmt.setString(3, utilisateur.getLogin());
			pstmt.setString(4, utilisateur.getPassword());

			int rowsAffected = pstmt.executeUpdate();

			// Récupérer l'ID généré
			if (rowsAffected > 0) {
				ResultSet rs = pstmt.getGeneratedKeys();
				if (rs.next()) {
					utilisateur.setId(rs.getInt(1));
				}
			}

			return rowsAffected > 0;

		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
	}

	public boolean modifier(Utilisateur utilisateur) {
		String sql = "UPDATE utilisateur SET nom=?, prenom=?, login=?, password=? WHERE id=?";

		try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {

			pstmt.setString(1, utilisateur.getNom());
			pstmt.setString(2, utilisateur.getPrenom());
			pstmt.setString(3, utilisateur.getLogin());
			pstmt.setString(4, utilisateur.getPassword());
			pstmt.setInt(5, utilisateur.getId());

			return pstmt.executeUpdate() > 0;

		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
	}

	public boolean supprimer(int id) {
		String sql = "DELETE FROM utilisateur WHERE id=?";

		try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {

			pstmt.setInt(1, id);
			return pstmt.executeUpdate() > 0;

		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
	}

	public ArrayList<Utilisateur> lister() {
		ArrayList<Utilisateur> utilisateurs = new ArrayList<>();
		String sql = "SELECT * FROM utilisateur";

		try (Connection conn = getConnection();
				Statement stmt = conn.createStatement();
				ResultSet rs = stmt.executeQuery(sql)) {

			while (rs.next()) {
				Utilisateur u = new Utilisateur(rs.getInt("id"), rs.getString("nom"), rs.getString("prenom"),
						rs.getString("login"), rs.getString("password"));
				utilisateurs.add(u);
			}

		} catch (SQLException e) {
			e.printStackTrace();
		}

		return utilisateurs;
	}

	public Utilisateur get(int id) {
		String sql = "SELECT * FROM utilisateur WHERE id=?";

		try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {

			pstmt.setInt(1, id);
			ResultSet rs = pstmt.executeQuery();

			if (rs.next()) {
				return new Utilisateur(rs.getInt("id"), rs.getString("nom"), rs.getString("prenom"),
						rs.getString("login"), rs.getString("password"));
			}

		} catch (SQLException e) {
			e.printStackTrace();
		}

		return null;
	}

	public Utilisateur getByLogin(String login) {
		String sql = "SELECT * FROM utilisateur WHERE login=?";

		try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {

			pstmt.setString(1, login);
			ResultSet rs = pstmt.executeQuery();

			if (rs.next()) {
				return new Utilisateur(rs.getInt("id"), rs.getString("nom"), rs.getString("prenom"),
						rs.getString("login"), rs.getString("password"));
			}

		} catch (SQLException e) {
			e.printStackTrace();
		}

		return null;
	}
}