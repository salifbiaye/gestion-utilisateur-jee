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

<form action="<c:url value='/login'/>" method="post" class="form-login">
    
    <label for="login">Login :</label>
    <input type="text" name="login" id="login" value="${param.login}">

    <label for="password">Mot de passe :</label>
    <div class="password-wrapper">
        <input type="password" name="password" id="password">
        <button type="button" class="toggle-password" onclick="togglePassword('password', this)" aria-label="Afficher/masquer le mot de passe">
            <svg class="eye-open" xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            <svg class="eye-closed" xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
        </button>
    </div>

    <input type="submit" value="Connexion">
</form>

<script>
    function togglePassword(inputId, btn) {
        const input = document.getElementById(inputId);
        const eyeOpen = btn.querySelector('.eye-open');
        const eyeClosed = btn.querySelector('.eye-closed');
        if (input.type === 'password') {
            input.type = 'text';
            eyeOpen.style.display = 'none';
            eyeClosed.style.display = '';
        } else {
            input.type = 'password';
            eyeOpen.style.display = '';
            eyeClosed.style.display = 'none';
        }
    }
</script>

<%@ include file="/inc/footer.jsp" %>