# Custom Domain (GitHub Pages)

The portfolio deploys from `main` via GitHub Actions to:

**https://giselleevita.github.io/portfolio/**

To serve it from your own domain (for example `www.example.com`):

## 1. Add the domain in GitHub

1. Open **Settings → Pages** on the `portfolio` repository.
2. Under **Custom domain**, enter your hostname (e.g. `www.example.com`).
3. Enable **Enforce HTTPS** after DNS propagates.

## 2. Configure DNS at your registrar

For an apex domain (`example.com`):

| Type | Name | Value |
|------|------|-------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

For a subdomain (`www.example.com`):

| Type | Name | Value |
|------|------|-------|
| CNAME | `www` | `giselleevita.github.io` |

GitHub publishes current IP addresses in [their documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## 3. Update Open Graph URLs

After the domain is live, update `og:url` and `og:image` in `index.html` to use the
custom hostname so link previews resolve correctly.

## 4. Optional repository `CNAME` file

GitHub creates `CNAME` automatically when you save a custom domain in Settings. If you
manage DNS manually, the file should contain only the hostname:

```
www.example.com
```

Do not commit a `CNAME` until you own the domain and DNS is configured.
