# Resume Repository - Mark Young

## Purpose

This repo contains Mark Young's master resume and tooling to customize it per job application. The application reads `resume.md` as the source of truth and tailors the content to match a specific job's requirements.

## Files

- `resume.md` — Master resume. Full work history, skills, and education. This is the input to the customization application.
- `resume.master.txt` — Original raw resume data (reference only).

## Application Design (planned)

- Input: `resume.md` + a job description
- Output: a tailored resume that emphasizes relevant experience, reorders or trims sections, and aligns language to the job posting
- Approach: model-first — use an LLM agent to do the tailoring, not hand-written rules

## About Mark

Senior Software Engineer with 25+ years of experience across financial data systems (Citadel, Jump Trading), game publishing infrastructure (Blizzard/Microsoft), and data engineering (Buckstop Labs). Strong in Python, SQL, C++, DevOps, and technical leadership. Focused on roles where LLMs and AI agents are central to how software is built and operated.
