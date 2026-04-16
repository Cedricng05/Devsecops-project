# DevSecOps Project – Pipeline CI/CD sécurisé avec GitHub Actions

## Contexte

Ce projet a été réalisé dans le cadre du module DevSecOps du cursus CCSN.  
L’objectif est de mettre en place un pipeline CI/CD sécurisé en intégrant des contrôles de sécurité à différentes étapes du cycle de développement.

Ce projet s’appuie sur mes expériences personnelles.

---

## Objectifs

- Mettre en place un pipeline CI/CD avec GitHub Actions
- Intégrer des outils de sécurité (SCA, scan container, linting, policy-as-code)
- Appliquer les principes DevSecOps vus en cours (Shift-Left, automatisation)
- Trouver un équilibre entre sécurité et performance

---

## ⚙️ Pipeline CI/CD

Le pipeline est déclenché sur :
- push sur la branche `main`
- pull request

### Étapes principales :

1. **Build de l’image Docker**
2. **Scan SCA (filesystem) avec Trivy**
3. **Scan de l’image Docker avec Trivy**
4. **Lint des fichiers YAML**
5. **Vérification de conformité (Policy-as-Code) avec Conftest**

---

## 🔐 Sécurité intégrée

### 🔍 SCA – Software Composition Analysis

- Analyse des dépendances du projet
- Détection des vulnérabilités connues (CVE)
- Utilisation de Trivy en mode filesystem

👉 Non bloquant pour ne pas ralentir le développement

---

### 🐳 Scan des images Docker

- Analyse de l’image construite
- Blocage uniquement sur les vulnérabilités critiques

```yaml
exit-code: 1
severity: CRITICAL
ignore-unfixed: true