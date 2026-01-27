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


<div style="text-align: center; margin: 20px 0;">
	<a class="btn-add" href="<c:url value='/add'/>">
		Ajouter un utilisateur
	</a>
</div>


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
					<th>ID</th>
					<th>Nom</th>
					<th>Prénom</th>
					<th>Login</th>
					<th>Mot de passe</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				<c:forEach var="u" items="${utilisateurs}">
					<tr>
						<td>${u.id}</td>
						<td>${u.nom}</td>
						<td>${u.prenom}</td>
						<td>${u.login}</td>
						<td>${u.password}</td>
						<td>
							<a class="btn-edit" href="<c:url value='/update?id=${u.id}'/>">
								Modifier
							</a>
							<a class="btn-delete" 
							   href="<c:url value='/delete?id=${u.id}'/>"
							   onclick="return confirm('Êtes-vous sûr de vouloir supprimer cet utilisateur ?');">
								Supprimer
							</a>
						</td>
					</tr>
				</c:forEach>
			</tbody>
		</table>
	</c:otherwise>
</c:choose>

<%@ include file="/inc/footer.jsp" %>
