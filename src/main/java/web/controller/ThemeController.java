package web.controller;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/theme")
public class ThemeController extends HttpServlet {

	private void toggleTheme(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		String theme = (String) request.getSession().getAttribute("theme");

		if ("light".equals(theme)) {
			request.getSession().setAttribute("theme", "dark");
		} else {
			request.getSession().setAttribute("theme", "light");
		}

		String referer = request.getHeader("referer");
		response.sendRedirect(referer != null ? referer : request.getContextPath() + "/login");
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		toggleTheme(request, response);
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		toggleTheme(request, response);
	}
}
