## Utilize Unique Identifiers
 - Identify Common Identifiers or matches based on product attributes
 - Clean and then match (e.g., removing spaces, consistent formatting)
 - Optimization:
    - Divide datasets into smaller blocks based on shared attributes (e.g., same brand or category).

## ML
- Classifier
    - Use the small set of known matches.
    - Generate non-matching pairs (discussed [here](https://github.com/souro/FoodDataFusion/blob/main/Task3-ProdMatch/negative_samples_generation.md))
    - Models such as Logistic Regression or Neural Networks.
    - Use the trained model to predict the likelihood of pairs being matches.
    - Thresold: Select pairs with high confidence scores (say, probability > 0.9) as matches.
- Features that capture similarities and differences between product pairs (e.g., attribute similarities, image feature distances).
    - Maintain them in [Faiss](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/)
    - (n*n) similarity scoring

## Active Learning
- Train a preliminary model using the small set of known positive matches and a generated set of negative examples.
- Identify product pairs where the model is least confident.
- Focus manual efforts on these uncertain pairs
    - Iteration 1: Model identifies that it is unsure about matching "Product A" and "Product B."
    - Manual Step: Verify if "Product A" and "Product B" are a match.
    - Iteration 2: Update the model with this new information to improve future predictions.

## Minimal Manual Verification
- Randomly verify a subset of to ensure reliability.
- If accuracy is high (e.g., 95%), use the automated matches.

## Additional
-  Integrate data from other databases or APIs that provide additional product information.