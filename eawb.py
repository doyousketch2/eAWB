#!/usr/bin/env python
"""=========================================================="""
##  Copyright 17 Jan 2018  @Doyousketch2  <doyousketch2@yahoo.com>
##  GNU GPL v3 - http://www.gnu.org/licenses/gpl-3.0.html
"""=========================================================="""
##  Place script in directory that suits your OS:
##
##  /home/yourname/.gimp-2.8/plug-ins
##  /usr/share/gimp/2.0/plug-ins
##  ~/Library/Application/Support/GIMP/2.8/plug-ins
##
##  C:\Users\yourname\.gimp-2.8\plug-ins
##  C:\Program Files\GIMP 2\share\gimp\2.0\plug-ins
##  C:\Documents and Settings\yourname\.gimp-2.8\plug-ins
##
##  If needed, set file permissions to allow script execution
##  chmod +x awb.py
"""=========================================================="""
from gimpfu import *

##  simple clamping function with range 0 - 255
def minmax( x ):
  if x < 0:  x  = 0
  elif x > 255:  x  = 255
  return x


def eawb( img, draw, hi, blow, lo, burn, soft ):
  ##  ( drawable,  channel,  start-range,  end-range )  ( 0 <= range <= 255 )
  ##  channel = { HISTOGRAM-VALUE (0), HISTOGRAM-RED (1), HISTOGRAM-GREEN (2),
  ##              HISTOGRAM-BLUE (3), HISTOGRAM-ALPHA (4), HISTOGRAM-RGB (5) }

  ## group this entire procedure within one undo command
  pdb .gimp_image_undo_group_start( img )

  ##  determine low and high clipping amounts
  amt_lo  = 1.0 -lo /1000
  amt_hi  = amt_lo -hi /1000

  loR, loG, loB  = 0, 0, 0
  hiR, hiG, hiB  = 255, 255, 255

  ##  _,  are unused variables.  We only need "percentile"
  ##  which is the 6th value returned from pdb.gimp_histogram()
  ##  so we just skip the first 5 values with 5 blank spaces.

  ##  get full red percentile, then narrow in on this histogram channel
  _, _, _, _, _, prcntR  = pdb .gimp_histogram( draw, 1, loR, hiR )
  while prcntR > amt_lo:
    loR += 1  ##  increase red low end 'till percent is within lo clip amount
    _, _, _, _, _, prcntR  = pdb .gimp_histogram( draw, 1, loR, hiR )
  while prcntR > amt_hi:
    hiR -= 1  ##  decrease red high end 'till percent is within hi clip amount
    _, _, _, _, _, prcntR  = pdb .gimp_histogram( draw, 1, loR, hiR )


  ##  get full green percentile, then narrow in on this histogram channel
  _, _, _, _, _, prcntG  = pdb .gimp_histogram( draw, 2, loG, hiG )
  while prcntG > amt_lo:
    loG += 1  ##  increase green low end 'till percent is within lo clip amount
    _, _, _, _, _, prcntG  = pdb .gimp_histogram( draw, 2, loG, hiG )
  while prcntG > amt_hi:
    hiG -= 1  ##  decrease green high end 'till percent is within hi clip amount
    _, _, _, _, _, prcntG  = pdb .gimp_histogram( draw, 2, loG, hiG )


  ##  get full blue percentile, then narrow in on this histogram channel
  _, _, _, _, _, prcntB  = pdb .gimp_histogram( draw, 3, loB, hiB )
  while prcntB > amt_lo:
    loB += 1  ##  increase blue low end 'till percent is within lo clip amount
    _, _, _, _, _, prcntB  = pdb .gimp_histogram( draw, 3, loB, hiB )
  while prcntB > amt_hi:
    hiB -= 1  ##  decrease blue high end 'till percent is within hi clip amount
    _, _, _, _, _, prcntB  = pdb .gimp_histogram( draw, 3, loB, hiB )

  ##  back off a bit so we don't overshoot our target.

  if loR > 0:  ##  Red shadows
    if burn:  loR  = loR //1.2
    else:     loR -= 1

  if hiR < 255:  ##  Red highlights
    if blow:  hiR  = 255 -(255 -hiR) //1.5
    else:     hiR += 1

  if loG > 0:  ##  Green shadows
    if burn:  loG  = loG //1.2
    else:     loG -= 1

  if hiG < 255:  ##  Green highlights
    if blow:  hiG  = 255 -(255 -hiG) //1.5
    else:     hiG += 1

  if loB > 0:  ##  Blue shadows
    if burn:  loB  = loB //1.2
    else:     loB -= 1

  if hiB < 255:  ##  Blue highlights
    if blow:  hiB  =  255 -(255 -hiB) //1.5
    else:     hiB += 1

  if soft:  ##  soften tint change applied
    avgLo  = (loR +loG +loB) /3
    avgHi  = (hiR +hiG +hiB) /3

    loR -= abs(loR -avgLo) /2  ##  Red shadows
    loR  = minmax( loR )

    hiR += abs(hiR -avgHi) /2  ##  Red highlights
    hiR  = minmax( hiR )

    loG -= abs(loG -avgLo) /2  ##  Green shadows
    loG  = minmax( loG )

    hiG += abs(hiG -avgHi) /2  ##  Green highlights
    hiG  = minmax( hiG )

    loB -= abs(loB -avgLo) /2  ##  Blue shadows
    loB  = minmax( loB )

    hiB += abs(hiB -avgHi) /2  ##  Blue highlights
    hiB  = minmax( hiB )

  ##  apply RGB levels
  ##       ( draw, chan, lo-in, hi-in, gamma, lo-out, hi-out)
  pdb .gimp_levels( draw, 1, loR, hiR, 1.0, 0, 255 )
  pdb .gimp_levels( draw, 2, loG, hiG, 1.0, 0, 255 )
  pdb .gimp_levels( draw, 3, loB, hiB, 1.0, 0, 255 )

  ##  close up undo group, then refresh display
  pdb .gimp_image_undo_group_end( img )
  pdb .gimp_displays_flush()


register (
        "eawb",                 ##  commandline name
        "Enhanced Auto White Balance",  ##  blurb
        "Chops top & bottom off each RGB channel",  ##  help
        "Doyousketch2",      ##  author
        "GNU GPL v3",       ##  copyright
        "2018",            ##  date
        "<Image>/Filters/Enhance/Enhanced Auto White Balance",  ##  menu location
        "RGB*",          ##  image types
        [               ## var, gui label, default, (min, max, step)
          (PF_SLIDER, "hi",  "Highlight Clip", 7, (0, 50, 1) ),
          (PF_TOGGLE, "blow", "Reduce blown Highlights", 1 ),
          (PF_SLIDER, "lo",  "Shadow Clip", 10, (0, 50, 1) ),
          (PF_TOGGLE, "burn", "Reduce burnt Shadows", 1 ),
          (PF_TOGGLE, "soft", "Soft tint", 1 ),
        ],        ##  parameters
        [],      ##  results
        eawb )  ##  name of function

main()
