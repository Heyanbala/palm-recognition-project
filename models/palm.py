import tensorflow as tf

gpu_devices = tf.config.list_physical_devices('GPU')

if gpu_devices:
    print(f" GPU is ready now: {gpu_devices[0]}"
          )
else: 
    print("GPU NOT FOUND"
          )