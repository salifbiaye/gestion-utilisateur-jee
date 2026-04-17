<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${pageTitle != null ? pageTitle : 'Gestion des Utilisateurs'}</title>
<c:choose>
    <c:when test="${sessionScope.theme == 'light'}">
        <link rel="stylesheet" href="<c:url value='/css/light/design.css'/>">
        <link rel="stylesheet" href="<c:url value='/css/light/header.css'/>">
        <link rel="stylesheet" href="<c:url value='/css/light/footer.css'/>">
    </c:when>
    <c:otherwise>
        <link rel="stylesheet" href="<c:url value='/css/dark/design.css'/>">
        <link rel="stylesheet" href="<c:url value='/css/dark/header.css'/>">
        <link rel="stylesheet" href="<c:url value='/css/dark/footer.css'/>">
    </c:otherwise>
</c:choose>
</head>
<body>

<c:choose>

<c:when test="${sessionScope.isConnected == true}">

<div class="app-layout">

  <aside class="sidebar">

    <div class="sidebar-brand">
      <div class="sidebar-brand-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="18" height="18" rx="3"/>
          <path d="M9 9h6M9 12h6M9 15h4"/>
        </svg>
      </div>
      <div class="sidebar-brand-text">
        <span class="sidebar-brand-name">Gestion des Utilisateurs</span>
      </div>
    </div>

    <%-- Bloc utilisateur connecté --%>
    <div class="sidebar-user">
      <div class="sidebar-user-avatar">
        <c:out value="${fn:substring(sessionScope.prenom, 0, 1)}${fn:substring(sessionScope.nom, 0, 1)}" default="${fn:substring(sessionScope.login, 0, 2)}"/>
      </div>
      <div class="sidebar-user-info">
        <span class="sidebar-user-name">
          <c:choose>
            <c:when test="${not empty sessionScope.prenom and not empty sessionScope.nom}">
              ${sessionScope.prenom} ${sessionScope.nom}
            </c:when>
            <c:otherwise>${sessionScope.login}</c:otherwise>
          </c:choose>
        </span>
        <span class="sidebar-user-role sidebar-user-role--${sessionScope.role}"><c:choose><c:when test="${sessionScope.role eq 'admin'}">Administrateur</c:when><c:otherwise>Utilisateur</c:otherwise></c:choose></span>
      </div>
    </div>

    <nav class="sidebar-nav">
      <a href="<c:url value='/list'/>" class="nav-link ${currentPage == 'list' ? 'active' : ''}">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
          <circle cx="9" cy="7" r="4"/>
          <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
        </svg>
        <span>Liste des utilisateurs</span>
      </a>
      <c:if test="${sessionScope.role eq 'admin'}">
        <a href="<c:url value='/add'/>" class="nav-link ${currentPage == 'add' ? 'active' : ''}">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
            <circle cx="9" cy="7" r="4"/>
            <line x1="19" y1="8" x2="19" y2="14"/>
            <line x1="22" y1="11" x2="16" y2="11"/>
          </svg>
          <span>Ajouter un utilisateur</span>
        </a>
      </c:if>
    </nav>

    <div class="sidebar-footer">
      <form action="<c:url value='/theme'/>" method="post" class="form-no-space">
        <button type="submit" class="sidebar-btn">
          <c:choose>
            <c:when test="${sessionScope.theme == 'light'}">
              <%-- Mode clair actif → icône soleil --%>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none"
                   stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="5"/>
                <line x1="12" y1="1" x2="12" y2="3"/>
                <line x1="12" y1="21" x2="12" y2="23"/>
                <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
                <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
                <line x1="1" y1="12" x2="3" y2="12"/>
                <line x1="21" y1="12" x2="23" y2="12"/>
                <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
                <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
              </svg>
              <span>Mode clair</span>
            </c:when>
            <c:otherwise>
              <%-- Mode sombre actif (dark ou défaut) → icône lune --%>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none"
                   stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
              </svg>
              <span>Mode sombre</span>
            </c:otherwise>
          </c:choose>
        </button>
      </form>
      <form action="<c:url value='/logout'/>" method="get" class="form-no-space">
        <button type="submit" class="sidebar-btn sidebar-btn--danger">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
            <polyline points="16 17 21 12 16 7"/>
            <line x1="21" y1="12" x2="9" y2="12"/>
          </svg>
          <span>Déconnexion</span>
        </button>
      </form>
    </div>

  </aside>

  <div class="main-wrapper">
    <main class="main-content">

</c:when>

<c:otherwise>
<div class="theme-toggle-float">
  <form action="<c:url value='/theme'/>" method="post" class="form-no-space">
    <button type="submit" class="theme-btn">
      <c:choose>
        <c:when test="${sessionScope.theme == 'light'}">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"/>
            <line x1="12" y1="1" x2="12" y2="3"/>
            <line x1="12" y1="21" x2="12" y2="23"/>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
            <line x1="1" y1="12" x2="3" y2="12"/>
            <line x1="21" y1="12" x2="23" y2="12"/>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
          </svg>
          Mode clair
        </c:when>
        <c:otherwise>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
          </svg>
          Mode sombre
        </c:otherwise>
      </c:choose>
    </button>
  </form>
</div>
<main class="main-content-login">
</c:otherwise>

</c:choose>
