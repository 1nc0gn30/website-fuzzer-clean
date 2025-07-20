# Payload Visualizer

A simple but powerful CLI tool to inject and visualize how payloads flow through a target URL.

## Features
- Injects XSS, SQLi, or any custom payload
- Shows exact modified URLs
- Built in pure Python — no AI, no fluff

## Usage

```bash
python visualize.py --url "http://target.com/page?q=foo" --payload "<script>alert(1)</script>"

