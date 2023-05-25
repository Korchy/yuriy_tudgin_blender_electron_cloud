# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_blender_electron_cloud

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class ELECTRON_CLOUD_PT_panel(Panel):
    bl_idname = 'ELECTRON_CLOUD_PT_panel'
    bl_label = 'electron_cloud'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'electron_cloud'

    def draw(self, context):
        layout = self.layout
        layout.prop(
            data=context.scene.electron_cloud_props,
            property='src_files_path'
        )
        layout.prop(
            data=context.scene.electron_cloud_props,
            property='dest_files_path'
        )
        layout.prop(
            data=context.scene.electron_cloud_props,
            property='duplivert_icosphere'
        )
        layout.operator(
            operator='electron_cloud.create_cloud',
            icon='POINTCLOUD_DATA',
            text='Create Electron cloud'
        )


def register():
    register_class(ELECTRON_CLOUD_PT_panel)


def unregister():
    unregister_class(ELECTRON_CLOUD_PT_panel)
