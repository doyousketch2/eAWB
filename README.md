**awb.py**  
Enhanced **A**uto **W**hite **B**alance for GIMP

---
Enhanced, because you can specify the amount you wish to clip.  
4 seems to be a good amount, but you can set it higher or lower  
if you need more or less filtering.  

If you open your histogram and look at where the ranges are,  
you may notice an image has highlights, but no shadows.  

In this case, you can specify that you prefer it clip more from the shadows,  
and leave the highlights alone. Or vice-versa.  Your choice, it's enhanced.  

You can also call it from another script,  
which is a huge advantage over the one that was built in.  

in Python, aka python-fu:
`pdb.python_fu_awb(1, image, layer, hi, lo )`
in Scheme, aka script-fu:
`(python-fu-awb (1 image layer hi lo))`
