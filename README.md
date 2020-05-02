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
   1. PCA on original Image
   <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/pca_original.png" width="400" height="200">
   
   2. TSNE on original image
   <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/tsneOriginal.png" width="400" height="200">
   
- Selecting optimum Cluster uing SSE Plot
<br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/elbow_curve_shoes.png" width="400" height="200">

<b>- Clustering -</b>
    1. KMeans
     <b>1.1 PCA Results</b>
    * KMeans with PCA
    <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/kmeans/pcaKmeans.png" width="400" height="200">
    <b>1.2 TSNE Results </b>
    * [KMeans with TSNE]
    <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/kmeans/tsneKMeans.png" width="400" height="200">
    <b>2. Gaussian Mixture Model</b>
    2.1 PCA Results
    * [GMM with PCA]
    <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/GMM/pcaGmm.png" width="400" height="200">
    2.2 TSNE Results
    * [GMM with TSNE]
    <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/GMM/tsneGmm.png" width="400" height="200">
    <b> 3. Agglomerative Clustering </b>
    3.1 PCA Results
    * [AGG with PCA]
    <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/AGG/pcaAggWard.png" width="400" height="200">
    3.2 TSNE Results
    * [AGG with TSNE]
    <br/><img src="https://github.com/Gourang97/Fashion_dataset_uml/blob/master/Results/AGG/tsneAggWard.png" width="400" height="200">
 <b>- Select Best Clusterting technique to be used </b>
 <b>- Use Distance metrices to Recommend Images</b>
    Cosine Similarity and Spatial Distances
 
 
   
  
