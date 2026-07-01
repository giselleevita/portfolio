# Manual next steps

Items that require your account credentials or DNS — not automatable from CI.

## 1. GitHub billing (green CI badges)

GitHub Actions may fail on private repos (e.g. `abrahamic`, `aegisais`) when billing or spending limits block workflow minutes.

1. GitHub → **Settings → Billing and plans**
2. Resolve payment / increase Actions spending limit
3. Re-run failed workflows on `main`

Until then, rely on **Vercel** (abrahamic) and local `npm run build` / `docker compose` for review.

## 2. Publish ASG blog cross-posts

Drafts are ready in [agent-security-gate/docs/blog/cross-posts/](https://github.com/giselleevita/agent-security-gate/tree/main/docs/blog/cross-posts):

| Platform | File | Steps |
|----------|------|-------|
| LinkedIn | [`linkedin.md`](https://github.com/giselleevita/agent-security-gate/blob/main/docs/blog/cross-posts/linkedin.md) | Copy body → new post → confirm links |
| dev.to | [`devto.md`](https://github.com/giselleevita/agent-security-gate/blob/main/docs/blog/cross-posts/devto.md) | Paste markdown + front matter; canonical URL is pre-set |

Full checklist: [cross-posts/README.md](https://github.com/giselleevita/agent-security-gate/blob/main/docs/blog/cross-posts/README.md)

**Canonical URL (do not change):**  
`https://github.com/giselleevita/agent-security-gate/blob/main/docs/blog/agent-security-at-tool-boundary.md`

## 3. Portfolio custom domain (optional)

1. Configure DNS per [`CUSTOM_DOMAIN.md`](CUSTOM_DOMAIN.md)
2. Add domain in GitHub Pages settings
3. Run `./scripts/enable-custom-domain.sh www.yourdomain.com`

## 4. ToolShield

Remains **private, available on request** — no public repo change planned.
