[     UTC     ] Logs for quoteforge.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[15:39:23] 🚀 Starting up repository: 'quoteforge', branch: 'main', main module: 'app.py'

[15:39:23] 🐙 Cloning repository...

[15:39:23] 🐙 Cloning into '/mount/src/quoteforge'...

[15:39:23] 🐙 Cloned repository!

[15:39:23] 🐙 Pulling code changes from Github...

[15:39:23] 📦 Processing dependencies...

[15:39:23] 📦 Apt dependencies were installed from /mount/src/quoteforge/packages.txt using apt-get.

Hit:1 http://deb.debian.org/debian bookworm InRelease

Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]

Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]

Get:4 https://packages.microsoft.com/debian/11/prod bullseye InRelease [3650 B]

Get:5 http://deb.debian.org/debian-security bookworm-security/main amd64 Packages [290 kB]

Fetched 397 kB in 0s (971 kB/s)

Reading package lists...[2026-01-06 15:39:25.307248] 

Reading package lists...[2026-01-06 15:39:26.116839] 

Building dependency tree...[2026-01-06 15:39:26.372533] 

Reading state information...[2026-01-06 15:39:26.372913] 

libglib2.0-0 is already the newest version (2.74.6-2+deb12u7).

libglib2.0-0 set to manually installed.

libxext6 is already the newest version (2:1.3.4-1+b1).

libxext6 set to manually installed.

The following additional packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm-nouveau2 libdrm-radeon1

  libdrm2 libglapi-mesa libglvnd0 libglx-mesa0 libglx0 libllvm15 libpciaccess0

  libsensors-config libsensors5 libx11-xcb1 libxcb-dri2-0 libxcb-dri3-0

  libxcb-glx0 libxcb-present0 libxcb-randr0 libxcb-shm0 libxcb-sync1

  libxcb-xfixes0 libxfixes3 libxshmfence1 libxxf86vm1 libz3-4

Suggested packages:

  pciutils lm-sensors

The following NEW packages will be installed:

  libdrm-amdgpu1 libdrm-common libdrm-intel1 libdrm-nouveau2 libdrm-radeon1

  libdrm2 libgl1 libgl1-mesa-dri libgl1-mesa-glx libglapi-mesa libglvnd0

  libglx-mesa0 libglx0 libllvm15 libpciaccess0 libsensors-config libsensors5

  libx11-xcb1 libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-present0

  libxcb-randr0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxfixes3 libxrender1

  libxshmfence1 libxxf86vm1 libz3-4

0 upgraded, 31 newly installed, 0 to remove and 0 not upgraded.

Need to get 39.4 MB of archives.

After this operation, 172 MB of additional disk space will be used.

Get:1 http://deb.debian.org/debian bookworm/main amd64 libdrm-common all 2.4.114-1 [7112 B]

Get:2 http://deb.debian.org/debian bookworm/main amd64 libdrm2 amd64 2.4.114-1+b1 [37.5 kB]

Get:3 http://deb.debian.org/debian bookworm/main amd64 libdrm-amdgpu1 amd64 2.4.114-1+b1 [20.9 kB]

Get:4 http://deb.debian.org/debian bookworm/main amd64 libpciaccess0 amd64 0.17-2 [51.4 kB]

Get:5 http://deb.debian.org/debian bookworm/main amd64 libdrm-intel1 amd64 2.4.114-1+b1 [64.0 kB]

Get:6 http://deb.debian.org/debian bookworm/main amd64 libdrm-nouveau2 amd64 2.4.114-1+b1 [19.1 kB]

Get:7 http://deb.debian.org/debian bookworm/main amd64 libdrm-radeon1 amd64 2.4.114-1+b1 [21.8 kB]

Get:8 http://deb.debian.org/debian bookworm/main amd64 libglvnd0 amd64 1.6.0-1 [51.8 kB]

Get:9 http://deb.debian.org/debian bookworm/main amd64 libglapi-mesa amd64 22.3.6-1+deb12u1 [35.7 kB]

Get:10 http://deb.debian.org/debian bookworm/main amd64 libx11-xcb1 amd64 2:1.8.4-2+deb12u2 [192 kB]

Get:11 http://deb.debian.org/debian bookworm/main amd64 libxcb-dri2-0 amd64 1.15-1 [107 kB]

Get:12 http://deb.debian.org/debian bookworm/main amd64 libxcb-dri3-0 amd64 1.15-1 [107 kB]

Get:13 http://deb.debian.org/debian bookworm/main amd64 libxcb-glx0 amd64 1.15-1 [122 kB]

Get:14 http://deb.debian.org/debian bookworm/main amd64 libxcb-present0 amd64 1.15-1 [105 kB]

Get:15 http://deb.debian.org/debian bookworm/main amd64 libxcb-randr0 amd64 1.15-1 [117 kB]

Get:16 http://deb.debian.org/debian bookworm/main amd64 libxcb-shm0 amd64 1.15-1 [105 kB]

Get:17 http://deb.debian.org/debian bookworm/main amd64 libxcb-sync1 amd64 1.15-1 [109 kB]

Get:18 http://deb.debian.org/debian bookworm/main amd64 libxcb-xfixes0 amd64 1.15-1 [109 kB]

Get:19 http://deb.debian.org/debian bookworm/main amd64 libxfixes3 amd64 1:6.0.0-2 [22.7 kB]

Get:20 http://deb.debian.org/debian bookworm/main amd64 libxshmfence1 amd64 1.3-1 [8820 B]

Get:21 http://deb.debian.org/debian bookworm/main amd64 libxxf86vm1 amd64 1:1.1.4-1+b2 [20.8 kB]

Get:22 http://deb.debian.org/debian bookworm/main amd64 libz3-4 amd64 4.8.12-3.1 [7216 kB]

Get:23 http://deb.debian.org/debian bookworm/main amd64 libllvm15 amd64 1:15.0.6-4+b1 [23.1 MB]

Get:24 http://deb.debian.org/debian bookworm/main amd64 libsensors-config all 1:3.6.0-7.1 [14.3 kB]

Get:25 http://deb.debian.org/debian bookworm/main amd64 libsensors5 amd64 1:3.6.0-7.1 [34.2 kB]

Get:26 http://deb.debian.org/debian bookworm/main amd64 libgl1-mesa-dri amd64 22.3.6-1+deb12u1 [7239 kB]

Get:27 http://deb.debian.org/debian bookworm/main amd64 libglx-mesa0 amd64 22.3.6-1+deb12u1 [147 kB]

Get:28 http://deb.debian.org/debian bookworm/main amd64 libglx0 amd64 1.6.0-1 [34.4 kB]

Get:29 http://deb.debian.org/debian bookworm/main amd64 libgl1 amd64 1.6.0-1 [88.4 kB]

Get:30 http://deb.debian.org/debian bookworm/main amd64 libgl1-mesa-glx amd64 22.3.6-1+deb12u1 [14.5 kB]

Get:31 http://deb.debian.org/debian bookworm/main amd64 libxrender1 amd64 1:0.9.10-1.1 [33.2 kB]

debconf: delaying package configuration, since apt-utils is not installed

Fetched 39.4 MB in 0s (116 MB/s)

Selecting previously unselected package libdrm-common.

(Reading database ... 23146 files and directories currently installed.)

Preparing to unpack .../00-libdrm-common_2.4.114-1_all.deb ...

Unpacking libdrm-common (2.4.114-1) ...

Selecting previously unselected package libdrm2:amd64.

Preparing to unpack .../01-libdrm2_2.4.114-1+b1_amd64.deb ...

Unpacking libdrm2:amd64 (2.4.114-1+b1) ...

Selecting previously unselected package libdrm-amdgpu1:amd64.

Preparing to unpack .../02-libdrm-amdgpu1_2.4.114-1+b1_amd64.deb ...

Unpacking libdrm-amdgpu1:amd64 (2.4.114-1+b1) ...

Selecting previously unselected package libpciaccess0:amd64.

Preparing to unpack .../03-libpciaccess0_0.17-2_amd64.deb ...

Unpacking libpciaccess0:amd64 (0.17-2) ...

Selecting previously unselected package libdrm-intel1:amd64.

Preparing to unpack .../04-libdrm-intel1_2.4.114-1+b1_amd64.deb ...

Unpacking libdrm-intel1:amd64 (2.4.114-1+b1) ...

Selecting previously unselected package libdrm-nouveau2:amd64.

Preparing to unpack .../05-libdrm-nouveau2_2.4.114-1+b1_amd64.deb ...

Unpacking libdrm-nouveau2:amd64 (2.4.114-1+b1) ...

Selecting previously unselected package libdrm-radeon1:amd64.

Preparing to unpack .../06-libdrm-radeon1_2.4.114-1+b1_amd64.deb ...

Unpacking libdrm-radeon1:amd64 (2.4.114-1+b1) ...

Selecting previously unselected package libglvnd0:amd64.

Preparing to unpack .../07-libglvnd0_1.6.0-1_amd64.deb ...

Unpacking libglvnd0:amd64 (1.6.0-1) ...

Selecting previously unselected package libglapi-mesa:amd64.

Preparing to unpack .../08-libglapi-mesa_22.3.6-1+deb12u1_amd64.deb ...

Unpacking libglapi-mesa:amd64 (22.3.6-1+deb12u1) ...

Selecting previously unselected package libx11-xcb1:amd64.

Preparing to unpack .../09-libx11-xcb1_2%3a1.8.4-2+deb12u2_amd64.deb ...

Unpacking libx11-xcb1:amd64 (2:1.8.4-2+deb12u2) ...

Selecting previously unselected package libxcb-dri2-0:amd64.

Preparing to unpack .../10-libxcb-dri2-0_1.15-1_amd64.deb ...

Unpacking libxcb-dri2-0:amd64 (1.15-1) ...

Selecting previously unselected package libxcb-dri3-0:amd64.

Preparing to unpack .../11-libxcb-dri3-0_1.15-1_amd64.deb ...

Unpacking libxcb-dri3-0:amd64 (1.15-1) ...

Selecting previously unselected package libxcb-glx0:amd64.

Preparing to unpack .../12-libxcb-glx0_1.15-1_amd64.deb ...

Unpacking libxcb-glx0:amd64 (1.15-1) ...

Selecting previously unselected package libxcb-present0:amd64.

Preparing to unpack .../13-libxcb-present0_1.15-1_amd64.deb ...

Unpacking libxcb-present0:amd64 (1.15-1) ...

Selecting previously unselected package libxcb-randr0:amd64.

Preparing to unpack .../14-libxcb-randr0_1.15-1_amd64.deb ...

Unpacking libxcb-randr0:amd64 (1.15-1) ...

Selecting previously unselected package libxcb-shm0:amd64.

Preparing to unpack .../15-libxcb-shm0_1.15-1_amd64.deb ...

Unpacking libxcb-shm0:amd64 (1.15-1) ...

Selecting previously unselected package libxcb-sync1:amd64.

Preparing to unpack .../16-libxcb-sync1_1.15-1_amd64.deb ...

Unpacking libxcb-sync1:amd64 (1.15-1) ...

Selecting previously unselected package libxcb-xfixes0:amd64.

Preparing to unpack .../17-libxcb-xfixes0_1.15-1_amd64.deb ...

Unpacking libxcb-xfixes0:amd64 (1.15-1) ...

Selecting previously unselected package libxfixes3:amd64.

Preparing to unpack .../18-libxfixes3_1%3a6.0.0-2_amd64.deb ...

Unpacking libxfixes3:amd64 (1:6.0.0-2) ...

Selecting previously unselected package libxshmfence1:amd64.

Preparing to unpack .../19-libxshmfence1_1.3-1_amd64.deb ...

Unpacking libxshmfence1:amd64 (1.3-1) ...

Selecting previously unselected package libxxf86vm1:amd64.

Preparing to unpack .../20-libxxf86vm1_1%3a1.1.4-1+b2_amd64.deb ...

Unpacking libxxf86vm1:amd64 (1:1.1.4-1+b2) ...

Selecting previously unselected package libz3-4:amd64.

Preparing to unpack .../21-libz3-4_4.8.12-3.1_amd64.deb ...

Unpacking libz3-4:amd64 (4.8.12-3.1) ...

Selecting previously unselected package libllvm15:amd64.

Preparing to unpack .../22-libllvm15_1%3a15.0.6-4+b1_amd64.deb ...

Unpacking libllvm15:amd64 (1:15.0.6-4+b1) ...

Selecting previously unselected package libsensors-config.

Preparing to unpack .../23-libsensors-config_1%3a3.6.0-7.1_all.deb ...

Unpacking libsensors-config (1:3.6.0-7.1) ...

Selecting previously unselected package libsensors5:amd64.

Preparing to unpack .../24-libsensors5_1%3a3.6.0-7.1_amd64.deb ...

Unpacking libsensors5:amd64 (1:3.6.0-7.1) ...

Selecting previously unselected package libgl1-mesa-dri:amd64.

Preparing to unpack .../25-libgl1-mesa-dri_22.3.6-1+deb12u1_amd64.deb ...

Unpacking libgl1-mesa-dri:amd64 (22.3.6-1+deb12u1) ...

Selecting previously unselected package libglx-mesa0:amd64.

Preparing to unpack .../26-libglx-mesa0_22.3.6-1+deb12u1_amd64.deb ...

Unpacking libglx-mesa0:amd64 (22.3.6-1+deb12u1) ...

Selecting previously unselected package libglx0:amd64.

Preparing to unpack .../27-libglx0_1.6.0-1_amd64.deb ...

Unpacking libglx0:amd64 (1.6.0-1) ...

Selecting previously unselected package libgl1:amd64.

Preparing to unpack .../28-libgl1_1.6.0-1_amd64.deb ...

Unpacking libgl1:amd64 (1.6.0-1) ...

Selecting previously unselected package libgl1-mesa-glx:amd64.

Preparing to unpack .../29-libgl1-mesa-glx_22.3.6-1+deb12u1_amd64.deb ...

Unpacking libgl1-mesa-glx:amd64 (22.3.6-1+deb12u1) ...

Selecting previously unselected package libxrender1:amd64.

Preparing to unpack .../30-libxrender1_1%3a0.9.10-1.1_amd64.deb ...

Unpacking libxrender1:amd64 (1:0.9.10-1.1) ...

Setting up libxcb-dri3-0:amd64 (1.15-1) ...

Setting up libx11-xcb1:amd64 (2:1.8.4-2+deb12u2) ...

Setting up libpciaccess0:amd64 (0.17-2) ...

Setting up libxcb-xfixes0:amd64 (1.15-1) ...

Setting up libxrender1:amd64 (1:0.9.10-1.1) ...

Setting up libglvnd0:amd64 (1.6.0-1) ...

Setting up libxcb-glx0:amd64 (1.15-1) ...

Setting up libsensors-config (1:3.6.0-7.1) ...

Setting up libxcb-shm0:amd64 (1.15-1) ...

Setting up libxxf86vm1:amd64 (1:1.1.4-1+b2) ...

Setting up libxcb-present0:amd64 (1.15-1) ...

Setting up libz3-4:amd64 (4.8.12-3.1) ...

Setting up libxfixes3:amd64 (1:6.0.0-2) ...

Setting up libxcb-sync1:amd64 (1.15-1) ...

Setting up libsensors5:amd64 (1:3.6.0-7.1) ...

Setting up libglapi-mesa:amd64 (22.3.6-1+deb12u1) ...

Setting up libxcb-dri2-0:amd64 (1.15-1) ...

Setting up libxshmfence1:amd64 (1.3-1) ...

Setting up libxcb-randr0:amd64 (1.15-1) ...

Setting up libllvm15:amd64 (1:15.0.6-4+b1) ...

Setting up libdrm-common (2.4.114-1) ...

Setting up libdrm2:amd64 (2.4.114-1+b1) ...

Setting up libdrm-amdgpu1:amd64 (2.4.114-1+b1) ...

Setting up libdrm-nouveau2:amd64 (2.4.114-1+b1) ...

Setting up libdrm-radeon1:amd64 (2.4.114-1+b1) ...

Setting up libdrm-intel1:amd64 (2.4.114-1+b1) ...

Setting up libgl1-mesa-dri:amd64 (22.3.6-1+deb12u1) ...

Setting up libglx-mesa0:amd64 (22.3.6-1+deb12u1) ...

Setting up libglx0:amd64 (1.6.0-1) ...

Setting up libgl1:amd64 (1.6.0-1) ...

Setting up libgl1-mesa-glx:amd64 (22.3.6-1+deb12u1) ...

Processing triggers for libc-bin (2.36-9+deb12u13) ...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.11.14 environment at /home/adminuser/venv

Resolved 96 packages in 990ms

  × Failed to download and build `pycairo==1.29.0`

  ╰─▶ Build backend failed to build wheel through `build_wheel` (exit status:

      1)


      [stdout]

      + meson setup

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-3ynk06gu

      -Dbuildtype=release -Db_ndebug=if-release

      -Db_vscrt=md -Dwheel=true -Dtests=false

      --native-file=/home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-3ynk06gu/meson-python-native-file.ini

      The Meson build system

      Version: 1.10.0

      Source dir:

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src

      Build dir:

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-3ynk06gu

      Build type: native build

      Project name: pycairo

      Project version: 1.29.0

      C compiler for the host machine: cc (gcc 12.2.0 "cc (Debian

      12.2.0-14+deb12u1) 12.2.0")

      C linker for the host machine: cc ld.bfd 2.40

      Host machine cpu family: x86_64

      Host machine cpu: x86_64

      Program python3 found: YES

      (/home/adminuser/.cache/uv/builds-v0/.tmpTjzSdS/bin/python)

      Compiler for C supports arguments -Wall: YES

      Compiler for C supports arguments -Warray-bounds: YES

      Compiler for C supports arguments -Wcast-align: YES

      Compiler for C supports arguments -Wconversion: YES

      Compiler for C supports arguments -Wextra: YES

      Compiler for C supports arguments -Wformat=2: YES

      Compiler for C supports arguments -Wformat-nonliteral: YES

      Compiler for C supports arguments -Wformat-security: YES

      Compiler for C supports arguments -Wimplicit-function-declaration: YES

      Compiler for C supports arguments -Winit-self: YES

      Compiler for C supports arguments -Wmissing-format-attribute: YES

      Compiler for C supports arguments -Wmissing-noreturn: YES

      Compiler for C supports arguments -Wnested-externs: YES

      Compiler for C supports arguments -Wold-style-definition: YES

      Compiler for C supports arguments -Wpacked: YES

      Compiler for C supports arguments -Wpointer-arith: YES

      Compiler for C supports arguments -Wreturn-type: YES

      Compiler for C supports arguments -Wshadow: YES

      Compiler for C supports arguments -Wsign-compare: YES

      Compiler for C supports arguments -Wstrict-aliasing: YES

      Compiler for C supports arguments -Wundef: YES

      Compiler for C supports arguments -Wunused-but-set-variable: YES

      Compiler for C supports arguments -Wswitch-default: YES

      Compiler for C supports arguments -Wno-missing-field-initializers: YES

      Compiler for C supports arguments -Wno-unused-parameter: YES

      Compiler for C supports arguments -fno-strict-aliasing: YES

      Compiler for C supports arguments -fvisibility=hidden: YES

      Did not find pkg-config by name 'pkg-config'

      Found pkg-config: NO

      Did not find CMake 'cmake'

      Found CMake: NO

      Run-time dependency cairo found: NO


      ../cairo/meson.build:31:12: ERROR: Dependency lookup for cairo with

      method 'pkgconfig' failed: Pkg-config for machine host machine not

      found. Giving up.


      A full log can be found at

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-3ynk06gu/meson-logs/meson-log.txt


  help: `pycairo` was included because `svglib==1.6.0` depends on

        `rlpycairo==0.4.0` which depends on `pycairo`

Checking if Streamlit is installed

Installing rich for an improved exception logging

Using uv pip install.

Using Python 3.11.14 environment at /home/adminuser/venv

Resolved 4 packages in 117ms

Prepared 2 packages in 98ms

Installed 4 packages in 14ms

 + [2026-01-06 15:39:39.560604] markdown-it-py==4.0.0

 + mdurl==0.1.2

 + pygments==2.19.2

 + rich==14.2.0


────────────────────────────────────────────────────────────────────────────────────────



──────────────────────────────────────── pip ───────────────────────────────────────────


Using standard pip install.

Collecting streamlit (from -r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading streamlit-1.52.2-py3-none-any.whl.metadata (9.8 kB)

Collecting cadquery (from -r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading cadquery-2.6.1-py3-none-any.whl.metadata (17 kB)

Collecting pandas (from -r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading pandas-2.3.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (91 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.2/91.2 kB 7.9 MB/s eta 0:00:00[2026-01-06 15:39:41.682909] 

Collecting numpy (from -r /mount/src/quoteforge/requirements.txt (line 4))

  Downloading numpy-2.4.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)

Collecting stpyvista (from -r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading stpyvista-0.1.4-py3-none-any.whl.metadata (1.7 kB)

Collecting trimesh (from -r /mount/src/quoteforge/requirements.txt (line 6))

  Downloading trimesh-4.10.1-py3-none-any.whl.metadata (13 kB)

Collecting matplotlib (from -r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading matplotlib-3.10.8-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (52 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.8/52.8 kB 120.1 MB/s eta 0:00:00[2026-01-06 15:39:42.442555] 

Collecting reportlab (from -r /mount/src/quoteforge/requirements.txt (line 8))

  Downloading reportlab-4.4.7-py3-none-any.whl.metadata (1.7 kB)

Collecting lxml (from -r /mount/src/quoteforge/requirements.txt (line 9))

  Downloading lxml-6.0.2-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.6 kB)

Collecting tinycss2 (from -r /mount/src/quoteforge/requirements.txt (line 10))

  Downloading tinycss2-1.5.1-py3-none-any.whl.metadata (3.0 kB)

Collecting cssselect2 (from -r /mount/src/quoteforge/requirements.txt (line 11))

  Downloading cssselect2-0.8.0-py3-none-any.whl.metadata (2.9 kB)

Collecting svglib (from -r /mount/src/quoteforge/requirements.txt (line 12))

  Downloading svglib-1.6.0-py3-none-any.whl.metadata (11 kB)

Collecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading altair-6.0.0-py3-none-any.whl.metadata (11 kB)

Collecting blinker<2,>=1.5.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)

Collecting cachetools<7,>=4.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading cachetools-6.2.4-py3-none-any.whl.metadata (5.6 kB)

Collecting click<9,>=7.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)

Collecting packaging>=20 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)

Collecting pillow<13,>=7.1.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading pillow-12.1.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)

Collecting protobuf<7,>=3.20 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading protobuf-6.33.2-cp39-abi3-manylinux2014_x86_64.whl.metadata (593 bytes)

Collecting pyarrow>=7.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading pyarrow-22.0.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.2 kB)

Collecting requests<3,>=2.27 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)

Collecting tenacity<10,>=8.1.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)

Collecting toml<2,>=0.10.1 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)

Collecting typing-extensions<5,>=4.4.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)

Collecting watchdog<7,>=2.1.5 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.3/44.3 kB 119.6 MB/s eta 0:00:00[2026-01-06 15:39:44.324465] 

Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)

Collecting pydeck<1,>=0.8.0b4 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)

Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading tornado-6.5.4-cp39-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.8 kB)

Collecting cadquery-ocp<7.9,>=7.8.1 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading cadquery_ocp-7.8.1.1.post1-cp311-cp311-manylinux_2_31_x86_64.whl.metadata (707 bytes)

Collecting ezdxf>=1.3.0 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading ezdxf-1.4.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.9 kB)

Collecting multimethod<2.0,>=1.11 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading multimethod-1.12-py3-none-any.whl.metadata (9.6 kB)

Collecting nlopt<3.0,>=2.9.0 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading nlopt-2.10.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.1 kB)

Collecting typish (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading typish-1.9.3-py3-none-any.whl.metadata (7.2 kB)

Collecting casadi (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading casadi-3.7.2-cp311-none-manylinux2014_x86_64.whl.metadata (2.2 kB)

Collecting path (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading path-17.1.1-py3-none-any.whl.metadata (6.5 kB)

Collecting trame (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading trame-3.12.0-py3-none-any.whl.metadata (8.2 kB)

Collecting trame-vtk (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading trame_vtk-2.10.1-py3-none-any.whl.metadata (13 kB)

Collecting python-dateutil>=2.8.2 (from pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)

Collecting pytz>=2020.1 (from pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)

Collecting tzdata>=2022.7 (from pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)

Collecting bokeh (from stpyvista->-r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading bokeh-3.8.2-py3-none-any.whl.metadata (10 kB)

Collecting panel (from stpyvista->-r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading panel-1.8.5-py3-none-any.whl.metadata (15 kB)

Collecting pyvista (from stpyvista->-r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading pyvista-0.46.4-py3-none-any.whl.metadata (15 kB)

Collecting contourpy>=1.0.1 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading contourpy-1.3.3-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.5 kB)

Collecting cycler>=0.10 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)

Collecting fonttools>=4.22.0 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading fonttools-4.61.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (114 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.2/114.2 kB 53.9 MB/s eta 0:00:00[2026-01-06 15:39:46.400801] 

Collecting kiwisolver>=1.3.1 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading kiwisolver-1.4.9-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (6.3 kB)

Collecting pyparsing>=3 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading pyparsing-3.3.1-py3-none-any.whl.metadata (5.6 kB)

Collecting charset-normalizer (from reportlab->-r /mount/src/quoteforge/requirements.txt (line 8))

  Downloading charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)

Collecting webencodings>=0.4 (from tinycss2->-r /mount/src/quoteforge/requirements.txt (line 10))

  Downloading webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)

Collecting rlpycairo>=0.4.0 (from svglib->-r /mount/src/quoteforge/requirements.txt (line 12))

  Downloading rlpycairo-0.4.0-py3-none-any.whl.metadata (4.9 kB)

Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)

Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading jsonschema-4.25.1-py3-none-any.whl.metadata (7.6 kB)

Collecting narwhals>=1.27.1 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading narwhals-2.15.0-py3-none-any.whl.metadata (13 kB)

Collecting vtk==9.3.1 (from cadquery-ocp<7.9,>=7.8.1->cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading vtk-9.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)

Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)

Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)

Collecting idna<4,>=2.5 (from requests<3,>=2.27->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)

Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.27->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)

Collecting certifi>=2017.4.17 (from requests<3,>=2.27->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)

Collecting pycairo>=1.20.0 (from rlpycairo>=0.4.0->svglib->-r /mount/src/quoteforge/requirements.txt (line 12))

  Downloading pycairo-1.29.0.tar.gz (665 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 665.9/665.9 kB 62.1 MB/s eta 0:00:00[2026-01-06 15:39:47.705269] 

  Installing build dependencies: started

  Installing build dependencies: finished with status 'done'

  Getting requirements to build wheel: started

  Getting requirements to build wheel: finished with status 'done'

  Installing backend dependencies: started

  Installing backend dependencies: finished with status 'done'

  Preparing metadata (pyproject.toml): started

  Preparing metadata (pyproject.toml): finished with status 'error'

  error: subprocess-exited-with-error

  

  × Preparing metadata (pyproject.toml) did not run successfully.

  │ exit code: 1

  ╰─> [49 lines of output]

      + meson setup /tmp/pip-install-w_2draq1/pycairo_406136f717dc44aa84d86803590ac620 /tmp/pip-install-w_2draq1/pycairo_406136f717dc44aa84d86803590ac620/.mesonpy-0rmkj30o -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md -Dwheel=true -Dtests=false --native-file=/tmp/pip-install-w_2draq1/pycairo_406136f717dc44aa84d86803590ac620/.mesonpy-0rmkj30o/meson-python-native-file.ini

      The Meson build system

      Version: 1.10.0

      Source dir: /tmp/pip-install-w_2draq1/pycairo_406136f717dc44aa84d86803590ac620

      Build dir: /tmp/pip-install-w_2draq1/pycairo_406136f717dc44aa84d86803590ac620/.mesonpy-0rmkj30o

      Build type: native build

      Project name: pycairo

      Project version: 1.29.0

      C compiler for the host machine: cc (gcc 12.2.0 "cc (Debian 12.2.0-14+deb12u1) 12.2.0")

      C linker for the host machine: cc ld.bfd 2.40

      Host machine cpu family: x86_64

      Host machine cpu: x86_64

      Program python3 found: YES (/home/adminuser/venv/bin/python)

      Compiler for C supports arguments -Wall: YES

      Compiler for C supports arguments -Warray-bounds: YES

      Compiler for C supports arguments -Wcast-align: YES

      Compiler for C supports arguments -Wconversion: YES

      Compiler for C supports arguments -Wextra: YES

      Compiler for C supports arguments -Wformat=2: YES

      Compiler for C supports arguments -Wformat-nonliteral: YES

      Compiler for C supports arguments -Wformat-security: YES

      Compiler for C supports arguments -Wimplicit-function-declaration: YES

      Compiler for C supports arguments -Winit-self: YES

      Compiler for C supports arguments -Wmissing-format-attribute: YES

      Compiler for C supports arguments -Wmissing-noreturn: YES

      Compiler for C supports arguments -Wnested-externs: YES

      Compiler for C supports arguments -Wold-style-definition: YES

      Compiler for C supports arguments -Wpacked: YES

      Compiler for C supports arguments -Wpointer-arith: YES

      Compiler for C supports arguments -Wreturn-type: YES

      Compiler for C supports arguments -Wshadow: YES

      Compiler for C supports arguments -Wsign-compare: YES

      Compiler for C supports arguments -Wstrict-aliasing: YES

      Compiler for C supports arguments -Wundef: YES

      Compiler for C supports arguments -Wunused-but-set-variable: YES

      Compiler for C supports arguments -Wswitch-default: YES

      Compiler for C supports arguments -Wno-missing-field-initializers: YES

      Compiler for C supports arguments -Wno-unused-parameter: YES

      Compiler for C supports arguments -fno-strict-aliasing: YES

      Compiler for C supports arguments -fvisibility=hidden: YES

      Did not find pkg-config by name 'pkg-config'

      Found pkg-config: NO

      Did not find CMake 'cmake'

      Found CMake: NO

      Run-time dependency cairo found: NO

      

      ../cairo/meson.build:31:12: ERROR: Dependency lookup for cairo with method 'pkgconfig' failed: Pkg-config for machine host machine not found. Giving up.

      

      A full log can be found at /tmp/pip-install-w_2draq1/pycairo_406136f717dc44aa84d86803590ac620/.mesonpy-0rmkj30o/meson-logs/meson-log.txt

      [end of output]

  

  note: This error originates from a subprocess, and is likely not a problem with pip.

error: metadata-generation-failed


× Encountered error while generating package metadata.

╰─> See above for output.


note: This is an issue with the package mentioned above, not pip.

hint: See above for details.


[notice] A new release of pip is available: 24.0 -> 25.3

[notice] To update, run: pip install --upgrade pip

Checking if Streamlit is installed

Installing rich for an improved exception logging

Using standard pip install.

Collecting rich>=10.14.0

  Downloading rich-14.2.0-py3-none-any.whl.metadata (18 kB)

Collecting markdown-it-py>=2.2.0 (from rich>=10.14.0)

  Downloading markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)

Collecting pygments<3.0.0,>=2.13.0 (from rich>=10.14.0)

  Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)

Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.14.0)

  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)

Downloading rich-14.2.0-py3-none-any.whl (243 kB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 243.4/243.4 kB 12.4 MB/s eta 0:00:00[2026-01-06 15:39:54.606043] 

Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.3/87.3 kB 127.2 MB/s eta 0:00:00[2026-01-06 15:39:54.620244] 

Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 72.0 MB/s eta 0:00:00[2026-01-06 15:39:54.652191] 

Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)

Installing collected packages: pygments, mdurl, markdown-it-py, rich

  Attempting uninstall: pygments

    Found existing installation: Pygments 2.19.2

    Uninstalling Pygments-2.19.2:

      Successfully uninstalled Pygments-2.19.2

  Attempting uninstall: mdurl

    Found existing installation: mdurl 0.1.2

    Uninstalling mdurl-0.1.2:

      Successfully uninstalled mdurl-0.1.2

  Attempting uninstall: markdown-it-py

    Found existing installation: markdown-it-py 4.0.0

    Uninstalling markdown-it-py-4.0.0:

      Successfully uninstalled markdown-it-py-4.0.0

  Attempting uninstall: rich

    Found existing installation: rich 14.2.0

    Uninstalling rich-14.2.0:

      Successfully uninstalled rich-14.2.0

Successfully installed markdown-it-py-4.0.0 mdurl-0.1.2 pygments-2.19.2 rich-14.2.0


[notice] A new release of pip is available: 24.0 -> 25.3

[notice] To update, run: pip install --upgrade pip


────────────────────────────────────────────────────────────────────────────────────────


[15:39:56] ❗️ installer returned a non-zero exit code

[15:39:56] ❗️ Error during processing dependencies! Please fix the error and push an update, or try restarting the app.

[15:39:56] 🐙 Pulling code changes from Github...

[15:39:57] 📦 Processing dependencies...

[15:39:57] 📦 Apt dependencies were installed from /mount/src/quoteforge/packages.txt using apt-get.


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.11.14 environment at /home/adminuser/venv

Resolved 96 packages in 289ms

  × Failed to download and build `pycairo==1.29.0`

  ╰─▶ Build backend failed to build wheel through `build_wheel` (exit status:

      1)


      [stdout]

      + meson setup

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-nziufu2s

      -Dbuildtype=release -Db_ndebug=if-release

      -Db_vscrt=md -Dwheel=true -Dtests=false

      --native-file=/home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-nziufu2s/meson-python-native-file.ini

      The Meson build system

      Version: 1.10.0

      Source dir:

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src

      Build dir:

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-nziufu2s

      Build type: native build

      Project name: pycairo

      Project version: 1.29.0

      C compiler for the host machine: cc (gcc 12.2.0 "cc (Debian

      12.2.0-14+deb12u1) 12.2.0")

      C linker for the host machine: cc ld.bfd 2.40

      Host machine cpu family: x86_64

      Host machine cpu: x86_64

      Program python3 found: YES

      (/home/adminuser/.cache/uv/builds-v0/.tmp063NYw/bin/python)

      Compiler for C supports arguments -Wall: YES

      Compiler for C supports arguments -Warray-bounds: YES

      Compiler for C supports arguments -Wcast-align: YES

      Compiler for C supports arguments -Wconversion: YES

      Compiler for C supports arguments -Wextra: YES

      Compiler for C supports arguments -Wformat=2: YES

      Compiler for C supports arguments -Wformat-nonliteral: YES

      Compiler for C supports arguments -Wformat-security: YES

      Compiler for C supports arguments -Wimplicit-function-declaration: YES

      Compiler for C supports arguments -Winit-self: YES

      Compiler for C supports arguments -Wmissing-format-attribute: YES

      Compiler for C supports arguments -Wmissing-noreturn: YES

      Compiler for C supports arguments -Wnested-externs: YES

      Compiler for C supports arguments -Wold-style-definition: YES

      Compiler for C supports arguments -Wpacked: YES

      Compiler for C supports arguments -Wpointer-arith: YES

      Compiler for C supports arguments -Wreturn-type: YES

      Compiler for C supports arguments -Wshadow: YES

      Compiler for C supports arguments -Wsign-compare: YES

      Compiler for C supports arguments -Wstrict-aliasing: YES

      Compiler for C supports arguments -Wundef: YES

      Compiler for C supports arguments -Wunused-but-set-variable: YES

      Compiler for C supports arguments -Wswitch-default: YES

      Compiler for C supports arguments -Wno-missing-field-initializers: YES

      Compiler for C supports arguments -Wno-unused-parameter: YES

      Compiler for C supports arguments -fno-strict-aliasing: YES

      Compiler for C supports arguments -fvisibility=hidden: YES

      Did not find pkg-config by name 'pkg-config'

      Found pkg-config: NO

      Did not find CMake 'cmake'

      Found CMake: NO

      Run-time dependency cairo found: NO


      ../cairo/meson.build:31:12: ERROR: Dependency lookup for cairo with

      method 'pkgconfig' failed: Pkg-config for machine host machine not

      found. Giving up.


      A full log can be found at

      /home/adminuser/.cache/uv/sdists-v6/pypi/pycairo/1.29.0/MTp-wa9pA5s9YSzNBad-p/src/.mesonpy-nziufu2s/meson-logs/meson-log.txt


  help: `pycairo` was included because `svglib==1.6.0` depends on

        `rlpycairo==0.4.0` which depends on `pycairo`

Checking if Streamlit is installed

Installing rich for an improved exception logging

Using uv pip install.

Using Python 3.11.14 environment at /home/adminuser/venv

Audited 1 package in 1ms


────────────────────────────────────────────────────────────────────────────────────────



──────────────────────────────────────── pip ───────────────────────────────────────────


Using standard pip install.

Collecting streamlit (from -r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading streamlit-1.52.2-py3-none-any.whl.metadata (9.8 kB)

Collecting cadquery (from -r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading cadquery-2.6.1-py3-none-any.whl.metadata (17 kB)

Collecting pandas (from -r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading pandas-2.3.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (91 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.2/91.2 kB 8.9 MB/s eta 0:00:00[2026-01-06 15:40:03.145193] 

Collecting numpy (from -r /mount/src/quoteforge/requirements.txt (line 4))

  Downloading numpy-2.4.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)

Collecting stpyvista (from -r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading stpyvista-0.1.4-py3-none-any.whl.metadata (1.7 kB)

Collecting trimesh (from -r /mount/src/quoteforge/requirements.txt (line 6))

  Downloading trimesh-4.10.1-py3-none-any.whl.metadata (13 kB)

Collecting matplotlib (from -r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading matplotlib-3.10.8-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (52 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.8/52.8 kB 142.2 MB/s eta 0:00:00[2026-01-06 15:40:03.773090] 

Collecting reportlab (from -r /mount/src/quoteforge/requirements.txt (line 8))

  Downloading reportlab-4.4.7-py3-none-any.whl.metadata (1.7 kB)

Collecting lxml (from -r /mount/src/quoteforge/requirements.txt (line 9))

  Downloading lxml-6.0.2-cp311-cp311-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.6 kB)

Collecting tinycss2 (from -r /mount/src/quoteforge/requirements.txt (line 10))

  Downloading tinycss2-1.5.1-py3-none-any.whl.metadata (3.0 kB)

Collecting cssselect2 (from -r /mount/src/quoteforge/requirements.txt (line 11))

  Downloading cssselect2-0.8.0-py3-none-any.whl.metadata (2.9 kB)

Collecting svglib (from -r /mount/src/quoteforge/requirements.txt (line 12))

  Downloading svglib-1.6.0-py3-none-any.whl.metadata (11 kB)

Collecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading altair-6.0.0-py3-none-any.whl.metadata (11 kB)

Collecting blinker<2,>=1.5.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)

Collecting cachetools<7,>=4.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading cachetools-6.2.4-py3-none-any.whl.metadata (5.6 kB)

Collecting click<9,>=7.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)

Collecting packaging>=20 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)

Collecting pillow<13,>=7.1.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading pillow-12.1.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)

Collecting protobuf<7,>=3.20 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading protobuf-6.33.2-cp39-abi3-manylinux2014_x86_64.whl.metadata (593 bytes)

Collecting pyarrow>=7.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading pyarrow-22.0.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (3.2 kB)

Collecting requests<3,>=2.27 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)

Collecting tenacity<10,>=8.1.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)

Collecting toml<2,>=0.10.1 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)

Collecting typing-extensions<5,>=4.4.0 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)

Collecting watchdog<7,>=2.1.5 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.3/44.3 kB 176.8 MB/s eta 0:00:00[2026-01-06 15:40:05.552179] 

Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)

Collecting pydeck<1,>=0.8.0b4 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)

Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading tornado-6.5.4-cp39-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.8 kB)

Collecting cadquery-ocp<7.9,>=7.8.1 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading cadquery_ocp-7.8.1.1.post1-cp311-cp311-manylinux_2_31_x86_64.whl.metadata (707 bytes)

Collecting ezdxf>=1.3.0 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading ezdxf-1.4.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.9 kB)

Collecting multimethod<2.0,>=1.11 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading multimethod-1.12-py3-none-any.whl.metadata (9.6 kB)

Collecting nlopt<3.0,>=2.9.0 (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading nlopt-2.10.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.1 kB)

Collecting typish (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading typish-1.9.3-py3-none-any.whl.metadata (7.2 kB)

Collecting casadi (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading casadi-3.7.2-cp311-none-manylinux2014_x86_64.whl.metadata (2.2 kB)

Collecting path (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading path-17.1.1-py3-none-any.whl.metadata (6.5 kB)

Collecting trame (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading trame-3.12.0-py3-none-any.whl.metadata (8.2 kB)

Collecting trame-vtk (from cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading trame_vtk-2.10.1-py3-none-any.whl.metadata (13 kB)

Collecting python-dateutil>=2.8.2 (from pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)

Collecting pytz>=2020.1 (from pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)

Collecting tzdata>=2022.7 (from pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)

Collecting bokeh (from stpyvista->-r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading bokeh-3.8.2-py3-none-any.whl.metadata (10 kB)

Collecting panel (from stpyvista->-r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading panel-1.8.5-py3-none-any.whl.metadata (15 kB)

Collecting pyvista (from stpyvista->-r /mount/src/quoteforge/requirements.txt (line 5))

  Downloading pyvista-0.46.4-py3-none-any.whl.metadata (15 kB)

Collecting contourpy>=1.0.1 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading contourpy-1.3.3-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.5 kB)

Collecting cycler>=0.10 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)

Collecting fonttools>=4.22.0 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading fonttools-4.61.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (114 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 114.2/114.2 kB 123.6 MB/s eta 0:00:00[2026-01-06 15:40:07.553144] 

Collecting kiwisolver>=1.3.1 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading kiwisolver-1.4.9-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (6.3 kB)

Collecting pyparsing>=3 (from matplotlib->-r /mount/src/quoteforge/requirements.txt (line 7))

  Downloading pyparsing-3.3.1-py3-none-any.whl.metadata (5.6 kB)

Collecting charset-normalizer (from reportlab->-r /mount/src/quoteforge/requirements.txt (line 8))

  Downloading charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)

Collecting webencodings>=0.4 (from tinycss2->-r /mount/src/quoteforge/requirements.txt (line 10))

  Downloading webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)

Collecting rlpycairo>=0.4.0 (from svglib->-r /mount/src/quoteforge/requirements.txt (line 12))

  Downloading rlpycairo-0.4.0-py3-none-any.whl.metadata (4.9 kB)

Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)

Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading jsonschema-4.25.1-py3-none-any.whl.metadata (7.6 kB)

Collecting narwhals>=1.27.1 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading narwhals-2.15.0-py3-none-any.whl.metadata (13 kB)

Collecting vtk==9.3.1 (from cadquery-ocp<7.9,>=7.8.1->cadquery->-r /mount/src/quoteforge/requirements.txt (line 2))

  Downloading vtk-9.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)

Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)

Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->-r /mount/src/quoteforge/requirements.txt (line 3))

  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)

Collecting idna<4,>=2.5 (from requests<3,>=2.27->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)

Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.27->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)

Collecting certifi>=2017.4.17 (from requests<3,>=2.27->streamlit->-r /mount/src/quoteforge/requirements.txt (line 1))

  Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)

Collecting pycairo>=1.20.0 (from rlpycairo>=0.4.0->svglib->-r /mount/src/quoteforge/requirements.txt (line 12))

  Downloading pycairo-1.29.0.tar.gz (665 kB)

     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 665.9/665.9 kB 62.8 MB/s eta 0:00:00[2026-01-06 15:40:08.774382] 

  Installing build dependencies: started

  Installing build dependencies: finished with status 'done'

  Getting requirements to build wheel: started

  Getting requirements to build wheel: finished with status 'done'

  Installing backend dependencies: started

  Installing backend dependencies: finished with status 'done'

  Preparing metadata (pyproject.toml): started

  Preparing metadata (pyproject.toml): finished with status 'error'

  error: subprocess-exited-with-error

  

  × Preparing metadata (pyproject.toml) did not run successfully.

  │ exit code: 1

  ╰─> [49 lines of output]

      + meson setup /tmp/pip-install-peiwkdd6/pycairo_a5b020be9e3743a0b1142ac1f8b77e7e /tmp/pip-install-peiwkdd6/pycairo_a5b020be9e3743a0b1142ac1f8b77e7e/.mesonpy-f4gcvf9w -Dbuildtype=release -Db_ndebug=if-release -Db_vscrt=md -Dwheel=true -Dtests=false --native-file=/tmp/pip-install-peiwkdd6/pycairo_a5b020be9e3743a0b1142ac1f8b77e7e/.mesonpy-f4gcvf9w/meson-python-native-file.ini

      The Meson build system

      Version: 1.10.0

      Source dir: /tmp/pip-install-peiwkdd6/pycairo_a5b020be9e3743a0b1142ac1f8b77e7e

      Build dir: /tmp/pip-install-peiwkdd6/pycairo_a5b020be9e3743a0b1142ac1f8b77e7e/.mesonpy-f4gcvf9w

      Build type: native build

      Project name: pycairo

      Project version: 1.29.0

      C compiler for the host machine: cc (gcc 12.2.0 "cc (Debian 12.2.0-14+deb12u1) 12.2.0")

      C linker for the host machine: cc ld.bfd 2.40

      Host machine cpu family: x86_64

      Host machine cpu: x86_64

      Program python3 found: YES (/home/adminuser/venv/bin/python)

      Compiler for C supports arguments -Wall: YES

      Compiler for C supports arguments -Warray-bounds: YES

      Compiler for C supports arguments -Wcast-align: YES

      Compiler for C supports arguments -Wconversion: YES

      Compiler for C supports arguments -Wextra: YES

      Compiler for C supports arguments -Wformat=2: YES

      Compiler for C supports arguments -Wformat-nonliteral: YES

      Compiler for C supports arguments -Wformat-security: YES

      Compiler for C supports arguments -Wimplicit-function-declaration: YES

      Compiler for C supports arguments -Winit-self: YES

      Compiler for C supports arguments -Wmissing-format-attribute: YES

      Compiler for C supports arguments -Wmissing-noreturn: YES

      Compiler for C supports arguments -Wnested-externs: YES

      Compiler for C supports arguments -Wold-style-definition: YES

      Compiler for C supports arguments -Wpacked: YES

      Compiler for C supports arguments -Wpointer-arith: YES

      Compiler for C supports arguments -Wreturn-type: YES

      Compiler for C supports arguments -Wshadow: YES

      Compiler for C supports arguments -Wsign-compare: YES

      Compiler for C supports arguments -Wstrict-aliasing: YES

      Compiler for C supports arguments -Wundef: YES

      Compiler for C supports arguments -Wunused-but-set-variable: YES

      Compiler for C supports arguments -Wswitch-default: YES

      Compiler for C supports arguments -Wno-missing-field-initializers: YES

      Compiler for C supports arguments -Wno-unused-parameter: YES

      Compiler for C supports arguments -fno-strict-aliasing: YES

      Compiler for C supports arguments -fvisibility=hidden: YES

      Did not find pkg-config by name 'pkg-config'

      Found pkg-config: NO

      Did not find CMake 'cmake'

      Found CMake: NO

      Run-time dependency cairo found: NO

      

      ../cairo/meson.build:31:12: ERROR: Dependency lookup for cairo with method 'pkgconfig' failed: Pkg-config for machine host machine not found. Giving up.

      

      A full log can be found at /tmp/pip-install-peiwkdd6/pycairo_a5b020be9e3743a0b1142ac1f8b77e7e/.mesonpy-f4gcvf9w/meson-logs/meson-log.txt

      [end of output]

  

  note: This error originates from a subprocess, and is likely not a problem with pip.

error: metadata-generation-failed


× Encountered error while generating package metadata.

╰─> See above for output.


note: This is an issue with the package mentioned above, not pip.

hint: See above for details.


[notice] A new release of pip is available: 24.0 -> 25.3

[notice] To update, run: pip install --upgrade pip

Checking if Streamlit is installed

Installing rich for an improved exception logging

Using standard pip install.

Collecting rich>=10.14.0

  Downloading rich-14.2.0-py3-none-any.whl.metadata (18 kB)

Collecting markdown-it-py>=2.2.0 (from rich>=10.14.0)

  Downloading markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)

Collecting pygments<3.0.0,>=2.13.0 (from rich>=10.14.0)

  Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)

Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.14.0)

  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)

Downloading rich-14.2.0-py3-none-any.whl (243 kB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 243.4/243.4 kB 17.0 MB/s eta 0:00:00[2026-01-06 15:40:15.896308] 

Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.3/87.3 kB 65.1 MB/s eta 0:00:00

Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 89.9 MB/s eta 0:00:00[2026-01-06 15:40:15.938941] 

Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)

Installing collected packages: pygments, mdurl, markdown-it-py, rich

  Attempting uninstall: pygments

    Found existing installation: Pygments 2.19.2

    Uninstalling Pygments-2.19.2:

      Successfully uninstalled Pygments-2.19.2

  Attempting uninstall: mdurl

    Found existing installation: mdurl 0.1.2

    Uninstalling mdurl-0.1.2:

      Successfully uninstalled mdurl-0.1.2

  Attempting uninstall: markdown-it-py

    Found existing installation: markdown-it-py 4.0.0

    Uninstalling markdown-it-py-4.0.0:

      Successfully uninstalled markdown-it-py-4.0.0

  Attempting uninstall: rich

    Found existing installation: rich 14.2.0

    Uninstalling rich-14.2.0:

      Successfully uninstalled rich-14.2.0

Successfully installed markdown-it-py-4.0.0 mdurl-0.1.2 pygments-2.19.2 rich-14.2.0


[notice] A new release of pip is available: 24.0 -> 25.3

[notice] To update, run: pip install --upgrade pip


────────────────────────────────────────────────────────────────────────────────────────


[15:40:18] ❗️ installer returned a non-zero exit code