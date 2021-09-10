# Coffee Shop Full Stack

This project is mainly target for user authentication and authorization with Auth0 and RBAC flow. UI is writtern by angular and This is include following functinality:

- Barista Role
  - Can see the menu of coffee
  - Can see the detail of coffee
- Manager Role
  - Can create the new coffee type
  - Can edit the coffee
  - Can delete the coffee
  - Can see the coffee menu

### AUTH0 Account

```Python3
AUTH0_DOMAIN = 'lwincoffeeshop.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffeeshop'
```

### Manager Account

```Python3
Username = manager@testing.com
Password = Lwinmoe!23
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxhX1RlS212WHpELUZNZzhGVzlfZSJ9.eyJpc3MiOiJodHRwczovL2x3aW5jb2ZmZWVzaG9wLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0MmRhNThmZmI3NDAwNzFkYTBiODkiLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNjMxMjQyMjQxLCJleHAiOjE2MzEyNDk0NDEsImF6cCI6IjB0djBMZXByQTljdzZBWkFiUFRFTjFlbW9CVFRpdllBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.yEsLE5Eh-ZryA4f8gxIIElCoZQX8KlWX2OyBTj7SLkZw3OImmlScO0m4oYeeSPh2Y4QhMawOzen3UvqFae_3wEVqwJbLbGK9E3qOcM0iPSlmD_Eu9GXAxnoRaunf44D93I3K_VUCGYpOC_5c530usJnHdvUwK9NbifemulxU-RHhrVqyFsruSGIdGt8QOfib4-0xcDspW5hu0pVReikuCZfFtMn3tnSBgU9pMWaKTDCftL35TCoAcWKZ5tD050H2bph1dCWSLy6_GWLaReWREaTy2kSDbRL_pHhZq5uK-BWK2mWhwUOtDuPqKL86Cumj7za-T1Ok34BpkjOMqGouRA'
```

### Barista Account

```Python3
Username = user@testing.com
Password = Lwinmoe!23
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxhX1RlS212WHpELUZNZzhGVzlfZSJ9.eyJpc3MiOiJodHRwczovL2x3aW5jb2ZmZWVzaG9wLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0MmQ3MjY5MDk3ODAwNmMzZGZjNmQiLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNjMxMjQyMTI2LCJleHAiOjE2MzEyNDkzMjYsImF6cCI6IjB0djBMZXByQTljdzZBWkFiUFRFTjFlbW9CVFRpdllBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.MEA0S3lebHCBMagxlRDHyBAxw3WjGySIqDSxB4RQKu3MRUpbXcUNj_FqwCh8H5DMuMc8T97_vEEtazf1UOc_mduOvbzKxWljVlj933OsZOBr4CEihy4A2RD6AUdzF78TRpGCPayzSjmuCtLaGIkYpJyBuMQJ_mPrzlIW_j2flPpp3N-MURGoOHs7o5bu0dXRhAjRCwlisOAqb5Jx-oXIIeh3LpsMgeXMzey5KXH3MuDIqcs9Mmw0bsu4GGAe2Up_YIKEYEPBhFX24M3ESCdu5mAjX9LCVkbkZmGuq2E3WSarn-kmls-73lMV8wq3WNYlcYCPfgceZAV2DCztDahjUg'
```

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)
