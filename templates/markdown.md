---           
layout: post
title: {{title}}
comments: false
tags: {{tags}}
---

{# template for markdown with github pages #}

{%if source%}Font: {{source}}{%endif%}

{% for f in files %}
### {{f[1]}}
![{{f[1]}}]({{f[0]}})
{% endfor %}
