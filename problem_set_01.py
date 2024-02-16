# START PROBLEM SET 1
print("Problem Set 1 \n")

# PROBLEM 01
print("\nPROBLEM 01")

# 1frita_batidos = "Frita Batidos"
# zingerman's Delicatessen = "Zingerman's Delicatessen"
# nypd = New York Pizza Depot
hopcat = "HoPcAT"
fleetwood_diner = "Fleetwood Diner"
# tomukun_noodle_bar = "Tomukun Noodle Bar
jerk_pit = "JaMAIcaN JERk PIt"
# mama satto = "Mama Satto"
hola_seoul = "Hola Seoul"
# @shalimar = "Shalimar"

cottage_inn = "Cottage Inn Pizza"
print(cottage_inn)

madras_masala = "Madras Masala"
print(madras_masala)

# PROBLEM 02
print("\nPROBLEM 02")

hopcat_all_lower = hopcat.lower()
print(f"all_lower: {hopcat_all_lower}")

jerk_pit_all_upper = jerk_pit.upper()
print(f"all_upper: {jerk_pit_all_upper}")

madras_masala_count_m = madras_masala.count("m")
print(f"number of letter m: {madras_masala_count_m}")

has_diner = fleetwood_diner.endswith("Diner")
print(has_diner)

starts_seoul = hola_seoul.startswith("Seoul")
print(starts_seoul)

comment = "Truly authentic Jamaican food&drinks"
updated_comment = comment.replace("&", " and ")
print(f"updated comment: {updated_comment}")

# PROBLEM 03
print("\nPROBLEM 03")

num_chars = len(updated_comment)
print(f"number of characters: {num_chars}")

restaurants = [
    "Frita Batidos",
    "Zingerman's Delicatessen",
    "New York Pizza Depot",
    "Hopcat",
    "Fleetwood Diner",
    "Tomukun Noodle Bar",
    "Jamaican Jerk Pit",
    "Mama Satto",
    "Hola Seoul",
    "Shalimar",
    "Cottage Inn Pizza",
    "Madras Masala",
]

print(type(restaurants))

num_restaurants = len(restaurants)
print(f"number of restaurants: {num_restaurants}")

# PROBLEM 04
print("\nPROBLEM 04")
total_price = (18.99*4) + (6.99*5) + (7*2) + (10.49*5) + 22.25 + (17.99*2)
print(f"total price: {total_price}")

total_bill = total_price + (0.21 * total_price)
print(f"total bill: {total_bill}")

each_pay = total_bill / 7
print(f"each person pays: {each_pay}")

# PROBLEM 05
print("\nPROBLEM 05")

# TODO: Create f-string
print(f"Someone said '{updated_comment}' on Yelp for the restaurant {jerk_pit_all_upper}.")

# PROBLEM 06
print("\nPROBLEM 06")

# TODO: Create multiline string
print("""Frita Batidos
Zingerman's Delicatessen
New York Pizza Depot
Hopcat
Fleetwood Diner
Tomukun Noodle Bar
Jamaican Jerk Pit
Mama Satto
Hola Seoul
Shalimar
Cottage Inn Pizza
Madras Masala"""
)

# END PROBLEM SET
