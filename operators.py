"""
Microvellum 
Cabinet & Closet Designer
Stores the UI, Properties, and Operators for the cabinet and closet designer panel
the Panel definition is stored in an add-on.
"""

import bpy
import math
from os import path
from mv import fd_types, unit, utils
from bpy.app.handlers import persistent
from . import properties

class OPERATOR_Place_Decorative_Assembly(bpy.types.Operator):
    bl_idname = properties.LIBRARY_NAME_SPACE + ".place_decorative_assembly"
    bl_label = "Place Decorative Assembly"
    bl_description = "This allows you to place an decorative assembly into the scene."
    bl_options = {'UNDO'}
    
    #READONLY
    object_name = bpy.props.StringProperty(name="Object Name")
    
    object = None
    
    def invoke(self, context, event):
        self.object = bpy.data.objects[self.object_name]
        context.window.cursor_set('PAINT_BRUSH')
        context.scene.update() # THE SCENE MUST BE UPDATED FOR RAY CAST TO WORK
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel_drop(self,context,event):
        if self.object:
            utils.delete_object_and_children(self.object)
        bpy.context.window.cursor_set('DEFAULT')
        return {'FINISHED'}

    def faucet_drop(self,context,event):
        selected_point, selected_obj = utils.get_selection_point(context,event)
        bpy.ops.object.select_all(action='DESELECT')
        
        if selected_obj:
            wall_bp = utils.get_wall_bp(selected_obj)
            if wall_bp:
                self.object.rotation_euler.z = wall_bp.rotation_euler.z
                
        self.object.location = selected_point
        
        if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.object.draw_type = 'TEXTURED'
            bpy.context.window.cursor_set('DEFAULT')
            bpy.ops.object.select_all(action='DESELECT')
            utils.set_wireframe(self.object,False)
            context.scene.objects.active = self.object
            self.object.select = True
            return {'FINISHED'}
        
        return {'RUNNING_MODAL'}
    
    def modal(self, context, event):
        context.area.tag_redraw()
        
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}
        
        if event.type in {'ESC'}:
            self.cancel_drop(context,event)
            return {'FINISHED'}    
        
        return self.faucet_drop(context,event)

bpy.utils.register_class(OPERATOR_Place_Decorative_Assembly)
