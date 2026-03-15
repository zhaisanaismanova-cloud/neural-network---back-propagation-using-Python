import numpy as np
import matplotlib.pylab as plt

def main():
    
    l = [32,54,22,76,2]
    print(type(l))

    a = np.array(l)
    print(type(a))
    try:
        b = np.array(['ala ma kota'])
        print('{} {}'.format(b, type(b)))
    except Exception as e:
        print(e)
    print('Type a = {}'.format(a.dtype.name))
    print('Dim a = {}'.format(a.shape))
    print('Type b = {}'.format(b.dtype.name))
    print('Dim b = {}'.format(b.shape))

    c = np.array(l, dtype=np.float64)
    
    print('Type c = {}'.format(c.dtype.name))
    print('Dim c = {}'.format(c.shape))
    try:
        d = np.array(['ala ma kota'], dtype=np.float64)
        print('{} {}'.format(d, type(d)))
    except Exception as e:
        print(e)
        
    d = np.array([[1.5,2,3], [4,5,6]], np.float64)
    print('Type d = {}'.format(d.dtype.name))
    print('Dim d = {}'.format(d.shape))

    e = np.arange(6)
    print(e)
    
    e = e.reshape(3, 2)
    print(e)
    f = e.reshape(2, 3)
    print(f)
    
    print(d + f)  
    print(d * f)  
    print(e @ d)  

    np.zeros((2, 3))  
    np.linspace(1., 4., 6) 
    np.identity(3)

    g = np.transpose(f)
    g = f.T
    print('Transposed Matrix g= ')
    print(g)


    h = np.linalg.inv(f@np.transpose(f))
    print('Type h = {}'.format(h.dtype.name))
    print('Dim h = {}'.format(h.shape))

if __name__ == '__main__':
    main()