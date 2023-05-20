# The Levenshtein Distance 

In the field of computational linguistics, the Levenshtein distance, also known as the edit distance, is utilized to compare the similarity between two words or phrases.

The Levenshtein distance between two strings $a$ and $b$, with lengths $|a|$ and $|b|$ respectively, can be calculated using the function $\text{lev}(a, b)$. This function is defined as:

$$
\text{lev}(a, b) = 
\begin{cases}
  |a| & \text{if } |b| = 0 \\
  |b| & \text{if } |a| = 0 \\
  \text{lev}(\text{tail}(a),\text{tail}(b)) & \text{if } a[0] = b[0] \\
  1 + \min \begin{cases}
          \text{lev}(\text{tail}(a), b) \\
          \text{lev}(a, \text{tail}(b)) \\
          \text{lev}(\text{tail}(a), \text{tail}(b)) \\
       \end{cases} & \text{otherwise}
\end{cases}
$$

This is a piecewise function that is defined differently in different parts of its domain. In other words, it's like having multiple functions combined into one.

So, the Levenshtein distance is the minimum number of single-character edits required to transform one string into another. It measures the dissimilarity or difference between two words, where "similarity" is the resemblance between their spellings, pronunciations, meanings, or contexts.

The "distance between words" can be considered as the measure of how many changes are needed to transform one word into another. This can be calculated using various algorithms and techniques depending on the specific application or task.

Here are some examples to illustrate the concept of distance between words using the Levenshtein distance algorithm:

- The Levenshtein distance between "cat" and "hat" is 1 because changing the first letter "c" to "h" is equivalent to a single edit operation (a substitution).
- The Levenshtein distance between "cat" and "dog" is 3 because three edit operations (two substitutions and one deletion) are required to transform "cat" into "dog".
- The Levenshtein distance between "kitten" and "sitting" is 3. This is because the following 3 edits change one into the other, and there is no way to do it with fewer than 3 edits: (1) kitten → sitten (substitution of "s" for "k"), (2) sitten → sittin (substitution of "i" for "e"), and (3) sittin → sitting (insertion of "g" at the end).

To calculate the Levenshtein distance, a script has been created that defines a function called `levenshtein_distance`. This function takes two strings `s` and `t` as inputs, finds the minimum number of operations required to transform the prefix of the first string into the prefix of the second string, and returns an integer representing the Levenshtein distance between them.

<hr>

The Levenshtein distance is a useful tool for detecting fraud. A bank processing a large number of credit card applications can compare new applications to a database of legitimate past applications by calculating the Levenshtein distance. If the distance between a new application and the database exceeds a certain threshold, the bank may suspect fraud and investigate further.
In fact, fraudulent transactions may have slight variations from genuine ones, and the Levenshtein distance can be used to measure the degree of difference between them.

For example, let's say a new application has the following information:

    Name: John Doe
    Address: 123 Main St, Anytown USA
    Income: $50,000
    Employment: Full-time

The bank calculates the Levenshtein distance between this application and the applications in their database.
If they find an existing application with the same name, address, and employment information but a significantly different income, it may indicate that the new application is fraudulent and the income information has been falsified.

However, the Levenshtein distance algorithm is not perfect and may sometimes produce false positives or false negatives, depending on the specific use case and the quality of the data. Therefore, it's important to use this algorithm as a tool in conjunction with other techniques and human expertise to ensure accurate and reliable results.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Requirements
```
Just Python 3.6.9
```

## Test Coverage
| Name                                   | Stmts | Miss | Branch | BrPart | Cover |
|----------------------------------------|-------|------|--------|--------|-------|
| levenshtein_distance.py                 | 21    | 4    | 14     | 1      | 86%   |
| levenshtein_distanceFinanceFraud.py     | 15    | 3    | 8      | 1      | 74%   |
| levenshtein_distanceFinanceFraud_test.py| 19    | 1    | 4      | 1      | 91%   |
| levenshtein_distance_test.py            | 19    | 1    | 4      | 1      | 91%   |
| **TOTAL**                              | **74**| **9**| **30** | **4**  | **86%**|


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



