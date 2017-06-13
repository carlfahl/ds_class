### Week 1 - Liftoff, Intro to python3


#### Day 1:

##### Objectives

<!-- From the GA start -->
By the end of this course, students will be able to:
‣ Collect, extract, query, clean, and aggregate data for analysis
‣ Perform visual and statistical analysis on data using Python and its associated libraries and
tools
‣ Build, implement, and evaluate data science problems using appropriate machine learning
models and algorithms
‣ Use appropriate data visualization to communicate findings
‣ Create clear and reproducible reports to stakeholders
‣ Identify big data problems and articulate how distributed systems and parallel computing
technologies are solving these challenges
‣ Apply question, modeling, and validation problem-solving processes to datasets from various
industries in order to provide insight into real-world problems and solutions

<!-- From the GA end -->

##### Statistical methods



##### Basic data analysis



##### Big Data



##### Data Science

  * The Data Science Venn Diagram: http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram
  * The Steps of Data Science:
    * Data Exploration and Preparation
    * Data Representation and Transformation
    *

##### Machine Learning

##### Intro to Python
  * Why use Python
    * overview of other tools available - R, MatLab, Java, C
      * Advantages and Disadvantages.
      *
  * Python2 vs Python3
  * Overview of Prerequisites
  * Installing python
  * Assessment -
  * Installing and Using Jupyter Notebook
    * Jupyter Notebook is the succesor to the IPython project.  
    * To install and start jupyter notebook:

    ```
    pip install jupyter
    jupyter notebook
    ```
    Because we are using `pip` rather than `pip3`, this will set up jupyter notebook
    to create python2 notebooks.  To be able to run both type of notebooks, install the
    python3 kernel.

    `pip3 install ipykernel`

    Restart the jupyter notebook server and both Python2 and Python3 should appear in the new
    notebooks dropdown.  

    * Open a browser to the url provided by the `jupyter notebook` command.  
    Normally a browser window will open automatically.  

    * Intro to NumPy
      * numpyIntro.py
        *

    * Read and write csvdata in python with the csv module.  
      * csvReadWrite.py
        * exercies discribed in git commits for the creation of this file.
          * Reading CSV file.
          * adding the rows of a CSV file to another python list
          * converting the list to an array with Numpy
          * Manipulate the array with slicing and type casting.
          * Create data with arange and Manipulate with reshape.
          * Write out test data to new csv file.
      * Student exercies with csv files.

##### Day 2

  * Python warmup

  * Create GitHub account, push some code.

  * Array methods and data analysis in NumPy
    * Stat methods in Numpy
     * Numpy provides a large collection of basic statistical methods


##### Day 3

  * Introduction to SciPy
    * Getting Started
      * Installation
      *
    *
  * Basic plotting with Matplotlib and Seaborn

##### Day 4

  * Unix Command line
    * Basic commands.  Getting around in the terminal.
    * Text processing with awk and sed
    * Unix Command Line tools for data analysis.
