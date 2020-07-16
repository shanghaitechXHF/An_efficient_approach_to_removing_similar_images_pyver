"""
Author: ShanghaitechXHF

"""

import cv2




def orb_similarity(img1_path,img2_path):

    """
    # Calculate Similarity

    Method: ORB + BF

    param img1_path
    param img2_path
    return Similarity

    """

    try:
        # Load images
        img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
        #print(img1)
    except:
        print("Load Failure")
        return -1

    try:
        # Initialize ORB Tester
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
    except:
        print("Init Failure")
        return -1

    try:
        # Extract and calculate descriptor
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    except:
        print("BF Failure")
        return -1
    
    try:    
        # KnnMatch
    matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

        # MaxMatch, coeffcient = 0.6 or 0.75, gooddist < coeffcient* maxdist
        good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
        print(len(good))
        print(len(matches))
        similary = len(good) / len(matches)
        print("Similary:%s" % similary)
        return similary
    except:
        print('Match Failure')
        return -1



def main():

    img1_path = r'ex\11.jpg'
    img2_path = r'ex\12.jpg'
    similary = orb_similarity(img1_path,img2_path)
    img1_path = r'ex\21.jpg'
    img2_path = r'ex\22.jpg'
    similary = orb_similarity(img1_path,img2_path)
    img1_path = r'ex\31.jpg'
    img2_path = r'ex\33.jpg'
    similary = orb_similarity(img1_path,img2_path)

if __name__ == '__main__':
    main()