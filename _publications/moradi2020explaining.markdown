---
layout: publication
title: "Explaining Black-box Models for Biomedical Text Classification"
authors: Milad Moradi, Matthias Samwald
conference: 
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://dx.doi.org/10.1109/JBHI.2021.3056748"}
tags: []
---
In this paper, we propose a novel method named Biomedical Confident Itemsets
Explanation (BioCIE), aiming at post-hoc explanation of black-box machine
learning models for biomedical text classification. Using sources of domain
knowledge and a confident itemset mining method, BioCIE discretizes the
decision space of a black-box into smaller subspaces and extracts semantic
relationships between the input text and class labels in different subspaces.
Confident itemsets discover how biomedical concepts are related to class labels
in the black-box's decision space. BioCIE uses the itemsets to approximate the
black-box's behavior for individual predictions. Optimizing fidelity,
interpretability, and coverage measures, BioCIE produces class-wise
explanations that represent decision boundaries of the black-box. Results of
evaluations on various biomedical text classification tasks and black-box
models demonstrated that BioCIE can outperform perturbation-based and decision
set methods in terms of producing concise, accurate, and interpretable
explanations. BioCIE improved the fidelity of instance-wise and class-wise
explanations by 11.6% and 7.5%, respectively. It also improved the
interpretability of explanations by 8%. BioCIE can be effectively used to
explain how a black-box biomedical text classification model semantically
relates input texts to class labels. The source code and supplementary material
are available at https://github.com/mmoradi-iut/BioCIE.