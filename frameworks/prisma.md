---
title: PRISMA
---

# PRISMA: documenting a literature search

PRISMA is how we report a literature search in this course. A documented search lets someone else rerun it and get roughly the same set of papers, and the PRISMA flow diagram shows every number from the first hits to the papers you kept. Checkpoint 1, part 2 asks for both. We work through it in Class 3 ({% include classdate.html n="3" fmt="medium" %}).

## From a question to a search

### OR inside a concept, AND between concepts

Split your question into 2-4 concepts and list synonyms for each. Join the synonyms with OR, and the concepts with AND.

Example question: How does accent affect speech recognition accuracy?

| Accent | Recognition | Outcome |
| :---- | :---- | :---- |
| accent | "speech recognition" | accuracy |
| dialect | ASR | "error rate" |
| "non-native" | "automatic speech recognition" | WER |

`(accent OR dialect OR "non-native") AND ("speech recognition" OR ASR OR "automatic speech recognition") AND (accuracy OR "error rate" OR WER)`

### Where speech technology research is indexed

| Source | What you'll find there | Note |
| :---- | :---- | :---- |
| ISCA Archive | Interspeech and other ISCA events | Free; the core of our field |
| IEEE Xplore | ICASSP, IEEE/ACM TASLP | Via the UG library |
| ACL Anthology | ACL, EMNLP, NAACL and other NLP venues | Free |
| ACM Digital Library | CHI, CSCW, FAccT | HCI and fairness work |
| Scopus, Web of Science | Journals across disciplines | Best for documented Boolean searches |
| arXiv (eess.AS, cs.CL) | Preprints | Not peer reviewed: log them separately |

Health or perception questions: add PubMed or PsycINFO.

### Google Scholar searches can't be repeated

- **256 characters:** the longest query Google Scholar accepts, too short for most structured searches
- **1,000 results:** the most you can view for any query, however many it finds
- **No export or log:** no reliable way to export a full result set or rerun the same search later

Use it to get oriented and to chase citations. Don't use it as your main documented search. Sources: Bramer et al. (2016), *Systematic Reviews* 5:39; Gusenbauer and Haddaway (2020), *Research Synthesis Methods*.

### Criteria someone else could apply

An example for the accent question:

- **Include:** published 2015 or later; empirical evaluation of an ASR system; reports error rates by accent group
- **Exclude:** no breakdown by accent; abstracts or posters without results; duplicate versions of the same study

Every criterion needs a reason you could defend: why 2015, why only empirical work? If a classmate sorts a title differently from you, the criteria need sharpening, not your classmate.

## Run, log and count

### Log each search as you run it

Record the database, the date, the exact string, any filters and the number of hits. Use your own copy of the [search log template](https://docs.google.com/spreadsheets/d/10lVOSnlg8q8xI0CnXCMTcTmXghzxeEKMmJsQ9ph3E7k/copy); its PRISMA counts tab adds up the numbers for the flow diagram.

| Database | Date | Exact string | Filters | Hits |
| :---- | :---- | :---- | :---- | :---- |
| Scopus | 9 Feb 2027 | `TITLE-ABS-KEY((accent OR dialect) AND ("speech recognition" OR ASR))` | 2015-2027; English | 412 |
| ISCA Archive | 9 Feb 2027 | `accent speech recognition` | none | 238 |

The numbers above are illustrations.

### Change one thing at a time

- **Too many:** add a concept with AND, search title and abstract only, or narrow the dates
- **Too few:** add synonyms with OR, drop the least essential concept, check spelling variants such as non-native and nonnative
- **Off topic:** put phrases in quotes; use NOT only for terms you're sure about

Log each change and its new hit count, so you can explain why the final string looks the way it does.

## The PRISMA 2020 flow diagram

The diagram has three stages. Fill in every number.

**Identification**

- Records identified, per database (n = )
- Removed before screening: duplicates (n = )

**Screening**

- Records screened, title and abstract (n = )
- Records excluded (n = )
- Full texts assessed for eligibility (n = )
- Full texts excluded, with reasons (n = )

**Included**

- Studies included (n = )

Templates are at [prisma-statement.org](http://prisma-statement.org/). A hand-drawn diagram is fine for Checkpoint 1.

## References

Bramer, W. M., Giustini, D., & Kramer, B. M. R. (2016). Comparing the coverage, recall, and precision of searches for 120 systematic reviews in Embase, MEDLINE, and Google Scholar: A prospective study. *Systematic Reviews, 5*, 39. <https://doi.org/10.1186/s13643-016-0215-7>

Gusenbauer, M., & Haddaway, N. R. (2020). Which academic search systems are suitable for systematic reviews or meta-analyses? Evaluating retrieval qualities of Google Scholar, PubMed, and 26 other resources. *Research Synthesis Methods, 11*(2), 181-217. <https://doi.org/10.1002/jrsm.1378>

Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. <https://doi.org/10.1136/bmj.n71>

*Prepared for Research Design (MSc Speech Technology), University of Groningen*
