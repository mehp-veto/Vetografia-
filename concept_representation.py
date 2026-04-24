import numpy as np


def represent_concept(concept: str) -> np.ndarray:
    """Retorna uma representação vetorial simples para um conceito."""
    if concept == "Caminho":
        # Representação do conceito "Caminho": Ação + Relação + Origem
        return np.array([1.0, 0.8, 0.9])

    # Vetor padrão para conceito desconhecido
    return np.zeros(3)


if __name__ == "__main__":
    vetor_caminho = represent_concept("Caminho")
    print(vetor_caminho)
