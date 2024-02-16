# MLOps best practices
This page encompasses guidelines for DataOps, DevOps, and ModelOps. In DataOps, focus lies on operationalizing data through effective data management and reliable data pipelines. DevOps emphasizes automation and code quality. Meanwhile, ModelOps addresses aspects like model building, lifecycle management, and infrastructure design. Together, these principles aim to elevate reliability, maintainability, and scalability of ML assets.

## DataOps
1. **Document data structures and transformations**: Enhance comprehension and foster knowledge sharing.
2. **Automate data cataloging and metadata capture**: Regularly capture metadata from data and ML assets to increase adoption (e.g., through Feature Store).
3. **Unified data quality management**: Provide a holistic view of data assets to identify and address data quality issues.
4. **Use suitable data versioning and checkpointing**: Employ a suitable format exclusively for data versioning and checkpointing (e.g., Delta) to enable easy rollback in case of data corruption.


## DevOps
1. **Document functions and enforce data validation**: Document functions and enforce data validation for all variable inputs.
2. **Refactor code and avoid hardcoding**: Refactor code when possible and add parameters instead of hardcoding.
3. **Automate testing**: Include unit tests, integration tests, and performance tests within the build pipeline.
4. **Regularly review CI/CD pipeline**: Regularly review the CI/CD pipeline to incorporate platform product updates.
5. **Implement configuration management tools**: Use configuration management tools (e.g., Ansible) to ensure consistent configurations across different environments.
6. **Enforce version control practices and branching strategies**: Effectively track project changes, simplify rollback procedures, and facilitate collaboration.


## ModelOps
1. **Expand model selection**: Include more complex options like deep learning models in experiments, as they often perform better.
2. **Develop complete hyperparameter tuning scripts**: Improve prediction quality and uncover hidden reliability concerns.
3. **Standardize processes for model rollback**: Ensure the reliability of the overall ML system.
4. **Maintain centralized model registry**: Store and manage trained models, along with associated metadata and performance metrics.
5. **Continuous performance monitoring of deployed models**: Monitor accuracy, latency, and resource usage.
6. **Implement alerting system**: Promptly detect anomalies or deviations in model behavior and trigger appropriate actions.
7. **Establish and review retraining mechanisms**: Based on predefined criteria such as data drift or performance degradation.
8. **Employ techniques for model interpretability**: Comprehend and interpret the behavior and decisions of ML models for transparency and regulatory compliance.
9. **Design robust model serving infrastructure**: Capable of handling increased traffic and scaling horizontally or vertically as required.
10. **Document model details and workflow**: Include workflow scheduling, training methodologies, assumptions, and limitations to enhance collaboration and understanding among stakeholders.
