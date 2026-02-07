import qrcode
import re
import time
from urllib.parse import quote


def is_valid_upi(upi_id: str) -> bool:
    """Basic UPI ID validation (e.g. name@bank)."""
    pattern = r'^[\w.-]+@[a-zA-Z0-9]{2,}$'
    return re.match(pattern, upi_id) is not None


def get_amount() -> float:
    """Safely get a valid payment amount."""
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        print("Please enter a valid amount greater than zero.")
        return None


# ---- User Input ----

upi_id = input("Enter your UPI ID: ").strip()

if not is_valid_upi(upi_id):
    print("Invalid UPI ID (example: username@upi)")
    exit()

recipient_name = input("Enter recipient name: ").strip() or "Unknown"
note = input("Enter transaction note (optional): ").strip()

amount = get_amount()
if amount is None:
    exit()

# ---- UPI URL Generation ----

upi_url = (
    f"upi://pay?"
    f"pa={upi_id}"
    f"&pn={quote(recipient_name)}"
    f"&am={amount:.2f}"
    f"&cu=INR"
)

if note:
    upi_url += f"&tn={quote(note)}"

# ---- QR Code Creation ----

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

qr.add_data(upi_url)
qr.make(fit=True)

qr_image = qr.make_image(fill_color="black", back_color="white")

# ---- Save Option ----

save_choice = input("Save QR code? (yes/no): ").strip().lower()

if save_choice in ("yes", "y"):
    filename = f"upi_qr_{time.strftime('%Y%m%d_%H%M%S')}.png"
    qr_image.save(filename)
    print(f"QR code saved as {filename}")

# ---- Display QR ----

try:
    qr_image.show()
    print("Scan the QR code to make the payment.")
except Exception as err:
    print(f"Could not display QR code: {err}")
