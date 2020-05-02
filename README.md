# Image-based Product Recommendation System [An Unsupervised Way]

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

## Steps Involved for Building Recommender System in an Unsupervised Way- 
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
 
 ## Results-
 - Selecting optimum dimensions to be used using Scree and Elbow Plot.[https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/elbow_curve_tshirts.png]
 
 - Dimensionality Reduction
   1. PCA on original Image[https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/pca_original.png]
   2. TSNE on original image[https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/tsneOriginal.png]
- Selecting optimum Cluster uing SSE Plot []
- Clustering -
    1. KMeans
    1.1 PCA Results
    * [KMeans with PCA](https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/kmeans/kmeans_pca.png)
    1.2 TSNE Results
    * [KMeans with TSNE](https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/kmeans/tsnethenKmeans.png)
    2. Gaussian Mixture Model
    2.1 PCA Results
    * [GMM with PCA]()
    2.2 TSNE Results
    * [GMM with TSNE]()
    3. Agglomerative Clustering
    3.1 PCA Results
    * [AGG with PCA]()
    3.2 TSNE Results
    * [AGG with TSNE]()
 - Select Best Clusterting technique to be used
 - Use Distance metrices to Recommend Images
    1. Cosine Similarity
    2. Spatial Distances
 
 
   
  
