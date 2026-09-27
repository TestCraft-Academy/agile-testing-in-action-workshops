"""Keep the demonstrated observations reproducible without external packages."""

import subprocess
import sys
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "demos"))
from swiftcart import Item, Promotion  # noqa: E402


class PromotionDemonstrationTests(unittest.TestCase):
    def test_happy_path_still_passes(self) -> None:
        self.assertEqual(Promotion().apply("happy", [Item(Decimal("50"))], "SAVE20"), Decimal("10"))

    def test_gift_card_defect_is_reproducible(self) -> None:
        basket = [Item(Decimal("40")), Item(Decimal("10"), gift_card=True)]
        self.assertEqual(Promotion().apply("gift-card", basket, "SAVE20"), Decimal("8"))

    def test_retry_defect_is_reproducible(self) -> None:
        promotion = Promotion()
        basket = [Item(Decimal("50"))]
        self.assertEqual(promotion.apply("retry", basket, "SAVE20"), Decimal("10"))
        self.assertEqual(promotion.apply("retry", basket, "SAVE20"), Decimal("20"))

    def test_invalid_code_does_not_apply_discount(self) -> None:
        self.assertEqual(Promotion().apply("invalid", [Item(Decimal("50"))], "OTHER"), Decimal("0"))

    def test_all_scripts_run_from_repository_root(self) -> None:
        expectations = {
            "01_green_is_not_enough.py": "[DEFECT] Gift cards incorrectly count",
            "02_retry_changes_the_risk.py": "[DEFECT] Retrying applies",
            "03_release_conversation.py": "[ILLUSTRATIVE RECOMMENDATION]",
        }
        for filename, expected in expectations.items():
            with self.subTest(filename=filename):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "demos" / filename)],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                self.assertIn(expected, result.stdout)


if __name__ == "__main__":
    unittest.main()
