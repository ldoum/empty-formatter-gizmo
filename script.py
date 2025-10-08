import bpy

C=bpy.context
D=bpy.data


all_empties = [empty for empty in C.selected_objects if empty.type == 'EMPTY']

empty_type = ['PLAIN_AXES' , 'ARROWS' ,'SINGLE_ARROW' , 'CIRCLE' , 'CUBE' , 'SPHERE' ]

find = 1  #replace with dropdown.

for e in all_empties:
    
    print("Item named {} is an empty.".format(e.name))
        
    if e.empty_display_type != empty_type[find]:
        print("Item named {} turned into an arrow.".format(e.name))
        e.empty_display_type = empty_type[find]
    else:
        print("Item named {} is an arrow already.".format(e.name))
