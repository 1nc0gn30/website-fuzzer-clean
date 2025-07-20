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
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--payload", help="Single payload to inject (e.g., <script>alert(1)</script>)")
    group.add_argument("--wordlist", help="Path to file containing payloads (one per line)")

    args = parser.parse_args()

    if args.payload:
        inject_payload(args.url, args.payload)
    elif args.wordlist:
        try:
            with open(args.wordlist, "r") as file:
                for line in file:
                    payload = line.strip()
                    if payload:
                        print(f"[Payload] {payload}")
                        inject_payload(args.url, payload)
        except FileNotFoundError:
            print(f"[!] Wordlist file not found: {args.wordlist}")

if __name__ == "__main__":
    main()
