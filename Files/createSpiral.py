import bpy
import math

diameter = 200;
growth = 5;
resolution = 50;
passes = (diameter/2) / growth;
offset = growth / resolution;
thickness = 0.2;

# Create a new mesh object (line)
#mesh = bpy.data.meshes.new(name="Line");
#line = bpy.data.objects.new("Line", mesh);

## Link the line object to the scene
#bpy.context.collection.objects.link(line);

bpy.ops.curve.simple(align='WORLD', 
    location=(0, 0, 0), 
    rotation=(1.5708, 0, 0), 
    Simple_Type='Rectangle', 
    Simple_width=thickness, 
    Simple_length=thickness, 
    use_cyclic_u=True
);

rect = bpy.context.object;

bpy.ops.curve.primitive_nurbs_path_add(
    enter_editmode=True, 
    align='WORLD', 
    location=(0, 0, 0), 
    scale=(1, 1, 1)
);

path = bpy.context.object;

#bpy.context.object.data.bevel_object = bpy.data.objects["Rectangle"]
bpy.context.object.data.bevel_object = rect;
bpy.ops.curve.delete(type='VERT');

#curveObj = bpy.context.active_object;
#curveData = curveObj.data;
#spline = curveData.splines[0];
#controlPoints = curveData.splines.active.points

points = [];
for p in range(int(resolution * passes)):
    i = p % resolution;
    angle = math.radians(360.0/resolution * i);
        
    radius = offset * p;
    x = math.cos(angle) * radius;
    y = math.sin(angle) * radius;

#    points.append((x, y, 0));
    bpy.ops.curve.vertex_add(location=(x, y, 0.0))
#    controlPoints[i].co = (x, y, 0, 1);

#edges = [(i, i + 1) for i in range(len(points) - 1)]

# Set the vertices and edges of the mesh
#mesh.from_pydata(points, edges, [])

#skin = line.modifiers.new(name="Skin", type="SKIN");
#solidify = line.modifiers.new(name="Solidify", type="SOLIDIFY");
#solidify.thickness = thickness;


# Update the scene to reflect the changes
#bpy.context.view_layer.update()
