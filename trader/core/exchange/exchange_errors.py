from core.errors import Error


class ExchangeNotFoundError(Error):
    msg = (
        'Exchange {exhange_name} not found. Please specify exchange '
        'supported, verify spelling for accuracy and check internet '
        'connection.'
    )


class InvalidHistoryTimeframeError(Error):
    msg = (
        'CCXT timeframe {timeframe} not supported by the exchange.'
    )


class InvalidTickerError(Error):
    msg = (
        'Exchange {exhange_name} does not have {ticker} pair'
    )


class ExchangeRequestError(Error):
    msg = (
        'Request failed'
        '{e}'
    )
