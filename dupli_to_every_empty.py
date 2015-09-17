#blender script
#
#By James Sherratt
#
#duplicates and transforms the selected object to every empty, and deletes all the empties
#This script is a useful tool when making supertuxkart tracks.
#
#e.g. you can generate a particle system with empties, then convert it into multiple empties,
#then replace the empties with a linked object using this script. Making a particle system
#from a linked object, then converting the system to multiple objects will create brand 
#new objects, not linked objects. This will make the stk track considerably less efficient
#
#needed improvements: gui, tidying up, increase efficiency
#
#This code licensed is under the MIT license.

import bpy

def deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select = False

#get the reference value of the selected object
def find_obj_ref():
    for ref in range(0, (len(bpy.data.objects) - 1)):
        if bpy.data.objects[ref] == bpy.context.object:
            return ref

#find the value of the selected object in the list of objects: bpy.data.objects
def select(obj_ref):
    bpy.context.scene.objects.active = bpy.data.objects[obj_ref]
    bpy.data.objects[obj_ref].select = True

#duplicate the objects
dupli_obj_val = find_obj_ref()
for empty in bpy.data.objects:
    if empty.type == "EMPTY":
        bpy.ops.object.duplicate(linked = True)
        bpy.context.object.matrix_world  = empty.matrix_world
        deselect_all()
        empty.select = True
        bpy.ops.object.delete()
        select(dupli_obj_val)