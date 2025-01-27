## Task
- Determining whether two products from different datasets refer to the same item
- ypically framed as a binary classification: positive or negative
- multimodal - images and textual descriptions

## Model
- Siamese Networks
    - For feature extraction,
        - Convolutional Neural Networks (CNNs) like ResNet or EfficientNet for images
        - Transformers like BERT for text
    - Similarity and/or distance metric (e.g., Euclidean, Cosine) between the feature vectors
    - Binary classification based on the distance
- Transformer-based models with Cross-Attention
    - Image encoder (e.g., CNN or ViT)
    - Text encoder (e.g., BERT, RoBERTa)
    - Cross-attention layers
        - Make interaction between image and text features
    - Classification Head
        - Outputs the probability of the pair matching

## Loss Function
- BCE loss
- Contrastive loss
- Triplet loss

## Performance Metrics
- Precision, Recall, and F1-Score
- Confusion Matrix