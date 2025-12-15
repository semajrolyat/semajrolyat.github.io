---
layout: page
permalink: /advising/
title: advising
description: My advising page
nav: true
nav_order: 2
---

Advising at George Washington University (GWU).

<div class="gwu-advising">

{% assign selected_courses = site.advising | where: "university", "gwu" %}
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


