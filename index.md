# DL West Point Collaboration
In early 2022, Dr. Ryan Mc Cullough (Decision Lens) worked with Dr. Jonathan Roginski (West Point) on a proof of
concept use of DLC and AHP for prioritizing military needs.
The most important outcome from this part of their decision making
process is the 1-N list of alternatives (projects).  They brought
Dr. William Adams (Decision Lens) into the project in March 2022
to design and perform the analysis contained in this repository.

They have a weighting and rating structure to arrive at the scores of alternatives, and the scores give the ranks of the alternatives.  Leaders meet together to determine
the weights of the criteria in the model.  Everyone agrees on the ratings
of the projects (think of them as expert inputs).  The disagreement is
over which criteria are most important.  Effectively the disagreement about
the criteria weights is a disagreement about what needs will be most important
in the future.

However, the only reason they weigh the criteria is so that they can
get the 1-N list of alternatives.  And differences of opinions on ratings
are meaningless if they give rise to similar 1-N alternative rankings.

What we have is:

1. We have the combined weights of the group of participants for the criteria.
2. We also have the ratings scores of the alternatives/projects on those criteria.
3. We therefore have the combined rankings of the alternatives from those weights and scores.

The main question is:

* How sensitive is the 1-N rankings of alternatives to fluctuations/adjustments to the overall criteria weights?
* In other words, how much do you have to change the weights of the criteria to induce "impactful rank change".
* Some definitions of "impactful rank change" might be:
  * Any project changing its rank, even if only the last and 2nd to last are the only ones that change.
  * At least 1 project changing at least 3 ranks.
  * At least 3 projects changing by at least 2 ranks.
  * Something in the top 10 moving out of the top 10
  * etc.

## Our main definition of "impactful rank change"

* A rank change is "impactful" if it changes at least `m` alternatives ranks
by at least `r`.
* We find the smallest change in criteria weights required to get at least
`m` alternatives ranks to change by at least `r`.
* We then show a table of percentage change of weights required to get those
impactful alternative ranking changes.

# Files
* [Report-V1.ipynb](Report-V1.ipynb): This is a good place to start to see the results of the calculations.  Unfortunately it doesn't show up well on github directly.  You will need to clone this repository and run it locally.
* [wpt](wpt): This directory contains code that was originally designed and experimented with in [Research.ipynb](Research.ipynb).  This version of the code is cleaned up, and has unit tests.
* [wpt/math.py](wpt/math.py): The actual algorithm used to calculate weight changes needed to induce different kind of "impactful rank change".
* [tests](test): Unit tests for the code in [wpt](wpt).
* [initial-data.xlsx](initial-data.xlsx): The initial data from Ryan/Jon's proof of concept model.  This data was exported from a DLC AHP model.
* [Research.ipynb](Research.ipynb): Dr. Bill Adams' initial scrap notebook with research calculations.  This is not a pretty place to start, but has some useful bits in it.
* [LICENSE](LICENSE): The license for this software.

# Needed software
* Install [anacoda/python with jupyter](https://www.anaconda.com/products/distribution)
* I recommend installing [nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)
* Enable collapsible headings in nbextensions in Jupyter, and everything looks prettier :)
* Install `qgrid`, by doing `pip install qgrid` from the command line where the python from anaconda is available.
* I may have a few other things `pip` installs needed.  Whatever the jupyter notebook complains about, just `pip instal *****` the name of the missing package.
