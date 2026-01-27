<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<c:set var="pageTitle" value="Modifier un utilisateur" scope="request"/>
<c:set var="currentPage" value="update" scope="request"/>

<%@ include file="/inc/header.jsp" %>


<div class="page-header">
    <h1>Modifier un utilisateur</h1>
    <p>Modifier l'utilisateur ${form.prenom} ${form.nom}</p>
</div>

<c:if test="${not empty form.statusMessage}">
    <div class="message error">
        ${form.statusMessage}
    </div>
</c:if>

<form action="<c:url value='/update'/>" method="post">
    <input type="hidden" name="id" value="${form.id}">

    <label for="nom">Nom :</label>
    <input type="text" name="nom" id="nom" value="${form.nom}">
    <div style="margin-bottom: 20px;">
        <c:if test="${not empty form.errors.nom}">
            <span class="message error">${form.errors.nom}</span>
        </c:if>
    </div>

    <label for="prenom">Prénom :</label>
    <input type="text" name="prenom" id="prenom" value="${form.prenom}">
    <div style="margin-bottom: 20px;">
        <c:if test="${not empty form.errors.prenom}">
            <span class="message error">${form.errors.prenom}</span>
        </c:if>
    </div>

    <label for="login">Login :</label>
    <input type="text" name="login" id="login" value="${form.login}">
    <div style="margin-bottom: 20px;">
        <c:if test="${not empty form.errors.login}">
            <span class="message error">${form.errors.login}</span>
        </c:if>
    </div>

    <label for="password">Mot de passe :</label>
    <div class="password-wrapper">
        <input type="password" name="password" id="password" value="${form.password}">
        <span class="toggle-password" onclick="togglePassword()">👁️</span>
    </div>
    <div style="margin-bottom: 30px;">
        <c:if test="${not empty form.errors.password}">
            <span class="message error">${form.errors.password}</span>
        </c:if>
    </div>

    <input type="submit" value="Modifier">
</form>

<div style="text-align: center; margin-top: 20px;">
    <a href="<c:url value='/list'/>" class="btn-edit">
        Retour à la liste
    </a>
</div>

<script>
    function togglePassword() {
        const passwordInput = document.getElementById('password');
        const toggleIcon = document.querySelector('.toggle-password');
        
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            toggleIcon.textContent = '🙈';
        } else {
            passwordInput.type = 'password';
            toggleIcon.textContent = '👁️';
        }
    }
</script>

<%@ include file="/inc/footer.jsp" %>