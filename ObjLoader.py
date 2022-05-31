import numpy as np


class ObjLoader:
    buffer = []

    @staticmethod
    def search_data(data_values, coordinates, skip, data_type):
        for d in data_values:
            if d == skip:
                continue
            if data_type == 'float':
                coordinates.append(float(d))
            elif data_type == 'int':
                coordinates.append(int(d)-1)




    @staticmethod # TODO unsorted vertex buffer for use with glDrawElements function
    def create_unsorted_vertex_buffer(indices_data, vertices, textures, normals):
        num_verts = len(vertices) // 3

        for i1 in range(num_verts):
            start = i1 * 3
            end = start + 3
            ObjLoader.buffer.extend(vertices[start:end])

            for i2, data in enumerate(indices_data):
                if i2 % 3 == 0 and data == i1:
                    start = indices_data[i2 + 1] * 2
                    end = start + 2
                    ObjLoader.buffer.extend(textures[start:end])

                    start = indices_data[i2 + 2] * 3
                    end = start + 3
                    ObjLoader.buffer.extend(normals[start:end])

                    break



        if sorted:
            # use with glDrawArrays
            ObjLoader.create_sorted_vertex_buffer(all_indices, vert_coords, tex_coords, norm_coords)
        else:
            # use with glDrawElements
            ObjLoader.create_unsorted_vertex_buffer(all_indices, vert_coords, tex_coords, norm_coords)

        # ObjLoader.show_buffer_data(ObjLoader.buffer)

        buffer = ObjLoader.buffer.copy() # create a local copy of the buffer list, otherwise it will overwrite the static field buffer
        ObjLoader.buffer = [] # after copy, make sure to set it back to an empty list

        return np.array(indices, dtype='uint32'), np.array(buffer, dtype='float32')

