<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<c:set var="pageTitle" value="Connexion" scope="request"/>
<c:set var="currentPage" value="login" scope="request"/>

<%@ include file="/inc/header.jsp" %>

<div class="page-header">
    <h1>Connexion</h1>
    <p>Veuillez vous identifier</p>
</div>

<c:if test="${!empty param.message}">
	<div class="message ${param.status == 'success' ? 'success' : 'error'}">
		${param.message}
	</div>
</c:if>

<form action="<c:url value='/login'/>" method="post">
    
    <label for="login">Login :</label>
    <input type="text" name="login" id="login" value="${param.login}">

    <label for="password">Mot de passe :</label>
    <div class="password-wrapper">
        <input type="password" name="password" id="password">
        <span class="toggle-password" onclick="togglePassword('password', this)">👁️</span>
    </div>

    <input type="submit" value="Connexion">
</form>

<script>
    function togglePassword(inputId, iconElement) {
        const passwordInput = document.getElementById(inputId);

        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            iconElement.textContent = '🙈';
        } else {
            passwordInput.type = 'password';
            iconElement.textContent = '👁️';
        }
    }
</script>

<%@ include file="/inc/footer.jsp" %>