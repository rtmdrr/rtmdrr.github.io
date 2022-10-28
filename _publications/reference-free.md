---
title: "On the Limitations of Reference-Free Evaluations of Generated Text"
collection: publications
permalink: /publication/reference-free
date: 2022-12-07
venue: 'Empirical Methods in Natural Language Processing (EMNLP)'
paperurl: '[https://arxiv.org/abs/2210.12563]'
citation: '<b>"On the Limitations of Reference-Free Evaluations of Generated Text."</b> Daniel Deutsch, Rotem Dror, and Dan Roth. <i> In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing.</i>'
---

<b> Abstract </b>
There is significant interest in developing evaluation metrics which accurately estimate the quality of generated text without the aid of a human-written reference text, which can be time consuming and expensive to collect. However, in this work, we demonstrate that these reference-free metrics are inherently biased and limited in their ability to evaluate generated text, and we argue that they should not be used to measure progress on tasks like machine translation or summarization. We show how reference-free metrics are equivalent to using one generation model to evaluate another, which has several limitations: (1) the metrics can be optimized at test time to find the approximate best-possible output, (2) they are inherently biased toward models which are more similar to their own, and (3) they can be biased against higher-quality outputs, including those written by humans. Therefore, we recommend that reference-free metrics should be used as diagnostic tools for analyzing and understanding model behavior instead of measures of how well models perform a task, in which the goal is to achieve as high of a score as possible.
