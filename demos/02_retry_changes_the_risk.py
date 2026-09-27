"""Demo 02: a common retry turns an otherwise valid discount into a loss."""

from decimal import Decimal

from swiftcart import Item, Promotion


def main() -> None:
    promotion = Promotion()
    items = [Item(Decimal("50"))]

    first = promotion.apply("retry", items, "SAVE20")
    second = promotion.apply("retry", items, "SAVE20")
    assert first == Decimal("10")
    print(f"[FIRST REQUEST] £50 eligible basket -> £{first} discount")
    print(f"[RETRY] Same basket and code -> £{second} total discount")
    print("[DEFECT] Retrying applies the same promotion twice (40% instead of 20%).")
    print("[TEAM QUESTION] Which service prevents duplicate redemption after a timeout?")


if __name__ == "__main__":
    main()
