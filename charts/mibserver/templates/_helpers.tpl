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
{{- define "mibserver.serviceAccountName" -}}
{{- default ( include "mibserver.fullname" .) }}
{{- end }}

{{/*
Create mibserver.podAntiAffinity
*/}}
{{- define "mibserver.podAntiAffinity" -}}
{{- if .Values.podAntiAffinity }}
{{- printf "%s" .Values.podAntiAffinity }}
{{- else }}
{{- "soft" }}
{{- end }}
{{- end }}
