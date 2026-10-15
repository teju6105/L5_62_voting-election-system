# Lab 5: Static Code Analysis â€” Issues and Fixes



**Project:** Voting and Election Management System  

**File analyzed:** `election_system.py`  

**Tools used:** Pylint, Bandit, Flake8



## Issue Table



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| Weak MD5 hashing | Security â€” High | Voter registration function | The original code used MD5 to hash voter identifiers. MD5 is considered cryptographically weak. | Replaced MD5 with SHA-256 using `hashlib.sha256()`. |

| Suspicious bidirectional Unicode characters | Security â€” High | Officer-checking function | The original function contained suspicious Unicode characters that could make the source code misleading. | Replaced the function with a clear role comparison using `is_officer()`. |

| Unsafe XML parsing | Security â€” Medium | Postal ballot import function | The original code used an XML parsing implementation that raised security concerns. | Switched to `defusedxml.pulldom` for safer XML processing. |

| Hardcoded administrator password | Security â€” Medium | Global configuration | The original code contained an administrator password directly in the source file. | Replaced the hardcoded value with an environment-variable lookup using `os.environ.get()`. |

| Weak receipt generation | Security â€” Low | Receipt generation function | The original code used `random.randint()` to generate receipt identifiers. | Replaced it with `secrets.randbelow()`. |

| Duplicate voting | Logic error | Vote-casting function | A registered voter could cast multiple votes through the normal voting function. | Added a check for the voter's `voted` status and marked the voter as having voted after accepting a vote. |

| Voting after closing time | Logic error | Vote-casting function | Votes submitted at or after the configured closing hour were accepted. | Added a check against `POLLS_CLOSE_HOUR`. |

| Division by zero | Logic error | Percentage and turnout functions | Percentage calculations could fail when the ballot list or registered-voter collection was empty. | Added checks for empty collections before calculating percentages. |

| Incorrect announcements | Logic error | Announcement function | The original lambda-based implementation could repeatedly display incorrect candidate information. | Replaced it with a list comprehension that retrieves each candidate's actual vote count. |

| Unused imports and variables | Code quality | Multiple locations | Some imported modules and local variables were not used. | Removed unused imports and variables. |

| Formatting violations | Style | Multiple locations | The original file contained spacing, blank-line, and newline violations. | Corrected formatting and verified the file using Flake8. |



## Final Static Analysis Results



| Tool | Original result | Final result |

|---|---|---|

| Pylint | 5.33/10 | 10.00/10 |

| Bandit | Multiple findings | Zero issues identified |

| Flake8 | Multiple violations | Zero violations reported |



## Report Files



\- `pylint_report_before.txt`

\- `pylint_report_after.txt`

\- `bandit_report_before.txt`

\- `bandit_report_after.txt`

\- `flake8_report_before.txt`

\- `flake8_report_after.txt`


