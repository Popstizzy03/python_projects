import numpy as np

# Given data
FR = 150  # Resultant force in lb
theta_xR = 120  # Direction angle in degrees
theta_zR = 130  # Direction angle in degrees
F1 = 80  # Given force in lb

# Compute the components of the resultant force FR
FRx = FR * np.cos(np.radians(theta_xR))
FRz = FR * np.cos(np.radians(theta_zR))

# Since F1 acts along the y-direction, its components are:
F1x = 0
F1y = 80
F1z = 0

# Compute the y-component of FR using unit vector property
theta_yR = np.degrees(np.arccos((FR**2 - FRx**2 - FRz**2)**0.5 / FR))
FRy = FR * np.cos(np.radians(theta_yR))

# Compute F2 components
F2x = FRx - F1x
F2y = FRy - F1y
F2z = FRz - F1z

# Compute the magnitude of F2
F2_magnitude = np.sqrt(F2x**2 + F2y**2 + F2z**2)

# Compute the direction angles of F2
theta_x2 = np.degrees(np.arccos(F2x / F2_magnitude))
theta_y2 = np.degrees(np.arccos(F2y / F2_magnitude))
theta_z2 = np.degrees(np.arccos(F2z / F2_magnitude))

# Output results
F2_magnitude, theta_x2, theta_y2, theta_z2

