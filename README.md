# Description 
Roman number converter is able to convert the Roman number to numeric number or convert the numeric number to Roman number Depending on the request type.

# Request type
The program will prompts the user for an input with **How can i help you?**. the accepted input are one of the three possible kinds:
* Please convert ***
* Please convert *** using ***

if input is not of those kind. the program will print out:

* I don't get what you want, sorry mate!

## First kind of input -> Please convert ***
*** is a strictly positive integer that can be converted to a Roman number or a valid Roman number that can be converted tp a integer. The return response are:
* Hey, ask me something that's not impossible to do! (the input format is not right)
* Sure! It is *** (*** is either expected roman number of integer)

## Second kind of input -> Please convert *** using ***
The first *** is either a strictly positive integer or a sequence of letters. The second *** is a sequence of distinct letters.

* The second *** represented a sequence of generalised roman symbol. The classical Roman symbols corresponding to the sequence MDCLXVI, whose rightmost element is meant to represent 1, the second rightmost element, 5, the third rightmost element, 10, etc.
* If the first *** is not an integer, the first *** represent generalised Roman number, that is, a sequence of generalised Roman symbols that can be decoded using the provided sequence of generalised Roman symbols similarly to the way Roman numbers are represented. 

the return response are:
* Hey, ask me something that's not impossible to do! (the input format is not right or if it is not possible to convert the first *** from Arabic to generalised Roman or from generalised Roman to Arabic)
* Sure! It is *** (If the input is as expected and the conversion can be performed)

# Language
python

# How to use
clone the file to the local computer and simply hit python3 roman_arabic.py


