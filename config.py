# Orders database connection (demo repo: fictional values)
DB_HOST = "orders-db.example.internal"
DB_USER = "orders_app"
DB_PASSWORD = "Aurora#2026!"


def dsn():
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/orders"
