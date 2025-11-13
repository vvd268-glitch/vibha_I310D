import math

def calculate_volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

if __name__ == "__main__":
    print(calculate_volume_of_sphere(5))
