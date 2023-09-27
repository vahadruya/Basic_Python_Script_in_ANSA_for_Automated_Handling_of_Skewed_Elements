# Basic Python Script in ANSA for Automated Handling of Skewed Surface Mesh Elements

<details>
<summary>Table of Contents</summary>

1. [About the Study](#about-the-study)
2. [Background](#background)
3. [Script Approach](#script-approach)
4. [Results](#results)
5. [Libraries Used](#libraries-used)
6. [Contact](#contact)
</details>

## About the Study

This study focuses on an automated removal of skewed surface mesh elements using Python scripts which utilize modules and functions available within the ANSA environment. The primary objectives of this study are -
- To evaluate the usage of this Python scripting using the criterias of geometry distortion (accurace and reliabality) and the time taken for code completion
- General comparison of the same with the default in-built functions within the ANSA GUI

<div align = "right">    
  <a href="#basic-python-script-in-ansa-for-automated-handling-of-skewed-surface-mesh-elements">(back to top)</a>
</div>

## Background
The Scope of this study involves only removal of skewed elements and not warpage, Jacobian etc criterias as they are not usually considered for an all-tria mesh, which are generally used in CFD Surface Meshes. Nevertheless, it is quite easy to extend this quality criteria of **skew** to the others within the Python script.

In ANSA, there are two primary classes of in-built functions used to rectify the skewed elements
- Manual removal (using Cut, Join, Paste etc)
- Reconstruction, Fix Quality, Remeshing etc. methods which resolve at bulk

The developed script focuses on an intelligent combination of the methods present in the latter class - particularly **Fix Quality** and **Reconstruct**. Hence, it is to be noted that, the script is not absolute and various other methods (developed for various other combinations of the ANSA functions) can be developed for quality removal.

## Script Approach
The characteristics of **Fix Quality** and **Reconstruct** are as follows:
- **Fix Quality**
  - Least impact on feature modification
  - Lesser improvement power
  - Does not change the total count of elements
- **Reconstruct**
  - Superior improvement power
  - Greater the **Expand Level**, better the mesh improvement power, but consequently greater geometry distortion

The methods utilised for the script involve a sequence of the above functions, in an ascending order of risk of geometry modification, i.e., the **Fix Quality** function is executed first, followed by **Reconstruct** of increasing **Expand Level** (starting from zero) which works on the skewed elements remaining after the **Fix QUality** function. This ensures that there is minimal modification of the geometrical topology, while maintaining a good degree of accuracy for skewed element removal.

<div align = "right">    
  <a href="#basic-python-script-in-ansa-for-automated-handling-of-skewed-surface-mesh-elements">(back to top)</a>
</div>

## Results

Comment

| Metric | Model 1 | Model 2 | Model 3 |
| :--- |    :----:   | :----: | :---: |
| Total initial skewness | 335 | 225 | 903 |
| Total element count in model | x | x | x |
| Total skewness after executing script| 0 | 0 | 0 |
| Total skewness after Improve Algorithm (Expand Level 1) | 1 | 0 | 20 |
| Total time taken for running script | 1.4s | 0.3s | 12.7s |
| Approx. time for manual removal of skewness | 30min | 20min | 60min |

<div align = "right">    
  <a href="#basic-python-script-in-ansa-for-automated-handling-of-skewed-surface-mesh-elements">(back to top)</a>
</div>

## Conclusions



<div align = "right">    
  <a href="#basic-python-script-in-ansa-for-automated-handling-of-skewed-surface-mesh-elements">(back to top)</a>
</div>

## Libraries Used

OS, ANSA, MESH, BASE, CONSTANTS

<a href="https://pandas.pydata.org/" target="_blank"><img src="https://img.shields.io/badge/Pandas-black?style=flat-square&logo=Pandas&logoColor=white&link=https://pandas.pydata.org" alt="Pandas" width="84" height="25"></a>

<div align = "right">    
  <a href="#basic-python-script-in-ansa-for-automated-handling-of-skewed-surface-mesh-elements">(back to top)</a>
</div>


## Contact

<a href="https://www.linkedin.com/in/aditya-a-p-507b1b239/" target="_blank"><img src="https://img.shields.io/badge/Linkedin-0078b7?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/" alt="Linkedin" width="85" height="25"></a>
<a href="mailto:apaditya96@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-red?style=flat-square&logo=Gmail&logoColor=white" alt="Gmail" width="70" height="25"></a>
  
<div align = "right">    
  <a href="#basic-python-script-in-ansa-for-automated-handling-of-skewed-surface-mesh-elements">(back to top)</a>
</div>

