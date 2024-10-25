import bpy

obj = bpy.context.object;

if(obj.type == "MESH"):
    print(obj.name);
    mesh = obj.data;
    
    vertices = [[v.co.x, v.co.y, v.co.z] for v in mesh.vertices];
    print(vertices);
    
    edges = [[e.vertices[0], e.vertices[1]] for e in mesh.edges]
    print(edges);
    
    faces = [f.vertices[:] for f in mesh.polygons]
    print(faces);