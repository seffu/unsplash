import concurrent.futures
import os
import requests
import pandas as pd

def save_image_from_url(url, output_folder):
    image = requests.get(url.url)
    output_path = os.path.join(
        output_folder, f"{url.id}.png"
    )
    with open(output_path, "wb") as f:
        f.write(image.content)

def load(df, output_folder):    
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=5
    ) as executor:
        future_to_url = {
            executor.submit(save_image_from_url, url, output_folder): url
            for _, url in df.iterrows()
        }
        for future in concurrent.futures.as_completed(
            future_to_url
        ):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as exc:
                print(
                    "%r generated an exception: %s" % (url, exc)
                )

dataframe1 = pd.read_excel('face.xls')

load(dataframe1,'./face')