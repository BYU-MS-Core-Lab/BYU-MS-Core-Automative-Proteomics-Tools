# Security Policy

## Supported Versions

We actively maintain security updates for the following versions:

| Version | Supported          | Python Versions | Status              |
| ------- | ------------------ | --------------- | ------------------- |
| 0.2.x   | :white_check_mark: | 3.10 - 3.14     | Active Development  |
| 0.1.x   | :x:                | 3.10 - 3.13     | End of Life (EOL)   |

**Version Support Details:**
- **0.2.2+** - Current stable version with full security support
- **0.2.0-0.2.1** - Legacy versions; please upgrade to 0.2.2
- **0.1.x** - No longer supported; critical security issues only

## Reporting a Security Vulnerability

We take security seriously. If you discover a security vulnerability, please report it responsibly.

### How to Report

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, please email the security report to:
- **Primary Contact:** [mscorelab@byu.edu](mailto:mscorelab@byu.edu)
- **Subject:** `[SECURITY] Vulnerability Report - [Component]`

### Required Information

Please include the following details in your report:

1. **Description** - Clear explanation of the vulnerability
2. **Affected Version(s)** - Which version(s) are impacted (e.g., 0.2.2)
3. **Severity** - Critical, High, Medium, or Low (see [Severity Ratings](#severity-ratings) below)
4. **Steps to Reproduce** - Detailed steps to trigger the vulnerability
5. **Impact** - What could an attacker do with this vulnerability?
6. **Proof of Concept** - If applicable, minimal code to demonstrate the issue

### Example Report

```
Subject: [SECURITY] Vulnerability Report - Flask Backend

Vulnerability: SQL Injection in user input handling
Affected Version: 0.2.1, 0.2.2
Severity: High

Description:
The file upload handler in app.py does not properly sanitize filenames, 
allowing potential path traversal attacks...

Steps to Reproduce:
1. Upload a file with name: "../../../sensitive/file.txt"
2. Observe that the file is saved outside the intended directory...

Impact:
An attacker could read/write arbitrary files on the server.

Proof of Concept:
[Include minimal code or curl command to demonstrate]
```

## Response Timeline

We aim to respond to all security reports within the following timeframes:

| Severity | Initial Response | Fix Timeline     |
| -------- | --------------- | --------------- |
| Critical | 24 hours        | 3-7 days        |
| High     | 48 hours        | 1-2 weeks       |
| Medium   | 1 week          | 2-4 weeks       |
| Low      | 2 weeks         | Next release    |

**Timeline Clarifications:**
- "Initial Response" = Acknowledgment and assessment of validity
- "Fix Timeline" = Patch release availability (may be coordinated disclosure)
- All timelines are best-effort; critical infrastructure may adjust as needed

## Vulnerability Types & Scope

### In Scope (Report These)

✅ **Authentication/Authorization Issues**
- Unauthorized data access
- Privilege escalation
- Session hijacking

✅ **Injection Vulnerabilities**
- SQL injection
- Command injection
- Path traversal

✅ **Data Security**
- Unencrypted sensitive data transmission
- Improper password hashing
- Credential exposure in logs

✅ **Dependency Vulnerabilities**
- Critical CVEs in dependencies
- Known exploitable package versions

✅ **API Security**
- Broken access control
- Rate limiting bypass
- CSRF/CORS bypass

### Out of Scope (Report as Regular Issues)

❌ **Non-Security Issues**
- Feature requests
- Performance improvements
- Code quality/style issues

❌ **Low-Impact Issues**
- Typos in documentation
- Missing help text
- UI/UX improvements

❌ **Infrastructure Issues**
- Email server configuration for notifications
- Internal GitHub organization settings
- CI/CD pipeline access

## Coordinated Disclosure

We follow responsible disclosure practices:

1. **Report received** → We acknowledge receipt within 48 hours
2. **Verification** → We confirm the vulnerability and assess impact
3. **Fix development** → We create and test a patch (1-4 weeks typical)
4. **Embargo period** → Fix is prepared but not yet released
5. **Release coordination** → We coordinate a public disclosure date (typically 2 weeks after patch release)
6. **Publication** → Fix is released and vulnerability details are disclosed publicly

**Embargo Terms:**
- Standard embargo: 90 days after patch release
- Critical vulnerabilities: 30 days after patch release
- Reporter will be credited in release notes (unless requesting anonymity)

## Security Best Practices for Users

### Updates
- Subscribe to release notifications on GitHub
- Update to the latest version regularly
- Monitor the changelog for security-related patches

### Deployment
- Never run the web app with `debug=True` in production
- Use environment variables for sensitive configuration (API keys, database URLs)
- Run the application behind a reverse proxy (nginx/Apache) with HTTPS
- Keep Node.js and Python dependencies up to date

### Data Handling
- Validate all input files before processing
- Store analysis results securely (appropriate file permissions)
- Don't commit sensitive data (API keys, credentials) to version control
- Use `.gitignore` for data files and cached results

## Dependencies & Vulnerability Scanning

We maintain dependency security through:

- **Automated Updates:** Dependabot monitors all package versions
- **Vulnerability Scans:** CodeQL security analysis on every commit
- **Audit Tools:** Regular `pip audit` and `npm audit` checks
- **Changelog Monitoring:** Track security updates in major dependencies

**Current Dependencies Include:**
- Python: numpy, pandas, matplotlib, Flask, scipy
- Node.js: React, TypeScript, Vite
- Additional: pyteomics, pillow, ruff, pytest

View the full list in [pyproject.toml](../pyproject.toml).

## Security Headers & Best Practices

The web application implements:

✅ **Flask Configuration**
- Secret key for session management
- CORS restrictions (configurable for your environment)
- Content Security Policy headers

✅ **Frontend Security**
- TypeScript strict mode (prevents type-based attacks)
- Input validation on file uploads
- XSS prevention through React's auto-escaping

⚠️ **Production Deployment Notes**
- Enable HTTPS/SSL (recommended: Let's Encrypt)
- Use environment variables for configuration
- Implement rate limiting for API endpoints
- Configure appropriate file upload size limits

## Security Contacts

- **Lead Maintainer:** BYU MS Core Lab
- **Email:** [mscorelab@byu.edu](mailto:mscorelab@byu.edu)
- **GitHub Organization:** [MSCoreLab](https://github.com/MSCoreLab)

## Acknowledgments

We appreciate security researchers who responsibly disclose vulnerabilities. Contributors will be publicly credited in release notes unless they request anonymity.

---

**Last Updated:** March 5, 2026  
**Policy Version:** 1.1
