---
layout: publication
title: "Evaluating the Explainers: Black-Box Explainable Machine Learning for Student Success Prediction in MOOCs"
authors: Vinitra Swamy, Bahar Radmehr, Natasa Krco, Mirko Marras, Tanja Käser
conference: 
year: 2022
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2207.00551v1"}
tags: []
---
Neural networks are ubiquitous in applied machine learning for education.
Their pervasive success in predictive performance comes alongside a severe
weakness, the lack of explainability of their decisions, especially relevant in
human-centric fields. We implement five state-of-the-art methodologies for
explaining black-box machine learning models (LIME, PermutationSHAP,
KernelSHAP, DiCE, CEM) and examine the strengths of each approach on the
downstream task of student performance prediction for five massive open online
courses. Our experiments demonstrate that the families of explainers do not
agree with each other on feature importance for the same Bidirectional LSTM
models with the same representative set of students. We use Principal Component
Analysis, Jensen-Shannon distance, and Spearman's rank-order correlation to
quantitatively cross-examine explanations across methods and courses.
Furthermore, we validate explainer performance across curriculum-based
prerequisite relationships. Our results come to the concerning conclusion that
the choice of explainer is an important decision and is in fact paramount to
the interpretation of the predictive results, even more so than the course the
model is trained on. Source code and models are released at
http://github.com/epfl-ml4ed/evaluating-explainers.