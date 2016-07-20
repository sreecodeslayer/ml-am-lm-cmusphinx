## How to run the models for recognition

> <u>Note</u>:
>
> Before running the recognition, <b>make sure you have installed all the sphinx related executables as well as dependencies mentioned in the source </b> [README](https://github.com/sreecodeslayer/ml-am-lm-cmusphinx/blob/master/README.md).>
>

1. Open up the terminal in this root directory or ```cd``` your way through.
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

