FIND_PACKAGE(OpenCV REQUIRED)

ADD_EXECUTABLE(lsd_opencv_example lsd_opencv_example.cpp)
TARGET_LINK_LIBRARIES(lsd_opencv_example lsd ${OpenCV_LIBS})