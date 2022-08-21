---
layout: publication
title: "Confounder-Aware Visualization of ConvNets"
authors: Qingyu Zhao, Ehsan Adeli, Adolf Pfefferbaum, Edith V. Sullivan, Kilian M. Pohl
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1907.12727v2"}
tags: []
---
With recent advances in deep learning, neuroimaging studies increasingly rely
on convolutional networks (ConvNets) to predict diagnosis based on MR images.
To gain a better understanding of how a disease impacts the brain, the studies
visualize the salience maps of the ConvNet highlighting voxels within the brain
majorly contributing to the prediction. However, these salience maps are
generally confounded, i.e., some salient regions are more predictive of
confounding variables (such as age) than the diagnosis. To avoid such
misinterpretation, we propose in this paper an approach that aims to visualize
confounder-free saliency maps that only highlight voxels predictive of the
diagnosis. The approach incorporates univariate statistical tests to identify
confounding effects within the intermediate features learned by ConvNet. The
influence from the subset of confounded features is then removed by a novel
partial back-propagation procedure. We use this two-step approach to visualize
confounder-free saliency maps extracted from synthetic and two real datasets.
These experiments reveal the potential of our visualization in producing
unbiased model-interpretation.