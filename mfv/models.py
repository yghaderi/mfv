from typing import Literal, Optional, List
from pydantic import BaseModel, PositiveInt, model_validator


class Company(BaseModel):
    id: int
    name: str


class FinancialYear(BaseModel):
    start: PositiveInt
    length: PositiveInt


class CostingMethod(BaseModel):
    method: Literal["variable", "absorption"]


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


class CostAllocation(BaseModel):
    cost_center_id: int
    type: Literal["fixed", "variable"]
    ratio: float


class FixedAsset(BaseModel):
    id: int
    name: str
    book_value: PositiveInt
    useful_life: PositiveInt
    salvage_value: int
    accumulated_depreciation: int
    depreciation: int = 0
    maintenance: int
    depreciation_method: Literal[
        "straight_line", "declining_balance", "double_declining_balance"
    ]
    cost_allocation: List[CostAllocation]


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
    begin_improvement_year: int
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
    begin_improvement_year: int
    mature_year: int
    method: str


###############################################################################
# *********
class Inventory(BaseModel):
    id: int
    name: str
    unit: str
    management_approach: InventoryManagementApproach
    quantity: int
    value: int
    year: int
    beginning: bool
    current_turnover: float
    target_turnover: float
    begin_improvement_year: int
    mature_year: int


class InputType(BaseModel):
    id: int
    name: str
