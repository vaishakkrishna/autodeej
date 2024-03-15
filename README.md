# autodeej


## Installation
Install deps: `cat requirements.txt | xargs -n 1 pip install`

Prerequisites:
- Python3.10
- [portaudio](https://www.portaudio.com)


Madmom installation causes issues with this python version. To fix it, go to where the package is installed (`site-packages/madmom/processors.py`) and change 
`from collections import MutableSequence`
to 
`from collections.abc import MutableSequence`