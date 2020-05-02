# Image-based Product Recommendation System

## Idea
Current implementations of image recommendations are used by giant e-commerce portals like
Amazon, Alibaba, etc but still stand inefficient in the sense they require user text input. We, on
the other hand, intend to optimize the whole system by taking images as input from the user.
This would enhance the customer experience and fill up the gaps faced in text searches

## Problem Statement
Develop an image-based product recommendation system used primarily in the e-commerce
domain. This engine will take as input an image of a certain product and recommend 5 similar
products that resemble closely to the input image. We aim to achieve this goal by implementing
a combination of dimensionality reduction, clustering, modelling and recommendation system
techniques.

## Steps Involved for Recommending SImilar Products are- 
- Data Loading
- Selecting optimum dimensions to be used using Scree and Elbow Plot.
- Dimensionality Reduction
   1. PCA on original Image
   2. PCA on image with Reduced dimesnions
   3. TSNE on original image
   4. TSNE on image with Reduced dimensions
- Selecting optimum Cluster uing SSE Plot
- Clustering -
    1. KMeans
    2. Gaussian Mixture Model
    3. Agglomerative Clustering
 - Select Best Clusterting technique to be used
 - Use Distance metrices to Recommend Images
    1. Cosine Similarity
    2. Spatial Distances
