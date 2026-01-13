---
layout: page
permalink: /courses/
title: course
description: A record of my course teaching responsibilities
nav: true
nav_order: 1
---

This page lists courses for which I am currently or have been previously the instructor of record for and provides a link to available content if available.  Courses with dates before this website's initial deployment (December 2025) may have sparse information for course details; however, this website will provide comprehensive revisions of all courses taught after this date and I will attempt to move older course data into this format.

Here are my most recent course offering at George Washington University (GWU).

<div class="gwu-courses">

{% assign selected_courses = site.courses | where: "university", "gwu" %}
{% assign s0 = selected_courses | sort: "year" %}
{% assign s1 = s0 | group_by: "year" %}

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for s in s1 reversed %}
      {% assign s2 = s.items | sort: "term" %}
      {% for course in s2 %}
      {% include courses_horizontal.liquid %}
      {% endfor %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for s in s1 reversed %}
      {% assign s2 = s.items | sort: "term" %}
      {% for course in s2 %}
      {% include courses.liquid %}
      {% endfor %}
    {% endfor %}
  </div>
  {% endif %}

</div>
