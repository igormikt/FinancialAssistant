import os


def check_environment():
    required_vars = ['BOT_TOKEN', 'EXCHANGE_RATE_API_URL', 'EXCHANGE_RATE_API_KEY']

    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing required environment variable: {var}")

    print("✅ All environment variables are set correctly")


if __name__ == "__main__":
    check_environment()