# MLOps-best-practices
This repo groups a set of MLOps best practices

# DataOps Best Practices

1 - Document data structures and transformations to enhance comprehension and foster knowledge sharing.
1 - Automate data cataloging and regularly capture metadata from data and ML assets to increase their adoption (e.g. through Feature Store).
- Unify data quality management through a single medium, providing a holistic view of data assets, to identify and address data quality issues.
- Utilize Delta format exclusively for data versioning and checkpointing to enable easy rollback in case of data corruption.

# DevOps Best Practices

- Document the functions and enforce the data validation for all variables inputs.
- Refactor code when possible and add widgets instead of hardcoding.
- Automate testing, including unit tests, integration tests, and performance tests, within the build pipeline.
- Regularly review the CI/CD pipeline to incorporate Databricks product updates.
- Implement configuration management tools like Ansible to ensure consistent configurations across different environments.
- Enforce version control practices and branching strategies to effectively track project changes, simplify rollback procedures, and facilitate collaboration.

# Model Ops Best Practices

- Expand the selection list of models to include more complex options like deep learning models, as complex models perform better than simple ones in general.
- Develop detailed hyperparameter tuning scripts to improve prediction quality and uncover any hidden reliability concerns.
- Establish standardized processes for rolling back ML models to ensure the reliability of the overall ML system.
- Maintain a centralized model registry to store and manage trained models, along with associated metadata and performance metrics.
- Continuously monitor the performance of deployed ML models, including accuracy, latency, and resource usage.
- Implement an alerting system to promptly detect anomalies or deviations in model behavior and trigger appropriate actions.
- Establish and review models' retraining mechanisms based on predefined criteria such as data drift or performance degradation.
- Employ techniques and tools to comprehend and interpret the behavior and decisions of ML models, ensuring transparency and regulatory compliance.
- Design a robust model serving infrastructure capable of handling increased traffic and scaling horizontally or vertically as required.
- Document model details, workflow schedule, training methodologies, assumptions, and limitations to enhance collaboration and understanding among stakeholders.

