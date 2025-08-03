import os
import json
import svgwrite

class Computer:
    def __init__(self):
        self._file = None
        self._templates = self.read_json("libs/templates/types.json")

    def read_json(self, file_path = None):
        """Input wil be the file in the Inputs folder, input will be in JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"[ERROR] File not found: {file_path}")
        except json.JSONDecodeError as e:
            print(f"[ERROR] Failed to decode JSON: {e}")
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred: {e}")

    def write_svg(self):
        """Basically to finally generate the SVG to be able to print"""
        # write code to make SVG
        pass

    def add_component_into_svg(self,type,x_coordinate,y_coordinate):
        """"Add componentes to the svg as we go along the json,
            using the type and also the calculated x and y coordinates
            types == It is acquired by the code to be able to identify the type of component being added into the svg,
                    (Json in the componentes folder)"""
        pass

    def create_book(self,structure):
        page_type = structure["Page_Type"]

        for element,element_properties in structure.items():
            if element == "Page_Type":
                width, height = self._templates.get(page_type)["width"], self._templates.get(page_type)["height"]
            if element == "Start":
                pass
                        
            if element == "End":
                pass

        """Call all the needed function within the Class to make the book"""

    def export_output_as_pdf(self, output,output_location):
        """ This will take a string and write it to a file
        and export the file as a pdf to be printable"""
        pass
