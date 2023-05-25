# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_blender_electron_cloud

from . import electron_cloud_ops
from . import electron_cloud_ui
from . import electron_cloud_props
from .addon import Addon


bl_info = {
    'name': 'electron_cloud',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (3, 5, 0),
    'location': '3D Viewport - N-panel - Electron cloud',
    'doc_url': 'https://github.com/Korchy/yuriy_tudgin_blender_electron_cloud',
    'tracker_url': 'https://github.com/Korchy/yuriy_tudgin_blender_electron_cloud',
    'description': 'Create mesh from points cloud from file'
}


def register():
    if not Addon.dev_mode():
        electron_cloud_props.register()
        electron_cloud_ops.register()
        electron_cloud_ui.register()
    else:
        print('It seems you are trying to use the dev version of the '
              + bl_info['name']
              + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        electron_cloud_ui.unregister()
        electron_cloud_ops.unregister()
        electron_cloud_props.unregister()


if __name__ == '__main__':
    register()
