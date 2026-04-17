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
import mapper.UserMapper;
import service.UserService;
import web.form.AddUserForm;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {

	private static final String REGISTER_VIEW = "/WEB-INF/register.jsp";
	private final UserService service = new UserService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		// Si déjà connecté, rediriger
		HttpSession session = request.getSession(false);
		if (session != null && Boolean.TRUE.equals(session.getAttribute("isConnected"))) {
			String role = (String) session.getAttribute("role");
			if ("admin".equals(role)) {
				response.sendRedirect(request.getContextPath() + "/list");
			} else {
				response.sendRedirect(request.getContextPath() + "/welcome");
			}
			return;
		}

		request.setAttribute("form", new AddUserForm("", "", "", "", ""));
		getServletContext().getRequestDispatcher(REGISTER_VIEW).forward(request, response);
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		AddUserForm form = AddUserForm.fromMap(request.getParameterMap());
		// Forcer le rôle "user" pour l'inscription publique
		form.setRole("user");

		if (form.isValid()) {
			Utilisateur u = UserMapper.toUser(form);
			u.setRole("user"); // Sécurité : toujours "user"

			try {
				service.ajouter(u);
				String message = URLEncoder.encode("Inscription réussie ! Connectez-vous.", "UTF-8");
				response.sendRedirect(request.getContextPath() + "/login?message=" + message + "&status=success");
				return;
			} catch (RuntimeException e) {
				request.setAttribute("errorMessage", e.getMessage());
			}
		} else {
			request.setAttribute("errorMessage", form.getStatusMessage());
		}

		request.setAttribute("form", form);
		getServletContext().getRequestDispatcher(REGISTER_VIEW).forward(request, response);
	}
}
