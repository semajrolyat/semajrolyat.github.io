---
layout: page
permalink: /courses/
title: courses
description: A record of my courses.
nav: true
nav_order: 1
---

For now, this page is assumed to be a static description of your courses. You can convert it to a collection similar to `_projects/` so that you can have a dedicated page for each course.

Organize your courses by years, topics, or universities, however you like!

{% assign sorted_courses = site.courses | sort: "year" %}

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

