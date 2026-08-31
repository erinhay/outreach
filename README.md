# Resources for Public Engagement in Astronomy

By: [Erin Hayes](https://www.ast.cam.ac.uk/people/Erin.Hayes), PhD Candidate at the Institute of Astronomy (IoA), University of Cambridge

Welcome! In this Github repository, you will find a series of tutorials that guide students through questions in different areas of astronomy and introduce them to coding. The tutorials span several fields of astronomy from exoplanets to the expanding universe. For some topics, multiple levels of the tutorial have been developed to suit learners of different ages and experiences. All tutorials should take approximately 45 minutes to complete.

These resources are available in the form of jupyter notebooks. Jupyter notebooks are virtual "notebook" environments in which astronomers code. One way of using jupyter notebooks is through Google's coding platform "Google Colab." All the information you need about how to use a notebook in Google Colab is contained within the tutorials. To access the notebook via Google Colab, click the link listed under the tutorial of interest below!

Additional authors are listed by project. Please credit all contributers on a project if you use the resources! If any issues or confusion arise while trying to access or use any of the below resources, feel free to contact me at <eeh55@cam.ac.uk>. I'm also happy to hear your feedback to improve the resources! Thanks for joining me in a voyage through the universe!

### Contents
* [Discovering Exoplanets Through Coding Tutorials](https://github.com/erinhay/outreach?tab=readme-ov-file#discovering-exoplanets-through-coding)
  *  [Year 8-10 / 7th-9th Grade / Ages 13-15](https://github.com/erinhay/outreach#year-8-10--7th-9th-grade--ages-13-15)
  *  [Year 12-13 / 11th-12th Grade / Ages 16-18](https://github.com/erinhay/outreach#year-12-13--11th-12th-grade--ages-16-18)
* [Exploring the Expanding Universe With Supernovae Tutorials](https://github.com/erinhay/outreach#exploring-the-expanding-universe-with-supernovae)
  * [Year 7-9 / 6th-8th Grade / Ages 11-14](https://github.com/erinhay/outreach#year-7-9--6th-8th-grade--ages-11-14)

## Discovering Exoplanets Through Coding

![Kepler](https://github.com/erinhay/outreach/blob/main/Discovering-Exoplanets/images/kepler.jpeg?raw=1)

We developed a series of coding tutorials that introduce students to exoplanet detection using real Kepler Space Telescope data. Two levels of the tutorial have been developed to accommodate 1) students with little to no physics/coding experience, and 2) students with experience in physics and little to no coding experience. Students will be guided through how to identify the presence of exoplanets around stars via the transit method, and explore the diversity of exoplanets orbiting around other stars.

### Year 8-10 / 7th-9th Grade / Ages 13-15

The `discovering_exoplanets_IWD.ipynb` notebook (accessible below) was developed for students in Year 9 (age 13-14). The exercises are friendly to students who have no prior coding experience. Thanks to **Erik Rosenberg**, **Steve Young**, **Jessica Rigley**, and **Katherine Kauma** for their help in preparing this material!

Clicking on the following link will take you directly to a Google Colab page where you can start learning:

[https://githubtocolab.com/erinhay/outreach/blob/main/Discovering-Exoplanets/discovering_exoplanets_IWD.ipynb](https://githubtocolab.com/erinhay/outreach/blob/main/Discovering-Exoplanets/discovering_exoplanets_IWD.ipynb)

[Introductory slides for the notebook can be found here!](https://docs.google.com/presentation/d/1yp81eEi25TsnwC7Tj5q4aTMXgA4wmSRPiMUphiycehQ/edit?usp=sharing)

If you would prefer to git clone the repository and run it locally on your device, replace this block of code:

```
!git clone https://github.com/erinhay/outreach.git
!pip install ipympl
!pip install astropy
!pip install lightkurve > /dev/null 2>&1 

import os
os.chdir('/content/outreach/Discovering-Exoplanets/py')
from helpers import *
import lightkurve as lk

from google.colab import output
output.enable_custom_widget_manager()
%matplotlib widget

os.chdir('/content/outreach/Discovering-Exoplanets')
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

### Year 12-13 / 11th-12th Grade / Ages 16-18

The `discovering_exoplanets_SuttonTrust.ipynb` notebook (accessible below) was developed for students in Year 12 (age 17-18) and the exercises are best suited to students with GCSE/high-school level background in physics and some exposure to coding in python (1-2 previous classes), but are friendly to students who have no prior coding experience. Thanks to **Frances Rigby** and **Richard Anslow** for their help in preparing the materials and presenting it at the summer school!

Clicking on the following link will take you directly to a Google Colab page where you can start learning:

[https://githubtocolab.com/erinhay/outreach/blob/main/Discovering-Exoplanets/discovering_exoplanets_SuttonTrust.ipynb](https://githubtocolab.com/erinhay/outreach/blob/main/Discovering-Exoplanets/discovering_exoplanets_SuttonTrust.ipynb)

Solutions for the activities can be found here:

[https://githubtocolab.com/erinhay/outreach/blob/main/Discovering-Exoplanets/discovering_exoplanets_SuttonTrust_solutions.ipynb](https://githubtocolab.com/erinhay/outreach/blob/main/Discovering-Exoplanets/discovering_exoplanets_SuttonTrust_solutions.ipynb)

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

## Exploring the Expanding Universe with Supernovae

![Hubble](https://github.com/erinhay/outreach/blob/main/Exploring-the-Expanding-Universe/images/hubble-space-telescope.jpeg)

I developed a coding tutorial that introduce students to the study of supernovae using real Hubble Space Telescope data. The tutorial has been developed to accommodate students with little to no physics or coding experience, though students with more experience in physics can also enjoy the activity. Students will be guided through how astronomers use supernovae to understand the temperature and chemical composition of stars, and measure the distances to supernovae to create maps of the universe. By the end of the activity, the students will have recorded the distances to two supernovae observed by Hubble and discovered that the universe is expanding!

### Year 7-9 / 6th-8th Grade / Ages 11-14

The `exploring_the_expanding_universe_RSHC.ipynb` notebook (accessible below) was developed for students in 6th-8th grade (age 11-14). The exercises are friendly to students who have no prior coding experience. Clicking on the following link will take you directly to a Google Colab page where you can start learning:

[https://githubtocolab.com/erinhay/outreach/blob/main/Exploring-the-Expanding-Universe/exploring_the_expanding_universe_RSHC.ipynb](https://githubtocolab.com/erinhay/outreach/blob/main/Exploring-the-Expanding-Universe/exploring_the_expanding_universe_RSHC.ipynb)

[Introductory slides for the notebook can be found here!](https://docs.google.com/presentation/d/18EDUyupzZprRZD9lzUogrThhfc3Ggqpzxv3PLLEvt8o/edit?usp=sharing)

If you would prefer to git clone the repository and run it locally on your device, replace this block of code:

```
from google.colab import output
output.enable_custom_widget_manager()
%matplotlib widget

!git clone https://github.com/erinhay/outreach.git
!pip install ipympl
!pip install astropy
!pip install sncosmo

import os
os.chdir('/content/outreach/Exploring-the-Expanding-Universe/py')
from helpers import *
os.chdir('/content/outreach/Exploring-the-Expanding-Universe')

plt.style.use('./style/style.mplstyle')
```

with the following:

```
!pip install ipympl
!pip install astropy
!pip install sncosmo

from py.helpers import *

%matplotlib notebook
plt.style.use('./style/style.mplstyle')
```
