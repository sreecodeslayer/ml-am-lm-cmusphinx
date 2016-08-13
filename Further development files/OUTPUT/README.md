# About this Directory
This directory is setup with ```Google Summer of Code 2016``` submission in mind. So here goes, on how the project can be used as such or for reference on how it looks after development.

## Instructions or Key points
* Two sub-directories : ```am``` and ```lm```
* The ```am``` folder contains the Acoustic Model result parameters.
* The ```lm``` folder contains the Language Model as well as the Dictionary file required to run the recognition which is explained later in this README.
* These files are not for development. If that's what you are looking for then go [here](https://github.com/sreecodeslayer/ml-am-lm-cmusphinx/tree/master/Further%20development%20files) or go to the parent directory of ```OUTPUT```.
* To develop Language Model, you may read [this](https://medium.com/@imSreenadh/developing-the-language-model-64f63dbd932d#.balumhc8e) or the [official CMU Sphinx wiki](http://cmusphinx.sourceforge.net/wiki/tutoriallm)
* To develop Acoustic Model, you may read [this](https://medium.com/@imSreenadh/he-just-recognized-what-i-said-826b2ee32b78#.2teapf68g) or the [official CMU Sphinx wiki](http://cmusphinx.sourceforge.net/wiki/tutorialam)
* To get a more clear idea on how to proceed your way through the develop, I recommend reading my blog posts on [Medium](http://medium.com/@imSreenadh)
* Setting up your development environment is rather straight forward. Even then if you have any hickups, please consider reading the [root README.md](https://github.com/sreecodeslayer/ml-am-lm-cmusphinx/blob/master/README.md)

## How to run the models for recognition

> <u>Note</u>:
>
> Before running the recognition, <b>make sure you have installed all the sphinx related executables as well as dependencies mentioned in the source </b> [README](https://github.com/sreecodeslayer/ml-am-lm-cmusphinx/blob/master/README.md).>
>

1. Open up the terminal in this root directory or ```cd``` your way through upto this.
2. Type in the command:
	```
	$ pocketsphinx_continuous -hmm ./am/ -lm ./lm/ml.arpa -dict ./lm/ml.dic -inmic yes

	```
	>
	> Note:
	> The output on the terminal is a bit sketchy since Malayalam is not supported. A workaround would be to pipe an export ( the output which is the hypothesis from pocketsphinx ) to a text file.
	>
	
	```
	$ pocketsphinx_continuous -hmm ./am/ -lm ./lm/ml.arpa -dict ./lm/ml.dic -inmic yes | tee hypothesis.txt

	```

> <u>Note</u>:
> This model can also be used for making Android Malayalam Speech Recognition applications. For more details, you can visit [here.](https://github.com/sreecodeslayer/Samsaaram)
