---
layout: publication
title: "Synthetic Benchmarks for Scientific Research in Explainable Machine Learning"
authors: Yang Liu, Sujay Khandagale, Colin White, Willie Neiswanger
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2106.12543v4"}
tags: []
---
As machine learning models grow more complex and their applications become
more high-stakes, tools for explaining model predictions have become
increasingly important. This has spurred a flurry of research in model
explainability and has given rise to feature attribution methods such as LIME
and SHAP. Despite their widespread use, evaluating and comparing different
feature attribution methods remains challenging: evaluations ideally require
human studies, and empirical evaluation metrics are often data-intensive or
computationally prohibitive on real-world datasets. In this work, we address
this issue by releasing XAI-Bench: a suite of synthetic datasets along with a
library for benchmarking feature attribution algorithms. Unlike real-world
datasets, synthetic datasets allow the efficient computation of conditional
expected values that are needed to evaluate ground-truth Shapley values and
other metrics. The synthetic datasets we release offer a wide variety of
parameters that can be configured to simulate real-world data. We demonstrate
the power of our library by benchmarking popular explainability techniques
across several evaluation metrics and across a variety of settings. The
versatility and efficiency of our library will help researchers bring their
explainability methods from development to deployment. Our code is available at
https://github.com/abacusai/xai-bench.