# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/yuriy_tudgin_blender_electron_cloud

import os
import re
from .bpy_plus.file_system import Path
import bpy


class ElectronCloud:

    @classmethod
    def create_cloud(cls, context) -> None:
        # create electron cloud from files
        # read files
        for root, dirs, files in os.walk(
                Path.abs(path=context.scene.electron_cloud_props.src_files_path)):
            for file in files:
                if file.endswith('.txt') or file.endswith('.dat'):
                    # process [.txt, .dat] files
                    print('Processing file:', file)
                    # src and dest paths
                    src_file_path = os.path.join(root, file)
                    dest_file_dir = Path.abs(path=context.scene.electron_cloud_props.dest_files_path)
                    if not os.path.exists(path=dest_file_dir):
                        os.makedirs(dest_file_dir)
                    dest_file_path = os.path.join(
                        dest_file_dir,
                        os.path.splitext(file)[0] + '.blend'
                    )
                    # clear all scene
                    cls.clear_scene(context=context)
                    # create mesh
                    cls.create_cloud_mesh_from_file(
                        context=context,
                        path=src_file_path
                    )
                    # save to file
                    bpy.ops.wm.save_as_mainfile(
                        filepath=dest_file_path,
                        copy=True
                    )

    @classmethod
    def create_cloud_mesh_from_file(cls, context, path: str) -> None:
        # create mesh with points cloud from file
        vertices = []
        i = 0
        # read file
        with open(file=path, mode='r', encoding='UTF-8') as file:
            while line := file.readline():
                i += 1
                line = line.strip()
                vertices_so_str = re.split('\\s+', line, re.UNICODE)
                vertices_co = tuple((float(v) for v in vertices_so_str[:3]))
                vertices.append(vertices_co)
        # create mesh
        if vertices:
            cloud_object = cls.create_mesh(
                context=context,
                vertices=vertices
            )
            if cloud_object and context.scene.electron_cloud_props.duplivert_icosphere:
                # duplivert by icosphere
                bpy.ops.mesh.primitive_ico_sphere_add(
                    subdivisions=1,
                    radius=0.1,
                    calc_uvs=False,
                    location=(0, 0, 0)
                )
                icosphere = next((obj for obj in context.blend_data.objects if obj.name == 'Icosphere'), None)
                if icosphere:
                    icosphere.parent = cloud_object
                    icosphere.hide_set(True)
                    cloud_object.instance_type = 'VERTS'
            # cloud object is active and selected
            context.view_layer.objects.active = cloud_object
            cloud_object.select_set(True)

    @staticmethod
    def create_mesh(context, vertices: [list, tuple]):
        # create mesh
        # vertices = [(0.0, 0.0, 0.0), ...]
        edges = []
        faces = []
        new_mesh = context.blend_data.meshes.new('points_cloud')
        new_mesh.from_pydata(vertices, edges, faces)
        new_mesh.update()
        # make object from mesh
        new_object = context.blend_data.objects.new('points_cloud', new_mesh)
        # add object to scene collection
        context.collection.objects.link(new_object)
        return new_object

    @staticmethod
    def clear_scene(context) -> None:
        # clear scene
        for obj in context.blend_data.objects:
            context.blend_data.objects.remove(obj, do_unlink=True)
