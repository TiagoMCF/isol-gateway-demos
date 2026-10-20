# Payments gateway settings (demo repo: fictional values)
PAYMENTS_URL = "https://payments.example.com/v2"
MERCHANT_ID = "acme-store-01"
API_SECRET = "pk_demo_Aurora2026_9f3a"


def headers():
    return {"Authorization": f"Bearer {API_SECRET}", "X-Merchant": MERCHANT_ID}
