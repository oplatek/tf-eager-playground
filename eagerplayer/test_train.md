Without eager execution the code works fine
-------------------------------------------

	oplatek@gpu:master:tf-eager-playground$ ./eagerplayer/test_train.py
	Epoch 1/1
	2019-01-30 16:49:23.921582: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
	2019-01-30 16:49:24.032120: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:964] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
	2019-01-30 16:49:24.032526: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1432] Found device 0 with properties:
	name: GeForce GTX 1080 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.6575
	pciBusID: 0000:01:00.0
	totalMemory: 10.92GiB freeMemory: 10.76GiB
	2019-01-30 16:49:24.032540: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1511] Adding visible gpu devices: 0
	2019-01-30 16:49:24.230759: I tensorflow/core/common_runtime/gpu/gpu_device.cc:982] Device interconnect StreamExecutor with strength 1 edge matrix:
	2019-01-30 16:49:24.230787: I tensorflow/core/common_runtime/gpu/gpu_device.cc:988]      0
	2019-01-30 16:49:24.230792: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1001] 0:   N
	2019-01-30 16:49:24.230947: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 10407 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:01:00.0, compute capability: 6.1)
	1000/1000 [==============================] - 1s 745us/step - loss: 11.4860 - acc: 0.0810
	success


With eager execution non Keras optimizer is expected
----------------------------------------------------

	oplatek@gpu:master:tf-eager-playground$ ./eagerplayer/test_train.py eager
	2019-01-30 16:49:33.983911: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
	2019-01-30 16:49:34.069258: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:964] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
	2019-01-30 16:49:34.069657: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1432] Found device 0 with properties:
	name: GeForce GTX 1080 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.6575
	pciBusID: 0000:01:00.0
	totalMemory: 10.92GiB freeMemory: 10.76GiB
	2019-01-30 16:49:34.069671: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1511] Adding visible gpu devices: 0
	2019-01-30 16:49:34.266286: I tensorflow/core/common_runtime/gpu/gpu_device.cc:982] Device interconnect StreamExecutor with strength 1 edge matrix:
	2019-01-30 16:49:34.266311: I tensorflow/core/common_runtime/gpu/gpu_device.cc:988]      0
	2019-01-30 16:49:34.266316: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1001] 0:   N
	2019-01-30 16:49:34.266465: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 10407 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:01:00.0, compute capability: 6.1)
	Traceback (most recent call last):
	  File "./eagerplayer/test_train.py", line 35, in <module>
		fit_keras_model()
	  File "./eagerplayer/test_train.py", line 27, in fit_keras_model
		metrics=['accuracy'])
	  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/training/checkpointable/base.py", line 474, in _method_wrapper
		method(self, *args, **kwargs)
	  File "/usr/local/lib/python3.5/dist-packages/tensorflow/python/keras/engine/training.py", line 410, in compile
		'a %s' % type(optimizer))
	ValueError: optimizer must be an instance of tf.train.Optimizer, not a <class 'str'>

