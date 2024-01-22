import math

def calculate_grazing_area(R, r, theta):
    """Calculates the area of grass the goat can graze in an elliptical ranch.

    Args:
        R: Half of the horizontal dimension of the ranch.
        r: The length of the leash.
        theta: The angle formed between the point of tying and the horizontal axis in degrees.

    Returns:
        The total area of grass the goat can graze, rounded to three decimal points.
    """

    theta_rad = math.radians(theta)

    # Calculate the coordinates of the two points where the leash intersects the ellipse
    x1 = R + r * math.cos(theta_rad)
    y1 = r * math.sin(theta_rad)
    x2 = R - r * math.cos(theta_rad)
    y2 = -r * math.sin(theta_rad)

    # Calculate the areas of the two sectors formed by the leash and the ellipse
    sector1_area = 0.5 * (x1 * y1)  # Area of sector with positive x and y
    sector2_area = 0.5 * (x2 * y2)  # Area of sector with negative x and positive y

    # Calculate the area of the triangle formed by the two intersection points and the center of the ellipse
    triangle_area = 0.5 * r * r * math.sin(theta_rad)

    # Subtract the triangle area from the sum of sector areas to get the grazing area
    grazing_area = sector1_area + sector2_area - triangle_area

    return round(grazing_area, 3)

# Get input from the user
R = float(input())
r = float(input())
theta = float(input())

# Calculate and print the grazing area
grazing_area = calculate_grazing_area(R, r, theta)
print(grazing_area)
