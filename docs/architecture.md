# High-level architecture

See the Mermaid diagram in [`../README.md`](../README.md).

## Browser and identity
The browser downloads static files from CloudFront, whose private S3 origin uses OAC. Sign-in happens through Cognito. The browser obtains an access token via a standard OAuth 2.0 authorization-code-with-PKCE flow; no client secret is embedded in frontend source.

## Application requests
Frontend uses HTTPS and passes Cognito access token to API Gateway HTTP API. A managed JWT authorizer validates token signature and issuer/audience. Restrict accepted clients and validate user identity server-side. Route to Python Lambda. The Lambda uses the verified principal (`sub`) to namespace every DynamoDB query. Do not allow arbitrary client-supplied user ID to select records.

## Database proposal
One DynamoDB notes table. Partition key: `PK` (`USER#<sub>`). Sort key: `SK` (`NOTE#<timestamp>#<uuid>`). Attributes: `body`, `created_at`, `updated_at`, `pinned`. Access by user partition, paginated. Avoid scans. Search can be simple client-side search of the user's most recent notes for the MVP, with documented limitations.

## CORS & abuse resistance
Allow only the CloudFront domain as browser origin; CORS alone is not authentication. Cognito JWT authorization applies to all private API routes. Apply sensible request-body limits, pagination, and logging without storing note content in application logs.

## Deployment flow
GitHub Actions tests -> GitHub OIDC IAM role -> Terraform plan -> review/approval -> Terraform apply -> upload frontend to private S3 -> CloudFront invalidation if needed.

## Cost boundary
No always-on compute, NAT, RDS, load balancer, or paid custom domain required. Free allowances and pricing are account-, region-, tier-, and time-dependent. Budget alerts are not hard spending limits. Avoid unbounded log retention or write/scan patterns.
