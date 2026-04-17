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
    <div class="message error">${form.statusMessage}</div>
</c:if>

<form action="<c:url value='/update'/>" method="post">
    <input type="hidden" name="id" value="${form.id}">

    <div class="form-grid">

        <div class="form-field">
            <label for="nom">Nom</label>
            <input type="text" name="nom" id="nom" value="${form.nom}">
            <c:if test="${not empty form.errors.nom}">
                <span class="field-error">${form.errors.nom}</span>
            </c:if>
        </div>

        <div class="form-field">
            <label for="prenom">Prénom</label>
            <input type="text" name="prenom" id="prenom" value="${form.prenom}">
            <c:if test="${not empty form.errors.prenom}">
                <span class="field-error">${form.errors.prenom}</span>
            </c:if>
        </div>

        <div class="form-field form-field--full">
            <label for="login">Login</label>
            <input type="text" name="login" id="login" value="${form.login}">
            <c:if test="${not empty form.errors.login}">
                <span class="field-error">${form.errors.login}</span>
            </c:if>
        </div>

        <div class="form-field form-field--full">
            <label for="password">Mot de passe</label>
            <div class="password-wrapper">
                <input type="password" name="password" id="password" value="${form.password}">
                <button type="button" class="toggle-password" onclick="togglePassword()" aria-label="Afficher/masquer le mot de passe">
                    <svg class="eye-open" xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    <svg class="eye-closed" xmlns="http://www.w3.org/2000/svg" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
                </button>
            </div>
            <c:if test="${not empty form.errors.password}">
                <span class="field-error">${form.errors.password}</span>
            </c:if>
        </div>

        <div class="form-field form-field--full">
            <label for="role">Rôle</label>
            <select name="role" id="role" class="form-select">
                <option value="user" ${form.role == 'user' || empty form.role ? 'selected' : ''}>Utilisateur</option>
                <option value="admin" ${form.role == 'admin' ? 'selected' : ''}>Administrateur</option>
            </select>
        </div>

    </div>

    <input type="submit" value="Modifier">
</form>

<div style="text-align: center; margin-top: 20px;">
    <a href="<c:url value='/list'/>" class="btn-edit">Retour à la liste</a>
</div>

<script>
    function togglePassword() {
        const input = document.getElementById('password');
        const btn = document.querySelector('.toggle-password');
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
