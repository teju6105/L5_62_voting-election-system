# Lab 5: Static Code Analysis â€” Reflection



**Project:** Voting and Election Management System  

**Tools used:** Pylint, Bandit, Flake8



## 1. What is the importance of static code analysis?



Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, unused variables, and coding-style violations. In this lab, Pylint helped improve code quality, Bandit identified security concerns, and Flake8 detected formatting problems.



## 2. What issues did you identify and fix?



I identified several issues in the original voting and election management program. These included weak MD5 hashing, a hardcoded administrator password, potentially unsafe XML parsing, weak receipt generation, suspicious Unicode characters, and duplicate-voting logic. I also corrected formatting problems, removed unused imports and variables, and improved function names and documentation.



## 3. How did the static-analysis tools help improve your code?



The tools helped me identify problems that were difficult to notice through manual inspection alone. After making the changes, Pylint reported a score of 10.00/10, Bandit reported zero issues, and Flake8 reported no violations. These results demonstrate improvements in the code quality, security checks, and formatting detected by the tools.



## 4. What did you learn from this lab, and what would you improve in the future?



I learned that static analysis is an important part of software development because it helps identify problems early and encourages maintainable coding practices. In the future, I would add automated unit tests, improve administrator authentication, validate malformed XML input more thoroughly, and test additional voting scenarios. I would also review the election logic carefully before considering the application suitable for real-world use.


