from typing import List
from pydantic import validate_call
from mfv import models


class FixedAsset:
    def __init__(self, fixed_asset: models.FixedAsset):
        self.fa = fixed_asset

    def depreciation(self):
        match self.fa.depreciation_method:
            case "straight_line":
                return (self.fa.book_value
                        + self.fa.accumulated_depreciation
                        - self.fa.salvage_value
                        ) / self.fa.useful_life

    def book_value(self):
        return self.fa.book_value - self.fa.depreciation

    def accumulated_depreciation(self):
        return self.fa.accumulated_depreciation + self.fa.depreciation

    @property
    def fixed_asset(self):
        return self.fa.model_copy(
            update={
                "depreciation": self.depreciation(),
                "book_value": self.book_value(),
                "accumulated_depreciation": self.accumulated_depreciation()
            }
        )


class Valuation:
    @validate_call
    def __init__(
            self,
            financial_year: models.FinancialYear,
            fixed_assets: List[models.FixedAsset],
    ):
        self.f_years = self.generate_financial_year(financial_year)
        self.fixed_assets = fixed_assets

    @validate_call
    def generate_financial_year(self, financial_year: models.FinancialYear):
        return [financial_year.start + i for i in range(financial_year.length)]

