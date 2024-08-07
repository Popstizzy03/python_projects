import sympy as sp
import math

def rectangular_to_cylindrical(x, y, z):
    r = sp.sqrt(x**2 + y**2)
    theta = sp.atan2(y, x)
    return r, theta, z

def cylindrical_to_rectangular(r, theta, z):
    x = r * sp.cos(theta)
    y = r * sp.sin(theta)
    return x, y, z

def rectangular_to_spherical(x, y, z):
    rho = sp.sqrt(x**2 + y**2 + z**2)
    theta = sp.atan2(y, x)
    phi = sp.acos(z / rho)
    return rho, theta, phi

def spherical_to_rectangular(rho, theta, phi):
    x = rho * sp.sin(phi) * sp.cos(theta)
    y = rho * sp.sin(phi) * sp.sin(theta)
    z = rho * sp.cos(phi)
    return x, y, z

def cylindrical_to_spherical(r, theta, z):
    rho = sp.sqrt(r**2 + z**2)
    phi = sp.atan2(r, z)
    return rho, theta, phi

def spherical_to_cylindrical(rho, theta, phi):
    r = rho * sp.sin(phi)
    z = rho * sp.cos(phi)
    return r, theta, z

def main():
    sp.init_printing(use_unicode=True)
    
    print("Choose the coordinate system to convert from:")
    print("1. Rectangular (Cartesian)")
    print("2. Cylindrical")
    print("3. Spherical")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        x = sp.sympify(input("Enter x: "))
        y = sp.sympify(input("Enter y: "))
        z = sp.sympify(input("Enter z: "))
        print("Converting to Cylindrical...")
        r, theta, z_cyl = rectangular_to_cylindrical(x, y, z)
        print(f"Cylindrical: (r: {r}, θ: {theta}, z: {z_cyl})")
        print("Converting to Spherical...")
        rho, theta_sph, phi = rectangular_to_spherical(x, y, z)
        print(f"Spherical: (ρ: {rho}, θ: {theta_sph}, φ: {phi})")
    
    elif choice == 2:
        r = sp.sympify(input("Enter r: "))
        theta = sp.sympify(input("Enter θ: "))
        z = sp.sympify(input("Enter z: "))
        print("Converting to Rectangular...")
        x, y, z_rect = cylindrical_to_rectangular(r, theta, z)
        print(f"Rectangular: (x: {x}, y: {y}, z: {z_rect})")
        print("Converting to Spherical...")
        rho, theta_sph, phi = cylindrical_to_spherical(r, theta, z)
        print(f"Spherical: (ρ: {rho}, θ: {theta_sph}, φ: {phi})")
    
    elif choice == 3:
        rho = sp.sympify(input("Enter ρ: "))
        theta = sp.sympify(input("Enter θ: "))
        phi = sp.sympify(input("Enter φ: "))
        print("Converting to Rectangular...")
        x, y, z = spherical_to_rectangular(rho, theta, phi)
        print(f"Rectangular: (x: {x}, y: {y}, z: {z})")
        print("Converting to Cylindrical...")
        r, theta_cyl, z = spherical_to_cylindrical(rho, theta, phi)
        print(f"Cylindrical: (r: {r}, θ: {theta_cyl}, z: {z})")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
