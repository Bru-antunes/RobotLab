# Orion — ESP32-S3 Integrated Board [EN]
Para a versão em Português, [clique aqui](#pt)

---

## 🔗 Project Links

- 🔧 Hardware: [RobotLab/hardware/Orion](https://github.com/Bru-antunes/RobotLab/tree/main/hardware/Orion)
- 📚 Documentation: [RobotLab/docs/Orion](https://github.com/Bru-antunes/RobotLab/tree/main/docs/Orion)
- 🔖 References: [RobotLab/docs/References](https://github.com/Bru-antunes/RobotLab/tree/main/docs/References)


---



## Title
#### subtitle

---
<br><br><br>

# Orion — Placa Integrada ESP32-S3 [PT]

<a name="pt"> </a>
---
## 🔗 Links do Projeto

- 🔧 Hardware: [RobotLab/hardware/Orion](https://github.com/Bru-antunes/RobotLab/tree/main/hardware/Orion)
- 📚 Documentação: [RobotLab/docs/Orion](https://github.com/Bru-antunes/RobotLab/tree/main/docs/Orion)
- 🔖 Referências: [RobotLab/docs/References](https://github.com/Bru-antunes/RobotLab/tree/main/docs/References)

---

Este projeto consiste no desenvolvimento de uma placa eletrônica dedicada ao controle de um sistema embarcado voltado para o controle de um robô de sumô, baseada no microcontrolador ESP32-S3. A placa de circuito impresso Orion foi projetada visando maior integração dos circuitos, confiabilidade, facilidade de fabricação e expansão de funcionalidades, mantendo uma arquitetura modular que facilita a manutenção e futuras atualizações. O projeto foi dividido em quatro blocos funcionais principais: **potência**, **alimentação**, **controle** e **sensoriamento**, permitindo que cada subsistema desempenhe funções específicas.

O bloco de potência é responsável pelo acionamento das cargas do sistema, realizando a interface entre o circuito de controle e os dispositivos que demandam maior corrente elétrica. Para isso, são empregados componentes de proteção e chaveamento capazes de garantir operação segura, reduzindo riscos provenientes de sobrecorrente, surtos elétricos e inversão de polaridade. O dimensionamento desse estágio foi realizado considerando a eficiência energética, a dissipação térmica e a confiabilidade durante operação contínua. O bloco de alimentação é responsável pelo condicionamento da energia proveniente da fonte externa, fornecendo tensões estáveis para todos os circuitos da placa. São utilizados conversores de tensão, filtros e componentes de proteção que asseguram o correto funcionamento dos dispositivos eletrônicos mesmo diante de variações na alimentação. A distribuição das diferentes tensões foi organizada de forma a atender aos requisitos de cada circuito, minimizando ruídos e garantindo estabilidade ao sistema. O bloco de controle constitui o núcleo do sistema, sendo responsável pelo processamento das informações provenientes dos sensores e pelo gerenciamento dos dispositivos conectados à placa. Nessa etapa encontra-se o microcontrolador, responsável pela execução dos algoritmos de controle, comunicação entre periféricos, processamento dos sinais de entrada e geração dos comandos para os estágios de potência. A arquitetura foi desenvolvida priorizando modularidade, capacidade de expansão e integração com diferentes interfaces de comunicação. O bloco de sensoriamento reúne os circuitos responsáveis pela aquisição das informações necessárias para o funcionamento do sistema. Os sensores fornecem ao controlador dados referentes às condições de operação, permitindo monitoramento em tempo real e tomada de decisões baseada nas variáveis medidas. Para garantir maior confiabilidade das medições, foram incorporados circuitos de condicionamento de sinais, filtragem e proteção das entradas, reduzindo interferências eletromagnéticas e aumentando a robustez do sistema.


## Título

#### Subtítulo
