---
title: Syllabus
---
{%- assign s = site.data.schedule -%}
{%- assign first = s.classes | first -%}
{%- assign last = s.classes | last -%}

# Research Design syllabus {{ s.academic_year }}

## Course details

Research Design, MSc Speech Technology {{ s.academic_year }}

Lecturer: Assoc. Prof. Dr. Matt Coler

Course code: [{{ s.course_code }}](https://ocasys.rug.nl/{{ s.academic_year }}/catalog/course/{{ s.course_code }}) \| Level: Master \| Credits: 5 EC

## Introduction

Research Design equips you with skills in research methodology tailored for speech tech. You learn to formulate research questions, conduct systematic lit reviews, design sound methodologies, and communicate your research effectively.

This seminar takes an interactive, discussion-based approach. With a small cohort, we focus on structured activities and collaborative learning. Throughout the block you encounter game-based learning experiences designed to make abstract research concepts tangible and memorable.

The small cohort also serves a strategic purpose: you are piloting collaborative approaches and peer review systems that must scale to larger cohorts in future years. Your feedback on what works and what creates real learning directly shapes how this course evolves.

By the end of this course, you produce a complete research proposal on a speech technology topic of your choice. This proposal serves as a springboard for your master's thesis. Along the way, you gain experience in peer review, academic writing, and research ethics, all skills fundamental to careers in industry or academia.

Detailed information about the pedagogical approach, learning theory foundations, research supporting the course design, and the Course Learning Outcomes is in BrightSpace under "Course information".

## Course structure

The course runs over 7 teaching weeks with two 105-minute classes per week. Classes run from {{ first.date | date: "%-d %B" }} to {{ last.date | date: "%-d %B %Y" }}, on {{ s.days }}, {{ s.time }}. On {% include tripdate.html fmt="medium" %} we attend {{ s.fieldtrip.name }} in {{ s.fieldtrip.place }}, which replaces the {% include tripdate.html which="replaces" fmt="medium" %} class, so there are {{ s.classes.size }} classes plus the field trip. The final research proposal is due in the first week of the exam period.

The course uses a collaborative seminar structure organized into five sequential units that mirror the research lifecycle. You develop your research proposal through iterative cycles of work, peer consultation and feedback, with each unit building on the previous one.

Most classes follow the same rhythm: a 15-minute introduction, a 30-minute activity, a 15-minute break, a second 30-minute activity, and a 15-minute wrap-up. We sit in a circle, and slides serve as talking points for discussion.

Game-based activities run through the course: an ethics card game (Class 7), the LEGO reproducibility challenge (Class 11), and the Research Futures challenge at the poster session (Class 13). More information is in BrightSpace.

## Practical information

Lecturer: Dr [M. Coler](mailto:m.coler@rug.nl). Feel free to talk to me before or after class. General questions about procedures can go to the [Educational Secretariat & SSD CF](mailto:cf-sec@rug.nl).

### Sources

We use open access material and resources as much as possible. University of Groningen students also have access to study materials through the university library via [SmartCat](https://libguides.rug.nl/SmartCatNed).

### BrightSpace

BrightSpace is our platform for communication. Announcements about schedule or content changes are published there. You will also find quick links to [SmartCat](https://libguides.rug.nl/SmartCatNed) and University of Groningen tools such as [Ocasys](https://ocasys.rug.nl/), Enrollment and Photo, and [wireless printing](https://student.portal.rug.nl/infonet/studenten/ict/printen/). All essential course information is in this syllabus; check BrightSpace for up-to-date details.

### Cheating and plagiarism

Be transparent about where ideas come from, and show that you can identify and use academic sources in your own work. Indicate clearly where and when you rely on the work of others. Cheating and plagiarism can be academic offenses with severe consequences. Cases are reported to the Board of Examiners, which decides on the consequences. All assignments are checked for plagiarism by default.

### Use of AI in education

We develop class guidelines together in Week 1, based on your experiences and the university's [baseline policies](https://www.rug.nl/about-ug/organization/quality-assurance/education/artificial-intelligence-ai/). These guidelines are refined throughout the block as we engage with ethical considerations in research. All AI use must be transparent, critically evaluated, and support your independent thinking without replacing it.

### Attendance

The curriculum assumes you attend and participate in all classes. If you cannot attend because of unforeseeable circumstances such as illness, let me know as soon as possible so we can arrange remote attendance.

### Student support and well-being

If you need support during your studies, the UG offers a range of [student support](https://student.portal.rug.nl/infonet/studenten/studenten-welzijn/). Finding the right service can be a challenge, so see [who to contact](https://student.portal.rug.nl/infonet/studenten/studenten-welzijn/bij-wie-kan-ik-terecht2). Your first point of contact is often your study advisor, [Hieke Hoekstra](mailto:h.hoekstra@rug.nl); these conversations are confidential. More information on extra support facilities, and how to apply, is [here](https://student.portal.rug.nl/infonet/studenten/voorzieningen/studenten-service-centrum/extraordinary-circumstances/).

## Weekly schedule

The course follows a five-unit structure across {{ s.classes.size }} classes and a field trip. Preparation assignments, learning objectives, readings and submission deadlines for each class are in BrightSpace.

### Unit 1: Research foundations (Week 1, Classes 1-2)

Understanding research as conversation, positioning yourself in the field, and developing focused RQs. You learn what makes research meaningful and how to situate your work within existing scholarship.

### Unit 2: Literature mastery (Weeks 2-3, Classes 3-5)

Systematic lit discovery, critical analysis, and synthesis. You develop search strategies (PRISMA), apply an analytical framework (MERC), and identify meaningful research opportunities with the TIPS framework.

### Unit 3: Hypothesis development (Week 3, Class 6)

Transforming research gaps into testable predictions w/ theoretical grounding, and planning how the sections of your proposal connect.

### Unit 4: Research design (Weeks 4-5, Classes 7-9)

Integrating ethics into methodology, selecting and justifying methods, assessing feasibility and risk, and designing pilot studies. Features an ethics card game and an intensive peer review of Checkpoint 2 using FeedbackFruits.

### Unit 5: Research communication (Weeks 6-7, Classes 10-13)

Translating research for academic and public audiences through academic writing and revision, reproducibility and data management (LEGO challenge), science communication, and posters. Culminates in a poster session.

### Field trip: {{ s.fieldtrip.name }}

On {% include tripdate.html fmt="medium" %} we attend {{ s.fieldtrip.name }} ({{ s.fieldtrip.short }}) at {{ s.fieldtrip.venue }}. The trip replaces the {% include tripdate.html which="replaces" fmt="medium" %} class. You take field notes during the day and write them up as one page, due {% include deadline.html id="dust_notes" fmt="medium" %}; the field notes count towards participation. Class 8 ({% include classdate.html n="8" fmt="short" %}) explains what is expected.

### Class overview

{% include class-table.html %}

## Assignments

Your performance is evaluated through two checkpoints, a communication portfolio, a final research proposal, peer review, and ongoing participation. Assignment descriptions, rubrics and exact deadlines are in BrightSpace.

| Component | Weight | Assigned | Due (23:59 unless noted) |
| :---- | :---- | :---- | :---- |
| Checkpoint 1 | 5% | Class 2 ({% include classdate.html n="2" fmt="short" %}) | {% include deadline.html id="cp1_due" fmt="short" %} |
| Peer review of Checkpoint 1 | 5% |  | {% include deadline.html id="cp1_review" fmt="short" %} |
| Checkpoint 2 | 10% | Class 4 ({% include classdate.html n="4" fmt="short" %}) | {% include deadline.html id="cp2_due" fmt="short" %} |
| Peer review of Checkpoint 2 | 5% |  | {% include deadline.html id="cp2_review" fmt="short" %} |
| Communication portfolio: blog post, poster, poster presentation | 20% | Class 8 ({% include classdate.html n="8" fmt="short" %}) | Blog post: {% include deadline.html id="blog_due" fmt="short" %}. Poster PDF: {% include deadline.html id="poster_pdf" fmt="short" %}. Printed poster + presentation: Class 13 ({% include classdate.html n="13" fmt="short" %}, in class) |
| Peer review of communication portfolio | 5% |  | Blog post review: {% include deadline.html id="blog_review" fmt="short" %}. Poster review: Classes 12-13 (in class) |
| Research proposal | 40% | Class 9 ({% include classdate.html n="9" fmt="short" %}) | {% include deadline.html id="proposal_due" fmt="short" %} |
| Participation | 10% |  | Self-assessment: {% include deadline.html id="participation" fmt="short" %} |

Peer review is integrated throughout the course using FeedbackFruits. You give structured feedback on checkpoints and communication materials, which develops your critical evaluation skills and keeps grading manageable as the course scales. Completing the peer review is required for credit on the corresponding peer review component.

Checkpoints, the blog post and the proposal are written directly in Google Docs and shared via BrightSpace, so the full version history is visible.

Checkpoint 1 and the peer reviews are graded for completion. Checkpoint 2, the communication portfolio and the research proposal are graded with the rubric in each brief, which you can see from the day the assignment is set.

Participation is self-assessed. After Class 13 you fill in a short form in BrightSpace, due {% include deadline.html id="participation" fmt="medium" %}. For each of four areas you give yourself 0, 1 or 2 points and write one sentence of evidence: preparation (readings and prep tasks done before class), taking part (in discussions and activities), helping others (feedback and support beyond the required reviews), and the DuST field notes (submitted by {% include deadline.html id="dust_notes" fmt="medium" %}). Your total out of 8 becomes your participation grade. I check it against attendance and what I saw in class, and change it only if it's clearly out of line; if so, we talk first. If you can't come to DuST, tell me beforehand and I'll set an alternative task.

Academic integrity: all work must be your own, w/ proper APA citation. AI tool use must be documented transparently per the class policy we develop in Week 1. Plagiarism results in assignment failure and potential course consequences.
