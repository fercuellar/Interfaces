#include <iostream>
extern "C" {
    void multiply_coords(float& x, float& y, float& z)
    {
        x *= 100.0;
        y *= 100.0;
        z *= 100.0;
        return;
    };

}