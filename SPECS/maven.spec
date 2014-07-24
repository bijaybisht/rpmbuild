Name: 		apache-maven
Version: 	3.2.2
Release:        1%{?dist}
Summary:        apache maven rpm

Group:          Development
License:        Apache
URL:		http://maven.apache.org/
Source0:        ftp://mirror.reverse.net/pub/apache/maven/maven-3/3.2.2/binaries/apache-maven-3.2.2-bin.tar.gz


%description


%prep
%setup -q


%build


%install
rm -rf   %{buildroot}
mkdir -p %{buildroot}/opt/%{name}-%{version}-%{release}
mkdir -p %{buildroot}/usr/bin
cp -a .  %{buildroot}/opt/%{name}-%{version}-%{release}
ln -s                /opt/%{name}-%{version}-%{release}/bin/mvn \
         %{buildroot}/usr/bin/mvn


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/


%changelog
