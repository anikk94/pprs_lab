#include<iostream>
#include<librealsense2/rs.hpp>
// #include<opencv2/opencv.hpp>

int main()
{
    rs2::pipeline p;

    p.start();

    rs2::frameset frames = p.wait_for_frames();
    
    while (1) {

        rs2::depth_frame depth = frames.get_depth_frame();
    
        float width = depth.get_width();
        float height = depth.get_height();
    
        float dist_to_center = depth.get_distance(width/2, height/2);
    
        std::cout << "camera is facing object " << dist_to_center << " meters away \r";

    }

    // cv::Mat image = cv::imread("/root/xarm_ws/src/pprs_lab/pprs_lab_realsense/doc/stuff/raspberryPiImage.jpeg");

    // if(image.empty()){
    //     std::cout << "could not find or open the image" << std::endl;
    //     return -1;
    // }

    // cv::imshow("image", image);

    // cv::waitKey(0);

    // cv::destroyAllWindows();


    return 0;
}