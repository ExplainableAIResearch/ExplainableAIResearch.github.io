---
layout: publication
title: "Visual Saliency Based on Multiscale Deep Features"
authors: Guanbin Li, Yizhou Yu
conference: 
year: 2015
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1503.08663v3"}
tags: []
---
Visual saliency is a fundamental problem in both cognitive and computational
sciences, including computer vision. In this CVPR 2015 paper, we discover that
a high-quality visual saliency model can be trained with multiscale features
extracted using a popular deep learning architecture, convolutional neural
networks (CNNs), which have had many successes in visual recognition tasks. For
learning such saliency models, we introduce a neural network architecture,
which has fully connected layers on top of CNNs responsible for extracting
features at three different scales. We then propose a refinement method to
enhance the spatial coherence of our saliency results. Finally, aggregating
multiple saliency maps computed for different levels of image segmentation can
further boost the performance, yielding saliency maps better than those
generated from a single segmentation. To promote further research and
evaluation of visual saliency models, we also construct a new large database of
4447 challenging images and their pixelwise saliency annotation. Experimental
results demonstrate that our proposed method is capable of achieving
state-of-the-art performance on all public benchmarks, improving the F-Measure
by 5.0% and 13.2% respectively on the MSRA-B dataset and our new dataset
(HKU-IS), and lowering the mean absolute error by 5.7% and 35.1% respectively
on these two datasets.