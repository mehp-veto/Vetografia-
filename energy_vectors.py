import math


# Função para calcular 30! (fatorial)
def factorial(n: int) -> int:
    return math.factorial(n)


# Função para calcular a energia de mc^2
# parâmetros: mass (massa) e speed_of_light (velocidade da luz)
def energy_mc2(mass: float, speed_of_light: float) -> float:
    return mass * speed_of_light**2


# Função para calcular a energia de TNT (em Joules)
# 1 ton TNT = 4.184e9 Joules
def energy_tnt(tons: float) -> float:
    return tons * 4.184e9


def main() -> None:
    # Passo 1: calcular 30!
    fact_30 = factorial(30)

    # Passo 2: calcular mc^2 para m=500 kg e c=3e8 m/s
    m = 500  # massa em kg
    c = 3e8  # velocidade da luz em m/s
    energy_b = energy_mc2(m, c)

    # Passo 3: converter 1.000.000 toneladas TNT para Joules
    tons_tnt = 1e6
    energy_c = energy_tnt(tons_tnt)

    # Representações vetoriais (coeficiente + expoente para notação científica)
    a = ("NUM", "J", fact_30, 0)
    b = ("ENE", "J", 4.5, 19)
    c_vec = ("ENE", "J", 4.184, 15)

    # Dominância: termos com maior expoente
    dominant_vector = max([a, b, c_vec], key=lambda x: x[3])

    # Soma dos vetores (em Joules reais)
    total_energy = fact_30 + energy_b + energy_c
    sum_vector = ("SUM", "J", total_energy, 0)

    # Exibir resultados
    print(f"30! in Joules: {fact_30}")
    print(f"mc^2 in Joules: {energy_b}")
    print(f"e (1e6 ton TNT) in Joules: {energy_c}")
    print(f"Dominant vector (Δ): {dominant_vector}")
    print(f"Sum vector (⊕): {sum_vector}")
    print(f"Sum energy in ton TNT: {total_energy / 4.184e9}")


if __name__ == "__main__":
    main()
