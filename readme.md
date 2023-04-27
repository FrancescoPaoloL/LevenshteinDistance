# The Levenshtein_distance 
In computational linguistics, the Levenshtein distance, also known as the edit distance, is used to compare the similarity between two words or phrases.

The Levenshtein distance is calculated as the minimum number of single-character edits needed to transform one string into the other. In other words, the distance between words refers to the measure of dissimilarity or difference between two words, if we keep in mind that by "similarity" between two words, we mean the resemblance between their spellings, pronunciations, meanings, or contexts.

Here's a simple example to illustrate the concept of distance between words using the Levenshtein distance algorithm.

```
Consider the two words "cat" and "hat". The Levenshtein distance between these two words is 1 because "cat" can be transformed into "hat" by changing the first letter "c" to "h".

This change is equivalent to a single edit operation (a substitution). Therefore, the distance between "cat" and "hat" is 1.

Similarly, the distance between "cat" and "dog" is 3 because three edit operations 
(two substitutions and one deletion) are needed to transform "cat" into "dog".

```

Other example

```
The Levenshtein distance between "kitten" and "sitting" is 3, since the following 
3 edits change one into the other, and there is no way to do it with fewer than 3 edits:
    1. kitten → sitten (substitution of "s" for "k"),
    2. sitten → sittin (substitution of "i" for "e"),
    3. sittin → sitting (insertion of "g" at the end).
```

We can consider the "distance between words" as a measure of how many changes are needed to transform one word into another.

This can be calculated using various algorithms and techniques, depending on the specific application or task.

To do that, we've made a script which defines a function levenshtein_distance which:
- takes two strings s and t as inputs 
- find the minimum number of operations required to transform  the prefix of the first string into the prefix of the second string; and
- returns an integer representing the Levenshtein distance between them. 

[WIP]


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Requirements
```
Just Python 3.6.9
```
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



