---
layout: default
title: A Survey of Machine Learning for Big Code and Naturalness
---
### Explaining Machine Learning Algorithms


#### 🏷 Browse Papers by Tag
{% assign rawtags = Array.new %}
{% for publication in site.publications %}
  {% assign ttags = publication.tags  %}  
  {% assign rawtags = rawtags | concat: ttags %}  
{% endfor %}
{% assign rawtags = rawtags | uniq | sort_natural %}
{% for tag in rawtags %}<tag><a href="/tags.html#{{ tag }}">{{ tag }}</a></tag> {% endfor %}

### About This Site

This site serves as a [living literature review](https://en.wikipedia.org/wiki/Living_review) for exploring the domain of explainability. If you have written a paper or come across an interesting paper that is not already in the repository, please consider adding it by sending a pull request. 

### Contributing

This research area is evolving so fast that a static review cannot keep up.
But a website can! We hope to make this site a living document.
Anyone can add a paper to this web site, essentially by creating one Markdown file.
To contribute, open a pull request in GitHub, by following [these instructions 
for contributing](contributing.html).

### Contributors

The core taxonomy was created by. 

#### Contributors to the website
This website accepts external [contributions](/contributing.html).
Please, feel free to add your name below, once you contribute to this
website. A comprehensive list can be found [here](https://github.com/x/xx/graphs/contributors).

[Avinash Bhat](https://avinashbhat.github.io/about)
