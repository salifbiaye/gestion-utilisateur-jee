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
import web.form.AddUserForm;

@WebServlet("/add")
public class AddUserServlet extends HttpServlet {

	private static final long serialVersionUID = 1L;
	private static final String FORM_ADD_USER_VIEW = "/WEB-INF/ajouterUtilisateur.jsp";
	private final UserService service = new UserService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setAttribute("form", new AddUserForm("", "", "", "", ""));
		getServletContext().getRequestDispatcher(FORM_ADD_USER_VIEW).forward(request, response);

	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		AddUserForm form = AddUserForm.fromMap(request.getParameterMap());
		String message;
		String status;
		String url;
		if (form.isValid()) {
			Utilisateur u = UserMapper.toUser(form);

			try {
				service.ajouter(u);
				message = "Ajout effectué avec succès";
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
			getServletContext().getRequestDispatcher(FORM_ADD_USER_VIEW).forward(request, response);

		}

	}

}
