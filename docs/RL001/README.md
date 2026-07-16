# RL001 — Digital Infrared Sensor [EN]
Para a versão em Português, [clique aqui](#pt)

---

## 🔗 Project Links

- 🔧 Hardware: [RobotLab/hardware/RL001](https://github.com/Bru-antunes/RobotLab/tree/main/hardware/RL001)
- 📚 Documentation: [RobotLab/docs/RL001](https://github.com/Bru-antunes/RobotLab/tree/main/docs/RL001)
- 🔖 References: [RobotLab/docs/References](https://github.com/Bru-antunes/RobotLab/tree/main/docs/References)


The adoption of open-source technologies has played a fundamental role in the democratization of mobile robotics, enabling academic teams, researchers, and independent developers to access electronic designs, technical documentation, and development methodologies without the limitations imposed by proprietary solutions. This approach reduces implementation costs, facilitates the reproduction and adaptation of projects, and encourages collaboration among different research groups, thereby contributing to the scientific and technological advancement of the field [Berry et al., 2023; Gabriel Soares Borges et al., 2025]. In the context of competitive robotics, where small performance improvements can represent a decisive advantage during a competition, the development of custom hardware becomes a strategy to increase the technological autonomy of teams and reduce dependence on imported commercial components.

Among the various subsystems that make up a mobile robot, sensing stands out for establishing the interface between the control system and the external environment, enabling the identification of obstacles, arena boundaries, and opponents [Pawłow et al., 2018; Mohd Shukri et al., 2025]. Thus, the choice of sensing technology directly influences the robot's perception capabilities and, consequently, its performance in autonomous tasks. Digital infrared sensors continue to be employed in mobile robotics applications due to their low cost, short response time, and ease of integration, although they present limitations related to ambient lighting conditions and the optical properties of the detected materials [Ang and Min, 2024].

In this context, the development of open-source digital infrared sensors represents an alternative capable of combining competitive performance, accessibility, and knowledge dissemination. In addition to enabling the adaptation of the hardware to the specific requirements of the application, the open availability of the design allows other teams to reproduce, study, and improve the proposed solution, strengthening the robotics community and promoting practices aligned with the principles of open science and collaborative engineering [Berry et al., 2023]. Accordingly, this document presents the development of an open-source digital infrared sensor intended for opponent detection in mini sumo robots, covering the state of the art of the technology, its operating principles, the electronic design, simulation, and implementation of the proposed circuit.

---

## Applications
#### subtitle

---
<br><br><br>

# RL001 — Sensor Digital Infravermelho [PT]

<a name="pt"> </a>
---
## 🔗 Links do Projeto

- 🔧 Hardware: [RobotLab/hardware/RL001](https://github.com/Bru-antunes/RobotLab/tree/main/hardware/RL001)
- 📚 Documentação: [RobotLab/docs/RL001](https://github.com/Bru-antunes/RobotLab/tree/main/docs/RL001)
- 🔖 Referências: [RobotLab/docs/References](https://github.com/Bru-antunes/RobotLab/tree/main/docs/References)

---

A adoção de tecnologias open source tem desempenhado um papel fundamental na democratização da robótica móvel, permitindo que equipes acadêmicas, pesquisadores e desenvolvedores independentes tenham acesso a projetos eletrônicos, documentação técnica e metodologias de desenvolvimento sem as limitações impostas por soluções proprietárias. Essa abordagem reduz custos de implementação, favorece a reprodução e adaptação de projetos e estimula a colaboração entre diferentes grupos de pesquisa, contribuindo para o avanço científico e tecnológico da área [Berry et al., 2023 ; Gabriel Soares Borges et al.,2025]. No contexto da robótica competitiva, em que pequenas melhorias de desempenho podem representar vantagem decisiva durante uma competição, o desenvolvimento de hardware próprio torna-se uma estratégia para aumentar a autonomia tecnológica das equipes e reduzir a dependência de componentes comerciais importados.

Entre os diversos subsistemas que compõem um robô móvel, o sensoriamento destaca-se por estabelecer a interface entre o sistema de controle e o ambiente externo, permitindo a identificação de obstáculos, limites da arena e oponentes [Pawłow et al., 2018 ; Mohd Shukri et al., 2025]. Dessa forma, a escolha da tecnologia de sensoriamento influencia diretamente a capacidade de percepção do robô e, consequentemente, seu desempenho em tarefas autônomas. Sensores infravermelhos digitais continuam sendo empregados em aplicações de robótica móvel devido ao seu baixo custo, reduzido tempo de resposta e simplicidade de integração, embora apresentem limitações relacionadas à iluminação ambiente e às propriedades ópticas dos materiais detectados [Ang and Min, 2024].

Nesse cenário, a fabricação de sensores infravermelhos digitais de código aberto representa uma alternativa capaz de conciliar desempenho competitivo, acessibilidade e disseminação do conhecimento. Além de possibilitar a adaptação do hardware às necessidades específicas da aplicação, a disponibilização aberta do projeto permite que outras equipes reproduzam, estudem e aprimorem a solução desenvolvida, fortalecendo a comunidade de robótica e incentivando práticas alinhadas aos princípios da ciência aberta e da engenharia colaborativa [Berry et al., 2023]. Assim, essa documentação apresenta o desenvolvimento de um sensor infravermelho digital open source destinado à detecção de oponentes em robôs de mini sumô, abordando o estado da arte da tecnologia, os fundamentos de funcionamento, o projeto eletrônico, a simulação e a implementação do circuito proposto.



## Aplicações 

O estado da arte indica que sensores IR digitais permanecem relevantes em aplicações acadêmicas e industriais, especialmente quando utilizados em conjunto com outras tecnologias ou organizados em arquiteturas distribuídas. Revisões abrangentes, como \citep{A-Review-on-Sensor-Technologies}, posicionam os sensores infravermelhos dentro de um ecossistema mais amplo de tecnologias de percepção para robôs móveis, incluindo LiDAR, radar, sensores ultrassônicos e visão computacional. Embora apresentem boa precisão e baixa taxa de falha em aplicações como AGVs, esses sensores possuem limitações importantes, como sensibilidade à luz solar e dificuldade na detecção de materiais transparentes ou altamente absorventes, características também observadas em sensores IR digitais do tipo *maker*.

A literatura demonstra ainda que sensores IR digitais podem ser aplicados além da simples detecção de obstáculos. A tabela abaixo apresenta diferentes aplicações dessa tecnologia descritas no estado da arte. Em \citep{An-efficient-pulse}, por exemplo, sensores infravermelhos são empregados na detecção de pulsos cardíacos, explorando variações sutis na absorção da luz infravermelha provocadas pelo fluxo sanguíneo. Embora essa aplicação seja distinta da detecção de oponentes em robôs de mini sumô, o princípio físico permanece o mesmo, evidenciando o potencial de utilização desses sensores em sistemas mais sensíveis quando associados a técnicas adequadas de processamento de sinais. Em aplicações de automação e sistemas embarcados conectados, trabalhos como \citep{Design-and-implementation-of-IoT} demonstram a integração de sensores IR digitais com sensores ultrassônicos e microcontroladores dotados de conectividade, mantendo a lógica básica de saída binária. Já abordagens mais avançadas, como a apresentada em \citep{Dual-mode-Establishing}, mostram que o mesmo hardware infravermelho pode ser reutilizado tanto para detecção de obstáculos quanto para comunicação por linha de visão, ampliando sua funcionalidade sem alterações significativas no circuito. Além disso, o uso distribuído desses sensores também é explorado em \citep{Infrared-Sensor-based-Self-Adaptive}, no qual múltiplos sensores IR são empregados para estimar a densidade veicular e ajustar dinamicamente sistemas de controle.

| **Contexto de aplicação** | **Uso específico do sensor IR digital** |
|----------------------------|------------------------------------------|
| Robótica móvel acadêmica e industrial | Detecção de oponentes ou obstáculos em robôs móveis e AGVs. |
| Biomédica experimental | Detecção de pulsos cardíacos por variações na absorção da luz infravermelha. |
| Automação e sistemas embarcados | Detecção de presença integrada a microcontroladores e sistemas conectados. |
| Detecção e comunicação | Uso do sensor IR tanto para detecção de obstáculos quanto para comunicação por linha de visão. |
| Monitoramento de tráfego | Estimativa de densidade veicular a partir da detecção de passagem de veículos. |

**Tabela:** Aplicações de sensores infravermelhos digitais descritas no estado da arte. **Fonte:** RobotLab.


## Fundamentação

O sensor IR digital opera fundamentado em um par de componentes eletrônicos: um transmissor (LED infravermelho), responsável pela emissão de radiação infravermelha invisível ao olho humano, e um receptor (fotodiodo), sensível ao mesmo comprimento de onda. Seu funcionamento ocorre quando a luz emitida atinge a superfície de um objeto e é refletida de volta para o receptor, alterando sua resistência e a tensão de saída de forma proporcional à intensidade da luz recebida \citep{A-Review-on-Sensor-Technologies}. A figura abaixo ilustra o princípio de funcionamento de um sensor IR.

ADICIONAR IMAGEM AQUI 

Para processar esse sinal, o sensor utiliza um circuito comparador, que confronta a tensão gerada pelo fotodiodo com um limite predefinido ou ajustável \citep{Design-and-implementation-of-IoT, A-Review-Paper-on-Infrared-Sensor}. O resultado é uma saída digital binária (alto/baixo), que informa ao microcontrolador a presença de um obstáculo \citep{Infrared-Sensor-based-Self-Adaptive}. Devido à sua versatilidade, esse tipo de sensor é amplamente empregado em robótica para detecção e desvio de obstáculos em robôs móveis \citep{A-Review-on-Sensor-Technologies}. Além disso, pode ser utilizado em sistemas de comunicação entre dispositivos \citep{Dual-mode-Establishing}, aplicações na área da saúde \citep{An-efficient-pulse}, monitoramento de tráfego de veículos \citep{Infrared-Sensor-based-Self-Adaptive} e automação residencial.


