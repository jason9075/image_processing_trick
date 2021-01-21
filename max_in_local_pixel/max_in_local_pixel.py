import numpy as np
import scipy.ndimage as ndi


def main():
    input_array = np.random.randint(10, size=(10, 10))
    output_array = ndi.maximum_filter(input_array, size=3, mode='constant')
    output_array = np.logical_and(input_array == output_array, input_array > 0).astype(int)
    coord = output_array.nonzero()

    print(f'input:\n{input_array}')
    print(f'output:\n{output_array}')
    print(f'coord:\n{coord}')


if __name__ == '__main__':
    main()
