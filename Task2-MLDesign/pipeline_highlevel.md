## Data 

### Collection
- Images
- Metadata
    - such as product names, categories, existing nutritional facts (if available).

### Storage
- Use databases or Cloud Storage.

### Preprocessing
- Image
    - Resizing -  Standardize image sizes to ensure consistency
    - Normalization - Adjust pixel values for uniformity
    - Augmentation: Apply transformations (e.g., rotation, flipping) to increase data variability (if required)
- Text
    - Google Cloud Vision OCR to extract textual information from images
    - Remove noise, correct errors, and standardize textual data

### Split Strategy 
-  Stratified Splitting - each split (training, validation, testing) maintains the same distribution of nutritional labels as the original dataset
    - [Scikit-learn’s StratifiedKFold](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.StratifiedKFold.html)
- Prevent data leakage by ensuring that all samples from the same group (e.g., brand or category) are restricted to a single split.
- Cross-Validation Splits - evaluate model performance across multiple data partitions
- Custom Splitting
    - specific combinations of nutritional facts are adequately represented in each split
    - infrequent label combinations appear in training and evaluation sets


### Data Loaders
- PyTorch’s DataLoader

## Tasks

### For data processing
- For image feature using some pretrained pre-trained CNNs (e.g., ResNet, EfficientNet) and for text data, Tokenize and encode textual data using some pre-trained transformers (e.g., BERT, RoBERTa)
- Combine them to create a unified representation
- Utilizing multimodel model like [LayoutLMv3](https://huggingface.co/microsoft/layoutlmv3-large)

### Entity Tagging
- Identify key nutritional components to extract, such as:
    - Calories
    - Total Fat
    - Saturated Fat
    - Trans Fat
    - Cholesterol
    - Sodium
    - Total Carbohydrates
    - Dietary Fiber
    - Sugars
    - Protein
    - Vitamins and Minerals
- Analyze OCR-extracted text to locate and parse relevant nutritional information
- Use regex and/or NER

### Multi-label Classification
- each nutritional component is treated as a separate binary classification task
- Binary Cross-Entropy Loss for multi-label classification tasks
- Optimization, Regularization, Epochs and Batching
- Generate predictions for the presence of each nutritional fact
- Metrics: Precision, Recall, F1-Score, Confusion Matrix

##

