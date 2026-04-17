package web.controller;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@WebServlet("/welcome")
public class WelcomeServlet extends HttpServlet {

	private static final String WELCOME_VIEW = "/WEB-INF/welcome.jsp";

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		HttpSession session = request.getSession(false);

		if (session == null || session.getAttribute("isConnected") == null) {
			response.sendRedirect(request.getContextPath() + "/login");
			return;
		}

		getServletContext().getRequestDispatcher(WELCOME_VIEW).forward(request, response);
	}
}
