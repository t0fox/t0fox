# Kirill (t0fox)

**Systems & Backend Development · Linux Networking · DevOps**

I build open-source software for Linux and embedded routers, with a focus on network protocols, reliability, diagnostics, and reproducible releases. My projects cover low-level packet processing in **Rust and C**, backend development in **Go**, and automation for Linux/OpenWrt.

## Selected projects

| Project | What I work on |
| --- | --- |
| **[r2o](https://github.com/t0fox/r2o)** · Rust | Router-side networking system for OpenWrt/Keenetic: NFQUEUE datapath, TCP/TLS/QUIC traffic observation, automated strategy discovery, persistent state, and a separate controller. Includes multi-architecture builds, signed releases, and QEMU/differential tests. *Actively developed; real-device validation is ongoing.* |
| **[d2o](https://github.com/t0fox/d2o)** · C/C11 | Independent development based on d2k: packet processing and connection diagnostics, TCP/UDP/QUIC handling, Discord voice paths, a C11 Telegram proxy, and a web control panel. |
| **[z2kOW](https://github.com/t0fox/z2kOW)** · OpenWrt / Rust / Shell | OpenWrt port and extension of z2k. Integrates with **fw4/nftables, procd, UCI and ubus**; includes network diagnostics, a Rust Telegram component, architecture-specific packaging, signed updates, and rollback logic. |
| **[Subscription Aggregator API](https://github.com/t0fox/subscription-aggregator-api)** · Go | REST service using **Gin, PostgreSQL and pgx**: CRUD, reporting, migrations, pagination, health/readiness checks, Swagger, Docker Compose, and CI tests. |
| **[dev-ops-backend](https://github.com/t0fox/dev-ops-backend)** · Docker | Containerized Python backend behind **Nginx** with an isolated Docker network, health checks, and GitHub Actions smoke tests. |
| **[VelvLens](https://github.com/t0fox/VelvLens)** · Electron | Portable Windows desktop wrapper for Sub-Store with a loopback-only backend, pinned runtime, packaging, and automated smoke checks. |

## Technical stack

- **Languages:** Rust, C/C11, Go, Bash/Shell, Python, JavaScript.
- **Linux & networking:** Linux, OpenWrt, TCP/IP, TLS, UDP/QUIC, NFQUEUE, nftables, firewall rules, routing, network debugging.
- **Backend & infrastructure:** PostgreSQL, Gin, Docker, Docker Compose, Nginx, REST APIs, Git, GitHub Actions.
- **Testing & delivery:** cross-compilation, QEMU, automated tests, CI pipelines, release packaging, Ed25519 signatures, SHA-256 verification.

## Engineering interests

Resource-constrained Linux systems, network software, service lifecycle management, observability, automated regression testing, and reliable deployment/update workflows.

## GitHub activity

The contribution animation is generated daily by [GitHub Actions](https://github.com/t0fox/t0fox/actions/workflows/snake.yml).

![GitHub contribution snake — dark theme](https://raw.githubusercontent.com/t0fox/t0fox/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)
![GitHub contribution snake — light theme](https://raw.githubusercontent.com/t0fox/t0fox/output/github-contribution-grid-snake.svg#gh-light-mode-only)
