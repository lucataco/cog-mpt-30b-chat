# Cog wrapper for mosaicml/mpt-30b-chat

Attempt at creating a cog wrapper for [mosaicml/mpt-30b-chat](https://huggingface.co/mosaicml/mpt-30b-chat).

## Run

`cog build -t mpt-chat`

`docker run -d -p 5000:5000 --gpus all mpt-cha`

## Test

### Input

`curl http://localhost:5000/predictions -X POST -H 'Content-Type: application/json' -d '{ "input": {"max_new_tokens": 64, "prompt":Here is a recipe for vegan banana bread:"}}'`
