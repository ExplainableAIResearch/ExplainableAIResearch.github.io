---
layout: publication
title: "The elephant in the interpretability room: Why use attention as explanation when we have saliency methods?"
authors: Jasmijn Bastings, Katja Filippova
conference: Proceedings of the 2020 EMNLP Workshop BlackboxNLP
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2010.05607v1"}
tags: []
---
There is a recent surge of interest in using attention as explanation of
model predictions, with mixed evidence on whether attention can be used as
such. While attention conveniently gives us one weight per input token and is
easily extracted, it is often unclear toward what goal it is used as
explanation. We find that often that goal, whether explicitly stated or not, is
to find out what input tokens are the most relevant to a prediction, and that
the implied user for the explanation is a model developer. For this goal and
user, we argue that input saliency methods are better suited, and that there
are no compelling reasons to use attention, despite the coincidence that it
provides a weight for each input. With this position paper, we hope to shift
some of the recent focus on attention to saliency methods, and for authors to
clearly state the goal and user for their explanations.