import binvox_rw

with open('chair.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
print(model.dims)
print(model.scale)
print(model.translate)
print(model.data)
