"""Run a hyperdimensional-vector demo inspired by the project image.

The image mentions operations like `sum`, `combine_vectors`, `circular_multiply`,
and `XOR` over words such as `caminho`, `verdade`, `vida`, `amor`, and `amizade`.
This script turns that visual idea into a runnable example.
"""

from __future__ import annotations

import hashlib
import math
from typing import Dict, Iterable, List

DIM = 2048


def deterministic_vector(token: str, dim: int = DIM) -> List[int]:
    """Create a deterministic bipolar vector (-1/+1) for a token."""
    values: List[int] = []
    counter = 0
    while len(values) < dim:
        digest = hashlib.sha256(f"{token}:{counter}".encode("utf-8")).digest()
        for byte in digest:
            for bit_index in range(8):
                bit = (byte >> bit_index) & 1
                values.append(1 if bit else -1)
                if len(values) == dim:
                    break
            if len(values) == dim:
                break
        counter += 1
    return values


def vector_sum(vectors: Iterable[List[int]]) -> List[float]:
    vectors = list(vectors)
    if not vectors:
        return [0.0] * DIM
    result = [0.0] * len(vectors[0])
    for vector in vectors:
        for idx, value in enumerate(vector):
            result[idx] += value
    return result


def circular_shift(vector: List[int], amount: int = 1) -> List[int]:
    amount %= len(vector)
    return vector[-amount:] + vector[:-amount]


def circular_multiply(a: List[int], b: List[int]) -> List[int]:
    """Simple binding in bipolar space (element-wise product)."""
    return [x * y for x, y in zip(a, b)]


def xor_like(a: List[int], b: List[int]) -> List[int]:
    """XOR-like operation for bipolar vectors.

    In bipolar encoding, XOR in {0,1} maps naturally to multiplication in {-1,+1}.
    """
    return circular_multiply(a, b)


def cosine_similarity(a: List[float], b: List[int]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def top_similar(query: List[float], space: Dict[str, List[int]], k: int = 5) -> List[tuple[str, float]]:
    ranking = [(token, cosine_similarity(query, vec)) for token, vec in space.items()]
    ranking.sort(key=lambda item: item[1], reverse=True)
    return ranking[:k]


def main() -> None:
    tokens = ["amor", "amizade", "caminho", "verdade", "vida"]
    space = {token: deterministic_vector(token) for token in tokens}

    semantic_sum = vector_sum(space.values())

    # picture-inspired composition: circular_multiply + XOR + combine(sum)
    path_truth_binding = circular_multiply(space["caminho"], circular_shift(space["verdade"], 7))
    phrase_binding = xor_like(path_truth_binding, space["vida"])
    combined = vector_sum([semantic_sum, phrase_binding])

    print("Vetografia: execução da imagem")
    print("Frase-alvo: 'Jesus é o caminho, a verdade e a vida'")
    print("\nTop similar words for the combined vector:")
    for token, score in top_similar(combined, space):
        print(f"- {token:9s} -> cosine={score:.4f}")


if __name__ == "__main__":
    main()
