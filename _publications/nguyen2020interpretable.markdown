---
layout: publication
title: "Interpretable Time Series Classification using Linear Models and Multi-resolution Multi-domain Symbolic Representations"
authors: Thach Le Nguyen, Severin Gsponer, Iulia Ilie, Martin O'Reilly, Georgiana Ifrim
conference: Data Mining and Knowledge Discovery 33 (2019) 1183-1222
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2006.01667v1"}
tags: []
---
The time series classification literature has expanded rapidly over the last
decade, with many new classification approaches published each year. Prior
research has mostly focused on improving the accuracy and efficiency of
classifiers, with interpretability being somewhat neglected. This aspect of
classifiers has become critical for many application domains and the
introduction of the EU GDPR legislation in 2018 is likely to further emphasize
the importance of interpretable learning algorithms. Currently,
state-of-the-art classification accuracy is achieved with very complex models
based on large ensembles (COTE) or deep neural networks (FCN). These approaches
are not efficient with regard to either time or space, are difficult to
interpret and cannot be applied to variable-length time series, requiring
pre-processing of the original series to a set fixed-length. In this paper we
propose new time series classification algorithms to address these gaps. Our
approach is based on symbolic representations of time series, efficient
sequence mining algorithms and linear classification models. Our linear models
are as accurate as deep learning models but are more efficient regarding
running time and memory, can work with variable-length time series and can be
interpreted by highlighting the discriminative symbolic features on the
original time series. We show that our multi-resolution multi-domain linear
classifier (mtSS-SEQL+LR) achieves a similar accuracy to the state-of-the-art
COTE ensemble, and to recent deep learning methods (FCN, ResNet), but uses a
fraction of the time and memory required by either COTE or deep models. To
further analyse the interpretability of our classifier, we present a case study
on a human motion dataset collected by the authors. We release all the results,
source code and data to encourage reproducibility.