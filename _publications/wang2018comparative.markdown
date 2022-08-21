---
layout: publication
title: "A Comparative Study of Rule Extraction for Recurrent Neural Networks"
authors: Qinglong Wang, Kaixuan Zhang, Alexander G. Ororbia II, Xinyu Xing, Xue Liu, C. Lee Giles
conference: 
year: 2018
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/1801.05420v2"}
tags: []
---
Understanding recurrent networks through rule extraction has a long history.
This has taken on new interests due to the need for interpreting or verifying
neural networks. One basic form for representing stateful rules is
deterministic finite automata (DFA). Previous research shows that extracting
DFAs from trained second-order recurrent networks is not only possible but also
relatively stable. Recently, several new types of recurrent networks with more
complicated architectures have been introduced. These handle challenging
learning tasks usually involving sequential data. However, it remains an open
problem whether DFAs can be adequately extracted from these models.
Specifically, it is not clear how DFA extraction will be affected when applied
to different recurrent networks trained on data sets with different levels of
complexity. Here, we investigate DFA extraction on several widely adopted
recurrent networks that are trained to learn a set of seven regular Tomita
grammars. We first formally analyze the complexity of Tomita grammars and
categorize these grammars according to that complexity. Then we empirically
evaluate different recurrent networks for their performance of DFA extraction
on all Tomita grammars. Our experiments show that for most recurrent networks,
their extraction performance decreases as the complexity of the underlying
grammar increases. On grammars of lower complexity, most recurrent networks
obtain desirable extraction performance. As for grammars with the highest level
of complexity, while several complicated models fail with only certain
recurrent networks having satisfactory extraction performance.