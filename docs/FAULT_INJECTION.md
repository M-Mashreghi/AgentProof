# Fault Injection

Fault families:
- timeout
- connection error / HTTP500
- rate limit
- malformed JSON
- missing optional field
- stale response
- delayed response

Every fault records target, trigger, seed, duration, and recovery condition.

Fault must not alter hidden grader truth unless explicitly testing graceful failure.
