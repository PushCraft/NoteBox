# Learning roadmap

## Phase 1: local MVP
- [ ] Define message data model and REST endpoints
- [ ] Implement Python CRUD logic locally
- [ ] Implement basic browser interface
- [ ] Validate inputs and write basic tests

## Phase 2: AWS services
- [ ] DynamoDB table and permission model
- [ ] Lambda handler
- [ ] API Gateway HTTP routes
- [ ] Cognito sign-in and JWT authorization
- [ ] CloudFront + private S3 (OAC)
- [ ] Confirm correct user isolation with two test identities

## Phase 3: Terraform
- [ ] Define resource modules incrementally
- [ ] Configure safe state backend and locking
- [ ] Validate, plan, apply and destroy nonessential sandbox resources
- [ ] Keep sensitive outputs and state out of Git

## Phase 4: CI/CD
- [ ] Pull request linting and tests
- [ ] GitHub OIDC role, minimum AWS permissions
- [ ] Manual approval before deployment
- [ ] Automated frontend and backend deployment

## Phase 5: operations
- [ ] AWS Budgets alarms at $1, $3, $5 (notifications only)
- [ ] CloudWatch log retention and error alarm
- [ ] Backup and test restore
- [ ] Document rollback and recovery
