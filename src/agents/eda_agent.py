# src/agents/eda_agent.py
import pandas as pd
import numpy as np
from loguru import logger

def basic_eda(df: pd.DataFrame):
    num = df.select_dtypes(include=[np.number])
    cat = df.select_dtypes(exclude=[np.number])

    summary = {
        "n_rows": int(df.shape[0]),
        "n_cols": int(df.shape[1]),
        "num_columns": list(num.columns),
        "cat_columns": list(cat.columns),
        "missing": df.isnull().sum().to_dict(),
        "num_describe": num.describe().to_dict(),
    }
    if len(num.columns) >= 2:
        summary["correlation"] = num.corr().to_dict()
    logger.info("EDA completed")
    return summary
