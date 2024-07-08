# Music Recommendation System

This repository contains the implementation of a Music Recommendation System based on mood and lyrics, designed by Adithya Suresh Babu, Sai Sriram Ampapurapu, Goutham Reddy Jarugu, and Sushanth Reddy Marthala from the Department of Computer Science, University of Central Florida.

## Table of Contents

- [Introduction](#introduction)
- [System Overview](#system-overview)
- [Data Collection](#data-collection)
- [Data Preparation and Preprocessing](#data-preparation-and-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Recommendation System](#recommendation-system)
- [Generated Recommendations and Evaluation](#generated-recommendations-and-evaluation)
- [Experiments](#experiments)
- [Conclusion](#conclusion)
- [References](#references)
- [Links to Code](#links-to-code)

## Introduction

The popularity of digital music is at an all-time high. Listeners crave music that suits their tastes and moods. In this project, we designed, implemented, and analyzed a recommendation system using Spotify and Musixmatch datasets. The system recommends new music to users based on the lyrics and mood or tone of the songs they listen to.

## System Overview

The machine learning system consists of the following components:
1. Data Collection
2. Data Preparation and Preprocessing
3. Feature Engineering
4. Recommendation System
5. Generated Recommendations and Evaluation

## Data Collection

We used two major sources for data:
- **Kaggle**: Dataset with around 18,000 songs and lyrics.
- **Musixmatch**: Million song dataset with more than 300,000 songs data with lyrics.

## Data Preparation and Preprocessing

### Data Preparation
- Collected data contains features such as track_id, track_name, track_artist, lyrics, track_popularity, track_album_id, track_album_name, track_album_release_date, playlist_name, playlist_id, playlist_genre, playlist_subgenre, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, and language.

### Data Preprocessing
- **Removal of Punctuation**: Removed unnecessary punctuation from lyrics.
- **Tokenization**: Broke down long sentences into smaller chunks called tokens.
- **Word Lemmatization**: Reduced words to their root form for better data processing.
- Created new features called “final” (track_artist and preprocessed lyrics combined) and “final_genre_list” (genre and sub_genre combined).

## Feature Engineering

- Created a new feature called “sentiment” using Sentiment IntensityAnalyzer.
- Applied one-hot encoding to sentiment, subjectivity, key, and mode features.
- Used TF-IDF vectorization for the “final_genre_list” feature.
- Implemented word embedding to convert words into numerical vectors.
- Visualized songs using t-Distributed Stochastic Neighbor Embedding (t-SNE).

## Recommendation System

- Used content-based filtering with cosine similarity.
- Combined all songs on a playlist into a single summary vector.
- Compared the summary vector to every song in the database to find similarities.
- Recommended the most relevant song not in the playlist based on the similarity metric.

## Generated Recommendations and Evaluation

- Generated recommendations using the implemented system.
- Evaluated models using metrics like ROC curves and confusion matrices.

## Experiments

- Implemented a baseline model using Naive Bayes classifier to classify songs based on lyrics.
- Used different vectorizers on the Naive Bayes model to evaluate prediction accuracy.
- Compared ROC curves for Count Vectorizer, TF-IDF Vectorizer, and Bernoulli Naive Bayes.

## Conclusion

The project successfully developed a music recommendation system based on song features, mainly using lyrics and metadata to compute sentiment. Different visualizations showed that songs often overlap, suggesting multiple valid recommendations. Future improvements could involve mixing in techniques like collaborative filtering and convolutional neural networks.

## References

1. [Netflix Prize](https://en.wikipedia.org/wiki/Netflix_Prize)
2. S. -H. Chang, A. Abdul, J. Chen and H. -Y. Liao, "A personalized music recommendation system using convolutional neural networks approach," 2018 IEEE International Conference on Applied System Invention (ICASI), 2018, pp. 47-49, doi: 10.1109/ICASI.2018.8394293.
3. J.B. Schafer, D. Frankowski, J. Herlocker and S. Sen, "Collaborative filtering recommender systems", The Adaptive Web: Methods and Strategies of Web Personalization, pp. 291-324, 2007.
4. M.J. Pazzani and D. Billsus, "Content based recommendation systems", The Adaptive Web: Methods and Strategies of Web Personalization, pp. 325-341, 2007.
5. P. N, D. Khanwelkar, H. More, N. Soni, J. Rajani and C. Vaswani, "Analysis of Clustering Algorithms for Music Recommendation," 2022 IEEE 7th International conference for Convergence in Technology (I2CT), Mumbai, India, 2022, pp. 1-6, doi: 10.1109/I2CT54291.2022.9824160.
6. S. -H. Chang, A. Abdul, J. Chen and H. -Y. Liao, "A personalized music recommendation system using convolutional neural networks approach," 2018 IEEE International Conference on Applied System Invention (ICASI), Chiba, Japan, 2018, pp. 47-49, doi: 10.1109/ICASI.2018.8394293.
7. Visualizing Data using t-SNE Laurens van der Maaten, Geoffrey Hinton; 9(86):2579−2605, 2008.
8. D. Rani, R. Kumar and N. Chauhan, "Study and Comparision of Vectorization Techniques Used in Text Classification," 2022 13th International Conference on Computing Communication and Networking Technologies (ICCCNT), Kharagpur, India, 2022, pp. 1-6, doi: 10.1109/ICCCNT54827.2022.9984608.