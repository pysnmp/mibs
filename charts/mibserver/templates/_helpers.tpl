{{/*
Expand the name of the chart.
*/}}
{{- define "mibserver.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "mibserver.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "mibserver.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "mibserver.labels" -}}
helm.sh/chart: {{ include "mibserver.chart" . }}
{{ include "mibserver.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
app.kubernetes.io/component: mib-library

{{/*
Selector labels
*/}}
{{- define "mibserver.selectorLabels" -}}
app.kubernetes.io/name: {{ include "mibserver.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "mibserver.serviceAccount" -}}
{{- if .Values.serviceAccount }}
{{- .Values.serviceAccount | toYaml }}
{{- else }}
{{- dict "create" true "annotations" dict "name" "" | toYaml }}
{{- end }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "mibserver.serviceAccountName" -}}
{{- $serviceAccount := fromYaml (include "mibserver.serviceAccount" .)}}
{{- if $serviceAccount.create }}
{{- default (include "mibserver.fullname" .) $serviceAccount.name }}
{{- else }}
{{- default "default" $serviceAccount.name }}
{{- end }}
{{- end }}

{{/*
Create mibserver.service
*/}}
{{- define "mibserver.service" -}}
{{- if .Values.service }}
{{- .Values.service | toYaml }}
{{- else }}
{{- dict "type" "ClusterIP" "port" 80 | toYaml }}
{{- end }}
{{- end }}


{{/*
Create mibserver.autoscaling
*/}}
{{- define "mibserver.autoscaling" -}}
{{- if .Values.autoscaling }}
{{- .Values.autoscaling | toYaml }}
{{- else }}
{{- dict "enabled" true "minReplicas" 1 "maxReplicas" 3 "targetCPUUtilizationPercentage" 80 | toYaml }}
{{- end }}
{{- end }}

{{/*
Create mibserver.autoscaling
*/}}
{{- define "mibserver.podAntiAffinity" -}}
{{- if .Values.podAntiAffinity }}
{{- .Values.podAntiAffinity }}
{{- else }}
{{- "soft" }}
{{- end }}
{{- end }}

{{/*
Create mibserver.networkPolicy
*/}}
{{- define "mibserver.networkPolicy" -}}
{{- if .Values.networkPolicy }}
{{- .Values.networkPolicy | toYaml }}
{{- else }}
{{- dict "enabled" false | toYaml}}
{{- end }}
{{- end }}

{{/*
Whether to render pv and pvc for local mibs
*/}}
{{- define "mibserver.enablePV" -}}
{{- if and .Values.localMibs.pathToMibs ( eq .Values.localMibs.persistence.existingClaim "" ) }}
{{- "true" }}
{{- else }}
{{- "false" }}
{{- end }}
{{- end }}