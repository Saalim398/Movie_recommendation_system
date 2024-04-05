# Movie_recommendation_system

Version  `1.0`

## Python modules used:  
1. Numpy
2. Pandas
3. difflib
4. sklearn
5. os
   
## About Movie_recommendation_system
I developed a mechanism for recommending films while I was an intern at Acmgrade.
This machine learning-based project makes use of the following ideas:
1. Cosine Similarity : Cosine similarity, or the cosine kernel, computes similarity as the normalized dot product of X and Y:
K(X, Y) = <X, Y> / (||X||*||Y||)
2. Term frequency Inverse document frequency (TFIDF) is a statistical formula to convert text documents into vectors based on the relevancy of the word. It is based on the bag of the words model to create a matrix containing the information about less relevant and most relevant words in the document.
3. difflib - This module provides classes and functions for comparing sequences
4. This model predicts the movie based in generes, keyword, tagline, cast, director.

## To access this program follow the given steps:  
1. First make sure that you have installed python on your system
2. clone the git repository
   ```
    git clone https://github.com/Saalim398/Movie_recommendation_system.git
   ```
3. Locate the file and Run the program
   ```
       cd Movie_recommendation_system
       python Movie_Recommendation_system.py
   ```
   When you enter the name of your favourite movie, relevant searches for that movie will appear.
