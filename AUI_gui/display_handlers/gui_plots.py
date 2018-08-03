"""
general plots for matplotlib gui
"""
################
# imports of Scientific libraries and others

import  numpy           as      np
from    numpy           import  sin       # for better later code readability
from    numpy           import  cos       # for better later code readability
from    math            import  sqrt
from    random          import  randint

import  matplotlib.pyplot       as      plt
from    mpl_toolkits.mplot3d    import  Axes3D
from    matplotlib.patches      import  FancyArrowPatch, Circle, Rectangle
import  mpl_toolkits.mplot3d.art3d as   art3d
from    mpl_toolkits.mplot3d    import  proj3d

##################################

def plot_quad_system_geometry(stateSolMat, timeStep):
    '''
    stateSol is the state vector of the payload, for each time step
    X=x xDot y yDot theta thetaDot
    ax is the returned figure axis
    '''
    stateSol = stateSolMat[timeStep]
    # Figure #1
    fig = plt.figure(figsize=(13, 8))
    ax  = fig.gca()
    # ax.axis todo: set limits to axes so they are bigger then expected geometry

    ax.scatter(stateSol[0], stateSol[2], s=20, c='b') #stateSol[:,0]
    print (stateSol[0], stateSol[2])

    # # LumpedMass payload
    # lumpedPayload = Circle((stateSol[0,0], stateSol[0,0]), 13)
    # Circle.set_color(lumpedPayload, '0.75')
    # Circle.set_alpha(lumpedPayload, 0.1)
    # ax.add_patch(lumpedPayload)
    # print stateSol[0,0]

    # rectangular payload
    payloadW=1.2
    payloadH=0.1
    rectPayload = Rectangle((stateSol[0], stateSol[2]), payloadW, payloadH)
    Rectangle.set_color(rectPayload, '0.75')
    Rectangle.set_alpha(rectPayload, 0.71)   #1-opac 0-transparent
    ax.add_patch(rectPayload)

    return ax 

def axAddStars(ax):
    '''
    ax is a given figure axis, to add stars-likes, to it. in 2D.
    '''
    # Some stars (real stars should *NOT* move so quickly!)
#    ax.set_`
#    ax.set_axis_bgcolor('#060A49')
    for k in range(50):
        fact = 1
        rangeX = 15
        rangeY = 25
        X = randint(-rangeX * fact , rangeX * fact)
        Y = randint(-rangeY * fact * 2, rangeY * fact * 2)
        # Z = randint(-500000 * 2, 4000000 * 2)
        ax.scatter(X, Y, s=0.1, marker='x', c='white')

def plot_Phase_Space(x, xDot, xLb='', xDtLb='', title = 'Phase-Space plot'):
    '''
    main inputs:
    x
    xDot
    returns:
    fig - as new figure
    '''
    # 2nd Figure - phase plot
    fig = plt.figure(figsize=(13, 8))
    ax  = fig.gca()
    ax.scatter(x, xDot, s=20, c='y')
    plt.xlabel(xLb)
    plt.ylabel(xDtLb)
    plt.title(title)
    # title
    # axes

    return fig

def plot_Var_Vs_Time(y,t, displayParams=None, fig=None):
    '''
    https://matplotlib.org/2.0.2/api/lines_api.html
    main inputs:
    t - the time vector (for x-axis)
    y - the variable
    displayParams : dictionary of several parameters. if empty - stays with defauls
    fig : can add to given figure
    returns:
    fig - as new figure
    '''
    #defaults:
    lgndStr  = 'y var'
    title    = 'Var vs Time'
    xLabel   = 'time [sec]'
    yLabel   = 'y var'
    alpha    = 1
    lineStyle = '-'
    lineColor = 'r'
    #change from defaults:
    if displayParams!=None:
        if displayParams['lgndStr']!='':
            lgndStr = displayParams['lgndStr']
        if displayParams['title']!='':
            title   = displayParams['title']
        if displayParams['x-label']!='':
            xLabel  = displayParams['x-label']
        if displayParams['y-label']!='':
            yLabel  = displayParams['y-label']
        if displayParams['alpha']!='':
            alpha  = displayParams['alpha']
        if displayParams['lineStyle']!='':
            lineStyle = displayParams['lineStyle'] 
        if displayParams['lineColor']!='':
            lineColor = displayParams['lineColor'] 
        
    #3rd figure
    if fig==None:
        fig = plt.figure(figsize=(13, 8))
    ax = fig.gca()
#    plt.plot(t, y, 'g', label=lgndStr)  # todo: allow optional color
    plt.plot(t, y,ls=lineStyle, color=lineColor, alpha=alpha ,label=lgndStr)
    plt.legend(loc='best')
    plt.xlabel(xLabel) 
    plt.ylabel(yLabel)
    plt.title(title)
    plt.grid()

    return fig

def show_the_constructed_plots():
    plt.show()
    
    
def close_the_opened_plots(fig=None):
    if fig==None:
        plt.close("all")
    else:
        plt.close(fig)


# # Spaceship's orbit
# for k in range(10, len(x), 2270):
#     i = (k - 10) // 2270
#
#     ax.view_init(elev=i / 5, azim=i / 2)
#     ax.set_axis_off()
#     ax.set_xlim(0, 4 * 10 ** 8)
#     ax.set_ylim(-0.5 * 10 ** 8, 3 * 10 ** 8)
#     ax.set_zlim(-500000, 4000000)
#
#     # Moon
#     moon = ax.scatter(x[k], y[k], z[k], s=200, c='gray', marker='o')
#     ax.plot(x[:k], y[:k], z[:k], 'gray', linestyle='dashed', linewidth=0.4)
#
#     # Spaceship
#     spaceship = ax.scatter(a[k], b[k], c[k], s=50, c='red', marker='+')
#     ax.plot(a[:k], b[:k], c[:k], color='red', linestyle='dotted', linewidth=0.2)
#     if i < 10:
#         plt.savefig('animation_three_body/img00' + str(i) + '.png')
#     elif i < 100:
#         plt.savefig('animation_three_body/img0' + str(i) + '.png')
#     else:
#         plt.savefig('animation_three_body/img' + str(i) + '.png')
#     moon.remove()
#     spaceship.remove()

# pointMass = ax.scatter(currentLoc)
# show()
# pointMass.remove()

if __name__=='__main__':
    ax = plot_quad_system_geometry([[0,1,2,3,4,5]], 0)
    axAddStars(ax)
    show_the_constructed_plots()
else:
    # print __name__
    pass