# 66 Helm. Creating a chart
kubectl create configmap pg-init-scripts --from-file=./db/schema.sql --from-file=./db/seed.sql

values.yaml<<
primary:
  initdb:
    scriptsConfigMap: pg-init-scripts

helm install pg bitnami/postgresql -f values.yaml
