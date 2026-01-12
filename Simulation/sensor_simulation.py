import random
import time

def simulate_heart_rate(stress=False):
    if stress:
        return random.randint(95, 120)
    return random.randint(65, 85)

def simulate_acceleration(fall=False):
    if fall:
        return round(random.uniform(2.6, 4.0), 2)
    return round(random.uniform(0.3, 1.2), 2)

def simulate_gsr(stress=False):
    if stress:
        return round(random.uniform(6.0, 10.0), 2)
    return round(random.uniform(1.0, 4.0), 2)

def simulate_gps():
    return {
        "lat": 21.1702,   # Example: Gujarat
        "lon": 72.8311
    }

def threat_score(hr, accel, gsr):
    score = 0
    if hr > 100:
        score += 30
    if accel > 2.5:
        score += 40
    if gsr > 6.0:
        score += 30
    return score

print("SMART SAFETY WEARABLE – SENSOR SIMULATION\n")

while True:
    mode = input("Enter mode (normal / stress / fall / exit): ").lower()

    if mode == "exit":
        break

    stress = mode == "stress"
    fall = mode == "fall"

    hr = simulate_heart_rate(stress)
    accel = simulate_acceleration(fall)
    gsr = simulate_gsr(stress)
    gps = simulate_gps()

    score = threat_score(hr, accel, gsr)

    print("\n--- SENSOR DATA ---")
    print(f"Heart Rate: {hr} BPM")
    print(f"Acceleration: {accel} g")
    print(f"GSR Level: {gsr}")
    print(f"Threat Score: {score}")

    if score >= 60:
        print("🚨 SOS TRIGGERED")
        print(f"📍 Location: {gps}")
    else:
        print("✅ STATUS: SAFE")

    time.sleep(1)
