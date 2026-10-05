# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

FROM node:22-bookworm-slim

# Authoring toolset: creators fetch assets and self-test verifiers and reference solutions here,
# so common runtimes are preinstalled instead of downloaded on every run.
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bash \
        build-essential \
        ca-certificates \
        curl \
        file \
        gh \
        git \
        git-lfs \
        jq \
        python3 \
        python3-pip \
        python3-venv \
        ripgrep \
        tar \
        unzip \
        wget \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh \
        | env UV_INSTALL_DIR=/usr/local/bin UV_NO_MODIFY_PATH=1 sh

# Kept in its own layer so a new Codex release reuses the cached toolset above.
ARG CODEX_VERSION
RUN test -n "$CODEX_VERSION" \
    && npm install --global "@openai/codex@${CODEX_VERSION}" \
    && mkdir -p /root/.codex \
    && rm -rf /root/.npm

WORKDIR /workspace

ENTRYPOINT ["codex"]
