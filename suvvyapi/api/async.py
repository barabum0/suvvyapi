import httpx


class AsyncSuvvy(httpx.AsyncClient):
    """Asynchronous client for Suvvy AI API"""
    def __init__(
        self,
        token: str,
        *,
        base_url: str = "https://api.suvvy.ai",
    ) -> None:
        super().__init__(
            base_url=base_url,
            headers={
                "Authorization": f"Bearer {token}"
            },
            timeout=30,
        )

    async def
