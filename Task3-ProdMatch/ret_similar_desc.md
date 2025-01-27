## Two diff tasks
- Product Matching (as discussed [here]())

## Retrieving Similar Product Descriptions
- Given a product description, retrieve other descriptions that are semantically similar or represent the same product from a different dataset
- Can be framed as a similarity ranking or information retrieval problem
- primarily focused on the textual data
    - semantic content of descriptions

## Decision
- Both tasks objective wise diffrent 
    - Also handle different data modality
- But also they are similar in nature in the pipeline artitecture uses
- So, will not use the setup entirely
    - Shared components could be
        - text processing and the corresponding pre-trained model
        - same loss function
        - same metrics