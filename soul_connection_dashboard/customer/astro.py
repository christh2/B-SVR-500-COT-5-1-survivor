def check_client_compatibility(first, second):
    fire = ["aries", "leo", "sagittarius"]
    earth = ["virgo", "capricorn", "taurus"]
    air = ["gemini", "libra", "aquarius"]
    water = ["cancer", "scorpio", "pisces"]

    user_c = first.lower()
    dos_c = second.lower()

    if user_c in fire:
        if dos_c in fire + air:
            return 100
        elif dos_c in earth + water:
            return 50
        else:
            return 0
    elif user_c in earth:
        if dos_c in earth + water:
            return 100
        elif dos_c in fire + air:
            return 50
        else:
            return 0
    elif user_c in air:
        if dos_c in fire + air:
            return 100
        elif dos_c in earth + water:
            return 50
        else:
            return 0
    elif user_c in water:
        if dos_c in earth + water:
            return 100
    elif dos_c in fire + air:
        return 50
    else:
        return 0