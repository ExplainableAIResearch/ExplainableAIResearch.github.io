---
layout: publication
title: "Auditing Black-box Models for Indirect Influence"
authors: Philip Adler, Casey Falk, Sorelle A. Friedler, Gabriel Rybeck, Carlos Scheidegger, Brandon Smith, Suresh Venkatasubramanian
conference: 
year: 2016
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1602.07043v2"}
tags: []
---
Data-trained predictive models see widespread use, but for the most part they
are used as black boxes which output a prediction or score. It is therefore
hard to acquire a deeper understanding of model behavior, and in particular how
different features influence the model prediction. This is important when
interpreting the behavior of complex models, or asserting that certain
problematic attributes (like race or gender) are not unduly influencing
decisions.
  In this paper, we present a technique for auditing black-box models, which
lets us study the extent to which existing models take advantage of particular
features in the dataset, without knowing how the models work. Our work focuses
on the problem of indirect influence: how some features might indirectly
influence outcomes via other, related features. As a result, we can find
attribute influences even in cases where, upon further direct examination of
the model, the attribute is not referred to by the model at all.
  Our approach does not require the black-box model to be retrained. This is
important if (for example) the model is only accessible via an API, and
contrasts our work with other methods that investigate feature influence like
feature selection. We present experimental evidence for the effectiveness of
our procedure using a variety of publicly available datasets and models. We
also validate our procedure using techniques from interpretable learning and
feature selection, as well as against other black-box auditing procedures.