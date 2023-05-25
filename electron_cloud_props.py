# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_blender_electron_cloud

from bpy.types import PropertyGroup, Scene
from bpy.props import BoolProperty, PointerProperty, StringProperty
from bpy.utils import register_class, unregister_class


class ElectronCloudProps(PropertyGroup):
    # properties
    src_files_path: StringProperty(
        name='Source files:',
        default='//src_files/',
        subtype='DIR_PATH'
    )
    dest_files_path: StringProperty(
        name='Dest files:',
        default='//dest_files/',
        subtype='DIR_PATH'
    )
    duplivert_icosphere: BoolProperty(
        name='Duplivert by ICO-Sphere',
        default=True
    )


def register():
    register_class(ElectronCloudProps)
    Scene.electron_cloud_props = PointerProperty(type=ElectronCloudProps)


def unregister():
    del Scene.electron_cloud_props
    unregister_class(ElectronCloudProps)
