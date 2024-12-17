### Time Series Forecasting with LLM Based Foundation Models and Scalable MLOps on AWS

This solution demonstrates how to leverage AWS SageMaker's MLOps features to orchestrate the complete ML pipeline for training Chronos, a family of time series models based on large language model (LLM) architectures. We will also be covering how to deploy this solution in an endpoint. Like LLMs or vision-language models, Chronos is a foundation model that learns from large datasets to produce general representations useful for a wide range of tasks. This pretraining allows Chronos to achieve strong forecasting performance even with small amounts of user data, making it highly efficient and scalable for real-world applications.

### Getting Started

1. Clone the repository on [Amazon SageMaker](https://aws.amazon.com/sagemaker/).
2. Open the `chronos_pipeline.ipynb` Jupyter Notebook.
3. Select `Python 3` kernel with `Pytorch 2.1.0 Python 3.10 CPU Optimized` image. 
4. Run each cell in the `chronos_pipeline.ipynb` Jupyter Notebook.
5. Open the `chronos_pipeline_endpoint_inference.ipynb` Jupyter Notebook.
3. Select `Python 3` kernel with `Pytorch 2.1.0 Python 3.10 CPU Optimized` image. 
4. Run each cell in the `chronos_pipeline_endpoint_inference.ipynb` Jupyter Notebook.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
