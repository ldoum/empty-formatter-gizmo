import bpy

C=bpy.context
D=bpy.data

class GroupOfProperties(bpy.types.PropertyGroup):
    PropertyName: bpy.props.EnumProperty(
                    name="placeholder",
                    items=[
                            ('PLAIN_AXES', 'Plain axes', 'Description 1'),
                            ('ARROWS', 'Arrows', 'Description 2'),    
                            ('SINGLE_ARROW', 'Single arrow', 'Description 3'),
                            ('CIRCLE', 'Circle', 'Description 4'),
                            ('CUBE', 'Cube', 'Description 5'),    
                            ('SPHERE', 'Sphere', 'Description 6'),
                           ],
                    description="Description that shows in blender tooltips"
    )
    
    Size: bpy.props.FloatProperty(
                    name="Size",
                    description="Description that shows in blender tooltips",
                    default=1.0,
                    min=0.01,
                    max=100.0
    )

class MyClassName(bpy.types.Operator):
    bl_idname = "my_operator.my_class_name"
    bl_label = "My Class Name"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        reference = context.scene.instance

        #collect all objects and filter for empties
        all_empties = [empty for empty in C.selected_objects if empty.type == 'EMPTY']

        #check if empty is the exact type selected
        for e in all_empties:
            if e.empty_display_type != reference.PropertyName:
                print("Item named {} turned into an arrow.".format(e.name))
                e.empty_display_type = reference.PropertyName
                
            else:
                print("Item named {} is an arrow already.".format(e.name))
            
            #apply size in the meantime    
            e.empty_display_size = reference.Size
            print("Size of {} is now {}".format(e.name, reference.Size))
            
        return {"FINISHED"}


class PanelClassName(bpy.types.Panel):
    bl_idname = "panelname"
    bl_label = "Empty Formatter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    @classmethod
    def poll(cls,context):
        return context.selected_objects

    def draw(self, context):
        layout = self.layout
        inst = context.scene.instance
        layout.prop(inst,"Size")
        layout.prop(inst,"PropertyName")
        layout.operator("my_operator.my_class_name",text="Apply")
         ### design your panel here ###

classes = [GroupOfProperties, MyClassName, PanelClassName]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.instance = bpy.props.PointerProperty(type=GroupOfProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.register_class(cls)
    del bpy.types.Scene.instance

if __name__ == "__main__":
    register()        
