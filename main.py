# Group 11
# Kevin Kami
# Sage Taddeo
# Date: 11/05/2026
# Lab 10: Singleton - Space Station Meltdown
# Description: The user plays as an engineer who must repair the failing
# systems (shields, life support, and reactor cooling) of a damaged space
# station for 10 turns until a rescue crew arrives. The Reactor is a singleton
# shared by every system.

import check_input
import reactor
import lifesupport
import shields
import cooling

def check_failure(ls, sh):
    """Checks if the reactor has overheated, life support has failed, or the shields have failed.
    Args:
        ls: the station's LifeSupport system.
        sh: the station's Shields system.
    Returns:
        True if any system has failed, False otherwise.
    """
    r = reactor.Reactor()

    if r.temperature >= 100:
        print("\nReactor has overheated! The station is lost.")
        return True

    if ls.oxygen <= 0:
        print("\nLife support has failed! The station is lost.")
        return True

    if sh.shields <= 0:
        print("\nShields have failed! The station is lost.")
        return True

    return False


def display_station_stats(ls, sh):
    """Displays the reactor, life support, and shield levels, along with warnings for any system near failure.
    Args:
        ls: the station's LifeSupport system.
        sh: the station's Shields system.
    """
    r = reactor.Reactor()

    print(f"Reactor Power Level: {r.power}%")
    print(f"Reactor Temperature: {r.temperature}%")
    print(f"Life Support: {ls.oxygen}%")
    print(f"Shields: {sh.shields}%")

    # Warn the player about any system within 20 points of failure
    if r.power <= 20:
        print("Reactor's power level is low!")

    if r.temperature >= 80:
        print("Reactor's temperature is high! Repair the cooling system!")

    if ls.oxygen <= 20:
        print("Oxygen levels are low! Repair the life support system!")

    if sh.shields <= 20:
        print("Shields are low! Repair the station's shields!")


def main():
    """Runs the Space Station Meltdown game."""
    r = reactor.Reactor()
    ls = lifesupport.LifeSupport()
    sh = shields.Shields()
    cs = cooling.Cooling()

    hours_remaining = 10
    station_operational = True

    # Display the game's introduction
    print("-Space Station Meltdown-")
    print("Chief Engineer's Report: The")
    print("station is being bombarded by")
    print("meteors, systems are critical.")
    print("A rescue crew is on the way, but it")
    print("will take them hours to get here.")
    print("I must simultaneously maintain life")
    print("support, shields, and the reactor's")
    print("temperature until they arrive.")

    while hours_remaining > 0 and station_operational:
        result = ''

        # Display the current status of the station
        print(f'\nTime until repair crews arrive: {hours_remaining} hours.')
        display_station_stats(ls, sh)

        # Prompt the player to select generate power or repair a system.
        print("\nRepair Stations:")
        print("1. Generate Power")
        print("2. Repair Shields")
        print("3. Repair Life Support")
        print("4. Repair Cooling System")
        choice = check_input.get_int_range(">", 1, 4)

        if choice == 1:
            r.generate_power()
        elif choice == 2:
            result = sh.repair()
            print(result)
        elif choice == 3:
            result = ls.repair()
            print(result)
        elif choice == 4:
            result = cs.repair()
            print(result)

        # Keeps the same turn (hours) if player chooses to repair a system without sufficient power.
        if result == "Insufficient reactor power!":
            continue

        # Applies the end of turn damages
        sh.damage(10)
        ls.consume(10)
        r.consume_power(5)
        r.heat(5)

        # Checks if any of the systems have failed. End game if true
        if check_failure(ls, sh):
            station_operational = False

        # Decrements the hours remaining until the repair crew arrives
        hours_remaining -= 1

    # Display game results
    if station_operational:
        print("\nThe rescue crew has arrived! You have survived the station meltdown.")
    else:
        print("\nThe station has been lost. Game over.")


if __name__ == "__main__":
    main()
