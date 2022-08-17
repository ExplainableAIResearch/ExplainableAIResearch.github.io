---
layout: publication
title: "A Case for Backward Compatibility for Human-AI Teams"
authors: Gagan Bansal, Besmira Nushi, Ece Kamar, Dan Weld, Walter Lasecki, Eric Horvitz
conference: 
year: 2019
additional_links: 
   - {name: "ArXiv", url: "http://arxiv.org/abs/1906.01148v1"}
tags: []
---
AI systems are being deployed to support human decision making in high-stakes
domains. In many cases, the human and AI form a team, in which the human makes
decisions after reviewing the AI's inferences. A successful partnership
requires that the human develops insights into the performance of the AI
system, including its failures. We study the influence of updates to an AI
system in this setting. While updates can increase the AI's predictive
performance, they may also lead to changes that are at odds with the user's
prior experiences and confidence in the AI's inferences, hurting therefore the
overall team performance. We introduce the notion of the compatibility of an AI
update with prior user experience and present methods for studying the role of
compatibility in human-AI teams. Empirical results on three high-stakes domains
show that current machine learning algorithms do not produce compatible
updates. We propose a re-training objective to improve the compatibility of an
update by penalizing new errors. The objective offers full leverage of the
performance/compatibility tradeoff, enabling more compatible yet accurate
updates.