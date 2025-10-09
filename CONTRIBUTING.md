# 🤝 Contributing to Fullstack2026

Thank you for helping the Fullstack2026 curriculum shine! This guide distills our collaboration habits so every addition stays consistent, friendly, and beginner-focused.

## 🛣️ Quick Contribution Workflow
1. **Fork & Clone** – Keep your main branch clean; branch from `main` with a descriptive name (e.g., `feature/week3-form-validation`).
2. **Sync Often** – Rebase or merge from `main` regularly to avoid conflicts.
3. **Scope Your Work** – Prefer small, focused pull requests with a clear learning objective.
4. **Write & Run Tests** – Use the language-appropriate tooling (pytest, `node --test`, manual DOM checks) before opening a PR.
5. **Open the PR** – Fill in the template, link related issues, and summarise changes with one friendly emoji.
6. **Iterate Promptly** – Address review feedback quickly; add follow-up commits rather than force-pushing when conversations are ongoing.

## 🧾 Pull Request Checklist
- [ ] Update **README.md** and week-specific guides if paths, tooling, or learning outcomes change.
- [ ] Include screenshots/GIFs for front-end updates when feasible.
- [ ] Mention impacted folders and run commands in the PR description.
- [ ] Confirm linters/tests pass locally and note any intentional skips (with reason).
- [ ] Ensure docs cite source files or commands where possible to ease auditing.

## 🐞 Issue Reporting Guidelines
- Provide a concise title plus a detailed description (what happened, what you expected, reproduction steps).
- Tag the relevant week/day and label the issue (`bug`, `enhancement`, `docs`).
- Attach console logs, stack traces, or screenshots when available.
- Suggest a fix or learning outcome adjustment if you have ideas.

## 🧠 Coding Standards Overview
We align with the [Code Quality Standards](README.md) plus the extra details below.

### Python (Weeks 1–2)
- **Style**: PEP 8, snake_case for files/functions, PascalCase for classes.
- **Docstrings**: Google-style with examples for every public module, class, and function.
- **Error Handling**: Guard user input with `try/except`, surface actionable messages, and avoid leaking stack traces unless `--debug` is provided.
- **Structure**: Use `if __name__ == "__main__":` guards, factor repeated logic into helpers, prefer pure functions.
- **Tooling**: Run `flake8` and `pytest` (when tests exist). Future additions should include type hints to satisfy `mypy`.

### JavaScript & TypeScript (Weeks 3–5)
- **Modules**: Use ES modules (`import`/`export`).
- **Naming**: camelCase for variables/functions, PascalCase for classes and React components.
- **Documentation**: Add JSDoc to public APIs (functions, classes, modules) describing params, return values, and examples.
- **Error Handling**: Wrap DOM and async logic in `try/catch` or `.catch` blocks; validate user-provided data before use.
- **Tooling**: Run ESLint/Prettier (configs coming soon) and `tsc --noEmit` or `ts-node --transpile-only` for rapid feedback.

### Shared Expectations
- Keep content in English; emojis are optional but use them sparingly for clarity 💙.
- Avoid duplicating logic—extract helpers instead.
- Remove unused imports, variables, and files.
- Store sample data in `data/`, keep secrets out of the repo, and rely on `.env` for configuration stubs.

## 📁 Repository Hygiene
- Honour the [`.gitignore`](.gitignore); do not commit `dist/`, `node_modules/`, `__pycache__/`, SQLite databases, or IDE settings.
- When renaming folders, update all references in documentation and code.
- Prefer `pathlib` (Python) and `URL`/`new URL()` (JS/TS) for path manipulations.

## ✅ Submitting Your PR
- Use [Conventional Commits](https://www.conventionalcommits.org/) with a single emoji (e.g., `feat: Add async fetch demo ⚡`).
- Summarise your testing steps (commands + results) in the PR description.
- Request a review from the maintainers list in `README.md` and be ready to demo live exercises if asked.

## 🙏 Code of Conduct
Respectful communication keeps this community thriving. Be empathetic, encourage beginners, and celebrate progress loudly. If conflicts arise, contact the maintainers privately for mediation.

Happy coding and teaching! ☕
