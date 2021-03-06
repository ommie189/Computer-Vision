import numpy as np


def conv_nested(image, kernel):
    """A naive implementation of convolution filter.

    This is a naive implementation of convolution using 4 nested for-loops.
    This function computes convolution of an image with a kernel and outputs
    the result that has the same shape as the input image.

    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk).

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))#an array of zeros with shape and type of input

    ### YOUR CODE HERE
    pass
    for m in range(Hi):    #row
        for n in range(Wi):#column
            sum=0          #sum of pixel values
            for i in range(Hk):
                for j in range(Wk):
                    if m+1-i<0 or n+1-j <0 or m+1-i>=Hi or n+1-j>= Wi:
                     sum+=0
                    else:
                        sum+=image[m+1-i, n+1-j]*kernel[i,j]#formula
            out[m,n]=sum #(f*h)[m,n]
    ### END YOUR CODE

    return out

def zero_pad(image, pad_height, pad_width):#
    """ Zero-pad an image.

    Ex: a 1x1 image [[1]] with pad_height = 1, pad_width = 2 becomes:

        [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]         of shape (3, 5)

    Args:
        image: numpy array of shape (H, W).
        pad_width: width of the zero padding (left and right padding).
        pad_height: height of the zero padding (bottom and top padding).

    Returns:
        out: numpy array of shape (H+2*pad_height, W+2*pad_width).
    """

    H, W = image.shape
    out = None

    ### YOUR CODE HERE
    pass
    #pad with constant value 0
    out=np.pad(image, ((pad_height, pad_height),(pad_width, pad_width)), 'constant', constant_values=0)
    ### END YOUR CODE
    return out


def conv_fast(image, kernel):
    """ An efficient implementation of convolution filter.

    This function uses element-wise multiplication and np.sum()
    to efficiently compute weighted sum of neighborhood at each
    pixel.

    Hints:
        - Use the zero_pad function you implemented above
        - There should be two nested for-loops
        - You may find np.flip() and np.sum() useful

    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk).

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    ### YOUR CODE HERE
    pass
    #fill with zeros
    image = zero_pad(image, Hk//2, Wk//2)

    #flip the kernel horizontally and vertically
    kernel =np.flip(kernel, 0)
    kernel =np.flip(kernel, 1)

    #weighted sum of the neighbourhood at each pixel
    for m in range(Hi):
        for n in range(Wi):
            out[m,n]= np.sum(image[m:m+Hk, n:n+Wk]* kernel)
    ### END YOUR CODE

    return out

def conv_faster(image, kernel):
    """
    Args:
        image: numpy array of shape (Hi, Wi).
        kernel: numpy array of shape (Hk, Wk).

    Returns:
        out: numpy array of shape (Hi, Wi).
    """
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    ### YOUR CODE HERE
    pass
    ### END YOUR CODE

    return out

def cross_correlation(f, g):
    """ Cross-correlation of f and g.

    Hint: use the conv_fast function defined above.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    pass
    g = np.flip(g,0)
    g = np.flip(g,1)
    out = conv_fast(f,g)
    ### END YOUR CODE

    return out

def zero_mean_cross_correlation(f, g):
    """ Zero-mean cross-correlation of f and g.

    Subtract the mean of g from g so that its mean becomes zero.

    Hint: you should look up useful numpy functions online for calculating the mean.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    pass
    g-=np.mean(g)
    out = cross_correlation(f,g)
    ### END YOUR CODE

    return out

def normalized_cross_correlation(f, g):
    """ Normalized cross-correlation of f and g.

    Normalize the subimage of f and the template g at each step
    before computing the weighted sum of the two.

    Hint: you should look up useful numpy functions online for calculating 
          the mean and standard deviation.

    Args:
        f: numpy array of shape (Hf, Wf).
        g: numpy array of shape (Hg, Wg).

    Returns:
        out: numpy array of shape (Hf, Wf).
    """

    out = None
    ### YOUR CODE HERE
    pass
    
    g = g[:-1, :]  # changing dimensions of g
    normalised_g = (g - np.mean(g)) / np.std(g)

    Hf, Wf = f.shape
    Hg, Wg = g.shape

    out = np.zeros((Hf, Wf))

    sub_Hg = Hg // 2
    sub_Wg = Wg // 2

    #using the math formula
    for i in range(sub_Hg, Hf - sub_Hg):
        for j in range(sub_Wg, Wf - sub_Wg):
            patch = f[i - sub_Hg:i + sub_Hg +1, j - sub_Wg:j + sub_Wg + 1]
            normalised_f = (patch -np.mean(patch))/np.std(patch)
            out[i, j] = np.sum(normalised_f *normalised_g) #weighted sum
    ### END YOUR CODE

    return out
