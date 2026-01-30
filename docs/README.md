# CI/CD & Configuration managment project

## overview
This project demonstrates the use of CI/CD workflow using python, YAML configuration files, github actions, and pull-based change management.

## repository structure

- `src/`: Contains the main application code.
- `configs/`: Contains YAML configuration files for the application.
- `docs/`: Contains documentaion for project 
- `.github/workflows/`: Contains GitHub Actions workflow files for CI/CD.

## key practices 

- configuration-driven python code
- YAML configuration validated via CI
- Github actions runs on push and pull requests
- feature branch workflow (no direct commits to main)
- ci must pass before merge 
- main branch protect using github requests

## CI quality gate 

- YAML syntax is validated using yamllint
- Invalid configuration fails the pipeline 
- clear error messages are shown in CI logs
- pull requests cannot be merged if CI fails

## failure and recovery

- CI failure demonstrated using invalid YAML
- fix commited in a separate commit
- successful CI run after correction
- full traceability via git history

## summary

this project follows CI/CD workflow ensuring stable, validated, and review-driven changes through CI and protected branches