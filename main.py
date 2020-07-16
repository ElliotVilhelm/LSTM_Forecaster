import tensorflow as tf
import numpy as np
from datetime import datetime

from data_collection.yfinance_collector import get_multi_df
from analysis.distribution_analysis import get_class_sum
from data_processing.data_processing import get_tfds
from config import LABEL_UP, LABEL_UP_CHOP, LABEL_DOWN, LABEL_DOWN_CHOP, TICKERS
from tf_kit.callbacks import TENSORBOARD_CB, VALIDATION_CB, CONFUSION_CB
from tf_kit.model import get_lstm
from config import BATCH_SIZE, EPOCHS

tf.random.set_seed(42)

x_train, y_train, x_val, y_val = get_multi_df(TICKERS)

print(get_class_sum(y_train))
print(get_class_sum(y_val))
print(x_train.shape)
print(y_train.shape)
print(x_val.shape)
print(y_val.shape)

tfds_train, tfds_val = get_tfds(x_train, y_train, x_val, y_val)
window = int(x_train.shape[0] / BATCH_SIZE)

ssm = get_lstm()
history = ssm.fit(tfds_train, epochs=EPOCHS,
                  steps_per_epoch=window,
                  validation_data=tfds_val,
                  validation_steps=int(y_val.shape[0]/BATCH_SIZE),
                  callbacks=[VALIDATION_CB, TENSORBOARD_CB, CONFUSION_CB])

for x, y in tfds_val.take(10):
    print(ssm.predict(x), y)


