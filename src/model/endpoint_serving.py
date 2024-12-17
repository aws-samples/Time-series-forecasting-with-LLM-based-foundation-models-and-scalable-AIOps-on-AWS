"""

 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: MIT-0

 Permission is hereby granted, free of charge, to any person obtaining a copy of this
 software and associated documentation files (the "Software"), to deal in the Software
 without restriction, including without limitation the rights to use, copy, modify,
 merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
 PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""


import logging
import json
import torch

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def input_fn(request_body, request_content_type):
    logger.info("Running input_fn")
    data = json.loads(request_body)["inputs"]
    data = torch.tensor(data, dtype=torch.bfloat16)
    return data


def predict_fn(input_object, model_artifacts):
    logger.info("Running predict_fn")
    val_ts_tensor = input_object
    
    predictions = model_artifacts.predict(
        context=val_ts_tensor,
        prediction_length=12,
        num_samples=20,
    )    
    return predictions


def output_fn(predictions, content_type):
    logger.info("Running output_fn")
    return predictions
