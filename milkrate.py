from decimal import Decimal

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP_RATE = Decimal("0.40")
SNF_STEP_RATE = Decimal("0.30")


def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fat_steps = (fat - BASE_FAT) / Decimal("0.1")
    snf_steps = (snf - BASE_SNF) / Decimal("0.1")
    return BASE_RATE + fat_steps * FAT_STEP_RATE + snf_steps * SNF_STEP_RATE


def payout(litres, fat, snf):
    """Calculate payment for one delivery."""
    return litres * rate_per_litre(fat, snf)


if __name__ == "__main__":
    print(f"Example rate: Rs {rate_per_litre(Decimal('4.2'), Decimal('8.8')):.2f}")
