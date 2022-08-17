---
layout: publication
title: "Analogies and Feature Attributions for Model Agnostic Explanation of Similarity Learners"
authors: Karthikeyan Natesan Ramamurthy, Amit Dhurandhar, Dennis Wei, Zaid Bin Tariq
conference: 
year: 2022
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2202.01153v1"}
tags: []
---
Post-hoc explanations for black box models have been studied extensively in
classification and regression settings. However, explanations for models that
output similarity between two inputs have received comparatively lesser
attention. In this paper, we provide model agnostic local explanations for
similarity learners applicable to tabular and text data. We first propose a
method that provides feature attributions to explain the similarity between a
pair of inputs as determined by a black box similarity learner. We then propose
analogies as a new form of explanation in machine learning. Here the goal is to
identify diverse analogous pairs of examples that share the same level of
similarity as the input pair and provide insight into (latent) factors
underlying the model's prediction. The selection of analogies can optionally
leverage feature attributions, thus connecting the two forms of explanation
while still maintaining complementarity. We prove that our analogy objective
function is submodular, making the search for good-quality analogies efficient.
We apply the proposed approaches to explain similarities between sentences as
predicted by a state-of-the-art sentence encoder, and between patients in a
healthcare utilization application. Efficacy is measured through quantitative
evaluations, a careful user study, and examples of explanations.