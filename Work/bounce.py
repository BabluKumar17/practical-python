# bounce.py
#
# Exercise 1.5
'''
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. 
Write a program bounce.py that prints a table showing the height of the first 10 bounces.
'''

height = 100      # meters
bounceBack = 0.6  # 3/5 meters
bounce = 1

while bounce <= 10:
    height = height * bounceBack
    print(bounce, round(height, 4))
    bounce += 1