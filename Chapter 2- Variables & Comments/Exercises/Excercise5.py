def calculate_usb_sticks_and_change(Amount, price_per_usb):
    num_usb_sticks = Amount // price_per_usb
    change = Amount - (num_usb_sticks * price_per_usb)
    return num_usb_sticks, change

Amount = 50
price_per_usb = 6
num_usb_sticks, change = calculate_usb_sticks_and_change(Amount, price_per_usb)
print(f"She can buy {num_usb_sticks} USB sticks and will have £{change} left.")