#include<iostream>
#include<opencv2/opencv.hpp>

int main()
{
    cv::Mat image = cv::imread("/root/xarm_ws/src/pprs_lab/pprs_lab_realsense/doc/stuff/raspberryPiImage.jpeg");

    if(image.empty()){
        std::cout << "could not find or open the image" << std::endl;
        return -1;
    }

    cv::imshow("image", image);

    cv::waitKey(0);

    cv::destroyAllWindows();


    return 0;
}