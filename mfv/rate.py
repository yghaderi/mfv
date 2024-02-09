from typing import List, Optional
import polars as pl
from mfv.models import Year


def change_factor(
    year: Year, normal_rate: float, extra_rate: Optional[List[float]] = None
):
    """
    ..raw: html
        <div></div>

    Parameters
    ----------
    year: Year
        سالِ شروع و طولِ دوره
    normal_rate: float
        نرخِ تغییرِ عادی
    extra_rate: float
        نرخِ تغییرِ فرا-معمول

    Returns
    --------
    polars.DataFrame
    """
    year = Year(**year) if isinstance(year, dict) else year
    df = pl.DataFrame(
        {
            "year": [year.start + i for i in range(year.length)],
            "normal_rate": [normal_rate] * year.length,
            "extra_rate": extra_rate if extra_rate else [0] * year.length,
        }
    )
    df = df.with_columns(
        [(pl.col("normal_rate") + pl.col("extra_rate") + 1).cumprod().alias("rate")]
    )
    return df
