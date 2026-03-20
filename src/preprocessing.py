import pandas as pd

def clean_acquisitions(df):
    df = df.copy()
    df = df.drop_duplicates()

    df["Acquired Company"] = df["Acquired Company"].str.strip()
    df["Acquiring Company"] = df["Acquiring Company"].str.strip()

    df["Deal announced on"] = df["Deal announced on"].replace(
        ["Undisclosed", "-", "—", ""], None
    )

    df["Deal announced on"] = pd.to_datetime(
    df["Deal announced on"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
    )

    df["Status"] = df["Status"].fillna("Unknown")
    df["Acquisition Profile"] = df["Acquisition Profile"].fillna("Not Available")
    df["News"] = df["News"].fillna("Not Available")
    df["News Link"] = df["News Link"].fillna("Not Available")
    
    df["Decade"] = (df["Year of acquisition announcement"] // 10) * 10

    return df

def clean_acquiring_companies(df):
    df = df.copy()
    df = df.drop_duplicates()

    df["Acquiring Company"] = df["Acquiring Company"].str.strip()
    df["Year Founded"] = df["Year Founded"].fillna(0).astype(int)
    df["Market Categories"] = df["Market Categories"].fillna("Unknown")
    df["Country (HQ)"] = df["Country (HQ)"].fillna("Unknown")
    df["City (HQ)"] = df["City (HQ)"].fillna("Unknown")
    df["Description"] = df["Description"].fillna("Not Available")
    df["Homepage"] = df["Homepage"].fillna("Not Available")
    df["Twitter"] = df["Twitter"].fillna("Not Available")
    df["Total Funding ($)"] = df["Total Funding ($)"].fillna(0)
    df["Number of Employees"] = df["Number of Employees"].fillna("Unknown")

    return df

def clean_acquired_companies(df):
    df = df.copy()
    df = df.drop_duplicates()

    df["Company"] = df["Company"].str.strip()
    df["Acquired by"] = df["Acquired by"].fillna("Unknown")
    df["Year Founded"] = df["Year Founded"].fillna(0).astype(int)
    df["Market Categories"] = df["Market Categories"].fillna("Unknown")
    df["Country (HQ)"] = df["Country (HQ)"].fillna("Unknown")
    df["City (HQ)"] = df["City (HQ)"].fillna("Unknown")
    df["Description"] = df["Description"].fillna("Not Available")
    df["Homepage"] = df["Homepage"].fillna("Not Available")
    df["Twitter"] = df["Twitter"].fillna("Not Available")

    return df
