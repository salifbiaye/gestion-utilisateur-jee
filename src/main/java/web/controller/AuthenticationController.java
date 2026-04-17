package web.controller;

import java.io.IOException;
import java.net.URLEncoder;

import beans.Utilisateur;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import service.AuthenticationService;

@WebServlet({ "/login", "/logout" })
public class AuthenticationController extends HttpServlet {
	private static final long serialVersionUID = 1L;
	public static final String LOGIN_FORM = "/WEB-INF/login.jsp";
	private AuthenticationService service = new AuthenticationService();

	public AuthenticationController() {
		super();
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		String path = request.getServletPath();

		switch (path) {
		case "/login":

			HttpSession existingSession = request.getSession(false);
			if (existingSession != null && Boolean.TRUE.equals(existingSession.getAttribute("isConnected"))) {
				response.sendRedirect(request.getContextPath() + "/list");
				return;
			}

			String message = request.getParameter("message");
			String status = request.getParameter("status");

			if (message != null && status != null) {
				request.setAttribute("message", message);
				request.setAttribute("status", status);
			}

			getServletContext().getRequestDispatcher(LOGIN_FORM).forward(request, response);
			break;

		default:
			// Logout
			HttpSession session = request.getSession(false);
			String savedTheme = null;

			if (session != null) {
				savedTheme = (String) session.getAttribute("theme");
				session.invalidate();
			}

			HttpSession newSession = request.getSession(true);
			if (savedTheme != null) {
				newSession.setAttribute("theme", savedTheme);
			}

			String logoutMessage = "Déconnexion réussie";
			String logoutStatus = "success";
			String url = String.format("/login?message=%s&status=%s", URLEncoder.encode(logoutMessage, "UTF-8"),
					logoutStatus);
			response.sendRedirect(request.getContextPath() + url);
			break;
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String message;
		String status;
		String url;
		if (request.getServletPath().equals("/login")) {
			String login = request.getParameter("login");
			String password = request.getParameter("password");

			Utilisateur utilisateur = service.authenticate(login, password);

			if (utilisateur != null) {
				HttpSession session = request.getSession();
				session.setAttribute("isConnected", true);
				session.setAttribute("login", utilisateur.getLogin());
				session.setAttribute("role", utilisateur.getRole());
				session.setAttribute("nom", utilisateur.getNom());
				session.setAttribute("prenom", utilisateur.getPrenom());
				message = "Connexion réussie";
				status = "success";
				url = String.format("/list?message=%s&status=%s", URLEncoder.encode(message, "UTF-8"), status);
				response.sendRedirect(request.getContextPath() + url);
			} else {
				message = "Login ou mot de passe incorrect";
				status = "error";
				url = String.format("/login?message=%s&status=%s", URLEncoder.encode(message, "UTF-8"), status);
				response.sendRedirect(request.getContextPath() + url);
			}
		}
	}
}
