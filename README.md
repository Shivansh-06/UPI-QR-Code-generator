# UPI QR Code Generator

## Overview
This Python script generates a QR code for UPI payments. Users can enter their UPI ID, recipient name, transaction note, and amount. The script then creates a scannable QR code for quick and easy payments.

## Features
- Validates UPI ID format
- Allows input of recipient name and transaction note
- Accepts and validates the transaction amount
- Generates a UPI payment URL
- Creates a QR code for the payment
- Option to save the QR code as an image
- Displays the QR code for scanning

## Prerequisites
Ensure you have Python installed on your system. Additionally, install the required dependency:

```sh
pip install qrcode[pil]
```

## How to Use
1. Run the script using:
   ```sh
   python script.py
   ```
2. Enter the required details when prompted:
   - UPI ID (e.g., `user@upi`)
   - Recipient name
   - Transaction note (optional)
   - Amount
3. The script generates a QR code with the entered details.
4. Choose whether to save the QR code as an image.
5. Scan the displayed QR code to proceed with the payment.

## Error Handling
- The script validates the UPI ID format.
- Ensures the transaction amount is a positive number.
- Provides warnings if the QR code cannot be displayed.

## Example Output
```
Enter your UPI ID: user@upi
Enter recipient name: John Doe
Enter transaction note (optional): Coffee Payment
Enter amount: 50.00
Do you want to save the QR code? (yes/no): yes
✅ QR code saved as upi_qr_20250328_153000.png
📌 You can scan the displayed QR code to make the payment.
```

## Author
[Shivansh Goyal]

