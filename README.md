# 🧠 Payload Visualizer

A raw, powerful CLI tool that injects and visualizes how payloads flow through URLs.

Use it to test how XSS, SQLi, or any payload is encoded and placed into query parameters — great for understanding injection points and building safer apps.

> 🛡️ This tool is for **ethical hacking, education, and red team training**. Only test on sites you own or are authorized to assess.

---

## 🚀 Features

- 🔍 Injects a single payload or batch from a wordlist file
- 🌐 Auto-encodes payloads for safe HTTP usage
- 🔧 Works with multi-parameter URLs
- 🧱 Simple Python-only CLI — no external API or AI required
- 🧵 Easily extensible for future HTTP testing, POST support, etc.

---

## 📦 Installation

Requires Python 3.6+

```bash
git clone https://github.com/1nc0gn30/payload-visualizer.git
cd payload-visualizer
python3 visualize.py --help
