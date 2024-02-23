<p align="center">
<picture>
  <img src="https://github.com/Neocky/Text2McBook/assets/13088544/e138462c-8ecd-4a6f-ad68-aeb77764fee1" alt="Lorem ipsum preview book" height="300px">
</picture>
</p>

<h1 align="center">
  Text2McBook
</h1>

📚 Convert any textfile to a formatted text for minecraft books to use them as easily as possible ingame.

## Issues? Found a bug?

[Create an issue.](https://github.com/Neocky/Text2McBook/issues/new/choose) 

## About

This script will convert text from a textfile to a formatted minecraft book file. The file contains a native `/give` command which can be used ingame to get a `writable_book` with the text as content.  
It supports different book formats which can be choosen with the parameter [`-f FORMATNAME`](https://github.com/Neocky/Text2McBook#parmaters).  
I got inspiration from a post from [r/admincraft](https://www.reddit.com/r/admincraft/).

### Default

The `default` format will create a `/give` command which can be easily copied into a command block ingame to get the writable book.
It will also format the text in a way in which it can be easily copy and pasted in a book in the game. 

### Denizen

[Denizen](https://denizenscript.com/) is a scripting plugin for minecraft servers.  
The `denizen` format will format the text for the `text` property in [Book Script Containers](https://meta.denizenscript.com/Docs/Search/book#book%20script%20containers). It will replace new line symbols with `<n>` and indents the line with 4 spaces to make it easily pasteable in the `text` properties of `book script containers`.  

## Installation

### Python

Python (minimum: Version 3.10.4) needs to be installed on your machine.  
Get it [here](https://www.python.org/downloads/).

### Clone the repository / Download the latest release

Download the script:  
Clone the repository or get the latest release [here](https://github.com/Neocky/Text2McBook/releases).

## Usage

Create/edit the textfile in the same folder where the python script is with the name: `text.txt` and add your book text in there.  
This is the text that you want to be converted to a minecraft book format.  
Run the script: `text2mcbook.py`.  
Now a `booktext.txt` file should be created.  
In there is a `/give` command which can be inputted into a command block to get the book. There is also the formated text which you can easily copy & paste in a book in minecraft.


## Advanced Usage

### Parmaters

This script supports the following parameters to change the usage for the script.

#### Get help about all available parameters

```shell
py text2mcbook.py -h
```

#### Input file

```shell
py text2mcbook.py INPUTFILENAME
```

Default: `text.txt`  
Changes the input file.

#### Output file

```shell
py text2mcbook.py INPUTFILENAME OUTPUTFILENAME
```

Default: `booktext.txt`  
Changes the output file.

#### Book format

```shell
py text2mcbook.py -f FORMAT
py text2mcbook.py --format FORMAT
```

Default: `default`  
Possible Values: `default`, `denizen`  
Changes the book format and the resulting formatting.

#### Characters per line

```shell
py text2mcbook.py -c NUMBEROFCHARACTERSPERLINE
py text2mcbook.py --characterlimit NUMBEROFCHARACTERSPERLINE
```

Default: `19`  
The number of characters one book line can have.  
Warning: Don't set it to high or you are risking the loss of words!

### Examples

#### Example 1
```shell
py text2mcbook.py book_to_convert.txt book_formatted.txt
```

Changes the input file to `book_to_convert.txt` and outupts the formatted book text to `book_formatted.txt`.

#### Example 2

```shell
py text2mcbook.py -f denizen -c 20
```

Outputs denizen formated text, which can be used in the `text` propert of [Book Script Containers](https://meta.denizenscript.com/Docs/Search/book#book%20script%20containers) in [Denizen](https://denizenscript.com/). Also changes the number of characters per line to 20. 
