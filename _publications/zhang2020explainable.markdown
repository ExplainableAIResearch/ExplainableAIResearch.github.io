---
layout: publication
title: "Explainable Empirical Risk Minimization"
authors: L. Zhang, G. Karakasidis, A. Odnoblyudova, L. Dogruel, A. Jung
conference: 
year: 2020
additional_links: 
    - {name: "ArXiv", url: "http://arxiv.org/abs/2009.01492v3"}
tags: []
---
The successful application of machine learning (ML) methods becomes
increasingly dependent on their interpretability or explainability. Designing
explainable ML systems is instrumental to ensuring transparency of automated
decision-making that targets humans. The explainability of ML methods is also
an essential ingredient for trustworthy artificial intelligence. A key
challenge in ensuring explainability is its dependence on the specific human
user ("explainee"). The users of machine learning methods might have vastly
different background knowledge about machine learning principles. One user
might have a university degree in machine learning or related fields, while
another user might have never received formal training in high-school
mathematics. This paper applies information-theoretic concepts to develop a
novel measure for the subjective explainability of the predictions delivered by
a ML method. We construct this measure via the conditional entropy of
predictions, given a user feedback. The user feedback might be obtained from
user surveys or biophysical measurements. Our main contribution is the
explainable empirical risk minimization (EERM) principle of learning a
hypothesis that optimally balances between the subjective explainability and
risk. The EERM principle is flexible and can be combined with arbitrary machine
learning models. We present several practical implementations of EERM for
linear models and decision trees. Numerical experiments demonstrate the
application of EERM to detecting the use of inappropriate language on social
media.