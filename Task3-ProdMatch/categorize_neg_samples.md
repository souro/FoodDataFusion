## Easy Neg Samples
-  Pairs that are non-matching due to differences in attributes
    - Different brands, Categories
    - Visual Disparities (color, design,...)
    - Different descriptions

## Hard
- Pairs that look similar but have small differences that the model needs to detect
    - Different products from the same or similar brands and/or category, ...
    - Packaging designs that are visually similar
    - Product descriptions that share common keywords or phrases

## Strategy to separate easy and hard neg samples
- Similarity scores between product attributes and set thresholds to classify
    - Utilizing pre-trained models
    - Easy Negatives: Low similarity scores across all attributes
    - Hard Negatives: High similarity scores in one or more attributes
- Group negative samples based on similarity and classify clusters as easy or hard
    - Dense Clusters: Likely contain hard negatives due to high similarity
    - Sparse Clusters: Likely contain easy negatives with low similarity