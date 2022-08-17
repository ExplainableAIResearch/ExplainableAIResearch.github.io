---
layout: publication
title: "Model-Agnostic Counterfactual Explanations for Consequential Decisions"
authors: Amir-Hossein Karimi, Gilles Barthe, Borja Balle, Isabel Valera
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1905.11190v5"}
tags: []
---
Predictive models are being increasingly used to support consequential
decision making at the individual level in contexts such as pretrial bail and
loan approval. As a result, there is increasing social and legal pressure to
provide explanations that help the affected individuals not only to understand
why a prediction was output, but also how to act to obtain a desired outcome.
To this end, several works have proposed optimization-based methods to generate
nearest counterfactual explanations. However, these methods are often
restricted to a particular subset of models (e.g., decision trees or linear
models) and differentiable distance functions. In contrast, we build on
standard theory and tools from formal verification and propose a novel
algorithm that solves a sequence of satisfiability problems, where both the
distance function (objective) and predictive model (constraints) are
represented as logic formulae. As shown by our experiments on real-world data,
our algorithm is: i) model-agnostic ({non-}linear, {non-}differentiable,
{non-}convex); ii) data-type-agnostic (heterogeneous features); iii)
distance-agnostic ($\ell_0, \ell_1, \ell_\infty$, and combinations thereof);
iv) able to generate plausible and diverse counterfactuals for any sample
(i.e., 100% coverage); and v) at provably optimal distances.