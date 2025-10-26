import os
import json
import pickle
import pandas as pd

def read_csv(source, **kwargs) -> pd.DataFrame:
    return pd.read_csv(source, **kwargs)

def validate_salary_schema(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize column names (trim only, keep original case otherwise)
    df.columns = [c.strip() for c in df.columns]
    required = {"Experience", "Salary"}
    if not required.issubset(set(df.columns)):
        raise ValueError("CSV must contain columns: 'Experience' and 'Salary'")

    df["Experience"] = pd.to_numeric(df["Experience"], errors="coerce")
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
    if df["Experience"].isna().any() or df["Salary"].isna().any():
        raise ValueError("Non-numeric values found in 'Experience' or 'Salary'. Please clean and retry.")
    return df

def save_pickle(obj, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def load_pickle(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)

def save_json(obj, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f)

def load_json(path: str):
    with open(path, "r") as f:
        return json.load(f)
