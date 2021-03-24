File description:

info.py
This file unzip the big data I downloaded and turn them into a pandas dataframe. No need to run this one

extract.ipynb
This file shows the process of extracting the two datasets for training.

ML_pipline.ipynb
This file is the one you want to focus on. All the model training and data analysis are done here. 
Cross validation takes a lot of time. Change the global variable call_cross_validation to False will run faster.

Clarification:
I was planning to do a project related to fake review detection. But I recently found out that the considered factors for fake reviews are more complex than I thought.
I did talk about fake review in the report. Since my model is not predicting whether the review is fake or not, I can't name the project as fake review detection.
The program in codeForEffort is a labeling tool I implemented. I was thinking about labeling fake reviews by myself. But I felt that it's unrealistic to label everything by one person, so I gave up.