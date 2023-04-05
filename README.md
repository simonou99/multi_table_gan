# Multi-Table GAN

This repository contains the proof-of-concept methodology of a Generative Adversarial Network (GAN) for generating synthetic data from multiple relational tables while preserving both the statistical properties within each individual table and the relationships between them.  

This is done by combining the idea of WGAN (Wasserstein-GAN) and cGAN (Conditional GAN). It uses wasserstein loss with gradient clipping for faster learning and performance optimization. While a traditional GAN is trained on the whole data regardless of the content, this method takes the idea of cGAN which also takes an array of labels in to account during training, but with a twist. Since we want to preserve the inter-table relations, instead of taking an array of labels like in a standard cGAN as inputs, this GAN takes a dataframe of primary key and foreign keys as composite labels. In this case, this essentially making it 'reverse-predict' the likely features of a composite label, i.e. generates the corresponding synthetic table of a composite key of primary key and foreign keys.  

Hence, with a relational metadata or similar, we can first generate only the primary keys and foreign keys to ensure we have the correct cardinality and relations, then input them into the GAN to generate the corresponding relational tables.  

The best part is, it supports hybrid models within the same collection of relational tables, i.e. you can use a RNN based model specifically for sequential or time series table, and use a standard one for a normal table, with customizable parameters and model architecuals for individual table, but still preserve the relations within the collection.  

This method also uses KDE (kernel density estimation) to generate data to have distribution that is as similar as possible to its corresponding real data. (or other methods which user can specify, e.g. interpolation)  
A sample of the Auckland GTFS data collection (public data) is currently used for testing purpose.

*CODE WORK IN PROGRESS*
