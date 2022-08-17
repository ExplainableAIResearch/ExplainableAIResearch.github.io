---
layout: publication
title: "DeepRare: Generic Unsupervised Visual Attention Models"
authors: Phutphalla Kong, Matei Mancas, Bernard Gosselin, Kimtho Po
conference: 
year: 2021
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2109.11439v1"}
tags: []
---
Human visual system is modeled in engineering field providing
feature-engineered methods which detect contrasted/surprising/unusual data into
images. This data is "interesting" for humans and leads to numerous
applications. Deep learning (DNNs) drastically improved the algorithms
efficiency on the main benchmark datasets. However, DNN-based models are
counter-intuitive: surprising or unusual data is by definition difficult to
learn because of its low occurrence probability. In reality, DNN-based models
mainly learn top-down features such as faces, text, people, or animals which
usually attract human attention, but they have low efficiency in extracting
surprising or unusual data in the images. In this paper, we propose a new
visual attention model called DeepRare2021 (DR21) which uses the power of DNNs
feature extraction and the genericity of feature-engineered algorithms. This
algorithm is an evolution of a previous version called DeepRare2019 (DR19)
based on a common framework. DR21 1) does not need any training and uses the
default ImageNet training, 2) is fast even on CPU, 3) is tested on four very
different eye-tracking datasets showing that the DR21 is generic and is always
in the within the top models on all datasets and metrics while no other model
exhibits such a regularity and genericity. Finally DR21 4) is tested with
several network architectures such as VGG16 (V16), VGG19 (V19) and MobileNetV2
(MN2) and 5) it provides explanation and transparency on which parts of the
image are the most surprising at different levels despite the use of a
DNN-based feature extractor. DeepRare2021 code can be found at
https://github.com/numediart/VisualAttention-RareFamil}.