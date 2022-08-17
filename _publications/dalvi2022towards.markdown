---
layout: publication
title: "Towards Teachable Reasoning Systems"
authors: Bhavana Dalvi, Oyvind Tafjord, Peter Clark
conference: 
year: 2022
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/2204.13074v1"}
tags: []
---
Our goal is a teachable reasoning system for question-answering (QA), where a
user can interact with faithful answer explanations, and correct errors so that
the system improves over time. Our approach is three-fold: First, generated
chains of reasoning show how answers are implied by the system's own internal
beliefs. Second, users can interact with the explanations to identify erroneous
model beliefs and provide corrections. Third, we augment the model with a
dynamic memory of such corrections. Retrievals from memory are used as
additional context for QA, to help avoid previous mistakes in similar new
situations - a novel type of memory-based continuous learning. To our
knowledge, this is the first system to generate chains that are both faithful
(the answer follows from the reasoning) and truthful (the chain reflects the
system's own beliefs, as ascertained by self-querying). In evaluation, users
judge that a majority (65%+) of generated chains clearly show how an answer
follows from a set of facts - substantially better than a high-performance
baseline. We also find that using simulated feedback, our system (called
EntailmentWriter) continually improves with time, requiring feedback on only
25% of training examples to reach within 1% of the upper-bound (feedback on all
examples). We observe a similar trend with real users. This suggests new
opportunities for using language models in an interactive setting where users
can inspect, debug, correct, and improve a system's performance over time.