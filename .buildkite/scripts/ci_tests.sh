#!/usr/bin/env bash

BUILDKITE_ANALYTICS_TOKEN=$(buildkite-agent meta-data get analytics_token)
export BUILDKITE_ANALYTICS_TOKEN

pip install --no-cache-dir -r requirements.txt
pytest
