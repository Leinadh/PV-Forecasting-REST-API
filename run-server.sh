#!/bin/bash
nohup uvicorn main:app --reload --host 0.0.0.0 &

