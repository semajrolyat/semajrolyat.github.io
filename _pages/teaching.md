---
layout: page
permalink: /teaching/
title: teaching
description: My teaching portfolio
nav: true
nav_order: 1
---

This page lists courses for which I was instructor of record and provides a link to available content for those courses.  Courses with dates before this website's initial deployment (December 2025) may have sparse information, but this website will provide comprehensive revisions of all courses taught after this date.

<div class="gwu-courses">

The most recent offering of my courses at George Washington University (GWU).

{% assign selected_courses = site.courses | where: "university", "gwu" %}
{% assign sorted_courses = selected_courses | sort: "year" %}

  <!-- Generate cards for each course -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for course in sorted_courses reversed %}
      {% include courses_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for course in sorted_courses reversed %}
      {% include courses.liquid %}
    {% endfor %}
  </div>
  {% endif %}
</div>

