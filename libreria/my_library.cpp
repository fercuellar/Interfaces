/**
 * @file
 * @brief Librería para multiplicar coordenadas por 100
 */

#include <iostream>

/**
 * @brief Función para multiplicar las coordenadas por 100.
 *
 * @param[in,out] x - Coordenada X a multiplicar.
 * @param[in,out] y - Coordenada Y a multiplicar.
 * @param[in,out] z - Coordenada Z a multiplicar.
 */
extern "C" {
    void multiply_coords(float& x, float& y, float& z)
    {
        x *= 100.0;
        y *= 100.0;
        z *= 100.0;
        return;
    };
}
