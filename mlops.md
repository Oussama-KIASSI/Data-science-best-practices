# MLOps best practices
This page encompasses guidelines for DataOps, DevOps, and ModelOps. In DataOps, focus lies on operationalizing data through effective data management and reliable data pipelines. DevOps emphasizes automation and code quality. Meanwhile, ModelOps addresses aspects like model building, lifecycle management, and infrastructure design. Together, these principles aim to elevate reliability, maintainability, and scalability of ML assets.

## DataOps
1. **Document Data Structures and Transformations**: Enhance comprehension and foster knowledge sharing.
2. **Automate Data Cataloging and Metadata Capture**: Regularly capture metadata from data and ML assets to increase adoption (e.g., through Feature Store).
3. **Unified Data Quality Management**: Provide a holistic view of data assets to identify and address data quality issues.
4. **Use Suitable Data Versioning and Checkpointing**: Employ a suitable format exclusively for data versioning and checkpointing (e.g., Delta) to enable easy rollback in case of data corruption.


## DevOps
1. **Document Functions and Enforce Data Validation**: Document functions and enforce data validation for all variable inputs.
2. **Refactor Code and Avoid Hardcoding**: Refactor code when possible and add parameters instead of hardcoding.
3. **Automate Testing**: Include unit tests, integration tests, and performance tests within the build pipeline.
4. **Regularly Review CI/CD Pipeline**: Regularly review the CI/CD pipeline to incorporate platform product updates.
5. **Implement Configuration Management Tools**: Use configuration management tools (e.g., Ansible) to ensure consistent configurations across different environments.
6. **Enforce Version Control Practices and Branching Strategies**: Effectively track project changes, simplify rollback procedures, and facilitate collaboration.


## ModelOps
1. **Expand Model Selection**: Include more complex options like deep learning models in experiments, as they often perform better.
2. **Develop Complete Hyperparameter Tuning Scripts**: Improve prediction quality and uncover hidden reliability concerns.
3. **Standardize Processes for Model Rollback**: Ensure the reliability of the overall ML system.
4. **Maintain Centralized Model Registry**: Store and manage trained models, along with associated metadata and performance metrics.
5. **Continuous Performance Monitoring of Deployed Models**: Monitor accuracy, latency, and resource usage.
6. **Implement Alerting System**: Promptly detect anomalies or deviations in model behavior and trigger appropriate actions.
7. **Establish and Review Retraining Mechanisms**: Based on predefined criteria such as data drift or performance degradation.
8. **Employ Techniques for Model Interpretability**: Comprehend and interpret the behavior and decisions of ML models for transparency and regulatory compliance.
9. **Design Robust Model Serving Infrastructure**: Capable of handling increased traffic and scaling horizontally or vertically as required.
10. **Document Model Details and Workflow**: Include workflow scheduling, training methodologies, assumptions, and limitations to enhance collaboration and understanding among stakeholders.
