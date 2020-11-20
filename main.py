import cv2 as cv
import numpy as np
import os

base_dir = 'dataset/'

unknown_images = [f for f in os.listdir('dataset/Unknown/')]
training_images = [f for f in os.listdir('dataset/Training')]
print('Unknown Data:{}'.format(unknown_images))
print('Training Data:{}'.format(training_images))
results = []

for valid_pic in unknown_images:
    img1 = cv.imread(base_dir + 'Unknown/' + valid_pic, cv.IMREAD_GRAYSCALE)
    # load img2 in a f0r loop
    minHessian = 400
    detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
    kp1, d1 =  detector.detectAndCompute(img1, None)
    matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
    max_matches = 0
    any_good_matches = []
    image_match = ''
    # set up vars to use them outside inner scope
    img_matches = None
    for train_pic in training_images:
        training_path = base_dir + 'Training/' + train_pic
        img2 = cv.imread(base_dir + 'Training/' + train_pic, cv.IMREAD_GRAYSCALE)
        kp2, d2 =  detector.detectAndCompute(img2, None)
        # caching this data is prohibitive...
        knn_matches = matcher.knnMatch(d1, d2, 2)
        good_matches = []
        ratio_thresh = 0.5
        for m,n in knn_matches:
            if m.distance < ratio_thresh * n.distance:
                good_matches.append(m)
        if len(good_matches) > max_matches:
            any_good_matches.append((train_pic, good_matches))
            max_matches = len(good_matches)
            image_match = train_pic
        img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
        cv.drawMatches(img1, kp1, img2, kp2, good_matches, img_matches, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        # cv.imwrite('BEST_' + image_match + '_and_' + valid_pic + '.jpg', img_matches)

    print('Best match for {}: {} with {} matches'.format(valid_pic, image_match, max_matches))

    results.append([valid_pic, image_match, max_matches])

# because our image writing code just doesn't work...
for result in results:
    img1 = cv.imread(base_dir + 'Unknown/' + result[0], cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(base_dir + 'Training/' + result[1], cv.IMREAD_GRAYSCALE)
    detector = cv.xfeatures2d_SURF.create(hessianThreshold=400)
    kp1, d1 = detector.detectAndCompute(img1, None)
    matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
    kp2, d2 = detector.detectAndCompute(img2, None)
    knn_matches = matcher.knnMatch(d1, d2, k=2)
    good_matches = []
    ratio_thresh = 0.5
    for m,n in knn_matches:
        if m.distance < ratio_thresh * n.distance:
            good_matches.append(m)

    img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)

    cv.drawMatches(img1, kp1, img2, kp2, good_matches, img_matches, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv.imwrite(result[0] + '_and_' + result[1] + '_' + str(result[2]) + '.jpg', img_matches)