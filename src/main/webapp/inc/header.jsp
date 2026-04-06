<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
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

<header class="main-header">
	<div class="header-container">
		<div class="logo">
			<h1>Gestion Utilisateurs</h1>
		</div>

		<nav class="main-nav">
			<c:choose>
				<c:when test="${sessionScope.isConnected == true}">
					<a href="<c:url value='/list'/>" class="nav-link ${currentPage == 'list' ? 'active' : ''}">Liste</a>
					<a href="<c:url value='/add'/>" class="nav-link ${currentPage == 'add' ? 'active' : ''}">Ajouter</a>
				</c:when>
				<c:otherwise>
					<a href="<c:url value='/login'/>" class="nav-link ${currentPage == 'login' ? 'active' : ''}">Connexion</a>

				</c:otherwise>
			</c:choose>
		</nav>

		<form action="<c:url value='/theme'/>" method="post" class="form-no-space">
   		 	<button type="submit" class="theme-btn">
       			 🌗 Thème
    		</button>
	 	</form>

		<c:if test="${sessionScope.isConnected == true}">
			<form action="<c:url value='/logout'/>" method="get" class="form-no-space">
			    <button type="submit" class="deconnexion-btn">
			        Déconnexion
			    </button>
			</form>
		</c:if>

	</div>
</header>

<main class="main-content">