# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_blender_electron_cloud

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .electron_cloud import ElectronCloud


class ELECTRON_CLOUD_OT_create_cloud(Operator):
    bl_idname = 'electron_cloud.create_cloud'
    bl_label = 'Electron cloud: create cloud'
    bl_description = 'Electron cloud - create cloud operator'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ElectronCloud.create_cloud(
           context=context
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return True


def register():
    register_class(ELECTRON_CLOUD_OT_create_cloud)


def unregister():
    unregister_class(ELECTRON_CLOUD_OT_create_cloud)
