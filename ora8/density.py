lead_volume = 18
copper_volume = 23

lead_density = 11.34
copper_density = 8.69

lead_m = lead_density * lead_volume
copper_m = copper_density * copper_volume

print("Az ólom nehezebb: ", lead_m > copper_m)