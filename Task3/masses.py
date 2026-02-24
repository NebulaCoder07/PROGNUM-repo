masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e+22]
names = ["Sun", "Jupiter", "Saturn", "Neptune", "Uranus", "Earth", "Venus", "Mars", "Mercury", "Moon", "Pluto"]
smaller_than_moon=[]
for mass in masses:
    if mass <= masses[names.index("Moon")]:
        smaller_than_moon.append(mass)

print(f"Masses that are <= than the Moon's mass: {smaller_than_moon}")
lastmass = masses[slice(len(masses)-5,len(masses))]
print(f"The last 5 masses are: {lastmass}")
print(f"The verage mass in the list is: {sum(lastmass)/len(lastmass)} kg.")
