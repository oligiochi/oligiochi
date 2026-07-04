<!--
  ============================================================================
  GitHub Profile README — oligiochi
  ============================================================================
  HOW THIS FILE WORKS
  - This repository (oligiochi/oligiochi) is special: its README is rendered
    on your GitHub profile page.
  - Everything that must be replaced by you is marked with a comment starting
    with "CUSTOMIZE:".
  - Widgets are embedded twice (dark + light variant) inside <picture> tags so
    they adapt automatically to the viewer's GitHub theme.
  - Color palette used across all widgets (GitHub's own accent colors):
      dark  theme → accent #58A6FF, text #C9D1D9, muted #8B949E, bg #0D1117
      light theme → accent #0969DA, text #24292F, muted #57606A, bg #FFFFFF
    If you change one widget's colors, change them everywhere to keep the
    profile visually consistent.
  ============================================================================
-->

<h1 align="center">Hi, I'm Giovanni Oliverio</h1>

<p align="center">
  MSc Computer Engineering student · Distributed Systems · Backend · DevOps
</p>

---

## Introduction

I'm a Computer Engineering master's student at Roma Tre University, specializing in distributed systems and decentralized coordination. My thesis — developed in cooperation with Virginia Commonwealth University — is a leaderless peer-to-peer coordination system for vehicular networks, written in Rust and validated experimentally on an HPC cluster. Around that core I work on backend services, rootless containers, Linux networking, and security, because building systems and keeping them reliable and safe are the same job.

## Current Focus

- **ParKing — cooperative smart parking for VANETs**: a fully decentralized, leaderless system where vehicles coordinate parking with no infrastructure and no central consensus — H3 geospatial indexing, epidemic gossip, and CRDTs in Rust/Tokio. Validated through SUMO + ns-3 (NR-V2X Mode 2) co-simulation on an HPC cluster, reaching a 92–98% park-rate, with Bayesian parameter optimization (+33% over the sequential benchmark). Built on [VaN3Twin](https://github.com/h3-vanet/VaN3Twin), a multi-stack ETSI-compliant V2X framework for ns-3.
- **Homelab and Linux infrastructure**: rootless Podman containers — AdGuard Home serving on port 53 through an nftables DNAT redirect with zero system privileges — plus network namespaces, veth, and server-hardening experiments.
- **Security**: Capture The Flag challenges (CyberChallenge.IT) and a growing collection of web-security exercises — SQL injection, XSS, command injection, hardening.

## Technologies

<!--
  CUSTOMIZE: badges use shields.io with a uniform dark background (24292e) and
  white logos. To add one:
  https://img.shields.io/badge/<LABEL>-24292e?style=flat&logo=<SIMPLE_ICONS_SLUG>&logoColor=white
  Logo slugs come from https://simpleicons.org (Java's slug is "openjdk").
  If a slug doesn't exist the badge still renders, just without the icon.
  The top-languages card on the right only counts public repositories owned by
  this account; "hide=" filters noise languages. See SETUP.md to include
  private repositories (requires self-hosting).
-->

<table>
  <tr>
    <td valign="top">
      <strong>Languages</strong><br>
      <img alt="Rust" src="https://img.shields.io/badge/Rust-24292e?style=flat&logo=rust&logoColor=white">
      <img alt="Java" src="https://img.shields.io/badge/Java-24292e?style=flat&logo=openjdk&logoColor=white">
      <img alt="Kotlin" src="https://img.shields.io/badge/Kotlin-24292e?style=flat&logo=kotlin&logoColor=white">
      <img alt="Python" src="https://img.shields.io/badge/Python-24292e?style=flat&logo=python&logoColor=white">
      <img alt="C" src="https://img.shields.io/badge/C-24292e?style=flat&logo=c&logoColor=white">
      <img alt="C#" src="https://img.shields.io/badge/C%23-24292e?style=flat&logo=sharp&logoColor=white">
      <img alt="Bash" src="https://img.shields.io/badge/Bash-24292e?style=flat&logo=gnubash&logoColor=white">
      <br><br>
      <strong>Backend & Data</strong><br>
      <img alt="Spring Boot" src="https://img.shields.io/badge/Spring_Boot-24292e?style=flat&logo=springboot&logoColor=white">
      <img alt="REST APIs" src="https://img.shields.io/badge/REST_APIs-24292e?style=flat&logoColor=white">
      <img alt="SQL" src="https://img.shields.io/badge/SQL-24292e?style=flat&logoColor=white">
      <img alt="Elasticsearch" src="https://img.shields.io/badge/Elasticsearch-24292e?style=flat&logo=elasticsearch&logoColor=white">
      <img alt="Gradle" src="https://img.shields.io/badge/Gradle-24292e?style=flat&logo=gradle&logoColor=white">
      <img alt="Maven" src="https://img.shields.io/badge/Maven-24292e?style=flat&logo=apachemaven&logoColor=white">
      <br><br>
      <strong>Distributed Systems</strong><br>
      <img alt="Microservices" src="https://img.shields.io/badge/Microservices-24292e?style=flat&logoColor=white">
      <img alt="Kafka" src="https://img.shields.io/badge/Kafka-24292e?style=flat&logo=apachekafka&logoColor=white">
      <img alt="Consul" src="https://img.shields.io/badge/Consul-24292e?style=flat&logo=consul&logoColor=white">
      <img alt="CRDT" src="https://img.shields.io/badge/CRDT-24292e?style=flat&logoColor=white">
      <img alt="P2P" src="https://img.shields.io/badge/P2P-24292e?style=flat&logoColor=white">
      <img alt="VANET" src="https://img.shields.io/badge/VANET-24292e?style=flat&logoColor=white">
      <br><br>
      <strong>DevOps & Cloud Native</strong><br>
      <img alt="Podman" src="https://img.shields.io/badge/Podman_(rootless)-24292e?style=flat&logo=podman&logoColor=white">
      <img alt="Docker" src="https://img.shields.io/badge/Docker-24292e?style=flat&logo=docker&logoColor=white">
      <img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-24292e?style=flat&logo=kubernetes&logoColor=white">
      <img alt="Jenkins" src="https://img.shields.io/badge/Jenkins-24292e?style=flat&logo=jenkins&logoColor=white">
      <img alt="CI/CD" src="https://img.shields.io/badge/CI%2FCD-24292e?style=flat&logo=githubactions&logoColor=white">
      <br><br>
      <strong>Networking & Security</strong><br>
      <img alt="TCP/IP" src="https://img.shields.io/badge/TCP%2FIP-24292e?style=flat&logoColor=white">
      <img alt="Linux Networking" src="https://img.shields.io/badge/Linux_Networking-24292e?style=flat&logo=linux&logoColor=white">
      <img alt="nftables" src="https://img.shields.io/badge/nftables-24292e?style=flat&logoColor=white">
      <img alt="Web Security" src="https://img.shields.io/badge/Web_Security_%2F_CTF-24292e?style=flat&logoColor=white">
      <br><br>
      <strong>Simulation</strong><br>
      <img alt="SUMO" src="https://img.shields.io/badge/SUMO-24292e?style=flat&logoColor=white">
      <img alt="ns-3" src="https://img.shields.io/badge/ns--3_(NR--V2X)-24292e?style=flat&logoColor=white">
      <br><br>
      <strong>OS & Tools</strong><br>
      <img alt="Linux" src="https://img.shields.io/badge/Linux-24292e?style=flat&logo=linux&logoColor=white">
      <img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-24292e?style=flat&logo=ubuntu&logoColor=white">
      <img alt="Git" src="https://img.shields.io/badge/Git-24292e?style=flat&logo=git&logoColor=white">
      <img alt="IntelliJ IDEA" src="https://img.shields.io/badge/IntelliJ_IDEA-24292e?style=flat&logoColor=white">
      <img alt="VS Code" src="https://img.shields.io/badge/VS_Code-24292e?style=flat&logoColor=white">
      <img alt="Wireshark" src="https://img.shields.io/badge/Wireshark-24292e?style=flat&logo=wireshark&logoColor=white">
    </td>
    <td valign="top" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/top-langs/?username=oligiochi&layout=compact&langs_count=8&custom_title=Top%20Languages%20%C2%B7%20all-time%2C%20public%20repos&hide=jupyter%20notebook,html,css&hide_border=true&bg_color=00000000&title_color=58A6FF&text_color=C9D1D9">
        <img alt="Most used languages" src="https://github-stats-extended.vercel.app/api/top-langs/?username=oligiochi&layout=compact&langs_count=8&custom_title=Top%20Languages%20%C2%B7%20all-time%2C%20public%20repos&hide=jupyter%20notebook,html,css&hide_border=true&bg_color=00000000&title_color=0969DA&text_color=24292F">
      </picture>
    </td>
  </tr>
</table>

## GitHub Statistics

<!--
  Widgets, all actively maintained as of 2026:
  - Stats + Top Languages + repo pins: github-stats-extended
    (stats-organization/github-stats-extended), the maintained successor of
    anuraghazra/github-readme-stats.
  - Streak: DenverCoder1/github-readme-streak-stats (streak-stats.demolab.com).
  - Activity graph: ashutosh00710/github-readme-activity-graph.
  - Snake: Platane/snk + month/weekday labels, generated daily by
    .github/workflows/generate-snake.yml into the "output" branch.
  Each widget appears twice inside a <picture> tag: the <source> is the dark
  variant, the <img> fallback is the light variant. GitHub picks the right one
  based on the viewer's theme.
  CUSTOMIZE: "oligiochi" appears in every widget URL — replace it everywhere
  if you reuse this profile under a different username.
-->

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api?username=oligiochi&show_icons=true&include_all_commits=true&custom_title=GitHub%20Stats%20%C2%B7%20since%20Aug%202019&hide_border=true&bg_color=00000000&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9">
    <img height="170" alt="General GitHub statistics" src="https://github-stats-extended.vercel.app/api?username=oligiochi&show_icons=true&include_all_commits=true&custom_title=GitHub%20Stats%20%C2%B7%20since%20Aug%202019&hide_border=true&bg_color=00000000&title_color=0969DA&icon_color=0969DA&text_color=24292F">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=oligiochi&hide_border=true&background=0D1117&ring=58A6FF&fire=58A6FF&currStreakNum=C9D1D9&sideNums=C9D1D9&currStreakLabel=58A6FF&sideLabels=8B949E&dates=8B949E">
    <img height="170" alt="Contribution streak" src="https://streak-stats.demolab.com?user=oligiochi&hide_border=true&background=FFFFFF&ring=0969DA&fire=0969DA&currStreakNum=24292F&sideNums=24292F&currStreakLabel=0969DA&sideLabels=57606A&dates=57606A">
  </picture>
</div>

<br>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=oligiochi&custom_title=Contribution%20Activity%20%C2%B7%20last%2031%20days&hide_border=true&bg_color=0D1117&color=C9D1D9&line=58A6FF&point=58A6FF&area=true&area_color=58A6FF">
    <img alt="Contribution graph" src="https://github-readme-activity-graph.vercel.app/graph?username=oligiochi&custom_title=Contribution%20Activity%20%C2%B7%20last%2031%20days&hide_border=true&bg_color=FFFFFF&color=24292F&line=0969DA&point=0969DA&area=true&area_color=0969DA">
  </picture>
</div>

<br>

<!--
  Contribution snake: generated by .github/workflows/generate-snake.yml
  (Platane/snk + a post-processing script that adds month/weekday labels).
-->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/oligiochi/oligiochi/output/github-contribution-grid-snake-dark.svg">
    <img alt="Contribution snake animation" src="https://raw.githubusercontent.com/oligiochi/oligiochi/output/github-contribution-grid-snake.svg">
  </picture>
  <br>
  <!--
    "last updated" badge: reads the date of the latest commit on the "output"
    branch, i.e. the last time the snake was regenerated. The animation always
    covers the rolling last ~12 months of contributions up to that date.
  -->
  <img alt="Snake last generated" src="https://img.shields.io/github/last-commit/oligiochi/oligiochi/output?label=last%2012%20months%20%C2%B7%20updated&style=flat&color=58A6FF&labelColor=24292e">
</div>

<!--
  Visitor counter: intentionally omitted. Hit counters read as dated, the
  numbers are trivially inflated, and strong engineering profiles skip them.
  If you still want one, the least intrusive maintained option is komarev's
  profile-views badge — uncomment the line below:
  <p align="center"><img src="https://komarev.com/ghpvc/?username=oligiochi&style=flat&color=58A6FF" alt="Profile views"></p>
-->

## Featured Projects

<!--
  CUSTOMIZE: each card pins one repository via github-stats-extended.
  A card renders an error image until the repository exists and is public.
  To pin a repository that lives in one of your organizations, set BOTH
  "username=<org-name>" and "repo=<repo-name>" in the two URLs.
  Other pinnable repositories: progetto-asw2024/asw-goodmusic-kubernetes,
  progetto-asw2024/asw-goodmusic-kafka, SIWprojectMonteVerde/SIW-Ripetizioni,
  MonteGuacamole/DatasetGen2026, oligiochi/SiwBook, oligiochi/DiaDiaPlus.
  The ParKing thesis repo (h3-vanet/vanet-parking) can be pinned the same way
  once it is public.
-->

<div align="center">
  <a href="https://github.com/h3-vanet/VaN3Twin">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/pin/?username=h3-vanet&repo=VaN3Twin&hide_border=true&bg_color=00000000&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9">
      <img alt="VaN3Twin repository card" src="https://github-stats-extended.vercel.app/api/pin/?username=h3-vanet&repo=VaN3Twin&hide_border=true&bg_color=00000000&title_color=0969DA&icon_color=0969DA&text_color=24292F">
    </picture>
  </a>
  <a href="https://github.com/progetto-asw2024/asw-goodmusic">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/pin/?username=progetto-asw2024&repo=asw-goodmusic&hide_border=true&bg_color=00000000&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9">
      <img alt="asw-goodmusic repository card" src="https://github-stats-extended.vercel.app/api/pin/?username=progetto-asw2024&repo=asw-goodmusic&hide_border=true&bg_color=00000000&title_color=0969DA&icon_color=0969DA&text_color=24292F">
    </picture>
  </a>
</div>

<div align="center">
  <a href="https://github.com/oligiochi/cyberSecurity">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/pin/?username=oligiochi&repo=cyberSecurity&hide_border=true&bg_color=00000000&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9">
      <img alt="cyberSecurity repository card" src="https://github-stats-extended.vercel.app/api/pin/?username=oligiochi&repo=cyberSecurity&hide_border=true&bg_color=00000000&title_color=0969DA&icon_color=0969DA&text_color=24292F">
    </picture>
  </a>
  <a href="https://github.com/oligiochi/MazeGenKotlin">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api/pin/?username=oligiochi&repo=MazeGenKotlin&hide_border=true&bg_color=00000000&title_color=58A6FF&icon_color=58A6FF&text_color=C9D1D9">
      <img alt="MazeGenKotlin repository card" src="https://github-stats-extended.vercel.app/api/pin/?username=oligiochi&repo=MazeGenKotlin&hide_border=true&bg_color=00000000&title_color=0969DA&icon_color=0969DA&text_color=24292F">
    </picture>
  </a>
</div>

## Research Interests

- **Distributed systems** — leaderless coordination, epidemic gossip protocols, and conflict-free replicated data types (CRDTs); my thesis applies them to vehicular scenarios where no central authority or infrastructure can be assumed.
- **Vehicular networking (V2X)** — NR-V2X sidelink communication and large-scale co-simulation (SUMO + ns-3), including experimental validation on HPC clusters.
- **Cloud computing** — container isolation (rootless in particular), orchestration, and what "cloud native" actually costs in observability and operational complexity.
- **Security** — web security, exploitation techniques from CTF practice, and Linux server hardening as a design constraint rather than an afterthought.
- **Machine learning** — an academic grounding (BSc thesis on ML prediction of acoustic loads on aerospace launchers) I draw on when a systems problem genuinely calls for learned components.

## Connect

<!--
  CUSTOMIZE: replace "YOUR-LINKEDIN-HANDLE" with the last segment of your
  LinkedIn profile URL. Icons come from https://skillicons.dev — add more with
  <a href="..."><img src="https://skillicons.dev/icons?i=<name>" width="48"></a>
  (e.g. i=discord, i=twitter, i=stackoverflow).
-->

<div align="center">
  <a href="https://www.linkedin.com/in/YOUR-LINKEDIN-HANDLE">
    <img src="https://skillicons.dev/icons?i=linkedin" width="48" alt="LinkedIn">
  </a>
  &nbsp;&nbsp;
  <a href="mailto:oligiovi2@gmail.com">
    <img src="https://skillicons.dev/icons?i=gmail" width="48" alt="Email">
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/oligiochi">
    <img src="https://skillicons.dev/icons?i=github" width="48" alt="GitHub">
  </a>
</div>
