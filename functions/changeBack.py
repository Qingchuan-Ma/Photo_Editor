from mrcnn import utils
from mrcnn import model as modellib
import os
import sys
import numpy as np

# This function is used to change the colorful background information to grayscale.
# image[:,:,0] is the Blue channel,image[:,:,1] is the Green channel, image[:,:,2] is the Red channel
# mask == 0 means that this pixel is not belong to the object.
# np.where function means that if the pixel belong to background, change it to gray_image.
# Since the gray_image is 2D, for each pixel in background, we should set 3 channels to the same value to keep the grayscale.

def apply_mask(image, gray_image, mask):
    image[:, :, 0] = np.where(
        mask == 0,
        gray_image[:, :, 0],
        image[:, :, 0]
    )
    image[:, :, 1] = np.where(
        mask == 0,
        gray_image[:, :, 1],
        image[:, :, 1]
    )
    image[:, :, 2] = np.where(
        mask == 0,
        gray_image[:, :, 2],
        image[:, :, 2]
    )
    return image


# This function is used to show the object detection result in original image.
def display_instances(image, gray_image, boxes, masks, ids, names, scores):
    # max_area will save the largest object for all the detection results
    max_area = 0

    # n_instances saves the amount of all objects
    n_instances = boxes.shape[0]

    if not n_instances:
        print('NO INSTANCES TO DISPLAY')
    else:
        assert boxes.shape[0] == masks.shape[-1] == ids.shape[0]

    for i in range(n_instances):
        if not np.any(boxes[i]):
            continue

        # compute the square of each object
        y1, x1, y2, x2 = boxes[i]
        square = (y2 - y1) * (x2 - x1)

        # use label to select person object from all the 80 classes in COCO dataset
        label = names[ids[i]]
        if label == 'person':
            # save the largest object in the image as main character
            # other people will be regarded as background
            if square > max_area:
                max_area = square
                mask = masks[:, :, i]
            else:
                continue
        else:
            continue

        # apply mask for the image
    # by mistake you put apply_mask inside for loop or you can write continue in if also
    image = apply_mask(image, gray_image, mask)

    return image
def mask_rcnn_background(image, gray_image):
	#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#cv2.imshow('gray_image', gray_image)
	# Load the pre-trained model data
	ROOT_DIR = os.path.abspath("./libs/Mask_RCNN-master1")
	MODEL_DIR = os.path.join(ROOT_DIR, "logs")
	COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")
	if not os.path.exists(COCO_MODEL_PATH):
		utils.download_trained_weights(COCO_MODEL_PATH)

	sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))
	import coco

	# Change the config infermation
	class InferenceConfig(coco.CocoConfig):
		GPU_COUNT = 1
		IMAGES_PER_GPU = 1


	config = InferenceConfig()
	# COCO dataset object names
	model = modellib.MaskRCNN(
		mode="inference", model_dir=MODEL_DIR, config=config
	)
	model.load_weights(COCO_MODEL_PATH, by_name=True)
	class_names = [
		'BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
		'bus', 'train', 'truck', 'boat', 'traffic light',
		'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
		'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
		'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
		'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
		'kite', 'baseball bat', 'baseball glove', 'skateboard',
		'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
		'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
		'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
		'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
		'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
		'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
		'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
		'teddy bear', 'hair drier', 'toothbrush'
	]
	results = model.detect([image], verbose=0)
	r = results[0]
	frame = display_instances(
		image, gray_image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores']
	)
	return frame
	'''cv2.imshow('save_image', frame)

	k = cv2.waitKey(0)

	# Wait for keys to exit or save
	cv2.imwrite('save_image.jpg', frame)'''