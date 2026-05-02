from PIL import Image as I
import pygame as pg
import time as t
import re
import random
import time

# ====================================
#              RKO RENTAL SHOP
# ====================================

# ---------- FUNCTION FOR LOGO ----------
def open_logo():
    try:
        image = I.open("C:\\Users\\hari\\Downloads\\rko.jpeg")
        image.show()
    except:
        print("❌ Logo image not found")


# ---------- FUNCTION FOR MUSIC ----------
def play_music():

    try:
        pg.init()
        pg.mixer.init()

        pg.mixer.music.load("C:\\Users\\hari\\Downloads\\intro.mpeg")
        pg.mixer.music.play()

        # Music play timing
        t.sleep(23)

        pg.mixer.music.stop()

    except:
        print("❌ Music file not found")


# ---------- OPEN LOGO & PLAY MUSIC ----------
open_logo()
play_music()

print("🚗 Welcome to RKO Rental Shop 🚗")

# ---------------- LOGO ----------------
print("🚗======================================🚗")
print("         RKO RENTAL SHOP")
print("   Vehicle Rent Management System")
print("📍 Coimbatore | 📞 9876543210")
print("🚗======================================🚗")

# ---------------- DATABASE ----------------
bookings = []

# ---------------- VEHICLE STOCK ----------------
vehicle_stock = {
    "Bike": 15,
    "Car": 10,
    "Travels": 2,
    "Cycle": 34
}

# ---------------- VEHICLE RENT PRICE ----------------
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

# ---------------- VEHICLE SECTION ----------------
vehicle_section = {
    "Bike": "🏍️ Two Wheeler Section",
    "Car": "🚗 Premium Car Section",
    "Travels": "🚌 Travels Section",
    "Cycle": "🚲 Eco Ride Section"
}

# ---------------- DAMAGE PRICE LIST ----------------
damage_rates = {
    "1": ("Scratch", 500),
    "2": ("Side Mirror", 1500),
    "3": ("Seat Damage", 2000)
}


# ---------------- LICENSE CHECK ----------------
def check_license(lic):

    pattern = r"^[A-Z]{2}\d{2}\d{4}\d{5}$"

    return re.match(pattern, lic.replace(" ", "").upper())


# ---------------- GENERATE BOOKING ID ----------------
def generate_id():

    return "ID" + str(random.randint(1000, 9999))


# ---------------- RULES ----------------
def show_rules():

    print("\n📜 RENTAL RULES")
    print("📏 Extra KM Charge → ₹45/km")
    print("⌛ Late Fine → ₹100/hour")
    print("🔧 Damage Charge → Based on damage")
    print("⛽ Fuel should be maintained properly")
    print("🛡️ No vehicle damage allowed")


# ---------------- VEHICLE DISPLAY ----------------
def show_vehicle_details():

    print("\n🚘 AVAILABLE VEHICLE DETAILS")

    for vehicle in vehicle_stock.keys():

        print("\n--------------------------------")
        print("🚗 Vehicle:", vehicle)

        if vehicle in vehicle_section:
            print("🏢 Section:", vehicle_section[vehicle])

        if vehicle in vehicle_rent_price:
            print("💵 Rent Per Day: ₹", vehicle_rent_price[vehicle])

        if vehicle in km_limit_per_day:
            print("📏 KM Limit Per Day:",
                  km_limit_per_day[vehicle], "KM")

        print("📦 Available Stock:", vehicle_stock[vehicle])


# ---------------- RENT VEHICLE ----------------
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

    # ---------- LICENSE VALIDATION ----------
    while True:

        lic = input("🪪 Driving Licence: ")

        if check_license(lic):
            break

        print("❌ Invalid Licence Format")
        print("✅ Example Format → TN38202312345")

    # ---------- RENT DAYS ----------
    try:
        days = int(input("📅 Number of Days: "))
    except:
        print("❌ Invalid Days")
        return

    rent = vehicle_rent_price[vehicle]

    total = days * rent

    advance = total * 0.30

    km_limit = days * km_limit_per_day[vehicle]

    bid = generate_id()

    bookings.append({
        "id": bid,
        "name": name,
        "vehicle": vehicle,
        "days": days,
        "rent": rent,
        "advance": advance,
        "km_limit": km_limit
    })

    vehicle_stock[vehicle] -= 1

    print("\n✅ RENT SUCCESSFUL")
    print("🆔 Booking ID:", bid)
    print("🚘 Vehicle:", vehicle)
    print("🏢 Section:", vehicle_section[vehicle])
    print("💵 Rent Per Day: ₹", rent)
    print("📏 Total KM Limit:", km_limit, "KM")
    print("💳 Advance Paid: ₹", advance)


# ---------------- QUIZ QUESTIONS ----------------
questions = [
    {
        "q": "IPL 2023 Winner?",
        "opts": ["A.CSK", "B.MI", "C.RCB", "D.SRH"],
        "ans": "A"
    },

    {
        "q": "King Kohli?",
        "opts": ["A.Rohit", "B.Virat", "C.Dhoni", "D.Gill"],
        "ans": "B"
    },

    {
        "q": "Yellow Army?",
        "opts": ["A.MI", "B.GT", "C.CSK", "D.RR"],
        "ans": "C"
    },

    {
        "q": "IPL Full Form?",
        "opts": [
            "A.Indian Premier League",
            "B.Indian playing league",
            "C.International premier league",
            "D.indonesia premier league"
        ],
        "ans": "A"
    },

    {
        "q": "Captain Cool?",
        "opts": ["A.Hardik", "B.Rohit", "C.Dhoni", "D.KL"],
        "ans": "C"
    },

    {
        "q": "Most Titles?",
        "opts": ["A.CSK", "B.MI", "C.RCB", "D.KKR"],
        "ans": "B"
    },

    {
        "q": "RCB Color?",
        "opts": ["A.Yellow", "B.Blue", "C.Red", "D.Green"],
        "ans": "C"
    },

    {
        "q": "CSK Captain?",
        "opts": ["A.Dhoni", "B.Jadeja", "C.Raina", "D.Bravo"],
        "ans": "A"
    },

    {
        "q": "MI Ground?",
        "opts": ["A.Wankhede", "B.Chepauk", "C.Eden", "D.Kotla"],
        "ans": "A"
    },

    {
        "q": "IPL Start Year?",
        "opts": ["A.2005", "B.2008", "C.2010", "D.2012"],
        "ans": "B"
    }
]


# ---------------- ASK QUESTION ----------------
def ask_question(q):

    print("\n" + q["q"])

    for o in q["opts"]:
        print(o)

    print("⏳ You have 10 seconds")

    start = time.time()

    ans = input("👉 Answer: ").upper()

    end = time.time()

    if end - start > 10:
        print("⏰ Time Over")
        return 0

    if ans == q["ans"]:
        print("✅ Correct")
        return 1

    else:
        print("❌ Wrong")
        return 0


# ---------------- START QUIZ ----------------
def start_quiz():

    print("\n🎉 QUIZ START 🎉")

    score = 0

    for q in random.sample(questions, 5):
        score += ask_question(q)

    print("\n🏆 Your Score:", score, "/5")

    if score == 5:
        print("🎁 Amazing! You won a Powerbank 🔋")

    elif score == 4:
        print("🎁 Great! You won Sunglasses 🕶️")

    elif score == 3:
        print("🎁 Good! You won a Travel Bag 🎒")

    else:
        print("😔 Better luck next time!")

    print("\n🙏 Thank You for visiting RKO Rental Shop")


# ---------------- RETURN VEHICLE ----------------
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

    # ---------- LATE FINE ----------
    late = input("⌛ Late Return? (yes/no): ")

    late_fine = 0

    if late.lower() == "yes":

        hrs = int(input("⏰ Enter Late Hours: "))

        late_fine = hrs * 100

    # ---------- DAMAGE ----------
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

    # ---------- FINAL BILL ----------
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

    # ---------- PERFECT CUSTOMER ----------
    if extra == 0 and late_fine == 0 and damage_total == 0:

        print("\n🌟 CONGRATULATIONS 🌟")
        print("🎉 PERFECT CUSTOMER")
        print("🎯 You are eligible for the Prize Quiz")

        start_quiz()

    else:
        print("\n⚠️ Not Eligible For Quiz")


# ==================================================
#                     MAIN MENU
# ==================================================

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

        except:
            print("❌ Exit image not found")

        print("👋 Thank You for using RKO Rental Shop")
        break

    else:
        print("❌ Invalid Choice")