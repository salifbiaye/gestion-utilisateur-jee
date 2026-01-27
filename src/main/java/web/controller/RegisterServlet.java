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
	private static final long serialVersionUID = 1L;
	private static final String REGISTER_FORM_VIEW = "/WEB-INF/register.jsp";
	private final UserService service = new UserService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		if (isUserConnected(request)) {
			redirectToLogin(request, response, "Vous êtes deja connecté !!");
			return;
		}

		request.setAttribute("form", new AddUserForm("", "", "", "", ""));
		getServletContext().getRequestDispatcher(REGISTER_FORM_VIEW).forward(request, response);
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		if (isUserConnected(request)) {
			redirectToLogin(request, response, "Vous êtes deja connecté !!");
			return;
		}

		AddUserForm form = AddUserForm.fromMap(request.getParameterMap());
		String message;
		String status;
		String url;

		if (form.isValid()) {
			Utilisateur u = UserMapper.toUser(form);
			try {
				service.ajouter(u);
				message = "inscription effectué avec succès";
				status = "success";
			} catch (RuntimeException e) {
				message = e.getMessage();
				status = "error";
			}
			url = String.format("login?message=%s&status=%s", URLEncoder.encode(message, "UTF-8"), status);
			response.sendRedirect(url);
		} else {
			message = form.getStatusMessage();
			status = "error";
			request.setAttribute("form", form);
			getServletContext().getRequestDispatcher(REGISTER_FORM_VIEW).forward(request, response);
		}
	}

	private boolean isUserConnected(HttpServletRequest request) {
		HttpSession session = request.getSession(false);
		return session != null && Boolean.TRUE.equals(session.getAttribute("isConnected"));
	}

	private void redirectToLogin(HttpServletRequest request, HttpServletResponse response, String message)
			throws IOException {
		String url = String.format("%s/login?message=%s&status=error", request.getContextPath(),
				URLEncoder.encode(message, "UTF-8"));
		response.sendRedirect(url);
	}
}