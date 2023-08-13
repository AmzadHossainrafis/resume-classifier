# Resume classifier 


## Description

This project is a resume classifier that uses a Naive Bayes classifier to classify resumes into 30 different categories. The classifier is trained on a dataset of 1250 resumes. The dataset is available in the data folder.


## how to train the classifier 

1. Clone the repository
2. cd into the repository       
3. create a condaa environment using the command `conda create --name <env> `
4. activate the environment using the command `conda activate <env>`
5. install the requirements using the command `pip install -r requirements.txt` 
6. cd into src/componenet
7. run all the cells in the notebook `train.ipynb`


## how to use script

 1. cd into src/componenet
 2. download pretrain model from [here](https://drive.google.com/drive/folders/1qnPQWVQxN0ig5aPtWr9av-Kc_4FsZ2Qk?usp=sharing)
 3. paste this model in the src/componenet folder 
 4. run the command `python script.py --path <path to resumes>`


