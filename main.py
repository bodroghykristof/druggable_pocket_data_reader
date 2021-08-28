"""Main entry point of the application."""


from service.amino_acid_array_processor import amino_acid_array_processor_service
from service.data_reader import data_reader_service


def main():
    """Placeholder for running one of the 2 modules ot the applicaiton."""

    #####################################
    # ENTRY POINT OF DATA READER MODULE #
    #####################################
    data_reader_service.read_data()

    ####################################################
    # ENTRY POINT OF AMINO ACID ARRAY PROCESSOR MODULE #
    ####################################################
    amino_acid_array_processor_service.process_amino_acid_arrays()


if __name__ == '__main__':
    main()
