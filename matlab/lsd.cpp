#include <mex.h>
#include <lsd.h>
#include <cv.h>
#include <vector>
#include <string>
#include <highgui.h>
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
    std::string picture = mxArrayToString(prhs[0]);
    cv::Mat src = cv::imread(picture.c_str(), CV_LOAD_IMAGE_COLOR);
    cv::Mat tmp, src_gray;
    cv::cvtColor(src, tmp, CV_RGB2GRAY);
    tmp.convertTo(src_gray, CV_64FC1);

    image_double image = new_image_double(src_gray.cols, src_gray.rows);
    image->data = src_gray.ptr<double>(0);

    ntuple_list ntl = lsd(image);

    plhs[0] = mxCreateDoubleMatrix(5, ntl->size, mxREAL);
    double *pos_mat = mxGetPr(plhs[0]);

    for (int j = 0; j != ntl->size ; ++j)
    {
        pos_mat[5 * j + 0] = ntl->values[0 + j * ntl->dim] + 1;
        pos_mat[5 * j + 2] = ntl->values[1 + j * ntl->dim] + 1;
        pos_mat[5 * j + 1] = ntl->values[2 + j * ntl->dim] + 1;
        pos_mat[5 * j + 3] = ntl->values[3 + j * ntl->dim] + 1;
        pos_mat[5 * j + 4] = ntl->values[4 + j * ntl->dim]; // width
    }
}