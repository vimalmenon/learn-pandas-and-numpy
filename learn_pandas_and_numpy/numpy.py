import numpy as np


def create_array_with_types():
    value = np.array([1.8, 2.8, 3.8], dtype="int8")
    print(value)
    print(value.ndim)


if __name__ == "__main__":
    create_array_with_types()
