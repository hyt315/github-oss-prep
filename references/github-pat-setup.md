# GitHub authentication setup

Prefer a platform GitHub connector with OAuth or GitHub CLI's browser login. The normal setup is:

```text
gh auth login --web
gh auth status --active
```

Complete authentication in a trusted terminal or browser. Do not paste credentials into chat, commit them to a repository, store them in the skill folder, or embed them in Git remote URLs. Never use `gh auth status --show-token` in an agent workflow.

For MCP-capable hosts, use GitHub's maintained `github/github-mcp-server` and its current official configuration. Prefer remote OAuth when supported. Do not publish a user's personal MCP JSON as part of an open-source repository.

If a user explicitly needs a personal access token for another trusted tool, direct them to GitHub's official documentation and recommend the minimum repository scope, an expiration date and rotation after exposure. The trusted tool should receive and store the credential itself; the agent must not search for, extract, display or persist its value.
