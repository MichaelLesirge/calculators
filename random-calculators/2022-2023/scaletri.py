from helper import get_sint, get_point, sint

def scale(point_a: tuple[int, int], point_b: tuple[int, int], point_c: tuple[int, int], scale_factor: float, origin: tuple[int, int] = (0, 0)) -> tuple[tuple[int,int], tuple[int,int], tuple[int,int]]:
    # Translate the points by the origin
    point_a = (point_a[0] - origin[0], point_a[1] - origin[1])
    point_b = (point_b[0] - origin[0], point_b[1] - origin[1])
    point_c = (point_c[0] - origin[0], point_c[1] - origin[1])

    # Scale the points
    point_a = (sint(point_a[0] * scale_factor), sint(point_a[1] * scale_factor))
    point_b = (sint(point_b[0] * scale_factor), sint(point_b[1] * scale_factor))
    point_c = (sint(point_c[0] * scale_factor), sint(point_c[1] * scale_factor))

    # Translate the points back to their original positions
    point_a = (point_a[0] + origin[0], point_a[1] + origin[1])
    point_b = (point_b[0] + origin[0], point_b[1] + origin[1])
    point_c = (point_c[0] + origin[0], point_c[1] + origin[1])

    # Return the scaled triangle
    return (point_a, point_b, point_c)

while True:
    scale_by = get_sint("scale")
    origin = get_point("", "origin ")
    a, b, c = get_point("a"), get_point("b"), get_point("c")
    print(scale(a, b, c, scale_by, origin))
    print("Enlargement" if scale_by > 1 else "Reduction")
    print()