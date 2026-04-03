#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "app.h"

// Camadas do sistema
#include "safety_layer.h"
#include "low_level.h"
#include "mid_level.h"
#include "high_level.h"
#include "ground_station.h"

void app_start(void)
{
    printf("\n=== DARWINFLOW START ===\n");

    // ==========================
    // 🛑 SAFETY LAYER (máxima prioridade)
    // ==========================
    xTaskCreate(
        safety_layer_task,
        "safety_layer",
        2048,
        NULL,
        10,
        NULL
    );

    // ==========================
    // ⚙️ MID LEVEL
    // ==========================
    xTaskCreate(
        mid_level_task,
        "mid_level",
        4096,
        NULL,
        7,
        NULL
    );

    // ==========================
    // 🔌 LOW LEVEL
    // ==========================
    xTaskCreate(
        low_level_task,
        "low_level",
        4096,
        NULL,
        6,
        NULL
    );

    // ==========================
    // 🧠 HIGH LEVEL
    // ==========================
    xTaskCreate(
        high_level_task,
        "high_level",
        4096,
        NULL,
        5,
        NULL
    );

    // ==========================
    // 📡 GROUND STATION
    // ==========================
    xTaskCreate(
        ground_station_task,
        "ground_station",
        4096,
        NULL,
        3,
        NULL
    );
}
