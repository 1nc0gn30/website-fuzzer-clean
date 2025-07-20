import argparse
from urllib.parse import urlparse, parse_qs, urlencode

def inject_payload(url, payload):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    for key in params:
        injected_params = params.copy()
        injected_params[key] = payload
        query = urlencode(injected_params, doseq=True)
        injected_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{query}"
        print(f"[+] Injected on '{key}':\n    {injected_url}\n")

def main():
    parser = argparse.ArgumentParser(description="Visualize payload injection into URLs.")
    parser.add_argument("--url", required=True, help="URL to inject (e.g., http://site.com/page?q=)")
    parser.add_argument("--payload", required=True, help="Payload to inject (e.g., <script>alert(1)</script>)")
    args = parser.parse_args()
    inject_payload(args.url, args.payload)

if __name__ == "__main__":
    main()

