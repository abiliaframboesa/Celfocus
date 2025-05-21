# TelePlan
App desenvolvida no âmbito do Celfocus GenAI Hackathon

# Overview
Este projeto visa oferecer personalização hiper-recomendada para utilizadores de serviços de telecomunicações, com base na análise automatizada das suas faturas mensais. Através da inteligência de dados e automação, a plataforma identifica oportunidades de poupança e recomenda planos mais adequados ao perfil real de consumo do utilizador.

# Problem Statement
Utilizadores de telecoms frequentemente pagam por serviços que não usam totalmente ou que não são ideais para o seu perfil de consumo.

As operadoras não oferecem recomendações neutras ou personalizadas com base no uso real.

A comparação entre planos é complexa e pouco transparente para o utilizador comum.

# Solução Proposta
Criação de uma plataforma digital inteligente que permite ao utilizador:
- Fazer upload das suas faturas de telecomunicações (pdf ou imagem).
- Obter uma análise automática dos consumos (voz, dados, SMS, extras).
- Ver recomendações personalizadas com base:
  No seu perfil de uso;
  Nos planos disponíveis no mercado (extraídos via webscraping);
  Na economia potencial em relação ao plano atual.

# Funcionalidades
- Frontend
  Interface para upload de fatura.
  Exibição de análise detalhada.
  Recomendações e comparação de planos.
  Dashboard de economia potencial.

- Backend
  Módulo de OCR
  Extrai dados estruturados (minutos, dados móveis, custo, etc.) de faturas PDF/Imagem.
  Usa modelos OCR (ex: Tesseract, EasyOCR, Azure Form Recognizer).
  Módulo de Cálculo de Poupança
  Analisa o uso real vs. planos disponíveis.
  Calcula economia potencial por plano alternativo.

- Webscraping
  Recolhe plafonds e preços de planos atuais de operadoras (MEO, NOS, Vodafone, etc.).
  Atualizações periódicas para garantir informação atualizada.

# Futuras Expansões
Criação de perfil inteligente por IA com histórico de uso.
Envio automático de alertas mensais de poupança.
Integração com apps móveis.
API pública para parceiros (bancos, comparadores, etc.).

