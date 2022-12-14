---
layout: publication
title: "Person Re-identification by Saliency Learning"
authors: Rui Zhao, Wanli Ouyang, Xiaogang Wang
conference: 
year: 2014
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1412.1908v1"}
tags: []
---
Human eyes can recognize person identities based on small salient regions,
i.e. human saliency is distinctive and reliable in pedestrian matching across
disjoint camera views. However, such valuable information is often hidden when
computing similarities of pedestrian images with existing approaches. Inspired
by our user study result of human perception on human saliency, we propose a
novel perspective for person re-identification based on learning human saliency
and matching saliency distribution. The proposed saliency learning and matching
framework consists of four steps: (1) To handle misalignment caused by drastic
viewpoint change and pose variations, we apply adjacency constrained patch
matching to build dense correspondence between image pairs. (2) We propose two
alternative methods, i.e. K-Nearest Neighbors and One-class SVM, to estimate a
saliency score for each image patch, through which distinctive features stand
out without using identity labels in the training procedure. (3) saliency
matching is proposed based on patch matching. Matching patches with
inconsistent saliency brings penalty, and images of the same identity are
recognized by minimizing the saliency matching cost. (4) Furthermore, saliency
matching is tightly integrated with patch matching in a unified structural
RankSVM learning framework. The effectiveness of our approach is validated on
the VIPeR dataset and the CUHK01 dataset. Our approach outperforms the
state-of-the-art person re-identification methods on both datasets.