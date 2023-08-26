import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from cnnClassifier.entity.config_entity import PrepareCallbacksConfig


class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config


    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    @property
    def _create_early_stopping(self):
        return EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=True)
    
    @property
    def _create_reduce_lr(self):
        return ReduceLROnPlateau(monitor="val_loss", factor=0.2, patience=5, min_lr=1e-6)

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks,
            self._create_early_stopping,
            self._create_reduce_lr
        ]
