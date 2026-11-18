#!/bin/sh
set -eu
[ "$#" -gt 0 ] || {
  printf '%s\n' 'mibserver-entrypoint.sh requires a command' >&2
  exit 64
}
configure_ipv6_listeners() {
  listener_directory="$1"
  mib_listener="${listener_directory}/mib-ipv6.conf"
  status_listener="${listener_directory}/status-ipv6.conf"
  ipv6_enabled="${MIBSERVER_IPV6_ENABLED-false}"
  (
    umask 077
    mkdir -p "${listener_directory}"
    case "${ipv6_enabled}" in
      false)
        : >"${mib_listener}"
        : >"${status_listener}"
        ;;
      true)
        printf '%s\n' 'listen [::]:8000 ipv6only=on;' >"${mib_listener}"
        printf '%s\n' 'listen [::]:8080 ipv6only=on;' >"${status_listener}"
        ;;
      *)
        printf '%s\n' \
          "MIBSERVER_IPV6_ENABLED must be true or false, received: ${ipv6_enabled}" \
          >&2
        exit 64
        ;;
    esac
  )
}
configure_ipv6_listeners /tmp/mibserver-nginx/ipv6-listeners
/app/local_mibs.sh
exec "$@"
