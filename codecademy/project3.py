def cost_ground(weight):
    if weight <= 2:
        return (1.50 * weight) + 20
    elif 2 < weight <= 6:
        return (3.00 * weight) + 20
    elif 6 < weight <= 10:
        return (4.00 * weight) + 20
    elif weight > 10:
        if (4.75 * weight) + 20 > 125:
            return 125.00
        return (4.75 * weight) + 20


def cost_drone(weight):
    if weight <= 2:
        return 4.50 * weight
    elif 2 < weight <= 6:
        return 9.00 * weight
    elif 6 < weight <= 10:
        return 12.00 * weight
    return 14.25 * weight


def cheapest_option(weight):
    if cost_ground(weight) < cost_drone(weight):
        if cost_ground(weight) == 125.0:
            return ["Premium ground shipping is cheapest", cost_ground(weight)]
        return ["Ground shipping is cheapest", cost_ground(weight)]
    else:
        return ["Drone shipping is cheapest", cost_drone(weight)]


print(cost_ground(80.4))
print(cost_drone(1.5))
print(cheapest_option(41.5))
