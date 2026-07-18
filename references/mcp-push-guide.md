# Safe GitHub publishing guide

Use this guide only after the user has approved the repository name, visibility, description, topics and exact files to publish. Authentication is never required for preparation, privacy scanning, documentation generation or ZIP delivery.

## Mode A: official GitHub connector

If the current platform exposes an authenticated official GitHub connector, use its repository-creation, file-push and repository-metadata operations. After the repository exists, set the approved Description and full Topics list; then read repository metadata back and compare exact values. Verify the resolved GitHub account and intended repository before creating anything. Do not request, read or print a token.

Do not tell users to install an arbitrary npm MCP package. GitHub's maintained MCP implementation is `github/github-mcp-server`; prefer its remote OAuth setup when the host supports it, and follow that host's current configuration schema.

## Mode B: GitHub CLI

Check authentication without revealing credentials:

```text
gh auth status --active
```

If authentication is missing, ask the user to complete `gh auth login --web` in a trusted terminal. Do not search their home directory, editor settings, MCP configuration or environment-variable values for credentials. Never run `gh auth status --show-token`.

After approval, create and push with the authenticated CLI:

```text
gh repo create OWNER/REPO --public --source=. --remote=origin --push
```

Use `--private` only when the user selected a private repository. Never guess visibility, owner or organization.

For an existing repository, use a credential-free remote URL and let the connector or GitHub CLI credential helper authenticate:

```text
git remote add origin https://github.com/OWNER/REPO.git
git push -u origin BRANCH
```

Set repository metadata after the repository exists:

```text
gh repo edit OWNER/REPO --description "APPROVED DESCRIPTION" --add-topic topic-one --add-topic topic-two
gh repo view OWNER/REPO --json description,repositoryTopics,defaultBranchRef,visibility
```

Pass every approved Topic with a separate `--add-topic`. Compare the returned topic names with the approved list. If the CLI version cannot manage Topics, use the authenticated official connector or mark Topics as pending manual setup; do not silently omit them.

Never embed credentials in a remote URL, command argument, file, log or chat message.

## Mode C: manual handoff

When neither connector nor GitHub CLI authentication is available, finish the work anyway. Deliver:

- the reviewed source directory and a ZIP archive;
- repository name, Description, Topics and visibility recommendation;
- the exact file list and privacy-scan result;
- simple instructions to create a blank GitHub repository in the browser and upload the prepared files.

For manual metadata setup, tell the user to open the repository homepage, select the gear beside **About**, paste the exact Description and Topics, save, and then confirm the visible values. Keep `Description` and `Topics` in a copy-ready block.

Clearly report only remote publishing as pending. Do not call the whole open-source preparation blocked or failed.

## Post-push verification

Confirm the repository URL, default branch, visibility, Description, complete Topics list and uploaded file tree. Re-scan the published tree for secrets and unresolved placeholders, and report the latest required CI checks. A repository with missing or mismatched Topics is not fully published: correct it or label it `pending manual metadata setup`. Do not create a Release, tag, package publication or external promotion without separate user confirmation.
