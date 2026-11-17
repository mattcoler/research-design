---
title: Schedule
---
{%- assign s = site.data.schedule -%}

# Schedule {{ s.year }}

Classes run on {{ s.days }}, {{ s.time }}. Rooms, readings and prep tasks for each class are in BrightSpace.

## Classes

{% include class-table.html %}

## Deadlines

<table>
  <thead><tr><th>Due</th><th>What</th></tr></thead>
  <tbody>
{%- for d in s.deadlines %}
    <tr><td>{% if d.date == "" or d.date == nil %}{{ d.short }}{% else %}{{ d.date | date: "%a %-d %b" }}{% if d.time != "" %}, {{ d.time }}{% endif %}{% endif %}</td><td>{{ d.label }}</td></tr>
{%- endfor %}
  </tbody>
</table>

The printed poster and the poster presentation are due in Class 13 ({% include classdate.html n="13" fmt="short" %}). See the [assignment briefs]({{ '/assignments/' | relative_url }}) for what each deadline involves.
