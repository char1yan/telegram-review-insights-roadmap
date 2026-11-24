"""Download the raw dataset into data/raw/ (run from the repo root: python data/download_data.py).

Source: Grano et al. (2017), "Software Applications User Reviews" dataset (~288K Google Play reviews of
open-source Android apps). The notebook filters it to Telegram (org.telegram.messenger).
"""
from pathlib import Path
from urllib.request import urlretrieve

FILES = {
    "reviews.csv": "https://raw.githubusercontent.com/sealuzh/user_quality/master/csv_files/reviews.csv",
}

raw = Path(__file__).parent / "raw"
raw.mkdir(exist_ok=True)
for name, url in FILES.items():
    print(f"Downloading {name} (about 40 MB) ...")
    urlretrieve(url, raw / name)
print("Done.")
