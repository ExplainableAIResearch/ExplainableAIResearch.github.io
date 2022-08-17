---
layout: publication
title: "Revisiting Sanity Checks for Saliency Maps"
authors: Gal Yona, Daniel Greenfeld
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2110.14297v1"}
tags: []
---
Saliency methods are a popular approach for model debugging and
explainability. However, in the absence of ground-truth data for what the
correct maps should be, evaluating and comparing different approaches remains a
long-standing challenge. The sanity checks methodology of Adebayo et al
[Neurips 2018] has sought to address this challenge. They argue that some
popular saliency methods should not be used for explainability purposes since
the maps they produce are not sensitive to the underlying model that is to be
explained. Through a causal re-framing of their objective, we argue that their
empirical evaluation does not fully establish these conclusions, due to a form
of confounding introduced by the tasks they evaluate on. Through various
experiments on simple custom tasks we demonstrate that some of their
conclusions may indeed be artifacts of the tasks more than a criticism of the
saliency methods themselves. More broadly, our work challenges the utility of
the sanity check methodology, and further highlights that saliency map
evaluation beyond ad-hoc visual examination remains a fundamental challenge.