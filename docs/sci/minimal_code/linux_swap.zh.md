# swap linux

##  swap是什么

swap是linux系统中的一种内存管理机制，当物理内存不足时，系统会将一些不常用的内存页移动到磁盘上的swap分区或swap文件中，以释放物理内存供其他程序使用。

##  swap 分区和 swap 文件

swap分区是专门为swap使用的磁盘分区，而swap文件则是在现有文件系统上创建的一个普通文件，用于存储swap数据。两者的功能相同，但swap分区通常性能更好，因为它不受文件系统的限制。

## swap的使用

当系统需要使用swap时，会将一些不常用的内存页移动到swap分区或swap文件中，以释放物理内存供其他程序使用。swap的使用可以通过命令`swapon`和`swapoff`来启用或禁用swap。

## 当有swap分区时候 新建swap文件

如果系统已经有swap分区，但需要额外的swap空间，可以通过以下脚本
 

 适用于debian系统
```bash
#!/usr/bin/env bash
set -euo pipefail

TARGET_GB="${1:-16}"
SWAPFILE="${SWAPFILE:-/swapfile}"
SWAPPINESS="${SWAPPINESS:-20}"

if [[ "${EUID}" -ne 0 ]]; then
  echo "Please run with sudo: sudo bash $0 [swap_size_gb]"
  exit 1
fi

if ! [[ "${TARGET_GB}" =~ ^[0-9]+$ ]] || (( TARGET_GB < 1 )); then
  echo "Invalid swap size: ${TARGET_GB}. Use a positive integer in GB."
  exit 1
fi

if ! [[ "${SWAPPINESS}" =~ ^[0-9]+$ ]] || (( SWAPPINESS < 0 || SWAPPINESS > 100 )); then
  echo "Invalid SWAPPINESS=${SWAPPINESS}. Must be 0..100."
  exit 1
fi

TARGET_BYTES=$(( TARGET_GB * 1024 * 1024 * 1024 ))
NEED_KB=$(( TARGET_GB * 1024 * 1024 + 1024 * 1024 )) # swap size + 1GiB margin
AVAIL_KB="$(df --output=avail / | awk 'NR==2{print $1}')"

if (( AVAIL_KB < NEED_KB )); then
  echo "Not enough free space on /"
  echo "Available: $(( AVAIL_KB / 1024 / 1024 )) GiB, Required: $(( NEED_KB / 1024 / 1024 )) GiB"
  exit 1
fi

is_active_swapfile() {
  swapon --noheadings --raw --output=NAME 2>/dev/null | awk '{print $1}' | grep -Fxq "${SWAPFILE}"
}

need_create=0
if [[ -e "${SWAPFILE}" ]]; then
  CUR_BYTES="$(stat -c%s "${SWAPFILE}")"
  if (( CUR_BYTES != TARGET_BYTES )); then
    if is_active_swapfile; then
      swapoff "${SWAPFILE}"
    fi
    rm -f "${SWAPFILE}"
    need_create=1
  fi
else
  need_create=1
fi

if (( need_create == 1 )); then
  if ! fallocate -l "${TARGET_GB}G" "${SWAPFILE}" 2>/dev/null; then
    dd if=/dev/zero of="${SWAPFILE}" bs=1M count=$(( TARGET_GB * 1024 )) status=progress
  fi
  chmod 600 "${SWAPFILE}"
  mkswap -f "${SWAPFILE}" >/dev/null
fi

if ! is_active_swapfile; then
  swapon "${SWAPFILE}"
fi

FSTAB_LINE="${SWAPFILE} none swap sw,pri=10 0 0"
if grep -Eq "^[[:space:]]*${SWAPFILE//\//\\/}[[:space:]]+none[[:space:]]+swap" /etc/fstab; then
  sed -i -E "s|^[[:space:]]*${SWAPFILE//\//\\/}[[:space:]]+none[[:space:]]+swap.*$|${FSTAB_LINE}|g" /etc/fstab
else
  printf "\n%s\n" "${FSTAB_LINE}" >> /etc/fstab
fi

SYSCTL_FILE="/etc/sysctl.d/99-swappiness.conf"
printf "vm.swappiness=%s\n" "${SWAPPINESS}" > "${SYSCTL_FILE}"
if ! sysctl --system >/dev/null 2>&1; then
  sysctl -w "vm.swappiness=${SWAPPINESS}" >/dev/null
fi

echo
echo "Done. Current swap status:"
swapon --show
echo
free -h
echo
echo "Applied vm.swappiness=${SWAPPINESS}"

```


如果用户想用“休眠到磁盘”，swapfile 还涉及：

resume= 内核参数

swapfile 的物理偏移（不同发行版处理不一样）.


休眠（hibernate）对 swapfile 有额外配置要求，本笔记不覆盖，建议使用 swap 分区或查发行版文档。