---
layout: publication
title: "Can We Trust Your Explanations? Sanity Checks for Interpreters in Android Malware Analysis"
authors: Ming Fan, Wenying Wei, Xiaofei Xie, Yang Liu, Xiaohong Guan, Ting Liu
conference: 
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2008.05895v1"}
tags: []
---
With the rapid growth of Android malware, many machine learning-based malware
analysis approaches are proposed to mitigate the severe phenomenon. However,
such classifiers are opaque, non-intuitive, and difficult for analysts to
understand the inner decision reason. For this reason, a variety of explanation
approaches are proposed to interpret predictions by providing important
features. Unfortunately, the explanation results obtained in the malware
analysis domain cannot achieve a consensus in general, which makes the analysts
confused about whether they can trust such results. In this work, we propose
principled guidelines to assess the quality of five explanation approaches by
designing three critical quantitative metrics to measure their stability,
robustness, and effectiveness. Furthermore, we collect five widely-used malware
datasets and apply the explanation approaches on them in two tasks, including
malware detection and familial identification. Based on the generated
explanation results, we conduct a sanity check of such explanation approaches
in terms of the three metrics. The results demonstrate that our metrics can
assess the explanation approaches and help us obtain the knowledge of most
typical malicious behaviors for malware analysis.