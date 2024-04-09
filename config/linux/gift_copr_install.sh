#!/usr/bin/env bash
#
# This file is generated by l2tdevtools update-dependencies.py any dependency
# related changes should be made in dependencies.ini.

# Exit on error.
set -e

# Dependencies for running plaso, alphabetized, one per line.
# This should not include packages only required for testing or development.
PYTHON3_DEPENDENCIES="libbde-python3
                      libcaes-python3
                      libcreg-python3
                      libesedb-python3
                      libevt-python3
                      libevtx-python3
                      libewf-python3
                      libfcrypto-python3
                      libfsapfs-python3
                      libfsext-python3
                      libfsfat-python3
                      libfshfs-python3
                      libfsntfs-python3
                      libfsxfs-python3
                      libfvde-python3
                      libfwnt-python3
                      libfwsi-python3
                      liblnk-python3
                      libluksde-python3
                      libmodi-python3
                      libmsiecf-python3
                      libolecf-python3
                      libphdi-python3
                      libqcow-python3
                      libregf-python3
                      libscca-python3
                      libsigscan-python3
                      libsmdev-python3
                      libsmraw-python3
                      libvhdi-python3
                      libvmdk-python3
                      libvsapm-python3
                      libvsgpt-python3
                      libvshadow-python3
                      libvslvm-python3
                      python3-XlsxWriter
                      python3-acstore
                      python3-artifacts
                      python3-bencode
                      python3-certifi
                      python3-cffi
                      python3-chardet
                      python3-dateutil
                      python3-defusedxml
                      python3-dfdatetime
                      python3-dfvfs
                      python3-dfwinreg
                      python3-dtfabric
                      python3-flor
                      python3-idna
                      python3-lz4
                      python3-opensearch
                      python3-pefile
                      python3-psutil
                      python3-pyparsing
                      python3-pytsk3
                      python3-pytz
                      python3-pyyaml
                      python3-redis
                      python3-requests
                      python3-six
                      python3-urllib3
                      python3-xattr
                      python3-yara
                      python3-zmq
                      python3-zstd";

# Additional dependencies for running tests, alphabetized, one per line.
TEST_DEPENDENCIES="python3-fakeredis
                   python3-mock
                   python3-setuptools";

# Additional dependencies for development, alphabetized, one per line.
DEVELOPMENT_DEPENDENCIES="pylint
                          python-sphinx";

# Additional dependencies for debugging, alphabetized, one per line.
DEBUG_DEPENDENCIES="libbde-debuginfo
                    libbde-python3-debuginfo
                    libcaes-debuginfo
                    libcaes-python3-debuginfo
                    libcreg-debuginfo
                    libcreg-python3-debuginfo
                    libesedb-debuginfo
                    libesedb-python3-debuginfo
                    libevt-debuginfo
                    libevt-python3-debuginfo
                    libevtx-debuginfo
                    libevtx-python3-debuginfo
                    libewf-debuginfo
                    libewf-python3-debuginfo
                    libfcrypto-debuginfo
                    libfcrypto-python3-debuginfo
                    libfsapfs-debuginfo
                    libfsapfs-python3-debuginfo
                    libfsext-debuginfo
                    libfsext-python3-debuginfo
                    libfsfat-debuginfo
                    libfsfat-python3-debuginfo
                    libfshfs-debuginfo
                    libfshfs-python3-debuginfo
                    libfsntfs-debuginfo
                    libfsntfs-python3-debuginfo
                    libfsxfs-debuginfo
                    libfsxfs-python3-debuginfo
                    libfvde-debuginfo
                    libfvde-python3-debuginfo
                    libfwnt-debuginfo
                    libfwnt-python3-debuginfo
                    libfwsi-debuginfo
                    libfwsi-python3-debuginfo
                    liblnk-debuginfo
                    liblnk-python3-debuginfo
                    libluksde-debuginfo
                    libluksde-python3-debuginfo
                    libmodi-debuginfo
                    libmodi-python3-debuginfo
                    libmsiecf-debuginfo
                    libmsiecf-python3-debuginfo
                    libolecf-debuginfo
                    libolecf-python3-debuginfo
                    libphdi-debuginfo
                    libphdi-python3-debuginfo
                    libqcow-debuginfo
                    libqcow-python3-debuginfo
                    libregf-debuginfo
                    libregf-python3-debuginfo
                    libscca-debuginfo
                    libscca-python3-debuginfo
                    libsigscan-debuginfo
                    libsigscan-python3-debuginfo
                    libsmdev-debuginfo
                    libsmdev-python3-debuginfo
                    libsmraw-debuginfo
                    libsmraw-python3-debuginfo
                    libvhdi-debuginfo
                    libvhdi-python3-debuginfo
                    libvmdk-debuginfo
                    libvmdk-python3-debuginfo
                    libvsapm-debuginfo
                    libvsapm-python3-debuginfo
                    libvsgpt-debuginfo
                    libvsgpt-python3-debuginfo
                    libvshadow-debuginfo
                    libvshadow-python3-debuginfo
                    libvslvm-debuginfo
                    libvslvm-python3-debuginfo";

sudo dnf install -q dnf-plugins-core
sudo dnf copr -q -y enable @gift/dev
sudo dnf install -q -y ${PYTHON3_DEPENDENCIES}

if [[ "$*" =~ "include-debug" ]]; then
    sudo dnf install -q -y ${DEBUG_DEPENDENCIES}
fi

if [[ "$*" =~ "include-development" ]]; then
    sudo dnf install -q -y ${DEVELOPMENT_DEPENDENCIES}
fi

if [[ "$*" =~ "include-test" ]]; then
    sudo dnf install -q -y ${TEST_DEPENDENCIES}
fi
