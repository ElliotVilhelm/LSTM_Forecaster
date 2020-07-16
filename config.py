BATCH_SIZE = 16
BUFFER_SIZE = 10000
EPOCHS = 10
STEP = 1
HISTORY_SIZE = 4
TARGET_DIS = 1
FEATURES = ['Close', 'Volume', 'MA_short', 'Change_1', 'Change_4', 'Change_8']
DATA_DIR = 'data/SPY_2018_2020_1hr.csv'
DATA_SYM = 'SPY'
N_CLASSES = 4

LABEL_UP = [1, 0, 0, 0]
LABEL_UP_CHOP = [0, 1, 0, 0]
LABEL_DOWN = [0, 0, 1, 0]
LABEL_DOWN_CHOP = [0, 0, 0, 1]

TICKERS = ["SPY",
           "QQQ",
           "ROKU",
           "NVDA",
           "NFLX",
           "MSFT",
           "BA",
           "DDOG",
           "OKTA",
           "AAL",
           ]
