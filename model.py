import tensorflow as tf
import numpy as np
import os
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# train_ds = tf.keras.preprocessing.image_dataset_from_directory(
#     'dataset',
#     image_size=(256, 256),
#     batch_size=32,
#     subset='training',
#     seed=123,
#     shuffle=True,
#     validation_split=0.2,
# )
#
# val_ds = tf.keras.preprocessing.image_dataset_from_directory(
#     'dataset',
#     image_size=(256, 256),
#     batch_size=32,
#     subset='validation',
#     seed=123,
#     shuffle=True,
#     validation_split=0.2,
# )
#
#
# def normalize(i, anwer):
#     i = tf.cast(i / 255.0, tf.float32)
#     return i, anwer
#
#
# train_ds = train_ds.map(normalize)
# val_ds = val_ds.map(normalize)

img_generator = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20, # 회전
    zoom_range=0.15, # 확대
    width_shift_range=0.2, # 이동
    height_shift_range=0.2,
    shear_range=0.15,  # 굴정
    horizontal_flip=True, # 가로 반전
    fill_mode="nearest"
)

train_ds = img_generator.flow_from_directory(
    'dataset',
    class_mode='categorical', # 두개면 binary, 몇 개 더면 categorical
    shuffle=True,
    seed=123,
    color_mode='rgb',
    batch_size=64,
    target_size=(256, 256)
)

val_generator = ImageDataGenerator(rescale=1./255)

val_ds = val_generator.flow_from_directory(
    'dataset',
    class_mode='categorical',
    shuffle=True,
    seed=123,
    color_mode='rgb',
    batch_size=64,
)

Input = tf.keraslayers.Input(shape=(256, 256, 3))
x = tf.keras.layers.Conv2D(32, (3, 3),padding='same', activation='relu')(Input)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)
x = tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu')(x)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)
x = tf.keras.layers.Dropout(0.2)(x)
x = tf.keras.layers.Conv2D(128, (3, 3), padding='same', activation='relu')(x)
x = tf.keras.layers.MaxPooling2D((2, 2))(x)
x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(32, activation='relu')(x)
x = tf.keras.layers.Dense(16, activation='relu')(x)
Output = tf.keras.layers.Dense(1, activation='softmax')(x)


tensorboard = tf.keras.callbacks.TensorBoard(log_dir='./logs/{}'.format("model-"+str(int(time.time()))))

es = tf.keras.callbacks.EarlyStopping(
    monitor='accuracy',
    patience=5,
    mode='max',
)

model = tf.keras.models.Model(inputs=Input, outputs=Output)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

tf.keras.utils.plot_model(model,to_file='model.png',show_shapes=True,show_layer_names=True)

model.fit(train_ds, epochs=10, validation_data=val_ds, verbose=2, callbacks=[tensorboard, es])









