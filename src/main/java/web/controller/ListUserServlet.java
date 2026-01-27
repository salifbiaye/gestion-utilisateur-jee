package web.controller;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import service.UserService;

@WebServlet("/list")
public class ListUserServlet extends HttpServlet {

	private static final String LIST_USERS_VIEW = "/WEB-INF/listerUtilisateurs.jsp";
	private final UserService service = new UserService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		request.setAttribute("utilisateurs", service.lister());

		getServletContext().getRequestDispatcher(LIST_USERS_VIEW).forward(request, response);

	}
}
