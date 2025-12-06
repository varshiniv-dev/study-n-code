# write a program to develop trignometry for enginnering.
# import math
#
# angle_deg = [0, 30, 45, 60, 90, 120]
# angle_rad = [math.radians(a) for a in angle_deg]
#
# sine_values = [math.sin(a) for a in angle_rad]
# cosine_values = [math.cos(a) for a in angle_rad]
# tangent_values = [math.tan(a) for a in angle_rad]
#
# print("Angle (degrees) | Sine       | Cosine     | Tangent    ")
# for i in range(len(angle_deg)):
#    print(
#        f"{angle_deg[i]:15} | {sine_values[i]:10.6f} | "
#        f"{cosine_values[i]:10.6f} | {tangent_values[i]:10.6f}"
#    )
#
# or
# angles_degrees = [0, 30, 45, 60, 90]
# angles_radians = [math.radians(angle) for angle in angles_degrees]
# for anngle, radians in zip(angles_degrees, angles_radians):
#    print(f'Angle: {anngle} degrees, Radians: {radians:.2f}, Sine: {math.sin(radians):.2f}, Cosine: {math.cos(radians):.2f}, Tangent: {math.tan(radians):.2f}')

# write a program to create beam deflection formula.
# import math
# p = 500
# l = 2
# e = 210e9
# i = 8.33e-6
# delta = (p*math.pow(l, 3))/(48*e*i)
# print("Beam Deflection:", delta, "meters")

# write a python program to calculate distance between two points.
import math
x1, y1 = (2, 3)
x2, y2 = (5, 7)
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Distance between points:", distance)
