import kagglehub
from kagglehub import KaggleDatasetAdapter
from dotenv import load_dotenv
import os

load_dotenv()

file_path = os.getenv("DATASET_NAME")

output_path = "data/events.csv" 

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "mkechinov/ecommerce-events-history-in-electronics-store",
    file_path,
)

df.to_csv(output_path, index=False)

print("Dataset saved")
print(df.head())