from datetime import datetime
import pytz

def convert_utc_to_ist(utc_dt: datetime) -> datetime:
    ist = pytz.timezone("Asia/Kolkata")
    return utc_dt.astimezone(ist)

def convert_ist_to_utc(ist_dt:datetime) -> datetime:
    ist = pytz.timezone("Asia/Kolkata")
    return ist.localize(ist_dt).astimezone(pytz.utc)