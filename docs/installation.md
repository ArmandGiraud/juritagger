# Installation


## Stable release

To install juritagger, run this command in your terminal:

```batch

    $ pip install juritagger
```
Download the [spaCy model](https://spacy.io/models/fr#fr_core_news_md)
<br/>
```batch
python -m spacy download fr_core_news_md
```
This is the preferred method to install juritagger, as it will always
install the most recent stable release.

## From sources

The sources for juritagger can be downloaded from the 
[Github repo](https://github.com/ArmandGiraud/juritagger).

You can either clone the public repository:

```batch

    $ git clone git://github.com/ArmandGiraud/juritagger
```

Or download the [tarball](https://github.com/ArmandGiraud/juritagger/tarball/master):

```batch

    $ curl  -OL https://github.com/ArmandGiraud/juritagger/tarball/master
```

Once you have a copy of the source, you can install it with:

```batch

    $ python setup.py install
```
