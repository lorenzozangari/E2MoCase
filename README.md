# E2MoCase: A Dataset for Emotional, Event and Moral Observations in News Articles on High-impact Legal Cases

> The way media reports on legal cases can significantly shape public opinion, often embedding subtle biases that influence societal views on justice and morality. Analyzing these biases requires a holistic approach that captures the emotional tone, moral framing, and specific events within the narratives.
In this work we introduce E2MoCase, a novel dataset designed to facilitate the integrated analysis of emotions, moral values, and events within legal narratives and media coverage.  By leveraging advanced models for emotion detection, moral value identification, and event extraction, E2MoCase offers a multi-dimensional perspective on how legal cases are portrayed in news articles.


In this repository, we provide the [E2MoCase dataset](https://arxiv.org/abs/2409.09001) and we describe the process to obtain the raw data from the [SwissDox](https://www.liri.uzh.ch/en/services/swissdox.html) platform. The paper is available [here](https://arxiv.org/abs/2409.09001).

**We are continually working to further enhance the E2moCase dataset. Stay tuned for more updates.**


# Data Description

E2MoCase contains 97,251 paragraphs extracted from a total of 19,250 news articles. These news articles were obtained from about 100 candidate real-world cases related to legal matters that had significant media impact due to evidence of cultural biases, such as religious, political, gender, racial, and media biases. For each case, we manually verified its accuracy
in terms of reported news, we ensured it had significant media impact and it was covered by reputable
newspaper agencies.

All paragraphs are labeled with emotions and moralities. Of these, 50,975 paragraphs are also labeled with events, whereas the remaining ones do not contain events. For additional information, please refer to our [paper](https://arxiv.org/abs/2409.09001).


The dataset contains the following columns:


- `content_id`: Identification code of the news item within SwissDox.
- `P` : Paragraph identification code. It takes the form $P_i$, where $i$ is the $i$-th paragraph within the news item.
- `subject` :  Main subject of the news item (e.g., Amanda Knox case).
- `event` : List of events in JSON format
- `care`, `harm`, `fairness`, `cheating`, `loyalty`, `betrayal`, `authority`, `subversion`, `purity`, `degradation`: Real-valued scores (within 0 and 1) associated with moral values  
- `anticipation`, `trust`, `disgust`, `joy`, `optimism`, `surprise`, `love`, `anger`, `sadness`, `pessimism`, `fear`: Real-valued scores (within 0 and 1) associated with emotion values

After obtaining a valid SwissDox API key and running the instructions described in the [reconstruct_data.ipynb](reconstruct_data.ipynb) notebook (see the **Usage** section below), you will also obtain the **text** column containing the original textual content retrieved from SwissDox.

Below, is an example of a single row of the dataset:

**text**:  
```
"Mystery without an answer: Where is Meredith's murderer? 
Amanda Knox was acquitted of murdering Meredith Kercher. 
But if it wasn't her, then who killed the British woman with 43 stab wounds?"
```

**event**:

```
[
  {"mention": "murder", "entities": {"Amanda Knox": "murderer", "Meredith Kercher": "victim"}},
  {"mention": "kill", "entities": {"Amanda Knox": "murderer", "Meredith Kercher": "victim"}}
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


# Usage

For this work, we used media data made available via Swissdox@LiRI by the Linguistic Research Infrastructure of the University of Zurich (see https://www.liri.uzh.ch/en/services/swissdox.html for more information).

The raw news paragraphs required to reproduce the dataset cannot be openly shared [due to commercial restrictions](https://www.liri.uzh.ch/en/services/swissdox.html).  However, the original query (in YAML format) used for retrieving data from [Swissdox@LiRI](https://www.liri.uzh.ch/en/services/swissdox.html) can be found in the folder [**Queries**](./Queries/). Additionally, derived data (i.e., labels for emotions, morality, and events) for each news item are available in the [**e2mocase.csv**](./e2mocase.csv) file. 

Provided that the user holds a valid license for Swissdox@LiRI, in the notebook [reconstruct_data.ipynb](./reconstruct_data.ipynb) we describe how to retrieve the original text from which the labels for emotions, morality, and events were derived. 


# References

If you use either the code in this repository or the dataset, please cite our work:
```
@article{greco2024e2mocase,
  title={E2MoCase: A Dataset for Emotional, Event and Moral Observations in News Articles on High-impact Legal Cases},
  author={Greco, Candida M and Zangari, Lorenzo and Picca, Davide and Tagarelli, Andrea},
  journal={arXiv preprint arXiv:2409.09001},
  year={2024}
}
```


