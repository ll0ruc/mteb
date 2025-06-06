from __future__ import annotations

from mteb.abstasks.AbsTaskClustering import AbsTaskClustering
from mteb.abstasks.AbsTaskClusteringFast import (
    AbsTaskClusteringFast,
    check_label_distribution,
)
from mteb.abstasks.TaskMetadata import TaskMetadata

NUM_SAMPLES = 2048


class BigPatentClustering(AbsTaskClustering):
    superseded_by = "BigPatentClustering.v2"

    metadata = TaskMetadata(
        name="BigPatentClustering",
        description="Clustering of documents from the Big Patent dataset. Test set only includes documents"
        + " belonging to a single category, with a total of 9 categories.",
        reference="https://huggingface.co/datasets/NortheasternUniversity/big_patent",
        dataset={
            "path": "jinaai/big-patent-clustering",
            "revision": "62d5330920bca426ce9d3c76ea914f15fc83e891",
        },
        type="Clustering",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="v_measure",
        date=(
            "1971-01-01",
            "2019-06-10",
        ),  # start date from paper, end date - paper publication
        domains=["Legal", "Written"],
        task_subtypes=["Thematic clustering"],
        license="cc-by-4.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@article{DBLP:journals/corr/abs-1906-03741,
  author = {Eva Sharma and
Chen Li and
Lu Wang},
  bibsource = {dblp computer science bibliography, https://dblp.org},
  biburl = {https://dblp.org/rec/journals/corr/abs-1906-03741.bib},
  eprint = {1906.03741},
  eprinttype = {arXiv},
  journal = {CoRR},
  timestamp = {Wed, 26 Jun 2019 07:14:58 +0200},
  title = {{BIGPATENT:} {A} Large-Scale Dataset for Abstractive and Coherent
Summarization},
  url = {http://arxiv.org/abs/1906.03741},
  volume = {abs/1906.03741},
  year = {2019},
}
""",
    )


class BigPatentClusteringFast(AbsTaskClusteringFast):
    max_depth = 1
    metadata = TaskMetadata(
        name="BigPatentClustering.v2",
        description="Clustering of documents from the Big Patent dataset. Test set only includes documents"
        + " belonging to a single category, with a total of 9 categories.",
        reference="https://huggingface.co/datasets/NortheasternUniversity/big_patent",
        dataset={
            "path": "mteb/big-patent",
            "revision": "58a863a958586a5d6ba51088b94ac74a46aa864f",
        },
        type="Clustering",
        category="p2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="v_measure",
        date=(
            "1971-01-01",
            "2019-06-10",
        ),  # start date from paper, end date - paper publication
        domains=["Legal", "Written"],
        task_subtypes=["Thematic clustering"],
        license="cc-by-4.0",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@article{DBLP:journals/corr/abs-1906-03741,
  author = {Eva Sharma and
Chen Li and
Lu Wang},
  bibsource = {dblp computer science bibliography, https://dblp.org},
  biburl = {https://dblp.org/rec/journals/corr/abs-1906-03741.bib},
  eprint = {1906.03741},
  eprinttype = {arXiv},
  journal = {CoRR},
  timestamp = {Wed, 26 Jun 2019 07:14:58 +0200},
  title = {{BIGPATENT:} {A} Large-Scale Dataset for Abstractive and Coherent
Summarization},
  url = {http://arxiv.org/abs/1906.03741},
  volume = {abs/1906.03741},
  year = {2019},
}
""",
        adapted_from=["BigPatentClustering"],
    )

    def dataset_transform(self):
        for split in self.metadata.eval_splits:
            check_label_distribution(self.dataset[split])
        self.dataset = self.stratified_subsampling(
            self.dataset,
            self.seed,
            self.metadata.eval_splits,
            label="labels",
        )
