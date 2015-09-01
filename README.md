# PyPhonT<sup>2</sup>

## Python Phonetics Transcription Tool

## Project Description
PyPhonT<sup>2</sup> is a command line tool for translating words and groups of words into their [Iternational Phonetic Alphabet (IPA)](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) transcriptions, and (<i>hopefully</i>) vice versa.

This is NOT meant to translate from one language to another; I will not be including the functionality to translate between English and Spanish, for example. Translations will be from and to IPA or from and to Arpabet.

## Installation
Coming Soon!

## Usage
```bash
    pyphont <input language> [input file] <output language> <output file>
    
    $ pyphont -eng input.txt -ipa output.txt    # -eng Input --> -ipa Output
    $ pyphont -spa input.txt -arp               # -spa Input --> -arp Stdout
    $ pyphont input.txt                         # -eng (default) Input --> -ipa (default) Stdout
    
    $ pyphont --help
```

## Acknowledgments
Coming Soon!

## Contact

Benjamin S. Meyers < <lion.logic.org@gmail.com> >

## Licensing

The MIT License (MIT)

Copyright (c) 2015 Benjamin Meyers < <lion.logic.org@gmail.com> >

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
