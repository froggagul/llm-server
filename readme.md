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
2024-10-24 11:59:33,545 CRIT uncaptured python exception, closing channel <POutputDispatcher at 140193468705632 for <Subprocess at 140193468705152 with name uvicorn in state RUNNING> (stderr)> (<class 'OSError'>:[Errno 29] Illegal seek [/usr/lib/python3/dist-packages/supervisor/supervisord.py|runforever|220] [/usr/lib/python3/dist-packages/supervisor/dispatchers.py|handle_read_event|270] [/usr/lib/python3/dist-packages/supervisor/dispatchers.py|record_output|204] [/usr/lib/python3/dist-packages/supervisor/dispatchers.py|_log|173] [/usr/lib/python3/dist-packages/supervisor/loggers.py|info|327] [/usr/lib/python3/dist-packages/supervisor/loggers.py|log|345] [/usr/lib/python3/dist-packages/supervisor/loggers.py|emit|227] [/usr/lib/python3/dist-packages/supervisor/loggers.py|doRollover|264])
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
HTTP request from 137.68.192.128 to https://370c845eb6020003b38de447acd5063d.serveo.net/generate
2024-10-24 11:59:51,669 CRIT uncaptured python exception, closing channel <POutputDispatcher at 140193468705392 for <Subprocess at 140193468700064 with name tunnel in state RUNNING> (stdout)> (<class 'OSError'>:[Errno 29] Illegal seek [/usr/lib/python3/dist-packages/supervisor/supervisord.py|runforever|220] [/usr/lib/python3/dist-packages/supervisor/dispatchers.py|handle_read_event|270] [/usr/lib/python3/dist-packages/supervisor/dispatchers.py|record_output|204] [/usr/lib/python3/dist-packages/supervisor/dispatchers.py|_log|173] [/usr/lib/python3/dist-packages/supervisor/loggers.py|info|327] [/usr/lib/python3/dist-packages/supervisor/loggers.py|log|345] [/usr/lib/python3/dist-packages/supervisor/loggers.py|emit|227] [/usr/lib/python3/d
```

Now you can use this as development server for LLM inference.

```
curl -X POST "<server url from log>/generate" -H "Content-Type: application/json" -d '{"prompt": "Once upon a time"}'
```