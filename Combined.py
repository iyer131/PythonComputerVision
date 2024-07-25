import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

def ssd(I, T):
    
    I_w = I.shape[1] #grabs width of matrix I(width of source image)
    T_w = T.shape[1] #grabs width of matrix T(width of template image)
    I_h = I.shape[0] #grabs height of matrix I(height of source image)
    T_h = T.shape[0] #grabs height of matrix T(height of template image)

    #instantiates matrix R(output matrix). as the sliding of template over source will be by the top left corner of the template,
    #we subtract the width and height of template from dimensions
    R = np.empty((I_h-T_h+1,I_w-T_w+1)) 



    #iterating through R. define each element value
    for row in range(R.shape[0]):
        for col in range(R.shape[1]):

            #defining slice of I(size of template)
            I_matrix = I[row:row+T_h, col:col+T_w]  

            #subtract T from I
            subtracted_mat = I_matrix - T

            #squares subtracted matrix
            numer_term = subtracted_mat**2

            #sums numer_term values and assigns to element value of output matrix R
            R[row,col] = numer_term.sum()

        

    #PRINTING MIN VAL AND POINTS


    indices = np.where(R == np.amin(R)) #finds indices of min val in matrix R
    
    plt.imshow(R, cmap='gray')

    return indices[1][0], indices[0][0] #returns indices

def corr_coeff(I,T):

    I_w = I.shape[1] #grabs width of matrix I(width of source image)
    T_w = T.shape[1] #grabs width of matrix T(width of template image)
    I_h = I.shape[0] #grabs height of matrix I(height of source image)
    T_h = T.shape[0] #grabs height of matrix T(height of template image)

    #creates T_prime matrix. Follows equation provided in prompt
    T_mean =  np.full((T_h, T_w), T.mean())
    T_prime = T - T_mean 

    #instantiates I_prime: contains all mean values for I slices
    I_prime = np.empty((I_h,I_w))

    #instantiates output matrix R
    R = np.empty((I_h-T_h+1,I_w-T_w+1))

    #iterates through all elts of I_prime(also has size of R)
    for row in range(R.shape[0]):
        for col in range(R.shape[1]):
            I_matrix = I[row:row+T_h, col:col+T_w] #grabs slice of I(source) that is of slice T(template)
            I_prime[row,col] = I_matrix.mean() #calculates mean of I_matrix slice and inputs at element

    #iterates through all elts of R(output matrix)
    for row in range(R.shape[0]):
        for col in range(R.shape[1]):


            I_matrix = I[row:row+T_h, col:col+T_w] #grabs slice of I(source) that is of slice T(template)

            I_mean = np.full((T_h, T_w), I_prime[row,col]) #creates matrix size of T with all values being I_prime mean
            I_prime_subtract = I_matrix - I_mean #subtracts matrix of means from I_prime slice(formula provided in prompt)

            R[row,col] = np.sum(I_prime_subtract*T_prime) #multiplies(as per formula) and assigns to elt of R



    #FIND LARGEST NUMBER    
    indices = np.where(R == np.amax(R)) #finds indices of max val in matrix R
    plt.imshow(R, cmap='gray')
    return indices[1][0], indices[0][0] #returns indices
def norm_cross_correlation(I, T):
    I_w = I.shape[1]
    T_w = T.shape[1]
    I_h = I.shape[0]
    T_h = T.shape[0]
    R = np.empty((I_h-T_h+1,I_w-T_w+1))

    for row in range(I_h-T_h+1):
        for col in range(I_w-T_w+1):
            I_matrix = I[row:row+T_h, col:col+T_w]

            num = np.sum(I_matrix * T)

            denom1 = np.sum(I_matrix**2)
            denom2 = float(np.sum(T**2))
            denom = np.sqrt( denom1*denom2 )
            

            R[row,col] = num/denom
            
    indices = np.where(R == np.amax(R)) #finds indices of max val in matrix R
    plt.imshow(R, cmap='gray')
    return indices[1][0], indices[0][0] #returns indices
def get_dims(img):
    return img.shape[0], img.shape[1]


def plot_pt_on_img(source, x_pt_loc, y_pt_loc): 
    #MAX VALUE IN MATRIX 571921.0
    #INDICES OF MAX VAL IN MATRIX (array([999], dtype=int64), array([1198], dtype=int64)) 
    plt.imshow(source, cmap='gray')

    plt.grid()
    plt.plot(x_pt_loc, y_pt_loc, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
    plt.show()
       
def put_box_around(sourcecolor, tuple_point, T_height, T_width):
    fig,ax = plt.subplots()
    plt.imshow(sourcecolor)
    plt.grid()
    rect = patches.Rectangle(tuple_point, T_width, T_height, linewidth=1, edgecolor='lime', facecolor='none')
    ax.add_patch(rect)
    plt.show()

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def grayscale(w):

    img = mpimg.imread(w)
    gray_img = img.astype(np.uint8)     
    gray = rgb2gray(gray_img)    
    return gray
       
def cropping(source,indices_ssd,w,h):
    
    y=indices_ssd[1]
 
    x=(indices_ssd[0])
 
   
    fig,ax = plt.subplots()
    plt.imshow(source)
    
    rect = patches.Rectangle((indices_ssd[0],indices_ssd[1]), w, h, linewidth=3, edgecolor='lime', facecolor='none')
    ax.add_patch(rect)
    
    ax.set_xlim(x-w,x+w+75)
    ax.set_ylim(y+h+75,y-h)
    
    plt.show()


def main():

    color=input("Input name of color image: ")
    template=input("Input name of template image: ")

    method=input("Enter the type of template matching you would like to use (SSD, CC, NCC): ")
  
    if method=="SSD":
        pass
    elif method=="CC":
        pass
    elif method=="NCC":
        pass
    else:
        print("Please input a valid template matching type")
        return
        
    sourcecolor = mpimg.imread(f'{color}')
    source = grayscale(f'{color}') 
    colored = mpimg.imread(f'{color}')
    waldo = grayscale(f"{template}")

    H, W = get_dims(source)
    h, w = get_dims(waldo)
    
    if method == "SSD":
      indices_ssd = ssd(source, waldo)
      put_box_around(sourcecolor, indices_ssd, h,w)
      cropping(colored,indices_ssd,w,h)
    elif method == "CC": 
      indices_corr_coeff = corr_coeff(source, waldo)
      put_box_around(sourcecolor, indices_corr_coeff, h,w)
      cropping(colored,indices_corr_coeff,w,h)
    else: 
      indices_norm_cross_correlation = norm_cross_correlation(source, waldo)
      put_box_around(sourcecolor, indices_norm_cross_correlation, h,w)
      cropping(colored,indices_norm_cross_correlation,w,h)
    
    
    
if __name__ == '__main__':
    main()