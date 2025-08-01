#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>

int main()
{
    pcl::PCLPointCloud2::Ptr cloud(new pcl::PCLPointCloud2);
    pcl::PCLPointCloud2::Ptr voxel_cloud(new pcl::PCLPointCloud2);
    pcl::PCDReader cloud_reader;
    pcl::PCDWriter cloud_writer;

    std::string path = "/root/xarm_ws/src/pprs_lab/pprs_lab_realsense/doc/stuff/";
    cloud_reader.read(path+std::string("table_scene_lms400.pcd"), *cloud);

    std::cout << "source cloud points " << cloud->width * cloud->height << std::endl;
    
    pcl::VoxelGrid<pcl::PCLPointCloud2> voxel_filter;
    voxel_filter.setInputCloud(cloud);
    voxel_filter.setLeafSize(0.01, 0.01, 0.01);
    voxel_filter.filter(*voxel_cloud);

    std::cout << "output cloud points " << voxel_cloud->width * voxel_cloud->height << std::endl;


    cloud_writer.write(path+std::string("table_scene_lms400_voxelized_cloud.pcd"), *voxel_cloud, Eigen::Vector4f::Zero(), Eigen::Quaternionf::Identity(), false);

    return 0;
}