# src/agents/uploader_agent.py
def validate_file(path, max_rows=10_000_00):
    if not path.endswith(('.csv', '.parquet', '.xlsx')):
        raise ValueError("Unsupported file format (supported: .csv .parquet .xlsx)")
    # lightweight check for csv
    if path.endswith('.csv'):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            nrows = sum(1 for _ in f) - 1
    else:
        nrows = None
    if nrows and nrows > max_rows:
        raise ValueError(f"File too large ({nrows} rows)")
    return True
