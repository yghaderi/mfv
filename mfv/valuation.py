from typing import List
from pydantic import validate_call
from mfv.models import FixedAsset, FinancialYear


class Valuation:
    @validate_call
    def __init__(self, financial_year: FinancialYear, fixed_assets: List[FixedAsset]):
        self.f_years = self.generate_financial_year(financial_year)
        self.fixed_assets = fixed_assets

    @validate_call
    def generate_financial_year(self, financial_year: FinancialYear):
        return [financial_year.start + i for i in range(financial_year.length)]

    @validate_call
    def handel_fixed_asset(self, data: FixedAsset):
        fixed_asset = []
        match data.depreciation_method:
            case "straight_line":
                depr = (
                               data.book_value + data.accumulated_depreciation - data.salvage_value
                       ) / data.useful_life
                for fy in self.f_years:
                    data = data.model_copy(
                        update={
                            "depreciation": depr,
                            "book_value": data.book_value - depr,
                            "accumulated_depreciation": data.accumulated_depreciation
                                                        + depr,
                        }
                    )
                    fixed_asset.append((fy, data))
        return fixed_asset
