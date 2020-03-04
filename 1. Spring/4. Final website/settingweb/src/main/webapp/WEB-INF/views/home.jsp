<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
   <title>Home</title>
   <%@include file="./common_resource.jsp" %>
   <script type="text/javascript" src="${pageContext.request.contextPath }/resources/js/home.js"></script>
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <meta http-equiv="X-UA-Compatible" content="ie=edge" />
   <script src="https://d3js.org/d3.v5.min.js"></script>
   <script src="http://labratrevenge.com/d3-tip/javascripts/d3.tip.v0.6.3.js"></script>
   <link href="${pageContext.request.contextPath }/resources/css/home.css" rel="stylesheet">
   <style>
      .chart div {
        font: 20px sans-serif;
        background-color: orange;
        text-align: left;
        padding: 3px;
        margin: 1px;
        color: steelblue;
      }

      .chart div:hover {
        font: 25px sans-serif;
        background-color: orangered;
        text-align: left;
        padding: 10x;
        margin: 1px;
        color: steelblue;
      }
    </style>
</head>
<body>
   <h1>HTM_WineQuality</h1>
   <button id="load_movieList" type="button">Total data</button>
   <button id="load_mean" type="button">Average data</button>
   <table>
      <thead>
         <tr>
            <th>fixed_acidity</th>
            <th>volitile_acidity</th>
            <th>citric_acid</th>
            <th>residual_sugar</th>
            <th>chlorides</th>
            <th>free_dioxide</th>
            <th>total_dioxide</th>
            <th>density</th>
            <th>pH</th>
            <th>sulphates</th>
            <th>alcohol</th>
            <th>quality</th>
         </tr>
      </thead>
      <tbody id="movieList">
      </tbody>
      <tbody class="chart" id="chart"></tbody>
   </table>
</body>
</html>