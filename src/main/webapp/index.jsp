<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<c:choose>
    <c:when test="${sessionScope.isConnected == true}">
        <c:choose>
            <c:when test="${sessionScope.role eq 'admin'}">
                <c:redirect url="/list"/>
            </c:when>
            <c:otherwise>
                <c:redirect url="/welcome"/>
            </c:otherwise>
        </c:choose>
    </c:when>
    <c:otherwise>
        <c:redirect url="/login"/>
    </c:otherwise>
</c:choose>
