# ml-am-lm-cmusphinx
Instructions to use this Model for demo purpose ( I recommand using Unix-like enivironment ).

Firstly download the latest libraries needed to run the recognition:

1. [SphinxBase](http://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha)

2. [PocketSphinx](http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha)

3. [SphinxTrain](http://sourceforge.net/projects/cmusphinx/files/sphinxtrain/5prealpha)

4. [Sphinx4](http://sourceforge.net/projects/cmusphinx/files/sphinx4/5%20prealpha)

For more details head over to [CMUSphinx Download](http://cmusphinx.sourceforge.net/wiki/download)

Once you have downloaded, extracted to their corresponding folder, install them using:

In a unix-like environment (such as linux, solaris etc):
 * if you downloaded directly from the CVS repository, you need to do
   this at least once to generate the "configure" file:
  ```
  $ ./autogen.sh
  ```

 * if you downloaded the release version, or ran "autogen.sh" at least
   once, then compile and install:
  ```
   $ ./configure
   $ make clean all
   $ make check
   $ sudo make install
   ```

Now, download the zip of this repository, extract and open terminal inside the root folder.

Connect the microphone and use the command below to run the recognition.
I cannot assure accuracy as of yet as this a trail attempt towards building a more spanned model.
```
pocketsphinx_continuous -hmm ./ -lm samsaaram.arpa -dict samsaaram.dic -inmic yes | tee ml_terminal_output_export.txt
```

####Note:
> The installation of libraries can throw many errors depending on the various dependencies of ```autogen``` , ```configure``` , ```make``` . Make sure to patiently resolve those to have a successful installation. Also make sure to set the path variables in the environment.

> Audio driver package(s) (```osspd``` generally) of your system might need updation while launching the command : 
>```
>pocketsphinx_continuous
>``` 

> Try this and all should probably run fine after.
>```
>sudo apt-get update
>sudo apt-get install osspd
>```

## To contribute 
1. Fork this repository.
2. Record* the sentences^
3. Commit and make a Pull Request.

####Note:
> Record* - To record, use [Audacity](www.audacityteam.org/download/) , set Project Rate = 16000Hz, Default Sample Format as 16bit, and while saving, use WAV, PCM 16bit option

> sentences^ - The sentences [file](/Further development files/hugu+interstellar+queen - sentences.txt) can be found inside the file "hugu+interstellar+queen - sentences.txt" under Further Development.

> Please contact me before you start recording.
