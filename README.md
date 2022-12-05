This repository contains the following stuff:
1. python_course - homeworks from the DevOps course including:
    - Bash
    - Python
    - AWS
    - Docker
    - Kubernetes
2. project - project sources from the DevOps course including:
    - Project Name: Automated CI/CD for pull requests
    - Project details: once pull request is opened to main branch, the following checks will be done via Jenkins pipeline:
      - Project code is cloned from the github
      - Python container is created for the job
      - Application code is checked
      - Application unit tests are checked
      - In case of success:
        - Add successful comment to PR via github API
        - Approve PR via github API
        - Merge PR to main branch via github API
      - In case of failure:
        - Add failure comment to PR via github API
        - Reject PR and Request changes via github API
