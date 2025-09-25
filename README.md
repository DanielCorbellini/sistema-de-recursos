# Overview

Web application to manage assets, reservations, checkouts, and returns. Backend built with Django REST Framework and frontend with React + Tailwind.

# Main Technologies

- **Backend**: Django + Django REST Framework, JWT (`rest_framework_simplejwt`) — config in [`recursos.settings`](Backend/recursos/recursos/settings.py).
  Key files: [`Backend/recursos/manage.py`](Backend/recursos/manage.py), [`recursos/urls.py`](Backend/recursos/recursos/urls.py).
- **Frontend**: React (Create React App) + Tailwind CSS. Entry point: [`Frontend/recursos-front/src/App.js`](Frontend/recursos-front/src/App.js).
  Authentication/frontend service: [`AuthService`](Frontend/recursos-front/src/AuthService.js).
  Packages and scripts: [`Frontend/recursos-front/package.json`](Frontend/recursos-front/package.json).
- **Database**: SQLite (default for development) — configuration in [`recursos.settings`](Backend/recursos/recursos/settings.py).

# Project Structure (summary)

- **Backend/**

  - `recursos/` (project): [`recursos/urls.py`](Backend/recursos/recursos/urls.py), [`recursos/settings.py`](Backend/recursos/recursos/settings.py)
  - apps: `bem`, `retiradas`, `reservas`, `core`
    - Asset models: [`bem.models.Bem`](Backend/recursos/bem/models.py), [`bem.models.Kit`](Backend/recursos/bem/models.py)
    - Serializers: [`bem.serializers.BemSerializer`](Backend/recursos/bem/serializers.py)
    - Views: [`bem.views.BemListView`](Backend/recursos/bem/views.py) (list), other CRUD views in [`bem/views.py`](Backend/recursos/bem/views.py)
    - Reservations: [`reservas.models.Reserva`](Backend/recursos/reservas/models.py), [`reservas.models.ItensReserva`](Backend/recursos/reservas/models.py)
    - Checkouts: endpoints and logic in [`retiradas.views`](Backend/recursos/retiradas/views.py) and serializers in [`retiradas.serializer`](Backend/recursos/retiradas/serializer.py)

- **Frontend/recursos-front/**
  - main components:
    - Asset List/Create/Edit: [`Frontend/recursos-front/src/components/Bem/index.js`](Frontend/recursos-front/src/components/Bem/index.js), form: [`BemCreateForm`](Frontend/recursos-front/src/components/Bem/BemCreateForm/index.js), filter: [`BemFilterForm`](Frontend/recursos-front/src/components/Bem/BemFilterForm/index.js)
    - Checkout: [`Frontend/recursos-front/src/components/Retirada/index.js`](Frontend/recursos-front/src/components/Retirada/index.js), user lookup: [`Retirada/UserLookup`](Frontend/recursos-front/src/components/Retirada/UserLookup/index.js), asset lookup: [`Retirada/BemLookup`](Frontend/recursos-front/src/components/Retirada/BemLookup/index.js), items modal: [`Retirada/RetiradaTableItems`](Frontend/recursos-front/src/components/Retirada/RetiradaTableItems/index.js)
    - Reservation: [`Frontend/recursos-front/src/components/Reserva/index.js`](Frontend/recursos-front/src/components/Reserva/index.js) and filter: [`Reserva/ReservaFilterForm`](Frontend/recursos-front/src/components/Reserva/ReservaFilterForm/index.js)
    - Return: [`Frontend/recursos-front/src/components/Devolucao/index.js`](Frontend/recursos-front/src/components/Devolucao/index.js)
    - Layout / Navigation: [`Layout`](Frontend/recursos-front/src/components/Layout/index.js), [`Menu`](Frontend/recursos-front/src/components/Menu/index.js), [`Header`](Frontend/recursos-front/src/components/Header/index.js)

# Main Workflows

- **Authentication**

  - Frontend calls the authentication API (routes in [`core.urls`](Backend/recursos/core/urls.py)) via [`AuthService`](Frontend/recursos-front/src/AuthService.js).
  - Tokens are stored in localStorage (`token`, `user`) and used in requests (JWT).

- **Asset CRUD**

  - Listing/pagination: frontend uses [`bem.views.BemListView`](Backend/recursos/bem/views.py) — base route `/bem/listar/` (see [`recursos/urls.py`](Backend/recursos/recursos/urls.py)).
  - Create/Edit: forms in [`BemCreateForm`](Frontend/recursos-front/src/components/Bem/BemCreateForm/index.js) and editing modal in [`Bem/index.js`](Frontend/recursos-front/src/components/Bem/index.js).
  - Serialization: [`bem.serializers.BemSerializer`](Backend/recursos/bem/serializers.py).

- **Checkout Workflow**

  1. Select user via [`Retirada/UserLookup`](Frontend/recursos-front/src/components/Retirada/UserLookup/index.js).
  2. Search available assets via [`Retirada/BemLookup`](Frontend/recursos-front/src/components/Retirada/BemLookup/index.js).
  3. Build checkout and confirm in modal [`Retirada/RetiradaTableItems`](Frontend/recursos-front/src/components/Retirada/RetiradaTableItems/index.js).
  4. Backend creates record in `Retiradas` and items in `ItensRetirada` — logic in [`retiradas.views.RetiradaCreateView`](Backend/recursos/retiradas/views.py) and serializers in [`retiradas.serializer.ItensRetiradaSerializer`](Backend/recursos/retiradas/serializer.py).

- **Reservation Workflow**

  - User can reserve assets (if `permite_reserva` is enabled on the asset). Models: [`reservas.models.Reserva`](Backend/recursos/reservas/models.py) and [`reservas.models.ItensReserva`](Backend/recursos/reservas/models.py). Routes in `reservas` (see [`recursos/urls.py`](Backend/recursos/recursos/urls.py)).

- **Return Workflow**
  - Searches items checked out by user and marks them as returned (route used by frontend in [`Devolucao/index.js`](Frontend/recursos-front/src/components/Devolucao/index.js)). Update logic is handled in `retiradas` endpoints.

# How to Run (development)

1. **Backend**

   - Create venv, activate it, and install dependencies:
     - `pip install -r Backend/recursos/requirements.txt`
   - Run migrations and server:
     - `python Backend/recursos/manage.py migrate`
     - `python Backend/recursos/manage.py createsuperuser`
     - `python Backend/recursos/manage.py runserver`
   - Config file: [`Backend/recursos/recursos/settings.py`](Backend/recursos/recursos/settings.py)

2. **Frontend**
   - Go to frontend and install dependencies:
     - `cd Frontend/recursos-front`
     - `npm install`
   - Run:
     - `npm start`
   - Main file: [`Frontend/recursos-front/src/App.js`](Frontend/recursos-front/src/App.js)
   - Tailwind config: [`Frontend/recursos-front/tailwind.config.js`](Frontend/recursos-front/tailwind.config.js)

# Important Settings

- CORS / allowed origins in [`recursos.settings`](Backend/recursos/recursos/settings.py).
- Routes and mappings in [`recursos/urls.py`](Backend/recursos/recursos/urls.py).
- Adjust endpoints used by frontend in [`AuthService`](Frontend/recursos-front/src/AuthService.js) and axios calls in components (`/bem/`, `/retiradas/`, `/reservas/`).

# Useful Reference Files

- Backend settings: [`Backend/recursos/recursos/settings.py`](Backend/recursos/recursos/settings.py)
- Project URLs: [`Backend/recursos/recursos/urls.py`](Backend/recursos/recursos/urls.py)
- Asset/Kit models: [`Backend/recursos/bem/models.py`](Backend/recursos/bem/models.py)
- Asset serializers: [`Backend/recursos/bem/serializers.py`](Backend/recursos/bem/serializers.py)
- Asset views: [`Backend/recursos/bem/views.py`](Backend/recursos/bem/views.py)
- Checkout views/serializers: [`Backend/recursos/retiradas/views.py`](Backend/recursos/retiradas/views.py), [`Backend/recursos/retiradas/serializer.py`](Backend/recursos/retiradas/serializer.py)
- Reservation models: [`Backend/recursos/reservas/models.py`](Backend/recursos/reservas/models.py)
- Frontend App: [`Frontend/recursos-front/src/App.js`](Frontend/recursos-front/src/App.js)
- AuthService (frontend): [`Frontend/recursos-front/src/AuthService.js`](Frontend/recursos-front/src/AuthService.js)
- Components: [`Frontend/recursos-front/src/components/Bem/index.js`](Frontend/recursos-front/src/components/Bem/index.js), [`Frontend/recursos-front/src/components/Retirada/index.js`](Frontend/recursos-front/src/components/Retirada/index.js), [`Frontend/recursos-front/src/components/Devolucao/index.js`](Frontend/recursos-front/src/components/Devolucao/index.js), [`Frontend/recursos-front/src/components/Reserva/index.js`](Frontend/recursos-front/src/components/Reserva/index.js)
