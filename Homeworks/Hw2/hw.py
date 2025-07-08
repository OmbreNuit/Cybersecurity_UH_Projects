    def correction(self, distorted_image, k, interpolation_type):
        """Applies correction to a distorted image and performs interpolation
                image: the input image
                k: distortion parameter
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the corrected image"""
        col_y, row_x, channel = distorted_image.shape
        xCenter = row_x // 2
        yCenter = col_y // 2

        corrected_img = zeros((col_y, row_x, channel))

        for i in range(col_y):
            for j in range(row_x):
                x_dist = j - xCenter
                y_dist = i - yCenter

                r = math.sqrt(x_dist ** 2 + y_dist ** 2)
                r_inverse_distort = 1 + (k * r)

                x_cd = x_dist / r_inverse_distort
                y_cd = y_dist / r_inverse_distort

                x_correct = (r_inverse_distort + x_cd) + xCenter
                y_correct = (r_inverse_distort + y_cd) + yCenter
                interpolate = interpolation()
                if 0 <= y_correct < col_y and 0 <= x_correct < row_x:
                        if interpolation_type == "bilinear":
                            x1 = math.ceil(x_correct - 1)
                            x2 = math.floor(x_correct + 1)
                            y1 = math.ceil(y_correct - 1)
                            y2 = math.floor(y_correct + 1)

                            bilinear = interpolate.bilinear_interpolation(x1, x2, y1, y2, distorted_image)
                            corrected_img[i, j] = bilinear

                        elif interpolation_type == "nearest_neighbor":
                            corrected_img[i, j] = distorted_image[round(y_correct), round(x_correct)]

        return corrected_img


from dip import *
import math
class interpolation:

    def linear_interpolation(self, x, x1, x2, ix1, ix2):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for linear interpolation here
        if x1 == x2:
            return ix1
        linear = (((x2 - x) / (x2-x1)) * ix1) + (((x - x1) / (x2 - x1)) * ix2)
        return linear

    def bilinear_interpolation(self, px1, px2, py1, py2, image):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """
        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task
        Q11 = image[int(py1), int(px1)]
        Q21 = image[int(py1), int(px2)]
        Q12 = image[int(py2), int(px1)]
        Q22 = image[int(py2), int(px2)]

        R1 = self.linear_interpolation(px1, px1, px2, Q11, Q21)
        R2 = self.linear_interpolation(px1, px1, px2, Q12, Q22)
        i = self.linear_interpolation(py1, py1, py2, R1, R2)

        return i
