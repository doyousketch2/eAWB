**awb.py**  
Enhanced **A**uto **W**hite **B**alance for GIMP  

---

Enhanced, because you can specify the amount you wish to clip.  

4 seems to be a good amount, but you can set it higher or lower,  
if you prefer more, or less, filtering.  

![image](https://pbs.twimg.com/media/DTzLQn_WAAESxH9?format=jpg)  

When you open your histogram and look at where the ranges are,  
you may notice an image has highlights, but no shadows.  

In this case, you can specify that you prefer clipping more from the shadows,  
and leave the highlights alone.  Or vice-versa.  Your choice, it's enhanced.  

You can also call it from another script,  
which is a huge advantage over the one that was built in.  

in Python, *aka* **python-fu**:  
`pdb.python_fu_awb(1, image, layer, hi, lo)`  
in Scheme, *aka* **script-fu**:  
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
and was informed someone else was nearly simultaneously, asking about it, on StackOverflow  
https://stackoverflow.com/questions/48268068/how-do-i-do-the-equivalent-of-gimps-colors-auto-white-balance-in-python-fu  

Fortuitous event, for it led to a suitable answer.

  
