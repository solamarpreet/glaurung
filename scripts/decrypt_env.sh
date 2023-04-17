#!/bin/bash
gpg --quiet --batch --yes --decrypt --passphrase="$ENV_SECRET_PASSPHRASE" --output .env .env.gpg