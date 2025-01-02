## Dice Categorization via convolutional neural network
by Joshua Penrod 
___
This is a small machine learning applicaiton for the WGU C964 capstone project. A sequential CNN model was trained to recognize the different dice types including [d4,d6,d8,d10,d12,d20]


Requirements:

-  Windows 10 or 11 computer
- [Python](https://www.python.org/downloads/) 3.9 or later 
- [Git](https://git-scm.com/downloads) or you can download and extract the zip

___

# How to Run the Web App
### 1. Clone this repository using the command below, *or* download a zip of its contents and extract to a folder
-  You can type  "cmd" into the address bar of file explorer and then hit ENTER to open up a command prompt at that location. 
- Make sure you open up the command prompt at the projects main directory. You should see a 'requirements.txt'
```bash
git clone https://github.com/EnjoySkyBlue/C964_Dice_Project.git
```

### 2. Once you're in your command prompt, navigate to the project folder and create a virtual enviroment using the commands below. this may take a few seconds
```bash
cd C964_Dice_Project
```

```bash
py -m venv venv
```
```bash
.\venv\Scripts\activate
```
### 3. Install pip libraries from requirements. This may take a few minutes

```bash
pip install -r requirements.txt
```
### 4. Finally, run this command to pull up the webpage

```bash
voila DiceTypeMain.ipynb
```
# How to use the app

1. Under the Dice classification header, click the file select button to choose one of the images that were not trained or tested on in the model.  
2. After the image is trained, take a look and see if the model predicted correctly
3. Explore the three buttons on the bottom to see the different ways I've visualized the data

# How to see/use the model
if you would like to train it on new images, insert the images in the **./data/dicetype** directory seperating them into 6 folders based on the categories: [d4,d6,d8,d10,d12,d20]
- Run the model (Warning: this can take up to 25 minutes to run)
```
voila DiceTypeClassification.ipynb
```
- Open in Jupiter notebook (You can choose what runs and what does not)
```
jupyter DiceTypeClassification.ipynb
```