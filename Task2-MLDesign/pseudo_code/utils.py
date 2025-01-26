import os
import requests
from tqdm import tqdm

def download_image(url, save_path, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def batch_download_images(df, url_column, save_dir, max_workers=10):
    from concurrent.futures import ThreadPoolExecutor, as_completed

    os.makedirs(save_dir, exist_ok=True)
    results = []
    
    def worker(row):
        idx = row.name
        url = row[url_column]
        if pd.isna(url) or not isinstance(url, str) or not url.startswith('http'):
            return (idx, None, False)
        filename = f"product_{idx}.jpg"
        save_path = os.path.join(save_dir, filename)
        success = download_image(url, save_path)
        return (idx, save_path if success else None, success)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(worker, row): idx for idx, row in df.iterrows()}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Downloading Images"):
            idx, path, success = future.result()
            results.append((idx, path, success))
    
    df['image_path'] = df['image_path'].astype(object)
    df['image_downloaded'] = False
    
    for idx, path, success in results:
        df.at[idx, 'image_path'] = path
        df.at[idx, 'image_downloaded'] = success
    
    return df
