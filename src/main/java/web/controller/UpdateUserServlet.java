package web.controller;

import java.io.IOException;
import java.net.URLEncoder;

import beans.Utilisateur;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import mapper.UserMapper;
import service.UserService;
import web.form.UpdateUserForm;

@WebServlet("/update")
public class UpdateUserServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private static final String FORM_UPDATE_USER_VIEW = "/WEB-INF/modifierUtilisateur.jsp";
	private final UserService userService = new UserService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		try {
			int id = Integer.parseInt(request.getParameter("id"));
			Utilisateur utilisateur = userService.getUser(id);

			if (utilisateur == null) {
				throw new RuntimeException("L'utilisateur avec l'id " + id + " n'existe pas");
			}

			request.setAttribute("form", UserMapper.toUpdateUserForm(utilisateur));
			getServletContext().getRequestDispatcher(FORM_UPDATE_USER_VIEW).forward(request, response);
		} catch (NumberFormatException e) {
			String url = "list?message=" + URLEncoder.encode("ID invalide", "UTF-8") + "&status=error";
			response.sendRedirect(url);
		} catch (Exception e) {
			String url = "list?message=" + URLEncoder.encode(e.getMessage(), "UTF-8") + "&status=error";
			response.sendRedirect(url);
		}
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		UpdateUserForm form = UpdateUserForm.fromMap(request.getParameterMap());

		String message;
		String status;
		String url;

		if (form.isValid()) {
			Utilisateur u = UserMapper.toUserFromUpdate(form);
			try {
				userService.modifier(u);
				message = "Mise à jour effectuée avec succès";
				status = "success";
			} catch (RuntimeException e) {
				message = e.getMessage();
				status = "error";
			}
			url = String.format("list?message=%s&status=%s", URLEncoder.encode(message, "UTF-8"), status);
			response.sendRedirect(url);
		} else {
			message = form.getStatusMessage();
			status = "error";
			request.setAttribute("form", form);
			getServletContext().getRequestDispatcher(FORM_UPDATE_USER_VIEW).forward(request, response);
		}
	}
}