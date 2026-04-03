# 📂 Estrutura do Projeto
```
darwinflow/
│
├── README.md
│
├── main/                             # 🚀 Entry point
│   ├── main.c                        # criação das tasks
│   └── app.c                         # inicialização geral
│
├── Architecture/
│
│   ├── GroundStation/                # 📡 Camada externa
│   │   ├── ground_station.c          # 🔥 implementação da camada
│   │   ├── ground_station.h
│   │   │
│   │   ├── Robots/
│   │   │   ├── robot_a/
│   │   │   │   ├── robot_config.h
│   │   │   │   ├── strategy.json
│   │   │   │   └── pinout_override.h
│   │   │   │
│   │   │   └── ...
│   │   │
│   │   ├── config.h                  # robô ativo
│   │   │
│   │   └── Communication/            # módulos internos (sem .c próprio)
│   │       ├── wifi_manager.h
│   │       ├── ota_update.h
│   │       └── http_server.h
│   │
│   ├── HighLevel/                    # 🧠 Decisão
│   │   ├── high_level.c              # 🔥 camada completa
│   │   ├── high_level.h
│   │   │
│   │   ├── Strategies/
│   │   │   ├── aggressive.h
│   │   │   ├── defensive.h
│   │   │   └── search.h
│   │   │
│   │   └── Mission/
│   │       ├── mission_manager.h
│   │
│   ├── MidLevel/                     # ⚙️ Controle
│   │   ├── mid_level.c               # 🔥 camada completa
│   │   ├── mid_level.h
│   │   │
│   │   ├── Control/
│   │   │   ├── pid.h
│   │   │
│   │   ├── SensorFusion/
│   │   │   ├── fusion.h
│   │   │
│   │   ├── Perception/
│   │   │   ├── perception.h
│   │   │
│   │   └── State/
│   │       ├── system_state.h
│   │
│   ├── LowLevel/                     # 🔌 Hardware
│   │   ├── low_level.c               # 🔥 camada completa
│   │   ├── low_level.h
│   │   │
│   │   ├── Drivers/
│   │   │   ├── motor_driver.h
│   │   │   ├── encoder_driver.h
│   │   │   ├── imu_driver.h
│   │   │   ├── ir_opponent.h
│   │   │   └── ir_edge.h
│   │   │
│   │   ├── HAL/
│   │   │   ├── gpio_hal.h
│   │   │   ├── pwm_hal.h
│   │   │   └── i2c_hal.h
│   │   │
│   │   ├── Pinouts/
│   │   │   ├── esp32s3_default.h
│   │   │   └── ...
│   │   │
│   │   └── Boards/
│   │       ├── esp32s3_devkit.h
│   │       └── ...
│   │
│   └── SafetyLayer/                  # 🛑 Segurança
│       ├── safety_layer.c            # 🔥 camada crítica
│       ├── safety_layer.h
│       │
│       ├── ir_safety.h
│       ├── emergency_stop.h
│       └── safety_manager.h
│
├── Libs/                             # 📦 reutilizáveis
│   ├── Math/
│   ├── Filters/
│   └── Utils/
│
├── Scripts/                          # 🐍 automação
│   └── manager.py
