import io
from google.cloud import vision
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def initialize_vision_client():
    return vision.ImageAnnotatorClient()

def extract_text_from_image(client, image_path):
    try:
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        
        if texts:
            return texts[0].description.strip()
        else:
            return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

def ocr_worker(row, client, image_column):
    idx = row.name
    image_path = row[image_column]
    description = extract_text_from_image(client, image_path)
    return (idx, description)

def perform_ocr(df, image_column, max_workers=10):
    client = initialize_vision_client()
    df['description'] = ""
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(ocr_worker, row, client, image_column): idx
            for idx, row in df.iterrows()
        }
        
        for future in tqdm(as_completed(futures), total=len(futures), desc="Performing OCR"):
            idx, description = future.result()
            df.at[idx, 'description'] = description
    
    return df
