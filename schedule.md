---
title: Schedule
wide: true
---
{%- assign s = site.data.schedule -%}
{%- assign td = s.fieldtrip.date | date: "%Y%m%d" -%}
{%- assign prev = "00000000" -%}
{%- assign unit = 0 -%}

# Schedule

The course week by week, {{ s.year }}. Framework and game names link to their handouts. Prep tasks and readings are in BrightSpace.

<table class="schedule">
<thead><tr><th>Date</th><th>Class</th><th>Topic</th><th>Assignment</th></tr></thead>
<tbody>
{%- for c in s.classes %}
{%- assign cd = c.date | date: "%Y%m%d" -%}
{%- assign trip_here = false -%}
{%- if td > prev -%}{%- if td < cd -%}{%- assign trip_here = true -%}{%- endif -%}{%- endif -%}
{%- for d in s.deadlines -%}
{%- if d.date != "" -%}
{%- assign dd = d.date | date: "%Y%m%d" -%}
{%- if dd > prev and dd <= cd -%}
{%- if trip_here == false or dd < td %}
<tr class="due"><td class="nowrap">{{ d.date | date: "%a %-d %b" }}</td><td></td><td class="what" colspan="2">{% if d.url %}<a href="{{ d.url | relative_url }}">{{ d.label }}</a>{% else %}{{ d.label }}{% endif %}{% if d.time != "" %}, {{ d.time }}{% endif %}</td></tr>
{%- endif -%}
{%- endif -%}
{%- endif -%}
{%- endfor -%}
{%- if trip_here %}
<tr class="trip"><td class="nowrap">{{ s.fieldtrip.date | date: "%a %-d %b" }}</td><td>Trip</td><td colspan="2">{{ s.fieldtrip.name }}, {{ s.fieldtrip.place }} (replaces the {{ s.fieldtrip.replaces | date: "%a %-d %b" }} class)</td></tr>
{%- for d in s.deadlines -%}
{%- if d.date != "" -%}
{%- assign dd = d.date | date: "%Y%m%d" -%}
{%- if dd >= td and dd <= cd %}
<tr class="due"><td class="nowrap">{{ d.date | date: "%a %-d %b" }}</td><td></td><td class="what" colspan="2">{% if d.url %}<a href="{{ d.url | relative_url }}">{{ d.label }}</a>{% else %}{{ d.label }}{% endif %}{% if d.time != "" %}, {{ d.time }}{% endif %}</td></tr>
{%- endif -%}
{%- endif -%}
{%- endfor -%}
{%- endif -%}
{%- if c.unit != unit -%}
{%- assign unit = c.unit -%}
{%- assign u = s.units | where: "n", c.unit | first %}
<tr class="unit"><td colspan="4">Unit {{ u.n }}: {{ u.name }}</td></tr>
{%- endif %}
{%- assign t = c.topic -%}
{%- assign extra = "" -%}
{%- for r in c.read -%}
{%- assign href = r.url | relative_url -%}
{%- assign link = '<a href="' | append: href | append: '">' | append: r.label | append: '</a>' -%}
{%- if t contains r.label -%}{%- assign t = t | replace: r.label, link -%}{%- else -%}{%- assign extra = extra | append: '<br>' | append: link -%}{%- endif -%}
{%- endfor %}
<tr><td class="nowrap">{{ c.date | date: "%a %-d %b" }}</td><td>{{ c.n }}</td><td>{{ t }}{{ extra }}</td><td>{% if c.assign %}<a href="{{ c.assign.url | relative_url }}">{{ c.assign.label }}</a>{% endif %}</td></tr>
{%- assign prev = cd -%}
{%- endfor -%}
{%- for d in s.deadlines -%}
{%- assign dd = "99999999" -%}
{%- if d.date != "" -%}{%- assign dd = d.date | date: "%Y%m%d" -%}{%- endif -%}
{%- if dd > prev %}
<tr class="due"><td{% if d.date != "" %} class="nowrap"{% endif %}>{% if d.date != "" %}{{ d.date | date: "%a %-d %b" }}{% else %}{{ d.short }}{% endif %}</td><td></td><td class="what" colspan="2">{% if d.url %}<a href="{{ d.url | relative_url }}">{{ d.label }}</a>{% else %}{{ d.label }}{% endif %}{% if d.time != "" %}, {{ d.time }}{% endif %}</td></tr>
{%- endif -%}
{%- endfor %}
</tbody>
</table>
