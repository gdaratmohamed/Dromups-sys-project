#!/usr/bin/env sh
set -e
cd frontend
npm ci
npm test
