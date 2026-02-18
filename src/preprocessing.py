import pandas as pd

def clean_acquisitions(df):
    df = df.copy()

    df = df.drop_duplicates()

    df["Acquired Company"] = df["Acquired Company"].str.strip()
    df["Acquiring Company"] = df["Acquiring Company"].str.strip()

    df["Deal announced on"] = df["Deal announced on"].replace(
        ["Undisclosed", "-", "—", ""], None
    )

    # Now parse valid ones
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
