# Threat Modeling with PASTA

## Overview

This project demonstrates the application of the PASTA (Process for Attack Simulation and Threat Analysis) methodology to model threats for a sneaker e-commerce application. The analysis covers the stages of PASTA, from defining business objectives to analyzing risks and impacts.

## Project Files

* **PASTA Worksheet.pdf:** A worksheet detailing each stage of the PASTA methodology applied to the scenario.
* **PASTA Data Flow Diagram.pdf:** A data flow diagram illustrating the application's product search process.
* **PASTA Attack Tree.pdf:** An attack tree visualizing potential attack paths against the application.

## PASTA Methodology Stages

1.  **Define Business and Security Objectives:**
    * The primary business objective is to enable users to efficiently find shoes listed by sellers.
    * Security objectives include securely handling search queries, maintaining user trust, and preventing data manipulation.
2.  **Define the Technical Scope:**
    * Focus is on API OWASP compliance to ensure backend security and data integrity.
    * SQL queries are analyzed for potential vulnerabilities like SQL injection.
3.  **Decompose Application:**
    * A data flow diagram illustrates the product search process.
4.  **Threat Analysis:**
    * Identified threats include SQL injection and session hijacking.
5.  **Vulnerability Analysis:**
    * Vulnerabilities identified include lack of prepared statements and weak session management.
6.  **Attack Modeling:**
    * An attack tree visualizes potential attack paths.
7.  **Risk Analysis and Impact:**
    * Mitigation strategies include prepared statements, input validation, TLS cryptography, and session timeout.

## Key Findings

* The PASTA methodology provides a structured approach to threat modeling.
* SQL injection and session hijacking pose significant threats to the application.
* Implementing appropriate security controls can mitigate identified risks.

## Conclusion

This project demonstrates the effectiveness of the PASTA methodology in identifying and analyzing potential threats and vulnerabilities in a web application. It highlights the importance of proactive security measures to protect against cyber attacks.
