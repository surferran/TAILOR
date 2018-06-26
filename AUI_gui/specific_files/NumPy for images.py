"""
from 
http://scikit-image.org/docs/stable/user_guide/numpy_images.html
""" 
 
import sys
if __name__=='__main__':
    # trial for images (later check ffmpeg)
    from skimage import data
    from skimage.io import imread, imread_collection#, get_reader
    import matplotlib.pyplot as plt
#    %matplotlib wx  %inline

#    import imageop
#    reader = imageio.get_reader('<video0>')
#    plt.imshow(reader)
    
    

    camera = data.camera()
    print type(camera)
    print camera.shape
    print camera.size
    print camera.min(), camera.max()
    print camera.mean()
    
    # Get the value of the pixel on the 10th row and 20th column
    print camera[10, 20]
    """
    Be careful: in NumPy indexing, the first dimension (camera.shape[0]) 
    corresponds to rows, while the second (camera.shape[1]) corresponds to 
    columns, with the origin (camera[0, 0]) on the top-left corner. 
    This matches matrix/linear algebra notation, but is in contrast to 
    Cartesian (x, y) coordinates.
    """

    # Set to black the pixel on the 3rd row and 10th column
    camera[3, 10] = 0
        
    fig = plt.figure()
    
    
    cat = data.chelsea()
    print type(cat)
    print cat.shape 
    print cat[10, 20]

    # set the pixel at row 50, column 60 to black
    cat[50, 60] = 0
    # set the pixel at row 50, column 61 to green
    cat[50, 61] = [0, 255, 0] # [red, green, blue]
    
    # Using a 2D mask on a 2D color image

    cat = data.chelsea()
    cat = data.imread('cartoon-funny-dinosaur.jpg')
    cat = imread_collection('*.jpg')
    print len(cat)
    reddish = cat[0][:, :, 0] > 160
    cat[0][reddish] = [0, 255, 0]
    plt.imshow(cat[0])
    for img in cat:
        plt.figure()
        plt.imshow(img)

#    sys.exit(0)
    num=1
    
    print ('image #{}'.format(num))
           
           
#####
import skimage.io as io
from skimage import data_dir
coll = io.ImageCollection(data_dir + '/chess*.png')
len(coll)
coll[0].shape
ic = io.ImageCollection('/tmp/work/*.png:/tmp/other/*.jpg')

#############

from skimage import viewer
import numpy as np
coins = data.coins()

new_viewer = viewer.ImageViewer(coins) 
new_viewer.show()

new_viewer = viewer.ImageViewer(coins) 
from skimage.viewer.plugins import lineprofile
new_viewer += lineprofile.LineProfile() 
new_viewer.show() 

check = np.zeros((9, 9))
check[::2, 1::2] = 1
check[1::2, ::2] = 1
plt.matshow(check, cmap='gray')
plt.show()

from skimage import exposure
camera = data.camera()
camera_equalized = exposure.equalize_hist(camera)

plt.figure(figsize=(7, 3))

plt.subplot(121)
plt.imshow(camera, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(122)
plt.imshow(camera_equalized, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.tight_layout()
plt.show()

           
sys.exit()           
    
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

FLOOR = -10
CEILING = 10

class AnimatedScatter(object):
    def __init__(self, numpoints=5):
        self.numpoints = numpoints
        self.stream = self.data_stream()
        self.angle = 0

        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('draw_event',self.forceUpdate)
        self.ax = self.fig.add_subplot(111,projection = '3d')
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100, 
                                       init_func=self.setup_plot, frames=20)

    def change_angle(self):
        self.angle = (self.angle + 1)%360

    def forceUpdate(self, event):
        self.scat.changed()

    def setup_plot(self):
        X = next(self.stream)
        c = ['b', 'r', 'g', 'y', 'm']
        self.scat = self.ax.scatter(X[:,0], X[:,1], X[:,2] , c=c, s=200)

        self.ax.set_xlim3d(FLOOR, CEILING)
        self.ax.set_ylim3d(FLOOR, CEILING)
        self.ax.set_zlim3d(FLOOR, CEILING)

        return self.scat,

    def data_stream(self):
        data = np.zeros(( self.numpoints , 3 ))
        xyz = data[:,:3]
        while True:
            xyz += 2 * (np.random.random(( self.numpoints,3)) - 0.5)
            yield data

    def update(self, i):
        data = next(self.stream)
        self.scat._offsets3d = ( np.ma.ravel(data[:,0]) , np.ma.ravel(data[:,1]) , np.ma.ravel(data[:,2]) )
        return self.scat,

    def show(self):
        plt.show()

if __name__ == '__main__':
    a = AnimatedScatter()
    a.ani.save("movie.avi", codec='avi')
    a.show()
