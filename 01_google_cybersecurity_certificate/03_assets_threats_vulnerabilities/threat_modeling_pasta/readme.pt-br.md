# Modelagem de Ameaças com PASTA

## Visão Geral

Este projeto demonstra a aplicação da metodologia PASTA (Process for Attack Simulation and Threat Analysis) para modelar ameaças para um aplicativo de e-commerce de tênis. A análise cobre os estágios do PASTA, desde a definição dos objetivos de negócios até a análise de riscos e impactos.

## Arquivos do Projeto

* **PASTA Worksheet.pdf:** Uma planilha detalhando cada estágio da metodologia PASTA aplicada ao cenário.
* **PASTA Data Flow Diagram.pdf:** Um diagrama de fluxo de dados ilustrando o processo de busca de produtos do aplicativo.
* **PASTA Attack Tree.pdf:** Uma árvore de ataque visualizando os potenciais caminhos de ataque contra o aplicativo.

## Estágios da Metodologia PASTA

1.  **Definir Objetivos de Negócios e Segurança:**
    * O objetivo principal do negócio é permitir que os usuários encontrem eficientemente os tênis listados pelos vendedores.
    * Os objetivos de segurança incluem o tratamento seguro de consultas de busca, a manutenção da confiança do usuário e a prevenção da manipulação de dados.
2.  **Definir o Escopo Técnico:**
    * O foco está na conformidade com o OWASP API para garantir a segurança do backend e a integridade dos dados.
    * As consultas SQL são analisadas em busca de potenciais vulnerabilidades, como injeção de SQL.
3.  **Decompor o Aplicativo:**
    * Um diagrama de fluxo de dados ilustra o processo de busca de produtos.
4.  **Análise de Ameaças:**
    * As ameaças identificadas incluem injeção de SQL e sequestro de sessão.
5.  **Análise de Vulnerabilidades:**
    * As vulnerabilidades identificadas incluem a falta de prepared statements e o gerenciamento de sessão fraco.
6.  **Modelagem de Ataques:**
    * Uma árvore de ataque visualiza os potenciais caminhos de ataque.
7.  **Análise de Risco e Impacto:**
    * As estratégias de mitigação incluem prepared statements, validação de entrada, criptografia TLS e timeout de sessão.

## Principais Descobertas

* A metodologia PASTA fornece uma abordagem estruturada para a modelagem de ameaças.
* A injeção de SQL e o sequestro de sessão representam ameaças significativas ao aplicativo.
* A implementação de controles de segurança apropriados pode mitigar os riscos identificados.

## Conclusão

Este projeto demonstra a eficácia da metodologia PASTA na identificação e análise de potenciais ameaças e vulnerabilidades em um aplicativo web. Ele destaca a importância de medidas de segurança proativas para proteger contra ataques cibernéticos.
