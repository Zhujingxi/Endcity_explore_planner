#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <cmath>
#include <limits>
#include <algorithm>

namespace py = pybind11;

double distance_cal_noSqrt(const std::pair<double, double>& p1, const std::pair<double, double>& p2) {
    return std::pow(p1.first - p2.first, 2) + std::pow(p1.second - p2.second, 2);
}

std::vector<std::pair<double, double>> generate_path(const std::pair<double, double>& start_point, 
                                                     std::vector<std::pair<double, double>> corlist, 
                                                     int num_path) {
    std::vector<std::pair<double, double>> path;
    path.push_back(start_point);

    for (int p = 1; p < num_path; ++p) {
        double min_distance = std::numeric_limits<double>::infinity();
        int min_index = -1;
        for (size_t i = 0; i < corlist.size(); ++i) {
            double dist = distance_cal_noSqrt(path.back(), corlist[i]);
            if (dist < min_distance) {
                min_distance = dist;
                min_index = i;
            }
        }

        path.push_back(corlist[min_index]);
        corlist.erase(corlist.begin() + min_index);
    }

    return path;
}

PYBIND11_MODULE(generate_path_module, m) {
    m.def("generate_path", &generate_path, "Generate path",
          py::arg("start_point"), py::arg("corlist"), py::arg("num_path"));
}
