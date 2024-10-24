# build
```
docker build -t froggagul/llm-server .
```

# run
````
docker run --gpus all \
    -p 8000:8000 \
    -v ~/.cache/huggingface:/app/huggingface_cache \
    -e HUGGINGFACE_TOKEN=<hf_token> \
    -e MODEL_NAME=<model_name> \
    froggagul/llm-server
```

model_name stands for huggingface repository Ex) google/gemma-2-2b

# test

If docker runs correctly, you can see url from log. See the example in below.

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
HTTP request from 137.68.192.128 to https://370c845eb6020003b38de447acd5063d.serveo.net/generate
```

Now you can use this as development server for LLM inference.

```
curl -X POST "<server url from log>/generate" -H "Content-Type: application/json" -d '{"prompt": "Once upon a time"}'
```