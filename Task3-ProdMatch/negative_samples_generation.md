## Constraint
- only have a small set of manually validated positive matches
- no available negative cases

## Strategy

### Heuristic

- specific rules: if products belong to different categories, brands, or have distinct attributes, they can be considered negatives.

### Data Augmentation
 - Apply transformations to existing positive pairs to create variations that can serve as negative examples.
    - altering product images (e.g., rotate, crop) - that is different enough, modifying textual descriptions, or changing attributes slightly.

### Clustering
 - cluster unlabeled data to group similar products.
    - Group products based on features like brand, category, or attributes.
    - samples from different clusters can be treated as negative examples.

### ML
- Train an initial model on the small positive set, use it to predict matches on unlabeled data, and treat low-confidence predictions as potential negatives. 

