# Odoo Technical Triage Sheet

## Purpose

This document provides a structured method for recording, investigating,
prioritising and resolving technical issues affecting Odoo and related
integrations.

It is maintained as part of the W01 Prior Evidence File for
NX-INT-QP-101 Stage One.

---

## Triage Workflow

When a technical issue is identified:

1. Record the issue and affected system.
2. Assign an initial severity.
3. Record the observed behaviour and expected behaviour.
4. Reproduce the issue where possible.
5. Investigate the probable cause.
6. Record troubleshooting actions.
7. Implement or recommend a resolution.
8. Retest the affected functionality.
9. Record the final status and evidence.

---

## Severity Classification

| Severity | Meaning |
|---|---|
| Critical | Service unavailable, major security issue, or business-critical process blocked |
| High | Important functionality unavailable with significant operational impact |
| Medium | Functionality affected but a workaround exists |
| Low | Minor issue with limited operational impact |

---

## Issue Status

Issues may use the following statuses:

- Open
- Investigating
- Blocked
- Fix in Progress
- Retesting
- Resolved
- Closed

---

## Technical Triage Register

| Issue ID | Date | System | Issue | Severity | Status | Investigation / Root Cause | Resolution / Next Action | Evidence |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — |

---

## Issue Investigation Template

### Issue ID
`ODOO-XXX`

### Date
YYYY-MM-DD

### Affected System
Odoo / Make / API / Webflow / Integration / Other

### Issue Summary
Brief description of the problem.

### Expected Behaviour
What should normally happen.

### Actual Behaviour
What actually happened.

### Severity
Critical / High / Medium / Low

### Reproduction Steps
1. 
2. 
3. 

### Investigation
Record troubleshooting performed, API responses, logs, configuration checks,
or other relevant findings.

### Root Cause
Record the confirmed root cause when identified.

### Resolution
Record the fix or corrective action.

### Verification
Explain how the solution was tested after the fix.

### Status
Open / Investigating / Blocked / Fix in Progress / Retesting / Resolved / Closed

### Evidence
Reference screenshots, logs, Postman responses, commits, or other repository
evidence where applicable.

---

## Security and Evidence Rules

- API keys, passwords and access tokens must not be entered into this sheet.
- Sensitive values in screenshots or logs must be redacted.
- Technical evidence should be stored in its authoritative repository location
  and referenced from the issue rather than unnecessarily duplicated.
