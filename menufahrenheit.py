print(f"  Celsius    ->   Fahrenheit")
print(f"----------------------------")

for c in range(0,41):
    
    fah = (c * 1.8) + 32
    print(f"   {c:>3}       ->      {fah:5.1f}")
