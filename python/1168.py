"""
John wants to set up a panel containing different numbers of LEDs.
He does not have many leds, he is not sure if he will be able to mount the desired number. Considering the configuration 
of the LEDs of the numbers below, make an algorithm that helps John to discover the number of LEDs needed to set the value.
"""

led_quantity = {
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
    '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}

N = int(input())

for i in range(N):
    num = input().strip()
    total_leds = sum(led_quantity[digit] for digit in num)
    print(f"{total_leds} leds")