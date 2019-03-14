API_PATH: str = '/api/v1'
DEFAULT_API_HOST: str = 'localhost'
DEFAULT_API_PORT: int = 6000

WEB3_PROVIDER_DEFAULT: str = "http://127.0.0.1:8545"

DEFAULT_PERCENTAGE_FEE: int = 1000  # in ppm

DIVERSITY_PEN_DEFAULT: int = 5
MAX_PATHS_PER_REQUEST: int = 25
DEFAULT_MAX_PATHS: int = 5  # number of paths return when no `max_path` argument is given

DEFAULT_REVEAL_TIMEOUT: int = 50

DEFAULT_SETTLE_TO_REVEAL_TIMEOUT_RATIO = 2

DEFAULT_POLL_INTERVALL = 10

# When a new IOU session is started, this is the minimum number of blocks
# between the current block and `expiration_block`.
MIN_IOU_EXPIRY = 1000
