from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException


class Shortener(BaseShortener):
    """Git.io shortener Implementation

    Example:

        >>> import pyshorteners
        >>> s = pyshorteners.Shortener()
        >>> s.gitio.short('https://github.com/TEST')
        'https://git.io/abc123'
        >>> s.gitio.expand('https://git.io/abc123')
        'https://github.com/TEST'
    """

    api_url = "https://git.io"

    def short(self, url):
        """Short implementation for TinyURL.com

        Args:
            url: the URL you want to shorten

        Returns:
            A string containing the shortened URL

        Raises:
            ShorteningErrorException: If the API returns an error as response
        """
        shorten_url = self.api_url
        data = {"url": url}
        response = self._post(shorten_url, data=data)

        if not response.headers["Location"]:
            raise ShorteningErrorException()

        return response.headers["Location"]
