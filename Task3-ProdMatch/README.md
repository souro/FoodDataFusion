# Approach for the third task (Product Matching):

## Truth Set Creation with Minimal Manual Effort:

- [Details](https://github.com/souro/FoodDataFusion/blob/main/Task3-ProdMatch/truth_set_creation.md)

## Techniques for negative case generation:

- [Details](https://github.com/souro/FoodDataFusion/blob/main/Task3-ProdMatch/negative_samples_generation.md)

## Distinguishing Easy vs Hard Samples:

- Semantic similarity
- Feature vector proximity
- Embedding space distribution
- Prediction confidence
- Model uncertainty metrics

## Split Strategy:

- Initial split (with some hypothesis) 70% train, 15% validation, 15% test
- Incremental learning framework
- Continuous model refinement
- Active learning for challenging samples
- Periodic retraining with new labeled data

## Matching Pair Model Design:

- Siamese/Triplet neural network
- Transformer-based embeddings
- Contrastive loss function
- Key Performance Indicators (KPIs):
    - Precision
    - Recall
    - F1 Score
    - Mean Average Precision

## Similar Description Retrieval:

- Dense retrieval methods
- Semantic search techniques
- Difference from matching:
    - Neighborhood retrieval
    - Relaxed similarity constraints
    - Broader matching criteria