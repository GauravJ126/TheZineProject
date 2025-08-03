from libs.FileHandler import Computer

if __name__ == "__main__":
    computer = Computer()

    input = "Inputs/input.json"
    structure = computer.read_json(input)
    output = computer.create_book(structure)
    #
    # obj.export_output_as_pdf(output)

