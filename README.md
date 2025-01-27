# The repository involves experiments with the [Open Food Facts](https://world.openfoodfacts.org/data) dataset, focusing on three main parts:

## [Exploratory Data Analysis (EDA)](https://github.com/souro/FoodDataFusion/tree/main/Task1-EDA):


- Analyze the Open Food Facts dataset
- Extract useful statistics
- Identify data requirements for building an ML model that can extract nutritional table information from product images


## [ML Design](https://github.com/souro/FoodDataFusion/tree/main/Task2-MLDesign):


- Create a solution pipeline for extracting information from product images
- Focus on nutritional facts extraction
- Data splitting capabilities
- Handling multi-label classification
- Entity tagging
- Multimodal data loading (image and text)
- Model training and inference stages

## [Product Matching Challenge](https://github.com/souro/FoodDataFusion/tree/main/Task3-ProdMatch):


- Creating a Truth Set:
    - Identify matching products with minimal manual work
- Handling Limited Negative Cases:
    - Strategies when only have a few confirmed matches (positives)
- Distinguishing Samples:
    - (Obtain negative cases then) How to separate easy-to-match and hard-to-match pairs
- Data Splitting Strategy:
    - How to divide split the data for training
    - How to use new labeled data after deployment
- Model Design for Matching:
    - What type of model, loss function, and performance metrics to use
- Retrieving Similar Descriptions:
    - Whether to use the same setup as the matching task for finding similar product descriptions
