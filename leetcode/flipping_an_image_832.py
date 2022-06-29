class Solution:
    def flipAndInvertImage(self, image):
        # for i in range(len(image)):
        #     image[i] = image[i][::-1]
        #     #invert each element of the image replace 0 with 1 and 1 with 0
        #     for j in range(len(image[i])):
        #         image[i][j] = 1 - image[i][j]
        # return image
        #93 ms
        return [[x ^ 1 for x in x][::-1] for x in image] 