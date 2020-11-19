import cv2 as cv
import numpy as np
import os
import argparse

# p = argparse.ArgumentParser()
# p.add_argument("image", help="Path to image file")
# args = p.parse_args()
# print(args.image)

unknown_images = [f for f in os.listdir('mass_data/Unknown')]
training_images = [f for f in os.listdir('mass_data/Training')]
f = open('data.txt', 'w')
m = open('matches.txt', 'w')


for valid_pic in unknown_images:
    img1 = cv.imread(valid_pic, cv.IMREAD_GRAYSCALE)
    # load img2 in a f0r loop
    minHessian = 400
    detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
    kp1, d1 =  detector.detectAndCompute(img1, None)
    matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
    max_matches = 0
    any_good_matches = []
    image_match = ''
    # set up vars to use them outside inner scope
    img2 = None
    kp2, d2 = 0, 0
    img_matches = None
    for train_pic in training_images:
        img2 = cv.imread(train_pic, cv.IMREAD_GRAYSCALE)
        kp2, d2 =  detector.detectAndCompute(img2, None)
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
        cv.imwrite(image_match + ' and ' + valid_pic + '.jpg', img_matches)
    print('Best match for {}: {} with {} matches'.format(valid_pic, image_match, max_matches))
    f.write('Best match for {}: {} with {} matches.\n'.format(valid_pic, image_match, max_matches))
    m.write('{}\n'.format(any_good_matches))
    img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
    cv.drawMatches(img1, kp1, img2, kp2, good_matches, img_matches, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imwrite(image_match + ' and ' + valid_pic + '.jpg', img_matches)
#f.close()
#m.close()
