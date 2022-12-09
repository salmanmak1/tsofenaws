This repository contains the following stuff:
1. python_course - homeworks from the DevOps course including:
    - Bash
    - Python
    - AWS
    - Docker
    - Kubernetes
2. project - project sources from the DevOps course including:
    - Project Name: Automated CI/CD for pull requests
    - Project details: once pull request is opened to main branch, the following steps will be executed via Jenkins pipeline job:
      - Docker container is created to run the job
      - Project code is cloned from the github
      - Project unit tests are cloned from the github
      - Application code is run and checked
      - Application unit tests are run and checked
      - Application clean code quality review are run and checked (not implemented)
      - Application security code quality review are run and checked (not implemented)
      - In case of success:
        - Add successful comment to PR via github API
        - Approve PR via github API
        - Merge PR to main branch via github API
      - In case of failure:
        - Add failure comment to PR via github API
        - Reject PR and Request changes via github API
    - Project High Level Design:
        
