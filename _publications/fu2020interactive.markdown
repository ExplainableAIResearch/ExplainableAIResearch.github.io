---
layout: publication
title: "Interactive Knowledge Distillation"
authors: Shipeng Fu, Zhen Li, Jun Xu, Ming-Ming Cheng, Zitao Liu, Xiaomin Yang
conference: 
year: 2020
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2007.01476v3"}
tags: []
---
Knowledge distillation is a standard teacher-student learning framework to
train a light-weight student network under the guidance of a well-trained large
teacher network. As an effective teaching strategy, interactive teaching has
been widely employed at school to motivate students, in which teachers not only
provide knowledge but also give constructive feedback to students upon their
responses, to improve their learning performance. In this work, we propose an
InterActive Knowledge Distillation (IAKD) scheme to leverage the interactive
teaching strategy for efficient knowledge distillation. In the distillation
process, the interaction between teacher and student networks is implemented by
a swapping-in operation: randomly replacing the blocks in the student network
with the corresponding blocks in the teacher network. In the way, we directly
involve the teacher's powerful feature transformation ability to largely boost
the student's performance. Experiments with typical settings of teacher-student
networks demonstrate that the student networks trained by our IAKD achieve
better performance than those trained by conventional knowledge distillation
methods on diverse image classification datasets.