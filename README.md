# Giselle Evita Koch — Enforceable AI Security

[![Deploy](https://github.com/giselleevita/portfolio/actions/workflows/pages.yml/badge.svg)](https://github.com/giselleevita/portfolio/actions/workflows/pages.yml)

**Enforceable AI Security** — a portfolio site built around one artifact: authorization at the agent tool-call boundary.

**Live site:** https://giselleevita.github.io/portfolio

Open Graph metadata and a shareable preview image (`og-image.png`, 1200×630) are included for link previews.

## The story

One artifact, with the evidence and the tradeoffs published:
[agent-security-gate](https://github.com/giselleevita/agent-security-gate) — fail-closed
policy authorization immediately before an agent tool call.

- [Case study](https://github.com/giselleevita/agent-security-gate/blob/main/docs/case-study.md)
- [Benchmark evidence](https://github.com/giselleevita/agent-security-gate/blob/main/docs/benchmark-results/agentdojo-local.md)
- [Security reviewer guide](https://github.com/giselleevita/agent-security-gate/blob/v0.7.1/docs/security-reviewer-guide.md)
- [Independent reproduction request](https://github.com/giselleevita/agent-security-gate/issues/65) — no independent validation is claimed yet
- [Upstream proposal — AgentDojo issue #184](https://github.com/ethz-spylab/agentdojo/issues/184) (open)

Three 90-second proof paths complement that central artifact:
[ToolShield](https://giselleevita.github.io/ToolShield/) evaluates prompt-injection
detectors under distribution shift, the
[DK Security Pack](https://github.com/giselleevita/dk-procurement-security-pack-generator)
demonstrates independently verifiable evidence, and
[Abrahamic](https://abrahamic.vercel.app) demonstrates licensed-content boundaries,
role-aware publishing, and transactional audit history in a full-stack application.

## Local preview

Open `index.html` directly or serve the directory with any static HTTP server.

## License

Code (`style.css`, `script.js`, `scripts/`) is MIT-licensed — see [LICENSE](LICENSE). Text and images are all rights reserved.
