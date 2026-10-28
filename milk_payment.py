from decimal import Decimal, InvalidOperation

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP_RATE = Decimal("0.40")
SNF_STEP_RATE = Decimal("0.30")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
BONUS_LIMIT = Decimal("500")
BONUS_RATE = Decimal("0.50")


def rate_per_litre(fat, snf, month=1):
    """Return the rate per litre for the given fat, SNF and month."""
    if 4 <= month <= 6:
        base_rate = Decimal("32.00")
        fat_step_rate = Decimal("0.45")
    else:
        base_rate = BASE_RATE
        fat_step_rate = FAT_STEP_RATE

    fat_steps = (fat - BASE_FAT) / Decimal("0.1")
    snf_steps = (snf - BASE_SNF) / Decimal("0.1")
    return base_rate + fat_steps * fat_step_rate + snf_steps * SNF_STEP_RATE


def payout(litres, fat, snf, month=1):
    """Return payment for one delivery."""
    return litres * rate_per_litre(fat, snf, month)


def bonus_for_ten_days(total_litres):
    """Return the ten-day bonus when the total exceeds 500 litres."""
    if total_litres > BONUS_LIMIT:
        return total_litres * BONUS_RATE
    return Decimal("0.00")


def ten_day_total(deliveries):
    """Return the sum of delivery payments."""
    return sum(deliveries, Decimal("0.00"))


def main():
    farmer_id = input("Farmer ID: ").strip()
    try:
        litres = Decimal(input("Milk quantity (litres): ").strip())
        fat = Decimal(input("Fat percentage: ").strip())
        snf = Decimal(input("SNF percentage: ").strip())
        month = int(input("Month number (1-12): ").strip())
    except (InvalidOperation, ValueError):
        print("Invalid input. Enter numbers in the requested format.")
        return

    if not farmer_id:
        print("Farmer ID cannot be empty.")
        return
    if not litres.is_finite() or litres <= 0:
        print("Milk quantity must be a positive number.")
        return
    if not fat.is_finite() or not MIN_FAT <= fat <= MAX_FAT:
        print("Fat must be between 2.0 and 7.0.")
        return
    if not snf.is_finite() or snf < 0:
        print("SNF cannot be negative.")
        return
    if not 1 <= month <= 12:
        print("Month must be between 1 and 12.")
        return

    rate = rate_per_litre(fat, snf, month)
    amount = payout(litres, fat, snf, month)
    print("\\n--- Ksheera Milk Payment Receipt ---")
    print(f"Farmer ID       : {farmer_id}")
    print(f"Milk quantity   : {litres:.2f} litres")
    print(f"Fat percentage  : {fat:.2f}%")
    print(f"SNF percentage  : {snf:.2f}%")
    print(f"Rate per litre  : Rs {rate:.2f}")
    print(f"Payment         : Rs {amount:.2f}")


if __name__ == "__main__":
    main()
