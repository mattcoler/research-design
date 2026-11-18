---
title: TIPS
section: Content
parent:
  title: Frameworks
  url: /frameworks/
---

# The TIPS framework for evaluating research gaps

## What is TIPS?

TIPS is the framework we use in this course to decide whether a gap in the literature is worth a master's thesis. Finding something nobody has studied is easy. Finding something worth studying, that you can actually do, is the hard part. A strong gap scores well on:

- **T**heoretical significance
- **I**mpact potential
- **P**ractical feasibility
- **S**trategic positioning

FARES tests your research question, MERC tests the papers you read, and TIPS tests the gap that connects them.

## Why "nobody has done this" isn't enough

Absence of research is not a reason to do research. Some combinations are unstudied because nobody would learn anything from them. Sandberg and Alvesson (2011) reviewed 52 articles and found that spotting gaps is by far the most common way researchers build their questions, and they argue that questions which challenge an assumption in existing work tend to produce more interesting results. Keep both routes in mind: filling a gap, or questioning something the field takes for granted.

## The 4 TIPS criteria

### 1/ Theoretical significance

Addressing the gap should change what we understand. One more data point isn't enough.

Considerations:

- Would the answer test, extend, or reconcile existing explanations?
- Do current findings or theories predict anything about it?
- Would a result in either direction be informative?
- Does it resolve a contradiction you found in your synthesis?

**Common problems:** the gap exists only because a particular model-dataset combination hasn't been tried; nothing in the literature predicts what should happen; only one outcome would be interesting.

Example transformation:

Weak: "No study has evaluated model X on Frisian."

Stronger: "Multilingual ASR models are often expected to transfer from closely related high-resource languages. Frisian speakers frequently switch into Dutch, so Frisian is a good test of whether that transfer holds for mixed-language speech."

### 2/ Impact potential

Someone specific should be able to do something differently once the gap is filled.

Considerations:

- Who benefits: users, developers, clinicians, policymakers, other researchers?
- What would they do with the result?
- Does the field's current practice depend on the answer?

**Common problems:** impact claimed for "society" or "everyone"; beneficiaries couldn't act on the result; the result would only interest the researcher.

Example transformation:

Weak: "This will improve speech technology for everyone."

Stronger: "A speaker-group error analysis gives developers of Dutch public-service voice assistants a test set they can run before deployment."

### 3/ Practical feasibility

You must be able to address the gap within a master's thesis, with the data, tools and time you actually have. This is the hard constraint: a gap that fails here doesn't qualify, however interesting it is.

Considerations:

- Can you get the data? Does it need ethics approval, consent, or a data agreement?
- Do methods exist that you can run, with the compute you have?
- Can it be done in the months available for the thesis, including writing?
- Is there supervision available for this topic?

**Common problems:** needs data you can't get (for example clinical recordings without approval); requires training large models from scratch; needs a longitudinal design over years.

Example transformation:

Weak: "Train a new end-to-end model for 20 low-resource languages."

Stronger: "Fine-tune an existing pretrained model on one low-resource language with an available corpus, and compare it with zero-shot performance."

### 4/ Strategic positioning

The gap should fit you: your skills, languages, background, and where you want to go next.

Considerations:

- What do you bring that others working on this might not?
- Who else is likely working on it? Could a large lab publish the answer next month?
- Does it fit your supervisor's expertise and your lab's resources?
- Will it help your next step, in industry or a PhD?

**Common problems:** chosen because it is fashionable; needs skills you can't learn in time; competes directly with well-resourced industry labs.

Example transformation:

Weak: "I'll benchmark the newest large speech model."

Stronger: "With native Mandarin and phonetics training, I can annotate tone errors that automatic metrics miss."

## Using TIPS in practice

### Rate and compare your gaps

1. Write each candidate gap in one or two sentences.
2. Rate each gap on every TIPS criterion: strong, needs work, or weak. Note one reason per rating.
3. Drop any gap that is weak on Practical feasibility.
4. Among the rest, prefer gaps that are strong on Theoretical significance or Impact potential.
5. Compare your 2-3 gaps in a small table. A table is fine in Checkpoint 2, part 3.

### Check the gap is real

Before you commit, search for the exact gap: the last two or three years, including arXiv and recent Interspeech and ICASSP proceedings. Ask who would most likely have done this already, and look at their recent work. If someone has, your gap may become a replication or an extension, which can still be a good thesis.

### Types of gaps to look for

- **Methodological:** current methods can't answer an important question well.
- **Theoretical:** existing explanations don't account for an observed result, or two accounts conflict.
- **Population or context:** findings from one group, language, or setting may not hold in another that matters.
- **Integration:** two research traditions haven't been connected, although each could inform the other.
- **Application:** findings haven't been turned into practice despite clear potential.

In speech technology, watch especially for limits in language and dialect coverage, read versus spontaneous speech, benchmark versus real-world conditions, and ethical questions that new systems raise.

### Writing a gap statement

Use this structure as a starting point:

*"Studies of \[topic\] have examined \[A\] (citations) and \[B\] (citations), but not \[C\]. This matters because \[theoretical significance or impact\]. A master's thesis can address it by \[feasible approach\]. I'm well placed to do this because \[positioning\]."*

Weak: "More research is needed on accents." (No boundaries, no evidence, no reason.)

Stronger: "Studies of accent bias in ASR have compared read speech across English varieties (citations), but not spontaneous speech from non-native speakers in workplace meetings. This matters because meeting transcription is a common deployment... " (and so on through P and S).

### Peer review using TIPS

- Ask for the evidence first: which papers show the gap?
- Take each criterion in turn, and say which is weakest.
- Play the sceptic: "Hasn't X already done this?" "Who would use the answer?" "Could you finish it within the thesis period?"
- Name the problem and suggest a fix.

## Quick reference checklist

**Theoretical significance:** tests, extends or reconciles existing explanations; either result would be informative.

**Impact potential:** named beneficiaries; they could act on the result.

**Practical feasibility:** data accessible; methods runnable; fits the thesis timeline; ethics manageable.

**Strategic positioning:** fits your skills and interests; you bring something others may not; not a race against large labs.

**And:** you've searched for the exact gap in the last two or three years of work.

## Where TIPS is used in this course

- Class 5 ({% include classdate.html n="5" fmt="medium" %}): gap identification and positioning.
- Checkpoint 2, part 3: 2-3 gaps evaluated with TIPS (due {% include deadline.html id="cp2_due" fmt="medium" %}).
- Class 6 onward: your strongest gap becomes the basis for your hypothesis.

## References

Müller-Bloch, C., & Kranz, J. (2015). A framework for rigorously identifying research gaps in qualitative literature reviews. In *Proceedings of the International Conference on Information Systems (ICIS 2015)*, Fort Worth, TX. <https://aisel.aisnet.org/icis2015/proceedings/ResearchMethods/2>

Sandberg, J., & Alvesson, M. (2011). Ways of constructing research questions: Gap-spotting or problematization? *Organization, 18*(1), 23-44. <https://doi.org/10.1177/1350508410372151>

Alvesson, M., & Sandberg, J. (2011). Generating research questions through problematization. *Academy of Management Review, 36*(2), 247-271.

*Prepared for Research Design (MSc Speech Technology), University of Groningen*
