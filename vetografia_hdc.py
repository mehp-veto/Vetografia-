import numpy as np


def create_hdc_vector(concept, size=1000, rng=None):
    """Generates a high-dimensional (HDC) vector for a given concept."""
    if rng is None:
        rng = np.random.default_rng()
    vector = rng.random(size)
    if concept == "amor":
        vector *= 0.9
    elif concept == "amizade":
        vector *= 0.8
    elif concept == "verdade":
        vector *= 1.0
    return vector


def combine_vectors(vector1, vector2):
    """Combines two vectors by addition."""
    return np.add(vector1, vector2)


def circular_multiply(vector1, vector2):
    """Circular multiplication of vectors using XOR over integer projections."""
    return np.bitwise_xor(vector1.astype(int), vector2.astype(int)).astype(float)


def run_experiment(seed=42, size=1000):
    rng = np.random.default_rng(seed)
    amor_vector = create_hdc_vector("amor", size=size, rng=rng)
    amizade_vector = create_hdc_vector("amizade", size=size, rng=rng)
    verdade_vector = create_hdc_vector("verdade", size=size, rng=rng)

    combined_vector = combine_vectors(amor_vector, amizade_vector)
    combined_with_verdade = combine_vectors(combined_vector, verdade_vector)
    multiplied_vector = circular_multiply(amor_vector, amizade_vector)

    return combined_vector, combined_with_verdade, multiplied_vector


def main():
    combined_vector, combined_with_verdade, multiplied_vector = run_experiment()
    np.set_printoptions(precision=2, suppress=True)
    print("Combined (amor + amizade) first 10:")
    print(combined_vector[:10])
    print("Combined with verdade first 10:")
    print(combined_with_verdade[:10])
    print("Circular multiplied (amor ⊗ amizade) first 10:")
    print(multiplied_vector[:10])


if __name__ == "__main__":
    main()
