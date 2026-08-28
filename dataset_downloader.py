import kagglehub
import os
import shutil


def download_dataset(dataset_name, folder_name):
    os.makedirs(folder_name, exist_ok=True)
    print(f"Downloading dataset: {dataset_name}")
    path = kagglehub.dataset_download(dataset_name)

    # Move files to target folder
    for item in os.listdir(path):
        shutil.move(os.path.join(path, item), folder_name)

    print(f"Dataset files moved to {folder_name}/ folder")


if __name__ == "__main__":
    dataset_name = input("Enter Kaggle dataset link: ")
    folder_name = input("Enter local folder name to store the dataset: ")
    download_dataset(dataset_name, folder_name)
