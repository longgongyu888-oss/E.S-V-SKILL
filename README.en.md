# E.S-V SKILL

[中文说明](README.md) · [Design notes and source projects](docs/design-notes.md) · [Test record](docs/tests.md)

E.S-V helps you learn a course from the materials you choose. Start with your instructor’s slides and textbook, or ask for a shortlist of readings first. Once you confirm the sources, the agent draws a course map, teaches the material and checks what you can do independently on a fresh problem. You can ask for lessons in your preferred language.

## Use it with your agent

Choose the setup your agent supports.

| Your agent can… | How to start |
| --- | --- |
| Load an Agent Skills directory | Download this repository. Use your agent’s skill import or installation feature to add the entire [e-s-v folder](skills/e-s-v/), keeping its references alongside SKILL.md. Start a new session if your host requires it, then select **e-s-v** in its skill picker or name it in your request. |
| Read an attached or local file | Download [E.S-V.portable.md](E.S-V.portable.md). Attach it to the chat or give the agent access to the file. Say “Use the attached E.S-V guide to tutor me in this course. Work in English.” Then describe your course and add any materials you have chosen. |
| Accept pasted text | Open the [standalone guide](E.S-V.portable.md) and paste its contents into the chat as instructions. Add “Apply this guide to the course I describe next.” Paste the relevant course excerpts in subsequent messages, keeping slide and page numbers. |

The portable file includes the teaching instructions and reference guides in one document. The guide is written in Chinese. You can request lessons, explanations and feedback in English or your preferred language. In a text-only chat, the agent can draw a visible map with branch characters and labelled arrows, then deliver the lesson and practice in the conversation. Web access enables it to verify video and reading links. File generation enables a DOCX handout for WPS. Ask the agent to identify which files it created and which pages or media it could open.

### Optional installation for Codex

With Node.js and the Skills CLI available, run the following command. You can then invoke the skill in a new Codex chat with `$e-s-v`.

```sh
npx skills add longgongyu888-oss/E.S-V-SKILL --skill e-s-v -a codex -g
```

## Try it on a course

**Choose a reading path**

> I’m studying epigenetics for the first time. Help me choose a textbook, a review and a classic methods paper. Tell me what each covers and which chapters or figures to read. Wait for my selection, then show me the course map and teach the first lesson.

**Study from materials you have already chosen**

> Use my instructor’s slides and the textbook I attached. I have five days. Start with the course map, then explain each chapter so I can study from your handout. Put the slide reference beside each topic. For the difficult mechanisms, include a published diagram and a short video with a question to answer as I watch. Give me a separate answer key. Please deliver a WPS-compatible DOCX if you can generate files.

**Work on a specific mistake**

> I can calculate eigenvalues, but I keep misjudging whether a matrix is diagonalizable. Give me one example to diagnose the mistake. After I explain my reasoning, change the matrix and check me again.

## What a lesson looks like

An opening map for a short linear algebra lesson can fit in a plain-text chat.

```text
When does Ax = b have a solution?
├─ Geometry → the columns span a space → does b lie in it?
└─ Elimination → reduce the augmented matrix → do any rows contradict?
```

Suppose the columns of a matrix are (1, 2) and (2, 4). Can the system *Ax = b* reach (3, 6)? Three copies of the first column give (3, 6). Every combination of the columns lies on the line *y = 2x*, so changing the target to (3, 7) makes the system inconsistent.

For a fresh test, change the columns to (1, 3) and (2, 6). Which of (4, 11) and (4, 12) can you reach? Write down the new line, then use elimination to check your reasoning. The [test record](docs/tests.md) includes the answers and examples from other subjects.

## What has been checked

The project’s development tests covered material selection, map construction, teaching examples and feedback in epigenetics, linear algebra, circuit physics and history. The epigenetics pilot used ten instructor slide decks to build a course map and a focused sample lesson. The [test record](docs/tests.md) gives the scope of each check and the revisions it prompted. Installation and document rendering depend on the host and its available tools.

## License

The original skill is distributed under the [MIT License](LICENSE). Course materials and third-party illustrations retain their respective licenses.
