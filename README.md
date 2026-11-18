# Research Design course site

Public course site for Research Design, MSc Speech Technology, University of Groningen Campus Fryslân.

Live site: https://mattcoler.github.io/research-design/

The site holds the course material that stays stable from year to year. BrightSpace holds everything specific to one cohort (announcements, submissions, FeedbackFruits, grades, rooms) and is authoritative if the two differ.

## How the site is built

GitHub Pages builds the site automatically with Jekyll every time something is committed to the `main` branch. It takes a minute or two. There's nothing to install.

| What | Where |
| :---- | :---- |
| All dates (classes, field trip, deadlines) | `_data/schedule.yml` |
| Home page (course details and how the course works) | `index.md` |
| Syllabus, including the AI policy | `syllabus.md` |
| Schedule page (built from the dates file) | `schedule.md` |
| Content hub | `content.md` |
| Assignment briefs | `assignments/` |
| FARES, PRISMA, MERC, TIPS, peer review guidelines | `frameworks/` |
| Games | `games.md` |
| Frozen copies of each year's briefs (made at release time) | `archive/<year>/` |
| Menu | `_data/navigation.yml` |
| Look and layout | `_layouts/default.html`, `assets/css/style.css` |

## Editing a page

1. Open the file on github.com and click the pencil icon.
2. Make the change. Pages are plain Markdown: `#` for headings, `-` for bullet points, `**bold**`.
3. Click **Commit changes**. The live site updates a minute or two later.

Leave the bits in `{% ... %}` and `{{ ... }}` alone. They pull in dates and links. For example `{% include classdate.html n="9" %}` prints the date of Class 9, and `{% include deadline.html id="cp2_due" time="y" %}` prints the Checkpoint 2 deadline with its time. The ids are listed under `deadlines:` in `_data/schedule.yml`.

## Rolling over to a new year

Do this once the old year is over and before you change any dates.

1. **Freeze the old briefs.** Ask Claude (or run `python3 scripts/render.py freeze 2026-27` on a computer with Python) to write a copy of each brief with its dates spelled out into `archive/2026-27/`. Commit it.
2. **Tag the release.** On github.com go to **Releases → Draft a new release**, type the year (for example `2026-27`) as a new tag, and publish. The tag is a permanent snapshot of every file.
3. **Change the dates.** Edit `_data/schedule.yml`: the year labels at the top, every class date, the field trip and every deadline. Nothing else needs a date change.
4. Update the briefs' content if the course itself changed.

## Licence

Course text: © Matt Coler, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Site code: MIT, see `LICENSE`. The LEGO challenge is adapted from the LEGO® Metadata for Reproducibility game pack by Mary Donaldson and Matt Mahon (University of Glasgow), CC BY 4.0.
