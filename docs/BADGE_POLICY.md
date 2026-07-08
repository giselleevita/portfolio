# README badge policy

How to show build/deploy status on portfolio repos **without paying for GitHub Actions**.

## Rules

| Repo visibility | Show in README | Do not show |
|-----------------|----------------|-------------|
| **Public** | GitHub Actions CI badge (unlimited free minutes) | — |
| **Private** | Live demo / Vercel badge, version, license | GitHub Actions CI badge |

**If a badge is red, remove it.** A missing badge is better than a misleading one.

## Public repos (CI badge OK)

- [agent-security-gate](https://github.com/giselleevita/agent-security-gate)
- [evidentia](https://github.com/giselleevita/evidentia)
- [aegisais](https://github.com/giselleevita/aegisais)
- [portfolio](https://github.com/giselleevita/portfolio) — Pages deploy badge only

Example:

```markdown
[![CI](https://github.com/giselleevita/evidentia/actions/workflows/ci.yml/badge.svg)](https://github.com/giselleevita/evidentia/actions/workflows/ci.yml)
```

## Private repos (live demo, not CI)

- abrahamic, gotham-lite, cloud-security-portfolio, ares-lite

Example:

```markdown
[![Live demo](https://img.shields.io/badge/demo-abrahamic.vercel.app-000?style=flat&logo=vercel&logoColor=white)](https://abrahamic.vercel.app)
```

Production deploy truth for private apps: **Vercel** (or local `npm run build` / `docker compose` for reviewers).

## Free tier notes

- **Public repos:** GitHub Actions minutes are **unlimited** on the free plan — no payment required.
- **Private repos:** 2,000 Actions minutes/month free. Prefer Vercel for deploy badges; keep workflows lean (PR-only if needed).
- **Never add a payment method** unless you choose to exceed free limits.

## Reviewer-facing copy

For private repos with a public demo, link reviewers to the live URL and [`docs/REVIEWER_GUIDE.md`](https://github.com/giselleevita/abrahamic/blob/main/docs/REVIEWER_GUIDE.md) (abrahamic) instead of a CI badge.
