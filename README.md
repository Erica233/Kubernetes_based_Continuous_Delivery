# 721 Project 2 - Kubernetes_based_Continuous_Delivery

[![Python application test with Github Actions](https://github.com/Erica233/Kubernetes_based_Continuous_Delivery/actions/workflows/main.yml/badge.svg)](https://github.com/Erica233/Kubernetes_based_Continuous_Delivery/actions/workflows/main.yml)

## Introduction
It is my 721 project 2. My microservice provides a simple profit margin calculator. It can calculate the profit margin, given cost and revenue. You can append "/cal_profit/{cost}/{revenue}" to the URL to get the results. For example, you can append "/cal_profit/100/200" to get "{"profit_margin":0.5}".


## How did I implement it
I wrote it on Cloud9 environment, and git push to my github repo and set up actions to deploy continuous integration of it.
I created a docker container for it, and pushed the docker image to ECR.
I created App Runner Service for automatically deploying the most updated version.
It is a Kubernetes based service containing Continuous Delivery.
