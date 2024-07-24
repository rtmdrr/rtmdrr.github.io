---
title: "State of What Art? A Call for Multi-Prompt LLM Evaluation"
collection: publications
permalink: /publication/prompt
date: 2024-01-30
venue: 'TACL'
paperurl: 'https://arxiv.org/abs/2401.00595'
citation: '<b>"State of what art? a call for multi-prompt llm evaluation."</b> Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, Gabriel Stanovsky. <i> arXiv preprint arXiv:2401.00595. Accepted to TACL</i>'
---

<b> Abstract </b>
Recent advances in large language models (LLMs) have led to the development of various evaluation benchmarks. These benchmarks typically rely on a single instruction template for evaluating all LLMs on a specific task. In this paper, we comprehensively analyze the brittleness of results obtained via single-prompt evaluations across 6.5M instances, involving 20 different LLMs and 39 tasks from 3 benchmarks. To improve robustness of the analysis, we propose to evaluate LLMs with a set of diverse prompts instead. We discuss tailored evaluation metrics for specific use cases (e.g., LLM developers vs. developers interested in a specific downstream task), ensuring a more reliable and meaningful assessment of LLM capabilities. We then implement these criteria and conduct evaluations of multiple models, providing insights into the true strengths and limitations of current LLMs.

<b> Github </b>
https://github.com/SLAB-NLP/Multi-Prompt-LLM-Evaluation
