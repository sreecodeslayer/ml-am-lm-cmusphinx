# About this directory

This is the Base folder for the Google Summer of Code 2016.<br>
<i>The project aims in creating a Language Model and Acoustic Model for Malayalam language for using the same with CMU Sphinx Speech Recognition System.</i> The project was started from scratch collecting the text data from various film subtitles in Malayalam, preparing corpus file out of it.<br>
#### Reason for film subtitles : 
The reason film sutitles from [here](http://www.malayalamsubtitles.com/) were used is because, snce these are dialogues. This means most of the natural way of speaking is bound to be present, which makes sorting out the required words for constructing the dictionary becomes a litlle bit easier.<br>
For those who are new to CMU Sphinx can take a look at here for familiarization : http://cmusphinx.sourceforge.net/ <br>
For those who wats to develop your own and you need a reference, read on. If you want to know how I completed this, you can read my blog posts on Medium here: http://www.medium.com/@imsreenadh

Let me walk you through the project directory setup now.

### ```AM``` and ```LM``` are the training folders.
  These folders can be used to train your own models after adding more data respectively. 
##### ```AM``` folder contains ```etc``` and ```wav``` folers.<br>
  ```etc``` folder contains various files created as per the documentation/tutorial provided by CMU Sphinx team. Know more from the documentation here : http://cmusphinx.sourceforge.net/wiki/tutorialam <br>
  ```wav``` folder contains the audio database arranged accordingly, as explained in the documentation of CMU Sphinx Acoustic Model training. The link above have these information as well.
##### ```LM``` folder contains the files required/generated while building the Statistical Language Model
  ```ml.arpa``` inside this folder is the final file which is a 3-gram language model. Other files in the folder are intermediate files. It was developed by following the documentation from here: http://cmusphinx.sourceforge.net/wiki/tutoriallm
  
### ```OUTPUT``` contains the trained models.
Details on how the OUTPUT Folder can be used is specified inside its README to reduce confusion.

### ```TEST``` folder contains the testing results for each batch of recorded speech.

### ```others``` folder contains the miscellaneuous, not so important files. ( you may skip this folder )
