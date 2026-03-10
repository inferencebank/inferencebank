# InferenceBank Python API library

The InferenceBank Python library provides convenient access to the InferenceBank REST API from any Python 3.11+
application.

# Usage

```python
import os
from inferencebank import InferenceBank

client = InferenceBank(api_key=os.environ.get("INFERENCEBANK_API_KEY"))
health_status = client.health_check()
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `INFERENCEBANK_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.