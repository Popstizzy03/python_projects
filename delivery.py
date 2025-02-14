import pandas as pd
import numpy as np
import geopy.distance  # For distance calculation
# !pip install folium # Install if needed for visualization
import folium

# 1. Sample Delivery Data (replace with your actual data)
data = {'Order': ['A', 'B', 'C', 'D', 'E'],
        'Latitude': [37.7749, 37.7880, 37.7500, 37.7920, 37.7600],
        'Longitude': [-122.4194, -122.4000, -122.4300, -122.4100, -122.4250]}
df = pd.DataFrame(data)

# 2. Distance Calculation Function
def calculate_distance(coord1, coord2):
    return geopy.distance.geodesic(coord1, coord2).km

# 3. Nearest Neighbor Route Optimization
def optimize_route(start_location, locations):
    route = [start_location]
    remaining_locations = locations.copy()
    current_location = start_location

    while remaining_locations:
        nearest_location = None
        min_distance = float('inf')

        for location in remaining_locations:
            distance = calculate_distance(current_location, location)
            if distance < min_distance:
                min_distance = distance
                nearest_location = location

        route.append(nearest_location)
        remaining_locations.remove(nearest_location)
        current_location = nearest_location

    return route

# 4. Example Usage
start_point = (df['Latitude'][0], df['Longitude'][0]) # Starting point (e.g., bakery location)
delivery_points = [(row['Latitude'], row['Longitude']) for index, row in df.iterrows()]
optimized_route = optimize_route(start_point, delivery_points[1:])  # Exclude the starting point from delivery points

# Print the optimized route (coordinates)
print("Optimized Route (Coordinates):")
for point in optimized_route:
    print(point)

# Print the optimized route (Order IDs)
print("\nOptimized Route (Order IDs):")
start_order = df['Order'][0]
optimized_order_ids = [start_order] + [df['Order'][i+1] for i, point in enumerate(optimized_route)] # i+1 because we excluded the starting point
print(optimized_order_ids)

# 5. Route Visualization (Optional - install folium)
m = folium.Map(location=start_point, zoom_start=12)
for i, point in enumerate([start_point] + optimized_route):
     folium.Marker(location=point, popup=optimized_order_ids[i]).add_to(m)
for i in range(len(optimized_route)):
    points = [start_point] + optimized_route
    folium.PolyLine(locations=[points[i], points[i+1]], color="blue", weight=2.5, opacity=1).add_to(m)

m.save("delivery_route.html") # Save the map to an HTML file
print("Map saved to delivery_route.html")