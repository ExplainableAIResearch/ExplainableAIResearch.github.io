---
layout: publication
title: "Looking Deeper into Tabular LIME"
authors: Damien Garreau, Ulrike von Luxburg
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2008.11092v3"}
tags: []
---
In this paper, we present a thorough theoretical analysis of the default
implementation of LIME in the case of tabular data. We prove that in the large
sample limit, the interpretable coefficients provided by Tabular LIME can be
computed in an explicit way as a function of the algorithm parameters and some
expectation computations related to the black-box model. When the function to
explain has some nice algebraic structure (linear, multiplicative, or sparsely
depending on a subset of the coordinates), our analysis provides interesting
insights into the explanations provided by LIME. These can be applied to a
range of machine learning models including Gaussian kernels or CART random
forests. As an example, for linear functions we show that LIME has the
desirable property to provide explanations that are proportional to the
coefficients of the function to explain and to ignore coordinates that are not
used by the function to explain. For partition-based regressors, on the other
side, we show that LIME produces undesired artifacts that may provide
misleading explanations.