import pandas as pd
from data_preprocessing import load_data, preprocess_data, stratified_split
from utils import batch_download_images
from ocr_processing import perform_ocr
from pipeline import prepare_labels, train_model, evaluate_model, save_model
import os

def main():
    # Load and preprocess data
    data_path = '...'
    df = load_data(data_path)
    df = preprocess_data(df)
    
    # Download images
    if 'image_path' not in df.columns or df['image_path'].isnull().all():
        df = batch_download_images(df, 'image_url', 'image_path', max_workers=20)
    
    # OCR to extract descriptions
    if 'description' not in df.columns or df['description'].isnull().all():
        df = perform_ocr(df, 'image_path', max_workers=10)
    
    # Save the DataFrame
    processed_path = '...'
    df.to_parquet(processed_path, index=False, compression='snappy')
    
    # Prepare labels
    label_columns = ['calories', 'fat', 'sugar', ...]
    y, mlb = prepare_labels(df, label_columns)
    
    # Split data
    train_df, test_df = stratified_split(df, label_columns, test_size=0.2, random_state=42)
    
    # Feature Extraction (e.g., embeddings)
    X_train, X_test = extract_features(train_df, test_df)
    
    # Train
    model = train_model(X_train, y[train_df.index])
    
    # Evaluate
    evaluate_model(model, X_test, y[test_df.index], mlb)
    
    # Save the model
    save_model(model, mlb, path='...')

if __name__ == "__main__":
    main()
