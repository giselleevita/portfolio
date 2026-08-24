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

Two supporting repositories show the work on either side of the enforcement boundary:
[vendor-red-team-passport](https://github.com/giselleevita/vendor-red-team-passport)
evaluates model/API behaviour, and
[secure-docs-aws](https://github.com/giselleevita/secure-docs-aws) shows a small,
threat-model-driven AWS implementation.

## Local preview

Open `index.html` directly or serve the directory with any static HTTP server.

## License

Code (`style.css`, `script.js`, `scripts/`) is MIT-licensed — see [LICENSE](LICENSE). Text and images are all rights reserved.
