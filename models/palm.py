import os

DATASET_DIR = "palm_data"

if not os.path.exists(DATASET_DIR):
    print(f" foldeer mising; i cant find '{DATASET_DIR}'"
          )
else:
    classes = [d for d in os.listdir(DATASET_DIR) if os.path.isdir(os.path.join(DATASET_DIR, d))
               ]
    print(f" sucess : found {len(classes)} people : {classes}")
