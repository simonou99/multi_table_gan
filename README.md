# Multi-Table GAN

This repository presents a POC methodological prototype of a KDE-hybrid GAN framework, that can generate synthetic relational data (i.e. graph data).

It combines the mechanisms of WGAN+GP, cGAN, DCGAN and KDE, for obtaining fast learning and generation speed, with the ability to mimic inter-table relational properties, as well as in-table statistical properties e.g. trend, distribution, etc. Thanks to the implementation of deep-CNN layers, it also enables the prototype's ability to learn/generate time-series data.

More in detail about the mechanisms, it divides the training tasks into using KDEs and GAN. It uses KDE to obtain the parent-child key-column distributions and the categorical-column distributions within each table. Then it uses cGANs to train on the numeric columns of each table, with key and categorical columns of that table as the GAN input. Such that, after training, for each table, it will have a KDE model that can generate its key columns and categorical columns, as well as a GAN-generator model that takes the generated keys and categories as input generate the more nuanced numeric columns. To make sure that the foreign keys in each child table does come from its parent model, we use the technique of interpolation, to interpolate the foreign key columns to have the correct range of keys without affecting the column distributions.

This prototype can achieve a score >80% with SDV's multi-table metrics.

The prototype was mainly tested on the [Auckland GTFS data](https://at.govt.nz/about-us/at-data-sources/general-transit-feed-specification/), as well as collections from SDV.

Documentations are written as docstrings and comments in the [`main_prototype.ipynb`](https://github.com/simonou99/multi_table_gan/blob/main/main_prototype.ipynb) notebook.

The [`main_metrics.ipynb`](https://github.com/simonou99/multi_table_gan/blob/main/main_metrics.ipynb) notebook presents the metric results.

[`main_benchmark.ipynb`](https://github.com/simonou99/multi_table_gan/blob/main/main_benchmark.ipynb) notebook was scrapped. Originally, the protype is to be benchmarked with the HMA model from SDV. However, HMA took over 1.5 hours but still showed no progress, in which the training process was stopped.

The `bm_#DataName.ipynb` and `bm_#DataName_benchmark.ipynb` present the implementation of the prototype on data collections from SDV and the benchmark metrics results, in which both the prototype and HMA were able to run.
