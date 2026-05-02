---
name: API Launch Checklist
about: Complete before every API goes live — no exceptions
title: "Launch Checklist: [API Name]"
labels: launch
---

## Pre-Launch Quality Checklist

All 10 items must be checked before the API is listed on RapidAPI.

### Code
- [ ] All endpoints return correct status codes (200, 400, 422, 429, 500)
- [ ] Input validation rejects bad data with clear error messages
- [ ] No secrets or API keys committed to the repo
- [ ] Tests written and passing in CI

### Infrastructure
- [ ] Deployed to Vercel (or Render) and responding on production URL
- [ ] Zuplo auth active — requests without a valid API key return 401
- [ ] Rate limiting active — exceeding the limit returns 429
- [ ] UptimeRobot monitor added for the production endpoint

### Documentation
- [ ] RapidAPI listing complete: name, tagline, description, use cases, pricing tiers, FAQ
- [ ] At least one working curl example in the docs

---
**Estimated time to complete checklist:** ~2 hours  
**Do not skip items.** A failed check creates support burden and subscriber churn.
