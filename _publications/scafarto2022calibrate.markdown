---
layout: publication
title: "Calibrate to Interpret"
authors: Gregory Scafarto, Nicolas Posocco, Antoine Bonnefoy
conference: 
year: 2022
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2207.03324v1"}
tags: []
---
Trustworthy machine learning is driving a large number of ML community works
in order to improve ML acceptance and adoption. The main aspect of trustworthy
machine learning are the followings: fairness, uncertainty, robustness,
explainability and formal guaranties. Each of these individual domains gains
the ML community interest, visible by the number of related publications.
However few works tackle the interconnection between these fields. In this
paper we show a first link between uncertainty and explainability, by studying
the relation between calibration and interpretation. As the calibration of a
given model changes the way it scores samples, and interpretation approaches
often rely on these scores, it seems safe to assume that the
confidence-calibration of a model interacts with our ability to interpret such
model. In this paper, we show, in the context of networks trained on image
classification tasks, to what extent interpretations are sensitive to
confidence-calibration. It leads us to suggest a simple practice to improve the
interpretation outcomes: Calibrate to Interpret.