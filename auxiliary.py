# Generates the Transformation Matrix for a Point
#   coord: The (x,y,z) point to transform
#   angle: The (a,b,c) angle to transform by
def shear_trans(coord=(0,0,0),angle=(0,0,0)):
    rot_x = np.array([[1,0,0],
                      [0,cos(angle[0]), sin(angle[0])],
                      [0,-sin(angle[0]),cos(angle[0])]],
                    dtype='float32')
    rot_y = np.array([[cos(angle[1]), 0, sin(angle[1])],
                      [0, 1, 0],
                      [-sin(angle[1]), 0, cos(angle[1])]],
                    dtype='float32')
    rot_z = np.array([[cos(angle[2]), -sin(angle[2]), 0],
                      [sin(angle[2]), cos(angle[2]), 0],
                      [0, 0, 1]],
                    dtype='float32')

    return np.dot(rot_x, rot_y, rot_z)

# Generates Points for Polygons of Specified Features
#   sides: Number of sides of polygon [default:3]
#   coord: Center of the polygon  
#   angle: Angle to rotate about center
#   scale: Value to magnify the polygon
#   shear: 3d Rotation to apply to polygon
def poly_gen(sides = 3,coord = (0,0), angle = 0, scale = 1, shear = (0,0,0)):
    p,x,y = [], *coord
    
    #Loop Through and Create All Verticies
    for s in range(sides):
        p.append( ( cos(s * 2 * pi / sides + angle) + x, sin(s * 2 * pi / sides + angle) + y))
        
    # Perform Shear Transform
    p = map(lambda q: np.dot(shear_trans((0,0,0), shear), np.array([*q,0]).T), p)
    p = list(map(lambda q: tuple(scale * (1 +  q.T[:-1] + np.array([x,y]))), p))
    
    return p
