# Resources for Public Engagement in Astronomy

By: [Erin Hayes](https://www.ast.cam.ac.uk/people/Erin.Hayes), PhD Candidate at the Institute of Astronomy, University of Cambridge

Additional authors listed by project. Please credit all contributers on a project if you use the resources!

## International Women's Day (IWD) at the Institute of Astronomy
In the IWD folder, you will find a jupyter notebook with a tutorial on detecting exoplanet transits using a combination of simulated and real Kepler data. The notebook particularly highlights contributions of women to the Kepler mission and exoplanet discovery. The notebook was first developed for students in Year 9 (age 13-14). The exercises are friendly to students who have no prior coding experience. Thanks to **Erik Rosenberg**, **Steve Young**, **Jessica Rigley**, and **Katherine Kauma** for their help in preparing the IWD educational material!

This notebook was formatted for use in Google Colab. It can be accessed via the following link:

[https://githubtocolab.com/erinhay/outreach/blob/main/IWD/IWD_transitingplanets.ipynb](https://githubtocolab.com/erinhay/outreach/blob/main/IWD/IWD_transitingplanets.ipynb)

[Introductory slides for the notebook can be found here!](https://docs.google.com/presentation/d/1yp81eEi25TsnwC7Tj5q4aTMXgA4wmSRPiMUphiycehQ/edit?usp=sharing)

To run the notebook locally by cloning the repository to your device, replace this block of code:

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

