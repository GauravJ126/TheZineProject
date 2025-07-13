import json
# Have to find a SVG library for handling SVG elements
class Computer:
    def __init__(self):
        self._file = None

    def compute_layout(self,inputs):
        """This should compute the layout of the Zine based on the Json Input"""
        pass

    def compute_component_position(self,inputs):
        """This should compute the placements of the component of the Zine based on the Json Input and the layout"""
        pass

    def read_json(self, input = None):
        """Input wil be the file in the Inputs folder, input will be in JSON"""
        # write code to read a json file
        self.compute_layout(input)
        self.compute_component_position(input)
        pass

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

