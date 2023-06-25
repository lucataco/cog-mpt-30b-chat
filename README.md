# bigcode/starcoder_py COG

Attempt at creating a cog wrapper for [bigcode/starcoder](https://huggingface.co/bigcode/starcoder).

## Run

`cog build -t starcoder`

`docker run -d -p 5000:5000 --gpus all starcoder`

## Test

### Input

`curl http://localhost:5000/predictions -X POST -H 'Content-Type: application/json' -d '{ "input": {"max_new_tokens": 64, "prompt":"#Python function that determines if a given number x is prime"}}'`

### Output

`{"input":{"prompt":"#Python function that determines if a given number x is prime","max_new_tokens":64},"output":"#Python function that determines if a given number x is prime or not\ndef is_prime(x):\n    if x == 2:\n        return True\n    if x % 2 == 0 or x == 1:\n        return False\n    for i in range(3, int(x**0.5)+1, 2):\n        if x % i","id":null,"version":null,"created_at":null,"started_at":"2023-06-25T05:27:29.225043+00:00","completed_at":"2023-06-25T05:27:40.372878+00:00","logs":"","error":null,"status":"succeeded","metrics":{"predict_time":11.147835},"output_file_prefix":null,"webhook":null,"webhook_events_filter":["logs","completed","start","output"]}`
