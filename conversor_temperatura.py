def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

temperatura_celsius = 25
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit:.1f} °F")
