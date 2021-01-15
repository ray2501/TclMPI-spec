%{!?directory:%define directory /usr}

Summary:	Tcl bindings for MPI
Name:		tclmpi
Version:	1.0
Release:	1
License:	BSD-3-Clause
Group:		Development/Languages/Tcl
Source0:	https://sites.google.com/site/akohlmey/software/tclmpi/tclmpi-1.0.tar.gz
URL:		https://sites.google.com/site/akohlmey/software/tclmpi
BuildRequires:	make
BuildRequires:	tcl-devel >= 8.6
BuildRequires:	openmpi-devel
Requires: tcl >= 8.6
Requires: openmpi
BuildRoot:	%{tmpdir}/${name}-%{version}

%description
The TclMPI package contains software that wraps an MPI library for Tcl
and allows MPI calls to be used from Tcl scripts.

%prep
%setup -q -n %{name}-%{version}

%build
export PATH=$PATH:/usr/lib64/mpi/gcc/openmpi/bin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p ${RPM_BUILD_ROOT}%{tcl_archdir}/%{name}%{version}
cp pkgIndex.tcl ${RPM_BUILD_ROOT}%{tcl_archdir}/%{name}%{version}
cp tclmpi.tcl ${RPM_BUILD_ROOT}%{tcl_archdir}/%{name}%{version}
cp _tclmpi.so ${RPM_BUILD_ROOT}%{tcl_archdir}/%{name}%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{tcl_archdir}

