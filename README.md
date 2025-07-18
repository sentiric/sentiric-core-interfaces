# Sentiric Core Interfaces

**Description:** This repository holds shared definitions for API contracts (e.g., gRPC Protocol Buffers files, OpenAPI/Swagger specifications), fundamental data structures, and universal constants used across all Sentiric microservices.

**Core Responsibilities:**
*   Ensuring consistent communication formats and data models between services.
*   Enabling automated code generation for API clients and servers in various programming languages.

**Technologies:**
*   Language-agnostic (e.g., `.proto` files for Protocol Buffers, `.yaml`/`.json` files for OpenAPI).
*   Code generation tools (e.g., `protoc`).

**Usage:**
This is **not a running service**; it's a **shared library/contracts repository**. Other services will include this repository as a development dependency and use its definitions to generate client/server code or to ensure data consistency.

**Local Development:**
1.  Clone this repository: `git clone https://github.com/sentiric/sentiric-core-interfaces.git`
2.  Navigate into the directory: `cd sentiric-core-interfaces`
3.  (Optional: If you have code generation tools configured) Run code generation: `make generate` (or similar command).

**Deployment:**
Not applicable as this is not a deployable service. Changes here require dependent services to be re-compiled and re-deployed.

**Contributing:**
We welcome contributions! Please refer to the [Sentiric Governance](https://github.com/sentiric/sentiric-governance) repository for coding standards and contribution guidelines. Strict review for changes is crucial due to broad impact.

**License:**
This project is licensed under the [License](LICENSE).
