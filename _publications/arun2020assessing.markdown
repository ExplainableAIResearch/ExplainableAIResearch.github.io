---
layout: publication
title: "Assessing the (Un)Trustworthiness of Saliency Maps for Localizing Abnormalities in Medical Imaging"
authors: Nishanth Arun, Nathan Gaw, Praveer Singh, Ken Chang, Mehak Aggarwal, Bryan Chen, Katharina Hoebel, Sharut Gupta, Jay Patel, Mishka Gidwani, Julius Adebayo, Matthew D. Li, Jayashree Kalpathy-Cramer
conference: 
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2008.02766v2"}
tags: []
---
Saliency maps have become a widely used method to make deep learning models
more interpretable by providing post-hoc explanations of classifiers through
identification of the most pertinent areas of the input medical image. They are
increasingly being used in medical imaging to provide clinically plausible
explanations for the decisions the neural network makes. However, the utility
and robustness of these visualization maps has not yet been rigorously examined
in the context of medical imaging. We posit that trustworthiness in this
context requires 1) localization utility, 2) sensitivity to model weight
randomization, 3) repeatability, and 4) reproducibility. Using the localization
information available in two large public radiology datasets, we quantify the
performance of eight commonly used saliency map approaches for the above
criteria using area under the precision-recall curves (AUPRC) and structural
similarity index (SSIM), comparing their performance to various baseline
measures. Using our framework to quantify the trustworthiness of saliency maps,
we show that all eight saliency map techniques fail at least one of the
criteria and are, in most cases, less trustworthy when compared to the
baselines. We suggest that their usage in the high-risk domain of medical
imaging warrants additional scrutiny and recommend that detection or
segmentation models be used if localization is the desired output of the
network. Additionally, to promote reproducibility of our findings, we provide
the code we used for all tests performed in this work at this link:
https://github.com/QTIM-Lab/Assessing-Saliency-Maps.