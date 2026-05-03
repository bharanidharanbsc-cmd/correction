from PIL import Image as I
import pygame as pg
import re
import random
import time
import pywhatkit

#RKO RENTAL SHOP


#  FUNCTION FOR LOGO
def open_logo():
    try:
        image = (I.
                 open("C:\\Users\\hari\\Downloads\\rko.jpeg"))
        image.show()
    except Exception as e:
        print("❌ Logo image not found")
        print("Error:", e)


#FUNCTION FOR MUSIC
def play_music():

    try:
        pg.init()
        pg.mixer.init()

        pg.mixer.music.load("C:\\Users\\hari\\Downloads\\intro.mpeg")
        pg.mixer.music.play()

        # Music play timing
        time.sleep(23)

        pg.mixer.music.stop()

    except Exception as e:
        print("❌ Music error:", e)


# ---------- OPEN LOGO & PLAY MUSIC ----------
open_logo()
play_music()

print("🚗 Welcome to RKO Rental Shop 🚗")

# ---------------- LOGO ----------------
print("🚗===========================🚗")
print("         RKO RENTAL SHOP")
print("   Vehicle Rent Management System")
print("📍 Coimbatore | 📞 9876543210")
print("🚗===========================🚗")
# DATABASE
bookings = []

# VEHICLE STOCK
vehicle_stock = {
    "Bike": 15,
    "Car": 10,
    "Travels": 2,
    "Cycle": 34
}

#  VEHICLE RENT PRICE
vehicle_rent_price = {
    "Bike": 800,
    "Car": 1700,
    "Travels": 3000,
    "Cycle": 200
}

# ---------------- KM LIMIT PER DAY ----------------
km_limit_per_day = {
    "Bike": 80,
    "Car": 150,
    "Travels": 250,
    "Cycle": 40
}

#  VEHICLE SECTION
vehicle_section = {
    "Bike": "🏍️ Two Wheeler Section",
    "Car": "🚗 Premium Car Section",
    "Travels": "🚌 Travels Section",
    "Cycle": "🚲 Eco Ride Section"
}

# DAMAGE PRICE LIST
damage_rates = {
    "1": ("Scratch", 500),
    "2": ("Side Mirror", 1500),
    "3": ("Seat Damage", 2000)
}

# LICENSE CHECK

def check_license(lic):

    pattern = r"^[A-Z]{2}\d{2}\d{4}\d{5}$"

    return re.match(pattern, lic.replace(" ", "").upper())

#             GENERATE BOOKING ID

def generate_id():

    return "ID" + str(random.randint(1000, 9999))

#            WHATSAPP MESSAGE

def send_whatsapp_message(number, customer, vehicle, booking_id):

    try:

        message = (
            f"🚗 RKO RENTAL SHOP 🚗\n"
            f"Hello {customer}\n"
            f"Your booking is confirmed.\n"
            f"Vehicle: {vehicle}\n"
            f"Booking ID: {booking_id}\n"
            f"Thank you for choosing RKO Rental Shop 🙏"
        )

        pywhatkit.sendwhatmsg_instantly(
            number,
            message,
            wait_time=15
        )

        print("✅ WhatsApp Message Sent")

    except Exception as e:

        print("❌ WhatsApp Message Failed")
        print("Error:", e)



# RULES

def show_rules():

    print("\n📜 RENTAL RULES")
    print("📏 Extra KM Charge → ₹45/km")
    print("⌛ Late Fine → ₹100/hour")
    print("🔧 Damage Charge → Based on damage")
    print("🛡️ No vehicle damage allowed")

#  VEHICLE DISPLAY

def show_vehicle_details():

    print("\n🚘 AVAILABLE VEHICLE DETAILS")

    for vehicle in vehicle_stock.keys():

        print("\n--------------------------------")
        print("🚗 Vehicle:", vehicle)

        print("🏢 Section:", vehicle_section[vehicle])

        print("💵 Rent Per Day: ₹", vehicle_rent_price[vehicle])

        print("📏 KM Limit Per Day:",
              km_limit_per_day[vehicle], "KM")

        print("📦 Available Stock:", vehicle_stock[vehicle])

#  RENT VEHICLE

def rent_vehicle():

    print("\n🚗 VEHICLE RENT")

    show_rules()

    show_vehicle_details()

    print("\n1. 🏍️ Bike")
    print("2. 🚗 Car")
    print("3. 🚌 Travels")
    print("4. 🚲 Cycle")

    c = input("👉 Enter Choice: ")

    vehicle_map = {
        "1": "Bike",
        "2": "Car",
        "3": "Travels",
        "4": "Cycle"
    }

    if c not in vehicle_map:
        print("❌ Invalid Choice")
        return

    vehicle = vehicle_map[c]

    if vehicle_stock[vehicle] == 0:
        print("❌ Vehicle Not Available")
        return

    print("\n🏢 Vehicle Section:", vehicle_section[vehicle])

    name = input("👤 Customer Name: ")

    phone = input("📱 Enter WhatsApp Number (+91xxxxxxxxxx): ")

    # --- LICENSE VALIDATION --
    while True:

        lic = input("🪪 Driving Licence: ")

        if check_license(lic):
            break

        print("❌ Invalid Licence Format")
        print("✅ Example Format → TN38202312345")

    # ---RENT DAYS ---
    try:
        days = int(input("📅 Number of Days: "))
    except:
        print("❌ Invalid Days")
        return

    rent = vehicle_rent_price[vehicle]

    total = days * rent

    advance = total * 0.30

    km_limit = days * km_limit_per_day[vehicle]

    booking_id = generate_id()

    bookings.append({
        "id": booking_id,
        "name": name,
        "vehicle": vehicle,
        "days": days,
        "rent": rent,
        "advance": advance,
        "km_limit": km_limit
    })

    vehicle_stock[vehicle] -= 1

    print("\n✅ RENT SUCCESSFUL")
    print("🆔 Booking ID:", booking_id)
    print("🚘 Vehicle:", vehicle)
    print("🏢 Section:", vehicle_section[vehicle])
    print("💵 Rent Per Day: ₹", rent)
    print("📏 Total KM Limit:", km_limit, "KM")
    print("💳 Advance Paid: ₹", advance)

    # --- WHATSAPP MESSAGE ---
    send_whatsapp_message(
        phone,
        name,
        vehicle,
        booking_id
    )

#                   QUIZ GAME

def start_quiz():

    score = 0

    print("\n🎉 IPL QUIZ GAME 🎉")
    print("⏰ You have only 10 seconds for each question")

    questions = random.sample(range(1, 11), 5)

    for q in questions:

        # QUESTION 1
        if q == 1:

            print("\n1. IPL 2023 Winner?")
            print("A. CSK")
            print("B. MI")
            print("C. RCB")
            print("D. SRH")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "A":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 2
        elif q == 2:

            print("\n2. King Kohli?")
            print("A. Rohit")
            print("B. Virat")
            print("C. Dhoni")
            print("D. Gill")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "B":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 3
        elif q == 3:

            print("\n3. Yellow Army?")
            print("A. MI")
            print("B. GT")
            print("C. CSK")
            print("D. RR")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "C":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 4
        elif q == 4:

            print("\n4. IPL Full Form?")
            print("A. Indian Premier League")
            print("B. Indian Power League")
            print("C. International Premier League")
            print("D. None")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "A":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 5
        elif q == 5:

            print("\n5. Captain Cool?")
            print("A. Hardik")
            print("B. Rohit")
            print("C. Dhoni")
            print("D. KL Rahul")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "C":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 6
        elif q == 6:

            print("\n6. Most IPL Titles?")
            print("A. CSK")
            print("B. MI")
            print("C. RCB")
            print("D. KKR")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "B":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 7
        elif q == 7:

            print("\n7. RCB Jersey Color?")
            print("A. Yellow")
            print("B. Blue")
            print("C. Red")
            print("D. Green")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "C":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 8
        elif q == 8:

            print("\n8. CSK Captain?")
            print("A. Dhoni")
            print("B. Jadeja")
            print("C. Raina")
            print("D. Bravo")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "A":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 9
        elif q == 9:

            print("\n9. MI Home Ground?")
            print("A. Wankhede")
            print("B. Chepauk")
            print("C. Eden Gardens")
            print("D. Kotla")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "A":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

        # QUESTION 10
        elif q == 10:

            print("\n10. IPL Started In?")
            print("A. 2005")
            print("B. 2008")
            print("C. 2010")
            print("D. 2012")

            start = time.time()

            ans = input("👉 Enter Answer: ").upper()

            end = time.time()

            if end - start > 10:
                print("⏰ Time Up")
            else:
                if ans == "B":
                    print("✅ Correct")
                    score += 1
                else:
                    print("❌ Wrong")

    #FINAL SCORE
    print("\n🏆 FINAL SCORE =", score, "/5")

    if score == 5:
        print("🎁 Amazing! You won Powerbank 🔋")

    elif score >= 4:
        print("🎁 Great! You won Sunglasses 🕶️")

    elif score >= 2:
        print("🎁 Good! You won Travel Bag 🎒")

    else:
        print("😔 Better Luck Next Time")

    print("\n🙏 Thank You For Visiting RKO Rental Shop")

# RETURN VEHICLE
def return_vehicle():

    print("\n🔄 RETURN VEHICLE")

    bid = input("👉 Enter Booking ID: ")

    found = None

    for b in bookings:

        if b["id"] == bid:
            found = b
            break

    if not found:
        print("❌ Invalid Booking ID")
        return

    print("🚘 Vehicle:", found["vehicle"])
    print("👤 Customer:", found["name"])

    total = found["days"] * found["rent"]

    advance = found["advance"]

    used = int(input("📏 Used KM: "))

    allowed = found["km_limit"]

    print("📏 Allowed KM:", allowed)

    extra_km = max(0, used - allowed)

    extra = extra_km * 45

    #  LATE FINE
    late = input("⌛ Late Return? (yes/no): ")

    late_fine = 0

    if late.lower() == "yes":

        hrs = int(input("⏰ Enter Late Hours: "))

        late_fine = hrs * 100

    #  DAMAGE
    print("\n🔧 DAMAGE CHECK")
    print("1. Scratch (₹500)")
    print("2. Side Mirror (₹1500)")
    print("3. Seat Damage (₹2000)")
    print("0. No Damage")

    damage_total = 0

    while True:

        choice = input("👉 Select Damage (0 to finish): ")

        if choice == "0":
            break

        elif choice in damage_rates:

            dname, price = damage_rates[choice]

            damage_total += price

            print(f"✅ Added {dname} - ₹{price}")

        else:
            print("❌ Invalid Choice")

    # --- FINAL BILL ---
    final = total + extra + late_fine + damage_total

    balance = final - advance

    print("\n🧾 FINAL BILL")
    print("💵 Vehicle Rent: ₹", total)
    print("📏 Extra KM Charge: ₹", extra)
    print("⌛ Late Fine: ₹", late_fine)
    print("🔧 Damage Charge: ₹", damage_total)
    print("💳 Advance Paid: ₹", advance)
    print("💰 Balance to Pay: ₹", balance)

    print("\n✅ Vehicle Returned Successfully")

    vehicle_stock[found["vehicle"]] += 1

    #  PERFECT CUSTOMER
    if extra == 0 and late_fine == 0 and damage_total == 0:

        print("\n🌟 CONGRATULATIONS 🌟")
        print("🎉 PERFECT CUSTOMER")
        print("🎯 You are eligible for the Prize Quiz")

        start_quiz()

    else:
        print("\n⚠️ Not Eligible For Quiz")

#                     MAIN MENU

while True:

    print("\n=================================")
    print("1. 🚗 Rent Vehicle")
    print("2. 🔄 Return Vehicle")
    print("3. 📋 Vehicle Details")
    print("4. ❌ Exit")
    print("=================================")

    ch = input("👉 Enter Choice: ")

    if ch == "1":
        rent_vehicle()

    elif ch == "2":
        return_vehicle()

    elif ch == "3":
        show_vehicle_details()

    elif ch == "4":

        try:
            image = I.open("C:\\Users\\hari\\Downloads\\exit.jpeg")
            image.show()

        except Exception as e:
            print("❌ Exit image not found")
            print("Error:", e)

        print("👋 Thank You for using RKO Rental Shop")
        break

    else:
        print("❌ Invalid Choice")