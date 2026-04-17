<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>

<c:set var="pageTitle" value="Bienvenue" scope="request"/>
<c:set var="currentPage" value="welcome" scope="request"/>

<%@ include file="/inc/header.jsp" %>

<c:if test="${!empty param.message}">
	<div class="message ${param.status == 'success' ? 'success' : 'error'}">
		${param.message}
	</div>
</c:if>

<div class="welcome-container">

    <!-- Welcome Hero Card -->
    <div class="welcome-hero">
        <div class="welcome-avatar">
            <c:out value="${fn:substring(sessionScope.prenom, 0, 1)}${fn:substring(sessionScope.nom, 0, 1)}" default="${fn:substring(sessionScope.login, 0, 2)}"/>
        </div>
        <h1 class="welcome-title">
            Bienvenue, <span class="welcome-name">${sessionScope.prenom} ${sessionScope.nom}</span>
        </h1>
        <p class="welcome-subtitle">
            Vous êtes connecté en tant que
            <span class="role-badge role-badge--${sessionScope.role}">
                <c:choose>
                    <c:when test="${sessionScope.role eq 'admin'}">Administrateur</c:when>
                    <c:otherwise>Utilisateur</c:otherwise>
                </c:choose>
            </span>
        </p>
    </div>

    <!-- Info Cards Grid -->
    <div class="welcome-cards">

        <div class="welcome-card">
            <div class="welcome-card-icon welcome-card-icon--user">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                    <circle cx="12" cy="7" r="4"/>
                </svg>
            </div>
            <div class="welcome-card-label">Identifiant</div>
            <div class="welcome-card-value">${sessionScope.login}</div>
        </div>

        <div class="welcome-card">
            <div class="welcome-card-icon welcome-card-icon--name">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5.52 19c.64-2.2 1.84-3 3.22-3h6.52c1.38 0 2.58.8 3.22 3"/>
                    <circle cx="12" cy="10" r="3"/>
                    <circle cx="12" cy="12" r="10"/>
                </svg>
            </div>
            <div class="welcome-card-label">Nom complet</div>
            <div class="welcome-card-value">${sessionScope.prenom} ${sessionScope.nom}</div>
        </div>

        <div class="welcome-card">
            <div class="welcome-card-icon welcome-card-icon--role">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                </svg>
            </div>
            <div class="welcome-card-label">Rôle</div>
            <div class="welcome-card-value">
                <c:choose>
                    <c:when test="${sessionScope.role eq 'admin'}">Administrateur</c:when>
                    <c:otherwise>Utilisateur</c:otherwise>
                </c:choose>
            </div>
        </div>

    </div>

    <!-- Quick Actions (admin only) -->
    <c:if test="${sessionScope.role eq 'admin'}">
    <div class="welcome-actions">
        <h2 class="welcome-actions-title">Accès rapide</h2>
        <div class="welcome-actions-grid">
            <a href="<c:url value='/list'/>" class="welcome-action-btn">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                    <circle cx="9" cy="7" r="4"/>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
                </svg>
                <span>Liste des utilisateurs</span>
            </a>
            <a href="<c:url value='/add'/>" class="welcome-action-btn welcome-action-btn--add">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
                    <circle cx="9" cy="7" r="4"/>
                    <line x1="19" y1="8" x2="19" y2="14"/>
                    <line x1="22" y1="11" x2="16" y2="11"/>
                </svg>
                <span>Ajouter un utilisateur</span>
            </a>
        </div>
    </div>
    </c:if>

</div>

<%@ include file="/inc/footer.jsp" %>
