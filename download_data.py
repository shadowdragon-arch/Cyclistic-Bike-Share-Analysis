import os

def setup_data_directory():
    # Create local data directory
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    print(f"Directory '{data_dir}/' is ready.")
    print("Note: Place your Cyclistic raw CSV files inside this folder locally.")

if __name__ == "__main__":
    setup_data_directory()
