<div align="center">

# SuvvyAPI

[![Supported Python versions](https://img.shields.io/pypi/pyversions/suvvyapi.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/suvvyapi)
[![PyPI version](https://img.shields.io/pypi/v/suvvyapi.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/suvvyapi)
[![PyPI downloads](https://img.shields.io/pypi/dm/suvvyapi.svg)](https://pypi.org/project/suvvyapi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Formatted with: isort](https://img.shields.io/badge/formatted%20with-isort-blue.svg)](https://github.com/psf/black)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

</div>

## About SuvvyAPI 📘

SuvvyAPI is an asynchronous Python API wrapper built on top of `httpx` for the Suvvy AI API, offering an easy and Pythonic way to interact with the Suvvy AI services.

## Installation 🛠️

To install SuvvyAPI, simply use pip:

```bash
pip install -U suvvyapi
```

## Usage 🚀

### Asynchronous Usage

You can use SuvvyAPI asynchronously as follows:

```python
import asyncio
from suvvyapi import AsyncSuvvy


async def main():
    async with AsyncSuvvy(
        token="<your token>",
    ) as suvvy:
        await suvvy.send_message(chat_id="somechat1", text="Привет!", source="Иван")


asyncio.run(main())

```
*Note: Replace "your token" with your actual token from [Suvvy AI](https://app.suvvy.ai/).*

### [More in documentation](https://github.com/suvvyai/suvvyapi/wiki)

## Troubleshooting 💡

For issues and troubleshooting, please refer to the [issues section](https://github.com/suvvyai/suvvyapi/issues) on the GitHub repository.

## Contribution 👥

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License 📄

SuvvyAPI is released under the [MIT License](https://github.com/suvvyai/suvvyapi/blob/main/LICENSE).
