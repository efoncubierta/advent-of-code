from sympy import symbols, Eq, solve
import numpy as np

def parse_input(str):
    ps = str.split(" @ ")

    pos = [*map(int, ps[0].split(", "))]
    vel = [*map(int, ps[1].split(", "))]
    return (pos, vel)

with open("input.txt", "r") as file:
    H = [
        parse_input(input)
        for input in file.read().split("\n")
    ]

def intersection(p1, v1, p2, v2):
    # Convertir listas a arrays de NumPy para facilitar el cálculo
    p1, p2, v1, v2 = map(np.array, [p1, p2, v1, v2])

    # Crear la matriz A y el vector b para el sistema de ecuaciones Ax = b
    A = np.array([v1, -v2]).T
    b = p2 - p1

    # Revisar si A es una matriz singular (lo que indicaría que no hay solución única)
    if np.linalg.matrix_rank(A) < 2:
        return (None, None, None)  # No hay intersección si el sistema no tiene solución única

    # Resolver para t y s (tiempos para cada partícula)
    try:
        t1, t2 = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        return (None, None, None)  # No hay intersección si el sistema no tiene solución

    # Calcular el punto de intersección
    p = p1 + v1 * t1

    return (t1, t2, p)

# LOW = 200000000000000
# HIGH = 400000000000000
# total = 0
# for i, (p1, v1) in enumerate(H):
#     for (p2, v2) in H[i+1:]:
#         (t1, t2, p) = intersection(p1, v1, p2, v2)
#         if t1 is None:
#             continue
#         if t1 >= 0 and t2 >= 0 and LOW <= p[0] <= HIGH and LOW <= p[1] <= HIGH:
#             total += 1

# print("Part 1: {}".format(total))


# Definir símbolos para la posición y velocidad iniciales y tiempos de intersección
x, y, z = symbols('x y z')  # Posición inicial
vx, vy, vz = symbols('vx vy vz')  # Velocidad inicial
t_intercepts = symbols(' '.join([f't_{i}' for i in range(len(H))]))  # Tiempos de intersección

# Crear sistema de ecuaciones
equations = []
for i, (sp, sv) in enumerate(H):
    t = t_intercepts[i]
    equations.append(Eq(x + vx * t, sp[0] + sv[0] * t))
    equations.append(Eq(y + vy * t, sp[1] + sv[1] * t))
    equations.append(Eq(z + vz * t, sp[2] + sv[2] * t))

# Resolver el sistema de ecuaciones
solution = solve(equations, (x, y, z, vx, vy, vz, *t_intercepts))

# Imprimir la solución
print(solution)