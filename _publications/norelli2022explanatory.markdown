---
layout: publication
title: "Explanatory Learning: Beyond Empiricism in Neural Networks"
authors: Antonio Norelli, Giorgio Mariani, Luca Moschella, Andrea Santilli, Giambattista Parascandolo, Simone Melzi, Emanuele Rodolà
conference: 
year: 2022
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2201.10222v1"}
tags: []
---
We introduce Explanatory Learning (EL), a framework to let machines use
existing knowledge buried in symbolic sequences -- e.g. explanations written in
hieroglyphic -- by autonomously learning to interpret them. In EL, the burden
of interpreting symbols is not left to humans or rigid human-coded compilers,
as done in Program Synthesis. Rather, EL calls for a learned interpreter, built
upon a limited collection of symbolic sequences paired with observations of
several phenomena. This interpreter can be used to make predictions on a novel
phenomenon given its explanation, and even to find that explanation using only
a handful of observations, like human scientists do. We formulate the EL
problem as a simple binary classification task, so that common end-to-end
approaches aligned with the dominant empiricist view of machine learning could,
in principle, solve it. To these models, we oppose Critical Rationalist
Networks (CRNs), which instead embrace a rationalist view on the acquisition of
knowledge. CRNs express several desired properties by construction, they are
truly explainable, can adjust their processing at test-time for harder
inferences, and can offer strong confidence guarantees on their predictions. As
a final contribution, we introduce Odeen, a basic EL environment that simulates
a small flatland-style universe full of phenomena to explain. Using Odeen as a
testbed, we show how CRNs outperform empiricist end-to-end approaches of
similar size and architecture (Transformers) in discovering explanations for
novel phenomena.