import tensorflow as tf
import time
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing.image import ImageDataGenerator

inception_model = InceptionV3(input_shape=(150, 150, 3), include_top=False, weights=None)
inception_model.load_weights('./save_models/inception_v3_weights.h5')

# w 값 안건드릴거임
# for inception_layer in inception_model.layers:
#     inception_layer.trainable = False

# 파인 튜닝
unfreeze = False
for i in inception_model.layers:
    if i.name == 'mixed6': # mixed 6부터 다시 트레이닝
        unfreeze = True
    if unfreeze == True :
        i.trainable = True

img_generator = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.15,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    fill_mode="nearest"
)

train_ds = img_generator.flow_from_directory(
    'dataset',
    class_mode='categorical', # 두개면 binary, 몇 개 더면 categorical
    shuffle=True,
    seed=123,
    color_mode='rgb',
    batch_size=64,
    target_size=(150, 150)
)

val_generator = ImageDataGenerator(rescale=1./255)

val_ds = val_generator.flow_from_directory(
    'dataset',
    class_mode='categorical',
    shuffle=True,
    seed=123,
    color_mode='rgb',
    batch_size=64,
    target_size=(150, 150)
)
last_layer = inception_model.get_layer('mixed7')

layer_1 = tf.keras.layers.Flatten()(last_layer.output)
dense_1 = tf.keras.layers.Dense(1024, activation='relu')(layer_1)
drop_1 = tf.keras.layers.Dropout(0.2)(dense_1)
output = tf.keras.layers.Dense(3, activation='softmax')(drop_1)

model = tf.keras.Model(inputs=inception_model.input, outputs=output)

model.summary()
tf.keras.utils.plot_model(model, to_file='model.png',show_shapes=True, show_layer_names=True)

tensorboard = tf.keras.callbacks.TensorBoard(log_dir='./logs/{}'.format("model-"+str(int(time.time()))))

es = tf.keras.callbacks.EarlyStopping(
    monitor='accuracy',
    patience=5,
    mode='max',
)

model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=0.00001), metrics=['accuracy'], callbacks=[tensorboard, es])

model.fit(train_ds, epochs=10, validation_data=val_ds)


