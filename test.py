def graphoTest(input):
    print(f"Entrada: {input}")
    if input > 1:
        print("Camino 1: input > 1")
    else:
        print("Camino 2: input <= 1")
        if input > 0:
            print("  Camino 2a: input > 0")
        else:
            print("  Camino 2b: input <= 0")
            return input

    if input < 3:
        print("Camino 3: input < 3")
    else:
        print("Camino 4: input >= 3")

test_cases = [
    2,      # Cubre: input > 1, input < 3
    0.5,    # Cubre: input <= 1, input > 0, input < 3
    -1,     # Cubre: input <= 1, input <= 0
    4,      # Cubre: input > 1, input >= 3
    1,      # Cubre: input <= 1, input > 0, input < 3 (borde)
]

for i, test_input in enumerate(test_cases, 1):
    print(f"\n--- Caso de Prueba {i} ---")
    result = graphoTest(test_input)
    if result is not None:
        print(f"Retornado: {result}")