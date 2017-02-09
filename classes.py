import os
from mv import fd_types, unit
from . import properties

def get_file_name(path):
    file_name = os.path.basename(path)
    return os.path.splitext(file_name)[0]

class Decorative_Assembly(fd_types.Assembly):
    
    library_name = properties.LIBRARY_FOLDER_NAME
    type_assembly = "PRODUCT"
    drop_id = properties.LIBRARY_NAME_SPACE + ".place_decorative_assembly"
    
    """ Path to blend file that contains a group of the appliance """
    assembly_path = ""
    
    def draw(self):
        self.create_assembly()
        assembly = self.add_assembly(file_path = self.assembly_path)
        assembly.set_name(get_file_name(self.assembly_path))
        assembly.obj_x.location.x = 0
        assembly.obj_y.location.y = 0
        assembly.obj_z.location.z = 0
        self.width = assembly.obj_x.location.x
        self.height = assembly.obj_z.location.z
        self.depth = assembly.obj_y.location.y