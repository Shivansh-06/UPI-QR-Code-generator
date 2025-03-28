import qrcode
import re
import time

# Validate UPI ID
def is_valid_upi(upi_id):
    return re.match(r'^[\w.-]+@[a-zA-Z0-9]{2,}$', upi_id) is not None

# Get UPI ID from user
UPI_id = input("Enter your UPI ID: ").strip()

if not is_valid_upi(UPI_id):
    print("❌ Invalid UPI ID! Please enter a valid one (e.g., user@upi).")
else:
    # Get recipient name
    recipient_name = input("Enter recipient name: ").strip()
    if not recipient_name:
        recipient_name = "Unknown"

    # Enter transaction note (optional)
    transaction_note = input("Enter transaction note (optional): ").strip()
    
    # Enter the amount to be paid
    try:
        amt = float(input("Enter amount: "))
        if amt <= 0:
            raise ValueError("Amount must be greater than zero.")
    except ValueError as e:
        print(f"❌ Invalid amount! {e}")
    else:
        # Generate the UPI payment URL
        upi_url = f'upi://pay?pa={UPI_id}&pn={recipient_name}&am={amt:.2f}&cu=INR'
        if transaction_note:
            upi_url += f"&tn={transaction_note.replace(' ', '%20')}"  # Encode spaces for URL

        # Create QR Code
        qr = qrcode.QRCode(
            version=3,  # Slightly larger QR version for better readability
            error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
            box_size=10,
            border=4,
        )
        qr.add_data(upi_url)
        qr.make(fit=True)

        # Generate the QR image
        qr_image = qr.make_image(fill="black", back_color="white")

        # Save QR code (optional)
        save_option = input("Do you want to save the QR code? (yes/no): ").strip().lower()
        if save_option in ["yes", "y"]:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            file_name = f"upi_qr_{timestamp}.png"
            qr_image.save(file_name)
            print(f"✅ QR code saved as {file_name}")
        else:
            print("📌 You can scan the displayed QR code to make the payment.")

        
        # Display QR code
        try:
            qr_image.show()
        except Exception as e:
            print(f"⚠️ Error displaying QR code: {e}")
