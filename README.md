# Resources for Public Engagement in Astronomy

By: [Erin Hayes](https://www.ast.cam.ac.uk/people/Erin.Hayes), PhD Candidate at the Institute of Astronomy (IoA), University of Cambridge

Additional authors listed by project. Please credit all contributers on a project if you use the resources!

If any issues or confusion arises while trying to access or use any of the below resources, feel free to contact me at <eeh55@cam.ac.uk>.

## International Women's Day (IWD) at the IoA
In celebration of IWD, we developed a coding tutorial on detecting exoplanets via the transit method using real Kepler Space Telescope data. The tutorial particularly highlights the contributions of women to the Kepler mission and the field of exoplanet science. This resource was first developed for students in Year 9 (age 13-14) and the exercises are friendly to students who have no prior coding experience. Thanks to **Erik Rosenberg**, **Steve Young**, **Jessica Rigley**, and **Katherine Kauma** for their help in preparing the IWD educational material!

This resource is in the form of a jupyter notebook. Jupyter notebooks are virtual "notebook" environments in which astronomers code. One way of using jupyter notebooks is through Google's coding platform "Google Colab." All the information you need about how to use a notebook in Google Colab is contained within the tutorial. Clicking on the following link will take you directly to a Google Colab page where you can start learning:

[https://githubtocolab.com/erinhay/outreach/blob/main/IWD/IWD_transitingplanets.ipynb](https://githubtocolab.com/erinhay/outreach/blob/main/IWD/IWD_transitingplanets.ipynb)

[Introductory slides for the notebook can be found here!](https://docs.google.com/presentation/d/1yp81eEi25TsnwC7Tj5q4aTMXgA4wmSRPiMUphiycehQ/edit?usp=sharing)

If you would prefer to git clone the repository and run it locally on your device, replace this block of code:

```
!git clone https://github.com/erinhay/outreach.git
!pip install ipympl
!pip install astropy
!pip install lightkurve > /dev/null 2>&1 

import os
os.chdir('/content/outreach/IWD/py')
from helpers import *
import lightkurve as lk

from google.colab import output
output.enable_custom_widget_manager()
%matplotlib widget

os.chdir('/content/outreach/IWD/')
plt.style.use('./style/style.mplstyle')
```

with the following:

```
!pip install lightkurve > /dev/null 2>&1 
import lightkurve as lk
from py.helpers import *
%matplotlib notebook

plt.style.use('./style/style.mplstyle')
```

## Sutton Trust Computer Science Summer School at Cambridge University

For the Sutton Trust Summer School hosted by the computer science department at Cambridge, we developed an interactive coding tutorial on detecting exoplanets using real Kepler Space Telescope data. The tutorial guides students through basic computations relating to Kepler's Third Law and plotting exoplanet transits in python. This resource was first developed for students in Year 12 (age 17-18) and the exercises are best suited to students with GCSE/high-school level background in physics and some exposure to coding in python (1-2 previous classes), but are friendly to students who have no prior coding experience. Thanks to **Francis Rigby** and **[helper name]** for their help in preparing the educational material and presenting it at the summer school!

This resource is in the form of a jupyter notebook. Jupyter notebooks are virtual "notebook" environments in which astronomers code. One way of using jupyter notebooks is through Google's coding platform "Google Colab." All the information you need about how to use a notebook in Google Colab is contained within the tutorial. Clicking on the following link will take you directly to a Google Colab page where you can start learning:

[https://githubtocolab.com/erinhay/outreach/blob/main/]()

[Introductory slides for the notebook can be found here!]()

If you would prefer to git clone the repository and run it locally on your device, replace this block of code:

```
!git clone https://github.com/erinhay/outreach.git
!pip install ipympl
!pip install astropy
!pip install lightkurve > /dev/null 2>&1 

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
import astropy.units as au
import astropy.constants as ac
import lightkurve as lk

from google.colab import output
output.enable_custom_widget_manager()
%matplotlib widget

plt.style.use('./style/style.mplstyle')
```

with the following:

```
!pip install lightkurve > /dev/null 2>&1

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
import astropy.units as au
import astropy.constants as ac
import lightkurve as lk

%matplotlib notebook
plt.style.use('./style/style.mplstyle')
```
