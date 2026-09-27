"""Demo 03: translate checks into a product-focused release conversation."""

from decimal import Decimal

from swiftcart import Item, Promotion


def main() -> None:
    promotion = Promotion()
    happy = promotion.apply("happy", [Item(Decimal("50"))], "SAVE20") == Decimal("10")
    gift_card = promotion.apply(
        "gift-card", [Item(Decimal("40")), Item(Decimal("10"), gift_card=True)], "SAVE20"
    ) == Decimal("0")
    first = promotion.apply("retry", [Item(Decimal("50"))], "SAVE20")
    retry = promotion.apply("retry", [Item(Decimal("50"))], "SAVE20") == first

    print("[EVIDENCE] Happy path:", "PASS" if happy else "FAIL")
    print("[EVIDENCE] Gift-card threshold:", "PASS" if gift_card else "FAIL")
    print("[EVIDENCE] Retry does not double discount:", "PASS" if retry else "FAIL")
    print("[CONTEXT] A larger green suite cannot erase these failed high-impact checks.")
    print("[ILLUSTRATIVE RECOMMENDATION] Do not ship this promotion as-is.")
    print("[WHY] Customers could qualify incorrectly or receive a discount twice.")
    print("[NEXT STEP] Fix and verify eligibility plus retry safety; discuss options as a team.")
    print("[LIMIT] This toy model does not assess the full release or make the decision for you.")


if __name__ == "__main__":
    main()
