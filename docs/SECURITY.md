# Security model

JARVIS follows a deny-by-default approach for actions that can change the machine.

- API keys are loaded from environment variables and never committed.
- Dangerous tools must be explicitly confirmed by the caller.
- Native command execution uses argument arrays and `shell=False`.
- File operations should be constrained to explicit user-selected paths.
- Browser automation belongs in an optional adapter rather than the core.
- External integrations must report failures instead of claiming success.

JARVIS is a personal local application, not a security sandbox. Do not grant it credentials or permissions that you would not grant to a normal local application.
