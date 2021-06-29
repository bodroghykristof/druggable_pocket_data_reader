from service import data_reader_service
from service import amino_acid_array_processor_service


def main():
    # data_reader_service.read_data()
    amino_acid_array_processor_service.process_amino_acid_arrays()


if __name__ == '__main__':
    main()
