# E2MoCase: A Dataset for Emotional, Event and Moral Observations in News Articles on High-impact Legal Cases

> The way media reports on legal cases can significantly shape public opinion, often embedding subtle biases that influence societal views on justice and morality. Analyzing these biases requires a holistic approach that captures the emotional tone, moral framing, and specific events within the narratives.
In this work we introduce E2MoCase, a novel dataset designed to facilitate the integrated analysis of emotions, moral values, and events within legal narratives and media coverage.  By leveraging advanced models for emotion detection, moral value identification, and event extraction, E2MoCase offers a multi-dimensional perspective on how legal cases are portrayed in news articles.


In this repository, we provide the [E2MoCase dataset](https://arxiv.org/abs/2409.09001) and the full code to obtain the raw data from the [SwissDox](https://www.liri.uzh.ch/en/services/swissdox.html) platform. The dataset is also available on [HuggingFace](https://huggingface.co/datasets/lorenzozan/E2MoCase), where sentence embedding of the source paragraphs, generated with various pretrained language models (e.g., bert-base-uncased, Qwen3-0.6B), along with their annotations can be downloaded.

A preprint paper is available [here](https://arxiv.org/abs/2409.09001).




**We are continuously refining and expanding the E2moCase dataset. Stay tuned for upcoming updates!**


# Data Description

E2MoCase contains 97,251 paragraphs extracted from a total of 19,250 news articles. These news articles were obtained from about 100 candidate real-world cases related to legal matters that had significant media impact due to evidence of cultural biases, such as religious, political, gender, racial, and media biases. For each case, we manually verified its accuracy
in terms of reported news, we ensured it had significant media impact and it was covered by reputable
newspaper agencies.

All paragraphs are labeled with emotions and moralities. Of these, 50,975 paragraphs are also labeled with events, whereas the remaining ones do not contain events. For additional information, please refer to our [paper](https://arxiv.org/abs/2409.09001). The statistics of E2MoCase and its variants are shown as follows.


|                      | E2MoCase            | E2MoCase_noEvents     | E2MoCase_full        |
|----------------------|---------------------|-----------------------|----------------------|
| **# paragraphs**     |    50,975             |    46,276                | 97,251               |
| **avg # tokens**     | 275.106 ± 245.303  | 139.402 ± 220.950     | 210.532 ± 243.647    |
| **avg # emotions**   | 1.164 ± 0.757      | 1.634 ± 0.680         | 1.678 ± 0.657        |
| **avg # morals**     | 3.517 ± 3.870      | 1.773 ± 1.644         | 2.795 ± 2.424        |
| **avg # events**     | 3.597 ± 2.940      | 0.0 ± 0.0             | 1.885 ± 2.785        |

E2MoCase_noEvents, is the dataset obtained by removing paragraphs that do not contain events, while
E2MoCase_full, is the version that also includes paragraphs that do not contain events.



The dataset contains the following columns:


- `content_id`: Identification code of the news item within SwissDox.
- `P` : Paragraph identification code. It takes the form $P_i$, where $i$ is the $i$-th paragraph within the news item.
- `subject` :  Main subject of the news item (e.g., Amanda Knox case).
- `event` : List of events in JSON format
- `care`, `harm`, `fairness`, `cheating`, `loyalty`, `betrayal`, `authority`, `subversion`, `purity`, `degradation`: Real-valued scores (within 0 and 1) associated with moral values  
- `anticipation`, `trust`, `disgust`, `joy`, `optimism`, `surprise`, `love`, `anger`, `sadness`, `pessimism`, `fear`: Real-valued scores (within 0 and 1) associated with emotion values

After obtaining a valid SwissDox API key and running the instructions described in the [reconstruct_data.ipynb](reconstruct_data.ipynb) notebook (see the **Usage** section below), you will also obtain the **text** column containing the original textual content retrieved from SwissDox.

### Example data
Given the following paragraph:  

```
"Mystery without an answer: Where is Sarah's murderer? 
Julia Rossi was acquitted of murdering Sarah Bianchi. 
But if it wasn't her, then who killed the Italian woman with 25 stab wounds?"
```

An annotated data instance associated with the paragraph is as follows:

**event**:

```
[
  {"mention": "murder", "entities": {"Julia Rossi": "murderer", "Sarah Bianchi": "victim"}},
  {"mention": "kill", "entities": {"Julia Rossi": "murderer", "Sarah Bianchi": "victim"}}
]
```

**Moral columns**:
| care | harm | fairness | cheating | loyalty | betrayal | authority | subversion | purity | degradation |
|-------------|-------------|-----------------|-----------------|----------------|-----------------|------------------|-------------------|---------------|--------------------|
| 0.0         | 0.985  | 0.0             | 0.901      | 0.0            | 0.910        | 0.0              | 0.0               | 0.0           | 0.221        |

**Emotion columns**:
| anticipation | trust | disgust | joy  | optimism | surprise | love | anger | sadness | pessimism | fear |
|--------------|-------|---------|------|----------|----------|------|-------|---------|-----------|------|
| 0.0          | 0.0   | 0.521   | 0.0  | 0.0      | 0.0      | 0.0  | 0.5   | 0.0     | 0.0       | 0.0  |


*Note: in the above example, all references to real persons have been replaced with fictitious names.*.


# Data access and reproducibility

For this work, we used media data made available via Swissdox@LiRI(see https://www.liri.uzh.ch/en/services/swissdox.html for more information).

The raw news paragraphs required to reproduce the dataset cannot be openly shared [due to commercial restrictions](https://www.liri.uzh.ch/en/services/swissdox.html).  However, the original query (in YAML format) used for retrieving data from [Swissdox@LiRI](https://www.liri.uzh.ch/en/services/swissdox.html) can be found in the folder [**queries**](./queries/). Additionally, aggregated/derived data (i.e., labels for emotions, morality, and events) for each paragraph are available in the [**e2mocase.csv**](./e2mocase.csv) file. In the notebook [reconstruct_data.ipynb](./reconstruct_data.ipynb) we describe how to retrieve the original text from which the labels for emotions, morality, and events were derived. 


You can also download the dataset with the sentence embedding of the source paragraphs, generated with various pretrained language models (e.g., bert-base-uncased, Qwen3-0.6B) [here](https://huggingface.co/datasets/lorenzozan/E2MoCase).




# Guidelines for human annotation

The file [human_annotations/Guidelines.pdf](human_annotations/Guidelines.pdf) contains the instruction provided to the human annotatore to label the dataset, as described in our paper.

# Prompt for event extraction 

The prompt descriptions for event extraction are available in the [prompts](./prompts/) folder.


# Hyper-parameters selection

All experiments fine-tuning PLMs were run for five epochs with a batch size of 8, using the Adam optimizer and a learning rate of 5e-5. The MLP with a TF-IDF configuration was run for 50 epochs, using a single hidden layer with 100 units and, where possible, the same hyper-parameters as the experiments with PLMs.

# References

Please cite the following preprint — referring to its most recent update — in any research product that relies on the data contained in this repository:

```
@article{greco2024e2mocase,
  title={E2MoCase: A Dataset for Emotional, Event and Moral Observations in News Articles on High-impact Legal Cases},
  author={Greco, Candida M and Zangari, Lorenzo and Picca, Davide and Tagarelli, Andrea},
  journal={arXiv preprint arXiv:2409.09001},
  year={2024}
}
```


Also refer to the following paper on the topic:

```
@inproceedings{zangari2025me2,
  title={ME2-BERT: Are Events and Emotions what you need for Moral Foundation Prediction?},
  author={Zangari, Lorenzo and Greco, Candida M and Picca, Davide and Tagarelli, Andrea},
  booktitle={Proceedings of the 31st International Conference on Computational Linguistics},
  pages={9516--9532},
  year={2025}
}
```


