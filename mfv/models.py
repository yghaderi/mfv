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
    .. raw:: html

        <div dir="rtl">
         جریانِ تولید
        </div>

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
        شناسه‌یِ نهاده
    cost_center_id: int
        شناسه‌یث مرکزِ هزینه
    name: str
        نامِ نهاده
    unit: int
        واحدِ اندازه-گیری
    value: float
        مقدار
    """

    id: int
    cost_center_id: int
    name: str
    unit: str
    value: float


##########################################
# Hypothesis
class CostingMethod(BaseModel):
    method: Literal["variable", "absorption"]


class InputOutputRate(BaseModel):
    """
    .. raw:: html

        <div dir="rtl">
         نرخ های اصلیِ بازارهای نهاده و ستاده
        </div>
    """

    id: int
    name: str
    unit: str
    value: float


class Weight(BaseModel):
    """
    .. raw:: html

        <div dir="rtl">
         فرض‌های فنیِ بازدهِ وزنی
        </div>
    """

    id: int
    name: str
    weight: float


class MainAssumption(BaseModel):
    """
    .. raw:: html

        <div dir="rtl">
         فرض‌های اصلی
        </div>
    """

    id: int
    name: str
    unit: str
    value: float


class FinancialRatio(BaseModel):
    """
    .. raw:: html

        <div dir="rtl">
         هدف های مربوط به منبع‌ها و مصرف‌های مالی
        </div>

    Parameters
    ----------
    id: int
        شناسه
    name: str
        نام
    current_value: float
        مقدارِ فعلی
    target_value: float
        مقدارِ هدف
    begin_improvement_at: int
        سالِ آغازِ بهبود
    mature_year: int
        سالِ بلوغ
    method: str
        روشِ تغییر
    """

    id: int
    name: str
    current_value: float
    target_value: float
    begin_improvement_at: int
    mature_year: int
    method: str
