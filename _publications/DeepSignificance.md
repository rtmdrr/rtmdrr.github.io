---
title: "Deep Dominance - How to Properly Compare Deep Neural Models"
collection: publications
permalink: /publication/deepsignificance
date: 2019-07-28
venue: 'Association for Computational Linguistics (ACL)'
paperurl: 'https://www.aclweb.org/anthology/P19-1266/'
citation: '<b>"Deep Dominance - How to Properly Compare Deep Neural Models."</b> Rotem Dror, Segev Shlomov and Roi Reichart. <i> In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL) 2019.</i>'
---

<b> Abstract </b>
Comparing between Deep Neural Network (DNN) models based on their performance on unseen data is crucial for the progress of the NLP field. However, these models have a large number of hyper-parameters and, being non-convex, their convergence point depends on the random values chosen at initialization and during training. Proper DNN comparison hence requires a comparison between their empirical score distributions on unseen data, rather than between single evaluation scores as is standard for more simple, convex models. In this paper, we propose to adapt to this problem a recently proposed test for the Almost Stochastic Dominance relation between two distributions. We define the criteria for a high quality comparison method between DNNs, and show, both theoretically and through analysis of extensive experimental results with leading DNN models for sequence tagging tasks, that the proposed test meets all criteria while previously proposed methods fail to do so. We hope the test we propose here will set a new working practice in the NLP community

<b> Github </b>
https://github.com/rtmdrr/deepComparison

Check out this github too:
https://github.com/Kaleidophon/deep-significance
