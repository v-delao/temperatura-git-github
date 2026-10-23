def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

ciudad = "Madrid"
temperatura_celsius = 18
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

print(f"En {ciudad}, {temperatura_celsius} °C equivalen a {temperatura_fahrenheit:.1f} °F")