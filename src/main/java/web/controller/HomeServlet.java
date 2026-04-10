package web.controller;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@WebServlet("/")
public class HomeServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		// Laisser Tomcat gérer les fichiers statiques
		String uri = request.getRequestURI();
		if (uri.endsWith(".css") || uri.endsWith(".js") || uri.endsWith(".png")) {
			request.getServletContext().getNamedDispatcher("default").forward(request, response);
			return;
		}

		HttpSession session = request.getSession(false);
		if (session != null && session.getAttribute("isConnected") != null) {
			response.sendRedirect(request.getContextPath() + "/list");
		} else {
			response.sendRedirect(request.getContextPath() + "/login");
		}
	}
}
