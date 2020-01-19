---
title: How Does a Database Work?
---

- What format is data saved in? (in memory and on disk)
- When does it move from memory to disk?
- Why can there only be one primary key per table?
- How does rolling back a transaction work?
- How are indexes formatted?
- When and how does a full table scan happen?
- What format is a prepared statement saved in?

In short, how does a database **work**?

I'm building a clone of [sqlite](https://www.sqlite.org/arch.html) from scratch in C and Golang in order to understand, and I'm going to document my process as I go.

Credits for C version: [cstack](https://github.com/cstack/db_tutorial)

# Table of Contents - C version
{% for part in site.parts %}- [{{part.title}}]({{site.baseurl}}{{part.url}})
{% endfor %}

# Table of Contents - Golang version
{% for part in site.goparts %}- [{{part.title}}]({{site.baseurl}}{{part.url}})
{% endfor %}

> "What I cannot create, I do not understand." -- [Richard Feynman](https://en.m.wikiquote.org/wiki/Richard_Feynman)

{% include image.html url="assets/images/arch2.gif" description="sqlite architecture (https://www.sqlite.org/arch.html)" %}
