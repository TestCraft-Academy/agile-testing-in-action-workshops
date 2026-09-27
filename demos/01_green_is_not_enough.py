"""Demo 01: a passing acceptance check can hide a missing business rule."""

from decimal import Decimal

from swiftcart import Item, Promotion


def main() -> None:
    promotion = Promotion()

    happy_path = promotion.apply("happy", [Item(Decimal("50"))], "SAVE20")
    assert happy_path == Decimal("10")
    print("[ACCEPTANCE CHECK] £50 eligible basket -> £10 discount: PASS")

    gift_card_mix = [Item(Decimal("40")), Item(Decimal("10"), gift_card=True)]
    actual = promotion.apply("gift-card", gift_card_mix, "SAVE20")
    expected = Decimal("0")
    print(f"[NEW EXAMPLE] £40 eligible + £10 gift card -> expected £{expected}, got £{actual}")
    print("[DEFECT] Gift cards incorrectly count towards the £50 threshold.")
    print("[TEAM QUESTION] What counts towards minimum spend? Agree before adding more checks.")


if __name__ == "__main__":
    main()
