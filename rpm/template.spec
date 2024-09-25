%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-mrpt-reactivenav2d
Version:        2.2.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mrpt_reactivenav2d package

License:        BSD
URL:            https://github.com/mrpt-ros-pkg/mrpt_navigation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-ament-cmake-lint-cmake
Requires:       ros-jazzy-ament-cmake-xmllint
Requires:       ros-jazzy-ament-lint-auto
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-mrpt-libnav
Requires:       ros-jazzy-mrpt-libros-bridge
Requires:       ros-jazzy-mrpt-nav-interfaces
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-rclcpp-components
Requires:       ros-jazzy-sensor-msgs
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-stereo-msgs
Requires:       ros-jazzy-tf2
Requires:       ros-jazzy-tf2-geometry-msgs
Requires:       ros-jazzy-tf2-ros
Requires:       ros-jazzy-visualization-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ament-cmake-lint-cmake
BuildRequires:  ros-jazzy-ament-cmake-xmllint
BuildRequires:  ros-jazzy-ament-lint-auto
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-mrpt-libnav
BuildRequires:  ros-jazzy-mrpt-libros-bridge
BuildRequires:  ros-jazzy-mrpt-nav-interfaces
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-rclcpp-components
BuildRequires:  ros-jazzy-sensor-msgs
BuildRequires:  ros-jazzy-std-msgs
BuildRequires:  ros-jazzy-stereo-msgs
BuildRequires:  ros-jazzy-tf2
BuildRequires:  ros-jazzy-tf2-geometry-msgs
BuildRequires:  ros-jazzy-tf2-ros
BuildRequires:  ros-jazzy-visualization-msgs
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Reactive navigation for wheeled robots using MRPT navigation algorithms (TP-
Space)

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Sep 25 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 2.2.0-1
- Autogenerated by Bloom

* Wed Sep 25 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 2.1.1-2
- Autogenerated by Bloom

* Mon Sep 02 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 2.1.1-1
- Autogenerated by Bloom

* Thu Aug 08 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 2.1.0-1
- Autogenerated by Bloom

* Tue May 28 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 2.0.0-1
- Autogenerated by Bloom

