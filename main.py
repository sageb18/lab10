# Group 11
# Kevin Kami
# Sage Taddeo
# Lab 10: Singleton
# Space Station Meltdown

import random 
import check_input
import reactor
import lifesupport
import shields
import cooling

def game_intro():
    print("-Space Station Meltdown-")
    print("Chief Engineer's Report: The")
    print("station is being bombarded by")
    print("meteors, systems are critical.")
    print("A rescue crew is on the way, but it")
    print("will take them hours to get here.")
    print("I must simultaneously maintain life")
    print("support, shields, and the reactor's")
    print("temperature until they arrive\n")

def menu():
    print("\nRepair stations:")
    print("1. Generate Power")
    print("2. Repair Shields")
    print("3. Repair Life Support")
    print("4. Repair Cooling System")

def check_failure(ls, sh):
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
    r = reactor.Reactor()

    print(f"Reactor Power Level: {r.power}%")
    print(f"Reactor Temperature: {r.temperature}%")
    print(f"Life Support: {ls.oxygen}%")
    print(f"Shields: {sh.shields}%")

    if r.power < 20:
        print("\nWarning: Reactor's power level is low!")

    if r.temperature > 80:
        print("\nWarning: Reactor's temperature is high!")   
        print("--> Repair the cooling system!") 

    if ls.oxygen < 20:
        print("\nWarning: Life support's oxygen level is low!")
        print("--> Repair life support!")

    if sh.shields < 20:
        print("\nWarning: Shields' level is low!")
        print("--> Repair the station's shields!")


def main():

    hours_remaining = 10
    r = reactor.Reactor()
    ls = lifesupport.LifeSupport()
    sh = shields.Shields()
    cs = cooling.Cooling()
    station_operational = True

    game_intro()

    while hours_remaining > 0 and station_operational:
        result = ''
        
        # Display the current status of the station
        print(f'\n\nTime until repair crews arrive: {hours_remaining} hours.')
        display_station_stats(ls, sh)

        # Prompt the player to select generate power or repair a system.
        menu()
        choice = check_input.get_int_range("Enter your choice: ", 1, 4)

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

        # Keeps the same turn if player chooses to repair a system but there is insufficient power
        if result == "Insufficient reactor power!":
            continue

        # Increments the  end of turn damages 
        sh.damage(10)
        ls.consume(10)
        r.consume_power(5)
        r.heat(5)

        # Checks if any of the systems have failed. End game if true
        if check_failure(ls, sh):
            station_operational = False
            break

        # Decrements the hours remaining until the repair crew arrives
        hours_remaining -= 1

    # Display game results
    if station_operational:
        print("\n\nThe rescue crew has arrived! You have survived the station meltdown.")
    else:
        print("\n\nThe station has been lost. Game over.")  

        
if __name__ == "__main__":
    main()