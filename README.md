# Qliqy QR Code Generator

![CI](https://github.com/ilia2003/Qliqy/actions/workflows/qrcode-generator-build.yml/badge.svg)
![Status](https://img.shields.io/badge/status-active%20development-b4492f)

QR generation worker for Qliqy.

## What It Does

- generates QR images for public form URLs
- supports the public sharing flow used by `webapi`

## How It Works

`webapi` requests QR creation through RabbitMQ. `qrcode_generator` creates the image and returns it so the backend can store and expose it through the public API.

## Product Note

Public registration is intentionally disabled while the platform is in a controlled testing stage.

Test account:

```json
{
  "email": "admin@admin.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "admin123"
}
```

- Developer: Ilia Fedorenko
- Teammate: Ernest Berezin
