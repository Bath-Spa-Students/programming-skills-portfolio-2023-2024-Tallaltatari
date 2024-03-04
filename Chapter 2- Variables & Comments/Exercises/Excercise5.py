def calculate_usb_sticks_and_change(Amount, price_per_usb):
    # Calculate how many USB sticks she can buy
    num_usb_sticks = Amount // price_per_usb
    # Calculate how much money she will have left
    change = Amount - (num_usb_sticks * price_per_usb)
    return num_usb_sticks, change

# Input values
Amount = 50
price_per_usb = 6

# Calculate and display the result
num_usb_sticks, change = calculate_usb_sticks_and_change(Amount, price_per_usb)
print(f"She can buy {num_usb_sticks} USB sticks and will have £{change} left.")