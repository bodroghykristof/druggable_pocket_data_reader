from service import data_reader_service
from service import amino_acid_array_processor_service

investigated_radius = 100
repeat_number = 1200


def main():
    # data_reader_service.read_data()
    amino_acid_array_processor_service.process_amino_acid_arrays()
    # limit_test(1201)


def limit_test(snapshot):
    lower_index = max(snapshot - investigated_radius, ((snapshot - 1) // repeat_number) * repeat_number + 1)
    higher_index = min(snapshot + investigated_radius, (((snapshot - 1) // repeat_number + 1) * repeat_number))
    print('LOWER: ' + str(lower_index))
    print('UPPER: ' + str(higher_index))


if __name__ == '__main__':
    main()
