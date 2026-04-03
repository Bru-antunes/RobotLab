#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#include "ground_station.h"
#include "config.h"

// Módulos internos (futuros)
#include "wifi_manager.h"
#include "ota_update.h"
#include "http_server.h"

static void ground_station_init(void)
{
    printf("[GROUND] Initializing Ground Station...\n");

    #if USE_WIFI
        wifi_manager_init();
    #endif

    #if USE_HTTP_SERVER
        http_server_start();
    #endif

    #if USE_OTA
        ota_init();
    #endif
}

static void ground_station_update(void)
{
    #if USE_WIFI
        wifi_manager_update();
    #endif

    #if USE_HTTP_SERVER
        http_server_update();
    #endif

    #if USE_OTA
        ota_handle();
    #endif
}

void ground_station_task(void *arg)
{
    ground_station_init();

    while (1)
    {
        ground_station_update();

        // Frequência baixa (não crítica)
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}
