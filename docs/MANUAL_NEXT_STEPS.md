# Manual next steps

Items that require your account credentials or DNS — not automatable from CI.

## Quick copy-paste (do these first)

1. **LinkedIn** — open [`agent-security-gate/docs/blog/cross-posts/linkedin.md`](https://github.com/giselleevita/agent-security-gate/blob/main/docs/blog/cross-posts/linkedin.md), copy body, paste as new post. Confirm **v0.6.0** release link works.
2. **dev.to** — paste [`devto.md`](https://github.com/giselleevita/agent-security-gate/blob/main/docs/blog/cross-posts/devto.md) including YAML front matter; verify canonical URL.
3. **Portfolio custom domain** (optional) — DNS per [`CUSTOM_DOMAIN.md`](CUSTOM_DOMAIN.md), then GitHub Pages → add domain → `./scripts/enable-custom-domain.sh www.yourdomain.com`, update `og:url` in `index.html`.
4. **Evidentia Entra login** — in staging, set `VITE_AZURE_CLIENT_ID`, `VITE_AZURE_TENANT_ID`, `VITE_AZURE_SCOPES` in `frontend/compliance-portal/.env`, run `npm run build`, verify MSAL 5 redirect login at `/`.

---

## 1. README badges (no payment required)

Follow [`docs/BADGE_POLICY.md`](BADGE_POLICY.md):

- **Public repos** → GitHub Actions CI badge (free, unlimited minutes).
- **Private repos** → Docker demo or live demo badge only; **no** CI badge.
- Remove any badge that stays red.

You do **not** need GitHub billing or a payment method for public-repo CI badges.

## 2. Publish ASG blog cross-posts

Drafts are ready in [agent-security-gate/docs/blog/cross-posts/](https://github.com/giselleevita/agent-security-gate/tree/main/docs/blog/cross-posts) (**v0.6.0** release links):

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

## 4. Evidentia Entra ID (staging)

MSAL 5 is on `main`; login requires Azure app registration:

```bash
# frontend/compliance-portal/.env
VITE_AZURE_CLIENT_ID=<app-registration-client-id>
VITE_AZURE_TENANT_ID=<tenant-id>
VITE_AZURE_SCOPES=api://<api-app-id>/access_as_user
# Or VITE_DEMO_MODE=true to skip Entra locally
```

Build gate: `cd frontend/compliance-portal && npm run build`. Manual: complete redirect login against staging API.

## 5. ToolShield

Remains **private, available on request** — no public repo change planned.
