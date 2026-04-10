<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<c:choose>
  <c:when test="${sessionScope.isConnected == true}">
    </main>
    <footer class="main-footer">
      <div class="footer-container">
        <p>&copy; 2025 Gestion des Utilisateurs. Tous droits réservés.</p>
        <p class="footer-info">Développé avec Java EE &amp; JSP</p>
      </div>
    </footer>
  </div><%-- /.main-wrapper --%>
</div><%-- /.app-layout --%>
  </c:when>
  <c:otherwise>
    </main>
  </c:otherwise>
</c:choose>

</body>
</html>
