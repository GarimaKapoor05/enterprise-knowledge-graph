import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "tech_ma"

def load_data():
    acquisitions = pd.read_csv(DATA_DIR / "Acquisitions.csv")
    acquiring_companies = pd.read_csv(DATA_DIR / "Acquiring Tech Companies.csv")
    acquired_companies = pd.read_csv(DATA_DIR / "Acquired Tech Companies.csv")
    
    return acquisitions, acquiring_companies, acquired_companies

if __name__ == "__main__":
    acquisitions, acquiring_companies, acquired_companies = load_data()
    print("Data Loading - Success")
    print("Acquisitions shape:", acquisitions.shape)
    print("Acquiring Companies shape:", acquiring_companies.shape)
    print("Acquired Companies shape:", acquired_companies.shape)

