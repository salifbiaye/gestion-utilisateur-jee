package filter;

import java.io.IOException;
import java.net.URLEncoder;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.FilterConfig;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.annotation.WebFilter;
import jakarta.servlet.http.HttpFilter;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@WebFilter({ "/add", "/update", "/delete", "/list" })
public class AuthenticationFilter extends HttpFilter implements Filter {

	public AuthenticationFilter() {
		super();
	}

	public void destroy() {
	}

	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		HttpServletRequest httpRequest = (HttpServletRequest) request;
		HttpServletResponse httpResponse = (HttpServletResponse) response;

		HttpSession session = httpRequest.getSession(false);
		String path = httpRequest.getServletPath();

		// Vérifier que l'utilisateur est connecté
		if (session == null || session.getAttribute("isConnected") == null) {
			httpResponse.sendRedirect(httpRequest.getContextPath() + "/login");
			return;
		}

		String role = (String) session.getAttribute("role");

		// /add, /delete, /update, /list sont réservés aux administrateurs
		if ((path.equals("/add") || path.equals("/delete") || path.equals("/update") || path.equals("/list"))
				&& !"admin".equals(role)) {
			String message = URLEncoder.encode("Accès refusé : réservé aux administrateurs", "UTF-8");
			httpResponse.sendRedirect(httpRequest.getContextPath() + "/welcome?message=" + message + "&status=error");
			return;
		}

		chain.doFilter(request, response);
	}

	public void init(FilterConfig fConfig) throws ServletException {
	}

}
