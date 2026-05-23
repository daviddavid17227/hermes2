#!/usr/bin/env bash
set -euo pipefail

cd /root/projects/sports-raise

# Stop old preview/tunnel processes if they exist.
pkill -f 'python3 -m http.server 8877' 2>/dev/null || true
pkill -f 'lt --port 8877' 2>/dev/null || true

# Start local static server.
nohup python3 -m http.server 8877 --bind 0.0.0.0 > /tmp/sports-raise-http.log 2>&1 &

# Start public tunnel.
nohup lt --port 8877 --local-host 127.0.0.1 > /tmp/sports-raise-tunnel.log 2>&1 &

sleep 3
URL=$(grep -Eo 'https://[^ ]+\.loca\.lt' /tmp/sports-raise-tunnel.log | tail -1 || true)
if [ -z "$URL" ]; then
  echo "Tunnel is still starting. Check: /tmp/sports-raise-tunnel.log"
  exit 1
fi

echo "Live URL: $URL/landing-page.html"
echo "If LocalTunnel shows a password page, enter this IP:"
curl -s https://loca.lt/mytunnelpassword || true
echo
