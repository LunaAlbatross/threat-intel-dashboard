# unblock_urls.py
import socket
import subprocess

def resolve_ip(url):
    try:
        # extract hostname from URL
        from urllib.parse import urlparse
        domain = urlparse(url).hostname
        if not domain:
            return None
        return socket.gethostbyname(domain)
    except Exception as e:
        print(f"Failed to resolve {url}: {e}")
        return None

def unblock_url(url):
    ip = resolve_ip(url)
    if not ip:
        return False, f"Could not resolve IP for {url}"

    try:
        subprocess.run(
            ["sudo", "ufw", "delete", "deny", "out", "to", ip],
            check=True
        )
        print(f"✅ Unblocked IP {ip} for {url}")
        return True, f"Unblocked {url} ({ip})"
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to unblock {url} with IP {ip}: {e}")
        return False, f"Failed to unblock {url}: {e}"