# Demo Issue

## Title
Fix incorrect retry behavior in API client

## Description
When network timeout occurs, retry counter is not reset between requests, causing subsequent successful requests to fail early.

## Expected
Retry state should be scoped per request.

## Actual
Retry state leaks across requests.
