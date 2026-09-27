"""Fictional, intentionally flawed promotion model for teaching Agile testing.

This is NOT a production implementation. The two defects are deliberate:
gift cards count towards eligibility and retries stack discounts.
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Item:
    price: Decimal
    gift_card: bool = False


class Promotion:
    def __init__(self) -> None:
        self.discounts: dict[str, Decimal] = {}

    def apply(self, basket_id: str, items: list[Item], code: str) -> Decimal:
        """Return accumulated discount for a basket (deliberately buggy)."""
        if code.strip().upper() != "SAVE20":
            return self.discounts.get(basket_id, Decimal("0"))

        # DEFECT 1: gift-card value should not count towards the £50 threshold.
        subtotal = sum((item.price for item in items), Decimal("0"))
        if subtotal < Decimal("50"):
            return self.discounts.get(basket_id, Decimal("0"))

        eligible = sum((item.price for item in items if not item.gift_card), Decimal("0"))
        discount = min(eligible * Decimal("0.20"), Decimal("30"))

        # DEFECT 2: applying the same code again adds a second discount.
        self.discounts[basket_id] = self.discounts.get(basket_id, Decimal("0")) + discount
        return self.discounts[basket_id]
