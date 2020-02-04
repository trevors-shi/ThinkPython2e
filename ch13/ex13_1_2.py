"""
Chapter 13, Exercise 1.2
From Think Python, 2nd Edition
http://greenteapress.com/thinkpython2/html/thinkpython2014.html
---

Go to Project Gutenberg (http://gutenberg.org) and download your favorite out-of-copyright book in plain text format.

Modify your program from the previous exercise to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.

Then modify the program to count the total number of words in the book, and the number of times each word is used.

Print the number of different words used in the book. Compare different books by different authors, written in different eras. Which author uses the most extensive vocabulary? 
"""
import sys
sys.path.append('ch13/')

import ex13_1_1 as wg

def word_count_dict(word_gen):
    wc_dict = {}
    
    for word in word_gen:
        word_lower = word.lower()
        wc_dict[word_lower] = wc_dict.get(word_lower, 0) + 1

    return wc_dict

if __name__ == '__main__':

    word_gen = wg.read_file('text/sherlock_1661-0.txt', skiplines=32)
    counts = word_count_dict(word_gen)

    print("{} unique words found".format(len(counts)))
