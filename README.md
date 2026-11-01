# Linux Systems · Networking · Infrastructure

Open-source projects focused on embedded Linux, network services, diagnostics, automation, and reliable software delivery.

## Featured engineering projects

### [r2o](https://github.com/t0fox/r2o) — Adaptive network processing

A router-side network engine for **OpenWrt and Keenetic**, with a dedicated packet-processing datapath, a separate controller, and automated discovery of connection problems.

- **Design:** NFQUEUE integration, TCP/TLS/QUIC traffic observation, persistent strategy state, and resource-aware background checks.
- **Verification:** automated regression tests, comparisons against the d2o implementation, QEMU/OpenWrt checks, and architecture-specific release builds.
- **Status:** actively developed; passing automated checks does not imply full validation on every physical router.

[Source & architecture](https://github.com/t0fox/r2o) · [CI](https://github.com/t0fox/r2o/actions/workflows/ci.yml) · [Releases](https://github.com/t0fox/r2o/releases)

### [z2kOW](https://github.com/t0fox/z2kOW) — Embedded Linux integration

An independent **OpenWrt port and extension of z2k**, integrating network tooling with the operating system rather than requiring a separate server.

- **System integration:** fw4/nftables, procd, UCI, ubus, routing, traffic diagnostics, and a local web panel.
- **Delivery:** per-architecture packages, signed update metadata, integrity checks, service lifecycle management, and rollback/recovery paths.

[Source](https://github.com/t0fox/z2kOW) · [CI](https://github.com/t0fox/z2kOW/actions/workflows/ci.yml) · [Releases](https://github.com/t0fox/z2kOW/releases) · [Operational documentation](https://github.com/t0fox/z2kOW/blob/main/docs/openwrt-release-operations.md)

### [d2o](https://github.com/t0fox/d2o) — Traffic analysis and diagnostics

An independent development of **d2k** for router-side traffic handling. It provides a C-based implementation used as a behavioral reference for r2o, while remaining its own project.

- **Networking:** connection monitoring, adaptive strategy selection, TCP/UDP/QUIC handling, and Discord voice paths.
- **Components:** local Telegram proxy, network diagnostics, router service integration, and web management.

[Source](https://github.com/t0fox/d2o) · [CI](https://github.com/t0fox/d2o/actions/workflows/ci.yml) · [Releases](https://github.com/t0fox/d2o/releases)

## Backend & infrastructure projects

| Project | Engineering scope |
| --- | --- |
| [Subscription Aggregator API](https://github.com/t0fox/subscription-aggregator-api) | REST API, PostgreSQL, migrations, pagination, Swagger, health/readiness probes, Docker Compose, and CI tests. |
| [dev-ops-backend](https://github.com/t0fox/dev-ops-backend) | Nginx reverse proxy, isolated Docker networking, containerized backend, and automated smoke tests. |
| [VelvLens](https://github.com/t0fox/VelvLens) | Portable desktop packaging, local-only backend, pinned upstream dependencies, runtime checks, and build verification. |

## Technical areas

**Linux & networking:** OpenWrt, TCP/IP, TLS, QUIC, NFQUEUE, nftables, firewall and routing integration.

**Infrastructure & backend:** Docker, Docker Compose, Nginx, PostgreSQL, REST APIs, service management, CI/CD.

**Testing & delivery:** QEMU, cross-architecture builds, regression testing, release automation, Ed25519 verification, SHA-256 checks, and rollback.

## GitHub activity

The animation runs over the contribution calendar without hiding its existing activity cells. Updated automatically by [GitHub Actions](https://github.com/t0fox/t0fox/actions/workflows/snake.yml).

![Contribution snake — dark theme](https://raw.githubusercontent.com/t0fox/t0fox/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)
![Contribution snake — light theme](https://raw.githubusercontent.com/t0fox/t0fox/output/github-contribution-grid-snake.svg#gh-light-mode-only)
