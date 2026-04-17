package web.controller;

import java.io.IOException;
import java.net.URLEncoder;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import service.UserService;

@WebServlet("/delete")
public class RemoveUserServlet extends HttpServlet {

	private static final long serialVersionUID = 1L;
	private final UserService userService = new UserService();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		String message;
		String status;

		try {
			int id = Integer.parseInt(request.getParameter("id"));
			userService.supprimer(id);

			message = "Suppression effectuée avec succès";
			status = "success";

		} catch (NumberFormatException e) {
			message = "ID invalide";
			status = "error";

		} catch (RuntimeException e) {
			message = e.getMessage();
			status = "error";
		}

		String url = String.format("list?message=%s&status=%s", URLEncoder.encode(message, "UTF-8"), status);

		response.sendRedirect(url);
	}
}
