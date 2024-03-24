# Constant Info
next_pol_num = 1944
basic_prem = 869.00
discount_add_cars = 0.25
extra_liab_cost = 130.00
glass_cov_cost = 86.00
loan_car_cost = 58.00
hst_rate = 0.15
process_fee = 39.99

# Valid provinces
valid_provinces = ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "NT", "NU", "YT"]

# Initialize lists
previous_claims = []

# Province Validation
def valid_province(province):
    return province.upper() in valid_provinces

# Calaculation of Premium
def premium(num_cars):
    return basic_prem + (num_cars - 1) * basic_prem * discount_add_cars

# Calculation of total cost
def total_cost(premium, num_cars, extra_liability, glass_coverage, loaner_car):
    extra_costs = (extra_liab_cost * extra_liability) + (glass_cov_cost * glass_coverage) + (loan_car_cost * loaner_car)
    total_premium = premium + extra_costs
    hst = total_premium * hst_rate
    total_cost = total_premium + hst
    return total_cost

# Display receipt
def display_receipt(customer_info, premium, total_cost):
    print("Receipt:")
    print("=" * 50)
    print("Customer Information:")
    print("-" * 50)
    for key, value in customer_info.items():
        print(f"{key:<25}: {value}")
    print("-" * 50)
    print(f"Insurance Premium (pre-tax): ${premium:>10.2f}")
    print(f"HST (15%): ${premium * hst_rate:>22.2f}")
    print(f"Total Cost: ${total_cost:>26.2f}")
    print("=" * 50)

# Function to add claim
def add_claim(claim_number, claim_date, claim_amount):
    previous_claims.append((claim_number, claim_date, claim_amount))

while True:
    # customer information
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ")
    province = input("Enter customer's province (2-letter abbreviation): ")

    while not valid_province(province):
        print("Invalid province. Please enter a valid 2-letter abbreviation.")
        province = input("Enter customer's province (2-letter abbreviation): ")

    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")
    num_cars = int(input("Enter the number of cars being insured: "))
    extra_liability = input("Extra liability coverage up to $1,000,000 (Y/N): ").upper() == 'Y'
    glass_coverage = input("Optional glass coverage (Y/N): ").upper() == 'Y'
    loaner_car = input("Optional loaner car coverage (Y/N): ").upper() == 'Y'
    payment_method = input("Payment method (Full/Monthly/Down Pay): ").upper()

    if payment_method == 'DOWN PAY':
        down_payment = float(input("Enter the down payment amount: "))
    else:
        down_payment = 0.0

    claim_number = input("Enter the claim number: ")
    claim_date = input("Enter the claim date (YYYY-MM-DD): ")
    claim_amount = float(input("Enter the claim amount: "))

    # Premium Calculation
    prem = premium(num_cars)

    # Total cost Calculation
    total = total_cost(prem, num_cars, extra_liability, glass_coverage, loaner_car)

    # Display receipt
    customer_info = {
        "First Name": first_name.title(),
        "Last Name": last_name.title(),
        "Address": address,
        "City": city.title(),
        "Province": province.upper(),
        "Postal Code": postal_code,
        "Phone Number": phone_number,
        "Number of Cars Insured": num_cars,
        "Extra Liability Coverage": "Yes" if extra_liability else "No",
        "Glass Coverage": "Yes" if glass_coverage else "No",
        "Loaner Car Coverage": "Yes" if loaner_car else "No",
        "Payment Method": payment_method,
        "Down Payment": f"${down_payment:.2f}" if down_payment else "N/A",
        "Claim Number": claim_number,
        "Claim Date": claim_date,
        "Claim Amount": f"${claim_amount:.2f}"
    }

    display_receipt(customer_info, prem, total)

    # current claim
    add_claim(claim_number, claim_date, claim_amount)

    # Update policy number for next customer
    next_pol_num += 1

    # Loop Information
    cont = input("Enter another customer (Y/N)? ").upper()
    if cont != 'Y':
        print("Policy data has been saved.Have a Wounderful Day!")
        break