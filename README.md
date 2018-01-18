**awb.py**  
Enhanced **A**uto **W**hite **B**alance for GIMP  
Filters > Enhance > Auto White Balance  

---

Enhanced, because you can specify the amount you wish to clip.  

somewhere around 5 seems to be a good amount,  
but you can set it higher or lower,  
if you prefer more, or less, filtering.  

![image](https://pbs.twimg.com/media/DTzLQn_WAAESxH9?format=jpg)  

*Some images may need more aggressive filtering.*  

*If the color appears off*, Undo,  
look at histogram for each of the colors,  
and decide if it needs more in the highlights or shadows.  

Eyes are more sensitive to light regions than shadows, so  
I would venture a guess highlights may need tweaking to get good results.  
You decide the direction you wanna take it.  

When you open your histogram and look at where the ranges are,  
you may notice an image has highlights, but no shadows.  

In this case, you can specify that you prefer clipping more from the shadows,  
and leave the highlights alone.  Or vice-versa.  Your choice, it's enhanced.  

This will, of course, depend upon your camera, and the lighting,  
So you will have better results with some pix than others.  

You can crank it all the way up to 50 if you like, which will boost the contrast,  
but discard pixels that may have otherwise contributed to the dynamic range.  

If you wanna do that, I'd suggest sliding shadows up to 50  
and leaving the highlights at 6 or so.  This gives a bold look,  
but keeps enough detail in the scene to be pleasing to the eye.  

You can also call it from another script,  
which is a huge advantage over the one that was built in.  

from a Python plug-in, *aka* **python-fu**:  
`pdb.python_fu_awb(1, image, layer, hi, lo)`  

from a Scheme script, *aka* **script-fu**:  
`(python-fu-awb 1 image layer hi lo)`  

---

Place script in directory that suits your OS:

    /home/yourname/.gimp-2.8/plug-ins  
  	/usr/share/gimp/2.0/plug-ins  
    ~/Library/Application/Support/GIMP/2.8/plug-ins  

  	C:\Users\yourname\.gimp-2.8\plug-ins  
  	C:\Program Files\GIMP 2\share\gimp\2.0\plug-ins  
  	C:\Documents and Settings\yourname\.gimp-2.8\plug-ins  

If needed, *set file permissions to allow script execution:*  
    `chmod +x awb.py`  
    
---
I was asking about this in r/Gimp  
https://www.reddit.com/r/GIMP/comments/7qw7eb/how_do_you_call_automatic_white_balance_from_a/  
and was informed someone else was, nearly simultaneously, asking about it on StackOverflow  
https://stackoverflow.com/questions/48268068/how-do-i-do-the-equivalent-of-gimps-colors-auto-white-balance-in-python-fu  

Fortuitous event, for it led to a suitable answer.

  
