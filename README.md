# Muse Backend API

Backend service for **Muse**, an AI-powered personal style assistant that helps users coordinate hairstyles, clothing, accessories, and personal preferences into intentional, personalized looks.

The backend provides the API layer connecting the Muse mobile application with authentication, user data, image processing, AI analysis, and recommendation services.

> **Project Status:** Active Development — MVP

---

## Overview

Muse is designed as a mobile-first application with a React Native frontend and a Python/FastAPI backend.

The backend is responsible for:

- User authentication and authorization
- User profiles and style preferences
- Image upload and processing
- AI-powered image and style analysis
- Personalized recommendation generation
- Persistence of user data and styling history
- API communication between the mobile client and backend services

The API is designed to keep the mobile client decoupled from internal services such as the database, image storage, and AI providers.

---

## Architecture

The backend follows a layered architecture designed to separate API routing, business logic, data access, and external service integrations.

```text
                    ┌─────────────────────┐
                    │   React Native App  │
                    └──────────┬──────────┘
                               │
                         HTTPS / REST
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI API      │
                    │      Layer          │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
       Authentication    User Services       AI Services
             │                 │                 │
             │                 │        ┌────────┼────────┐
             │                 │        │        │        │
             │                 │        ▼        ▼        ▼
             │                 │    Vision   Context   Prompt
             │                 │    Analysis Builder   Engine
             │                 │        │        │        │
             │                 │        └────────┼────────┘
             │                 │                 ▼
             │                 │          Recommendation
             │                 │             Engine
             │                 │
             └──────────┬──────┴─────────────────┘
                        │
                        ▼
                  PostgreSQL