from typing import Literal
from pydantic import BaseModel, PositiveInt


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
