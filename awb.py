#!/usr/bin/env python
"""=========================================================="""
##  Copyright 17 Jan 2018  @Doyousketch2  <doyousketch2@yahoo.com>
##  GNU GPL v3 - http://www.gnu.org/licenses/gpl-3.0.html
"""=========================================================="""
##  Place script in directory that suits your OS:
##
##	/home/yourname/.gimp-2.8/plug-ins
##	/usr/share/gimp/2.0/plug-ins
##  ~/Library/Application/Support/GIMP/2.8/plug-ins
##
##	C:\Users\yourname\.gimp-2.8\plug-ins
##	C:\Program Files\GIMP 2\share\gimp\2.0\plug-ins
##	C:\Documents and Settings\yourname\.gimp-2.8\plug-ins
##
##  If needed, set file permissions to allow script execution
##  chmod +x awb.py
"""=========================================================="""
from gimpfu import *

def awb( img, draw, hi_amt, lo_amt ):
  ##  ( drawable,  channel,  start-range,  end-range )  ( 0 <= range <= 255 )
  ##  channel = { HISTOGRAM-VALUE (0), HISTOGRAM-RED (1), HISTOGRAM-GREEN (2),
  ##              HISTOGRAM-BLUE (3), HISTOGRAM-ALPHA (4), HISTOGRAM-RGB (5) }

  ## group this entire procedure within one undo command
  pdb .gimp_image_undo_group_start( img )
  ##  determine low and high clipping amounts
  amt_lo  = 1.0 -lo_amt /1000
  amt_hi  = amt_lo -hi_amt /1000

  loR, loG, loB  = 0, 0, 0
  hiR, hiG, hiB  = 255, 255, 255

  ##  get full red percentile, then narrow in on this histogram channel
  _, _, _, _, _, prcntR  = pdb .gimp_histogram( draw, 1, loR, hiR )
  while prcntR > amt_lo:
    loR += 1  ##  increase red low end 'till percent is within clip amount
    _, _, _, _, _, prcntR  = pdb .gimp_histogram( draw, 1, loR, hiR )
  while prcntR > amt_hi:
    hiR -= 1  ##  decrease red high end 'till percent is within clip amount
    _, _, _, _, _, prcntR  = pdb .gimp_histogram( draw, 1, loR, hiR )


  ##  get full green percentile, then narrow in on this histogram channel
  _, _, _, _, _, prcntG  = pdb .gimp_histogram( draw, 2, loG, hiG )
  while prcntG > amt_lo:
    loG += 1  ##  increase green low end 'till percent is within clip amount
    _, _, _, _, _, prcntG  = pdb .gimp_histogram( draw, 2, loG, hiG )
  while prcntG > amt_hi:
    hiG -= 1  ##  decrease green high end 'till percent is within clip amount
    _, _, _, _, _, prcntG  = pdb .gimp_histogram( draw, 2, loG, hiG )


  ##  get full blue percentile, then narrow in on this histogram channel
  _, _, _, _, _, prcntB  = pdb .gimp_histogram( draw, 3, loB, hiB )
  while prcntB > amt_lo:
    loB += 1  ##  increase blue low end 'till percent is within clip amount
    _, _, _, _, _, prcntB  = pdb .gimp_histogram( draw, 3, loB, hiB )
  while prcntB > amt_hi:
    hiB -= 1  ##  decrease blue high end 'till percent is within clip amount
    _, _, _, _, _, prcntB  = pdb .gimp_histogram( draw, 3, loB, hiB )

  ##  apply RGB levels
  ##       ( draw, chan, lo-in, hi-in, gamma, lo-out, hi-out)
  pdb .gimp_levels( draw, 1, loR, hiR, 1.0, 0, 255 )
  pdb .gimp_levels( draw, 2, loG, hiG, 1.0, 0, 255 )
  pdb .gimp_levels( draw, 3, loB, hiB, 1.0, 0, 255 )

  ##  close up undo group, then refresh display
  pdb .gimp_image_undo_group_end( img )
  pdb .gimp_displays_flush()


register (
        "awb",                  ##  commandline name
        "Auto White Balance",  ##  blurb
        "Chops top & bottom off each RGB channel",  ##  help
        "Doyousketch2",      ##  author
        "GNU GPL v3",       ##  copyright
        "2018",            ##  date
        "<Image>/Filters/Enhance/Auto White Balance",  ##  menu location
        "*",             ##  image types
        [                                 ##  default, (min, max, step)
          (PF_SLIDER, "hi_amount",  "highlight clip", 4, (0, 50, 1)),
          (PF_SLIDER, "lo_amount",  "shadow clip", 4, (0, 50, 1)),
        ],            ##  parameters
        [],          ##  results
        awb )       ##  name of function

main()
