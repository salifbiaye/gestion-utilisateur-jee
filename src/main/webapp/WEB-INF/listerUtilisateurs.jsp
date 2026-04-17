<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<c:set var="pageTitle" value="Liste des utilisateurs" scope="request"/>
<c:set var="currentPage" value="list" scope="request"/>

<%@ include file="/inc/header.jsp" %>


<div class="page-header">
    <h1>Liste des utilisateurs</h1>
    <p>Gérez tous vos utilisateurs en un seul endroit</p>
</div>


<c:if test="${!empty param.message}">
	<div class="message ${param.status == 'success' ? 'success' : 'error'}">
		${param.message}
	</div>
</c:if>


<c:if test="${sessionScope.role eq 'admin'}">
<div style="text-align: center; margin: 20px 0;">
	<a class="btn-add" href="<c:url value='/add'/>">
		Ajouter un utilisateur
	</a>
</div>
</c:if>


<c:choose>
	<c:when test="${empty utilisateurs}">
    <div class="empty-state">
        <p>Aucun utilisateur trouvé</p>
        <span>Commencez par ajouter votre premier utilisateur</span>
    </div>
</c:when>
	<c:otherwise>
		<table>
			<thead>
				<tr>
					<c:choose>
						<c:when test="${sessionScope.role eq 'admin'}">
							<th>ID</th>
							<th>Nom</th>
							<th>Prénom</th>
							<th>Login</th>
							<th>Mot de passe</th>
							<th>Rôle</th>
							<th>Actions</th>
						</c:when>
						<c:otherwise>
							<th>Prénom</th>
							<th>Nom</th>
						</c:otherwise>
					</c:choose>
				</tr>
			</thead>
			<tbody>
				<c:forEach var="u" items="${utilisateurs}">
					<tr>
						<c:choose>
							<c:when test="${sessionScope.role eq 'admin'}">
								<td>${u.id}</td>
								<td>${u.nom}</td>
								<td>${u.prenom}</td>
								<td>${u.login}</td>
								<td><span class="password-masked">••••••••</span></td>
								<td><span class="role-badge role-badge--${u.role}"><c:choose><c:when test="${u.role eq 'admin'}">Administrateur</c:when><c:otherwise>Utilisateur</c:otherwise></c:choose></span></td>
								<td>
									<a class="btn-edit" href="<c:url value='/update?id=${u.id}'/>">Modifier</a>
									<button class="btn-delete" onclick="openDeleteModal('<c:url value='/delete?id=${u.id}'/>', '${u.prenom} ${u.nom}')">Supprimer</button>
								</td>
							</c:when>
							<c:otherwise>
								<td>${u.prenom}</td>
								<td>${u.nom}</td>
							</c:otherwise>
						</c:choose>
					</tr>
				</c:forEach>
			</tbody>
		</table>
	</c:otherwise>
</c:choose>

<!-- ── Delete Confirmation Modal ── -->
<div id="deleteModal" class="modal-overlay" onclick="closeDeleteModal(event)">
    <div class="modal-card">
        <div class="modal-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/></svg>
        </div>
        <h3 class="modal-title">Supprimer l'utilisateur</h3>
        <p class="modal-desc">Voulez-vous vraiment supprimer <strong id="deleteUserName"></strong> ? Cette action est irréversible.</p>
        <div class="modal-actions">
            <button class="modal-btn-cancel" onclick="closeDeleteModal()">Annuler</button>
            <a id="deleteConfirmLink" href="#" class="modal-btn-confirm">Supprimer</a>
        </div>
    </div>
</div>

<script>
    function openDeleteModal(url, name) {
        document.getElementById('deleteConfirmLink').href = url;
        document.getElementById('deleteUserName').textContent = name;
        document.getElementById('deleteModal').classList.add('open');
    }
    function closeDeleteModal(e) {
        if (!e || e.target === document.getElementById('deleteModal')) {
            document.getElementById('deleteModal').classList.remove('open');
        }
    }
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeDeleteModal();
    });
</script>

<%@ include file="/inc/footer.jsp" %>
