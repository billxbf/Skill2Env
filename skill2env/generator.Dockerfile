# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

FROM node:22-bookworm-slim

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        curl \
        file \
        gh \
        git \
        git-lfs \
        jq \
        tar \
        unzip \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Kept in its own layer so a new Codex release reuses the cached toolset above.
ARG CODEX_VERSION
RUN test -n "$CODEX_VERSION" \
    && npm install --global "@openai/codex@${CODEX_VERSION}" \
    && mkdir -p /root/.codex \
    && rm -rf /root/.npm

WORKDIR /workspace

ENTRYPOINT ["codex"]
