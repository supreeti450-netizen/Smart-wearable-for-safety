def threat_score(hr, accel):
    score = 0
    if hr > 100:
        score += 40
    if accel > 2.5:
        score += 50

    if score >= 60:
        return "SEND SOS"
    return "SAFE"

print(threat_score(120, 3.0))
