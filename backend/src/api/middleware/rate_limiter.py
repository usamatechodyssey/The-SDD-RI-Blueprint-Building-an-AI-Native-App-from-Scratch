#backend/src/api/middleware/rate_limiter.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp
from collections import defaultdict
import time

# Simple in-memory rate limiting, not suitable for production in distributed systems
# For production, consider solutions like Redis or a dedicated rate-limiting service.

# Dictionary to store request counts for each IP address
# Format: {ip_address: [(timestamp, count)]}
request_counts = defaultdict(list)

# Rate limiting configuration
RATE_LIMIT_DURATION = 60  # seconds
MAX_REQUESTS_PER_DURATION = 100


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        ip_address = request.client.host
        current_time = time.time()

        # Remove old requests outside the rate limit duration
        request_counts[ip_address] = [
            (timestamp, count)
            for timestamp, count in request_counts[ip_address]
            if current_time - timestamp < RATE_LIMIT_DURATION
        ]

        # Check if the number of requests exceeds the limit
        if len(request_counts[ip_address]) >= MAX_REQUESTS_PER_DURATION:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Too many requests.",
                    "rate_limit": f"{MAX_REQUESTS_PER_DURATION} requests per {RATE_LIMIT_DURATION} seconds",
                },
            )

        # Add current request to the count
        request_counts[ip_address].append((current_time, 1))

        response = await call_next(request)
        return response
