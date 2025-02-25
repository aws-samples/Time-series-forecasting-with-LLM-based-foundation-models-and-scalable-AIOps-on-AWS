### Time series forecasting with LLM-based foundation models and scalable AIOps on AWS

This solution demonstrates how to integrate Chronos, a cutting-edge family of time series models, into Amazon SageMaker Pipelines. Chronos leverages large language model (LLM) architectures to provide accurate zero-shot forecasts across multiple domains.

#### Key Features
- Utilizes Chronos, a foundation model pre-trained on diverse datasets
- Converts time series data into a discrete vocabulary for LLM processing
- Outperforms task-specific models on most benchmarked datasets
- Enables efficient forecasting with minimal data-specific tuning

#### Implementation
- Orchestrates the complete ML pipeline using Amazon SageMaker AIOps features
- Covers fine-tuning, deployment, and endpoint creation
- Demonstrates the process using a synthetic forecasting dataset

By following this guide, you'll learn how to streamline the development process for time series forecasting, making it applicable to various domains with minimal customization.

### Getting Started

1. Clone the repository on [Amazon SageMaker](https://aws.amazon.com/sagemaker/).
2. Open the `chronos_pipeline.ipynb` Jupyter Notebook.
3. Select `Python 3` kernel with `Pytorch 2.1.0 Python 3.10 CPU Optimized` image.
4. Run each cell in the `chronos_pipeline.ipynb` Jupyter Notebook to train, hyperparameter tune, and register a Chronos model.
5. Open the `chronos_pipeline_endpoint_inference.ipynb` Jupyter Notebook.
3. Select `Python 3` kernel with `Pytorch 2.1.0 Python 3.10 CPU Optimized` image.
4. Run each cell in the `chronos_pipeline_endpoint_inference.ipynb` Jupyter Notebook to deploy and inference the model.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
