#                    _                _
#   ___ ___ _ __ ___| |__  _ __ ___  (_) ___
#  / __/ _ \ '__/ _ \ '_ \| '__/ _ \ | |/ _ \
# | (_|  __/ | |  __/ |_) | | |  __/_| | (_) |
#  \___\___|_|  \___|_.__/|_|  \___(_)_|\___/
#
#Proprietary software created by CEREBRE.
#© CEREBRE, USA. All rights reserved.
#Visit us at: https://www.cerebre.io

#!/bin/bash
set -e

readonly service="$1"

cd "./$service"
echo "$service imports..."
readonly gofiles=$(find . -type f -iname '*.go' | grep -v /vendor/)
goimports -w $gofiles
echo "$service fmt..."
gofmt -w -s $gofiles
