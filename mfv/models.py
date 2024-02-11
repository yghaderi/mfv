from typing import Literal, Optional
from pydantic import BaseModel, PositiveInt, model_validator


class Year(BaseModel):
    start: int
    length: PositiveInt


class InventoryManagementApproach(BaseModel):
    """
    approach {
        1: 'خریدِ کسری و فروشِ مازاد'
        2: 'خریدِ کسری و عدمِ فروش'
        3: 'عدمِ خرید و فروشِ مازاد'
        4: 'عدمِ خرید و عدمِ فروش'
        5: 'خریدِ کسری برای مصرف و فروشِ مازادِ حاصل از تولید'
        6: 'محدودیتِ فروش-مصرف'
        }
    """

    approach: Literal[1, 2, 3, 4, 5, 6]


class ProductionFlow(BaseModel):
    """
    Parameters
    ---------
    id: int
        کد محصول
    year: int
        سال
    capacity: int
        ظرفیتِ تولید
    qty: int
        مقدار تولید
    pct_export: Optional[float] = 0
        درصد فروشِ صادراتی از کل
    pct_commission_prod: Optional[float] = 0
        درصدِ تولیدِ کارمزدی از کل
    """

    id: int
    year: int
    capacity: int
    qty: int
    pct_export: Optional[float] = 0
    pct_commission_prod: Optional[float] = 0


class Input(BaseModel):
    """
    .. raw:: html

        <div dir="rtl">
         مدلِ نهاده‌ها
        </div>

    Parameters
    -------
    id: int
        شناسه
    name: str
        نامِ نهاده
    unit: int
        واحدِ اندازه-گیری
    value: float
        مقدار
    """
    id: int
    name: str
    unit: int
    value: float

