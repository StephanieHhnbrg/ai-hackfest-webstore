# AI Hackfest Webstore

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?color=blue)](./LICENSE.md)
[![Angular](https://img.shields.io/badge/Angular-%23DD0031.svg?logo=angular&logoColor=white)](https://angular.dev/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)

### 📌 Introduction
This project is part of my contribution to the [AI Hackfest 2025](https://ai-hackfest-23772.devpost.com/)  \
The primary contribution is contained in the repository: \
👉 [ai-hackfest-marketeer](https://github.com/StephanieHhnbrg/ai-hackfest-marketeer).

The project is about mail marketing and tackles the problem of customers having overloaded inboxes, causing newsletters to go unnoticed, reducing their impact.
The goal is to boost sales and increase click-through rates (CTR) by delivering more effective and personalized content.

Therefore an AI-powered Marketing Platform, called Marketeer, was built that leverages A/B testing to optimize email campaigns and ensure they reach their full potential.

This repository hosts the mock e-commerce webstore and its associated Python backend scripts deployed via Google Cloud Run.
Its core purpose is to track user interactions coming from email campaigns and generate analytics for performance evaluation.

### 📈 Tracked events
* `email_opened`
* `email_bttn_clicked`
* `purchases_completed`
* `webpage_call`

It also records click-through time (from  opening the webstore until clicking on the purchase button), helping refine future targeting and scheduling.


### 🔗 Related Links
* [ai-hackfest-marketeer](https://github.com/StephanieHhnbrg/ai-hackfest-marketeer)
* [presentation slides](https://docs.google.com/presentation/d/e/2PACX-1vT4rmUlvcelOwf5hNHB_eoIHHoYhM1gh0xf7YV2z_uhADdzVt7d7KzcQUeL2MCCb8qpOc18vHEW7Ac6/pub?start=false&loop=false&delayms=3000)

### 🛠️ Local Setup
This project was generated using [Angular CLI](https://github.com/angular/angular-cli) version 19.2.7. \
The live version is deployed as a <a href='https://stephaniehhnbrg.github.io/ai-hackfest-webstore/' target='_blank'>Github Page</a>.

#### Run locally
- Install dependencies: `npm install`
- Start project: `npm run start`

#### Gcloud Run Setup
For each python script in the [gcloudrun direction](./gcloudrun), do as follow:
1. Go to [GCloud Run console](https://console.cloud.google.com/run)
2. Click on the `(...) Write a function button`
3. Configure:
- service name
- region
- runtime: Python 3.12
- authentication: Allow unauthenticated invocations
- minimum number of instances: 1
4. Add the [python scripts](./gcloudrun) and the requirements.txt into the code editor of the Source tab
5. Deploy, then copy the endpoint from the Networking tab and update it in the [enviroment variables](./src/environments) 

#### Firestore Setup
* Create a Firestore DB called `marketing campaign` via [Firestore Studio](https://console.cloud.google.com/firestore/databases)
* Enable the [Firestore API](https://console.cloud.google.com/apis/dashboard)
