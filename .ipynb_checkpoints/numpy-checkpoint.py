import numpy as np


def create_array_with_types():
    value = np.array([1, 2, 3, 4], dtype="int8")
    print(value)
    print(value.ndim)
    print("Shape")
    print(value.shape)
    print("Size")
    print(value.size)
    print(np.newaxis)
    print(np.empty(2))


if __name__ == "__main__":
    create_array_with_types()
