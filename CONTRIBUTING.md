# Contributing to Artha Server

Thanks for your interest in contributing.  

Please follow these guidelines to keep the project clean and consistent.  

---

## How to Contribute

Fork the repo and create your branch from `main`:

```bash
   git checkout -b feat/my-feature
```

Make your changes.

Run pre-commit hooks and linting before committing:

Push your branch and open a Pull Request (PR).

## Code Style
We use Ruff for Python linting.

Follow PEP8 style rules.

SQL/DB schema changes must be reviewed carefully before merging.

## Commit Messages
We follow Conventional Commits:

Feat: add rank model

Fix: resolve migration bug

Docs: update README

Refactor: clean up user service

## Pull Requests
Keep PRs small and focused (avoid big bang changes).

Add a clear description of what and why.

Link related issues (Closes #123).

## Tests

New features should include tests.

Run all tests before submitting a PR:
``
pytest
``
## Issues
Use the issue templates (Feature, User Story, Bug).

For new features, create an Epic if needed.

## Need Help?
Open an issue with the label question.

Or ping us in Discussions.
