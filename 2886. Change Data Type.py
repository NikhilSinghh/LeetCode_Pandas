import pandas as pd

def changeDatatype(s: pd.DataFrame) -> pd.DataFrame:
    return s.assign(grade=s['grade'].astype(int))
    
